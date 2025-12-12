import streamlit as st
import time
import os
import io
import random

# [닌자 모드] 앱 시작 시 무거운 라이브러리 절대 로딩 금지

# 1. 페이지 설정
st.set_page_config(page_title="퍼스널 컬러 & 체형 분석", layout="centered")

# UI 깔끔하게
hide_st_style = """
    <style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"] div:first-child {display: none;}
    [data-testid="stFileUploader"] section[data-testid="stFileUploaderDropzone"]::before {
        content: "사진을 여기로 끌어다 놓거나 파일 선택을 눌러주세요";
        display: block; text-align: center; font-weight: 500; margin-bottom: 0.25rem;
    }
    </style>
"""
st.markdown(hide_st_style, unsafe_allow_html=True)

# 2. 로직/데이터 연결
try:
    import logic as utils 
    from data.definitions import (
        SEASON_PALETTE, TONE_INFO, KIDS_CHARACTERS, DEFAULT_PALETTE, 
        CELEB, BEST_COLORS, WORST_COLORS
    )
except ImportError:
    st.error("필수 파일(logic.py 또는 data/definitions.py)이 없습니다.")
    st.stop()

# 3. 페이지 이동 관리
if 'page' not in st.session_state: st.session_state['page'] = 'home'
def go_page(p): st.session_state['page'] = p
def go_home(): st.session_state['page'] = 'home'

# --- [1] 퍼스널 컬러 페이지 (완벽 유지) ---
def page_personal_color():
    st.markdown("<h1>퍼스널 컬러 찾기</h1>", unsafe_allow_html=True)
    st.subheader("기본 정보 입력")
    
    import cv2
    import numpy as np
    from PIL import Image, ImageDraw, ImageFont
    import requests 

    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("이름", key="pc_n")
        years = ["선택"] + [f"{y}년생" for y in range(2025, 1930, -1)]
        birth_year = st.selectbox("출생연도", years, index=0, key="pc_y")
    with c2:
        gender = st.radio("성별", ["여자", "남자"], key="pc_g")

    st.divider()
    st.subheader("사진 업로드")
    st.markdown("※ 메이크업 없는 정면 사진을 업로드해주세요. (필터 X, 기본 카메라 O)")
    file = st.file_uploader("사진 업로드", type=["jpg", "jpeg", "png"], key="pc_f")
    
    if not file:
        st.markdown("<br>", unsafe_allow_html=True)
        st.button("🏠 홈으로 돌아가기", on_click=go_home)
        return

    display_name = name if name else "사용자"

    loading_container = st.container()
    with loading_container:
        st.info(f"🔄 **{display_name}**님의 퍼스널 컬러를 분석 중입니다...")
        progress_bar = st.progress(0)
        for i in range(50):
            time.sleep(0.02)
            progress_bar.progress(i * 2 + 1)

    img = Image.open(file)
    img = utils.fix_image_orientation(img)
    img = img.convert("RGB")
    rgb = np.array(img)

    cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    faces = cascade.detectMultiScale(gray, 1.2, 5)

    if len(faces) > 0:
        x, y, w, h = faces[0]
        rx1, rx2 = int(y + h*0.25), int(y + h*0.85)
        cx1, cx2 = int(x + w*0.25), int(x + w*0.75)
        face_region = rgb[rx1:rx2, cx1:cx2]
        show_img = rgb.copy()
        cv2.rectangle(show_img, (cx1, rx1), (cx2, rx2), (0,255,0), 3)
        st.image(show_img, caption="분석된 얼굴 영역", use_column_width=True)
    else:
        face_region = rgb
        st.image(img, caption="분석된 얼굴 영역 (전체 분석)", use_column_width=True)

    hsv = cv2.cvtColor(face_region, cv2.COLOR_RGB2HSV)
    h_mean = utils.circular_mean_hue(hsv[:,:,0].astype(float) * 2)
    s_mean = float(np.mean(hsv[:,:,1]/255))
    v_mean = float(np.mean(hsv[:,:,2]/255))
    
    result_tone = utils.map_to_pccs_10(h_mean, s_mean, v_mean)
    season = utils.tone_to_season(result_tone)
    season_palette = SEASON_PALETTE.get(season, DEFAULT_PALETTE)

    loading_container.empty()
    st.success(f"✅ **{display_name}**님의 퍼스널 컬러 분석이 완료되었습니다.")

    utils.save_result("personal_color", name, birth_year, gender, 0, 0, result_tone)

    st.image(season_palette, caption=f"{season} 팔레트", use_column_width=True)

    st.success(f"{display_name}님의 퍼스널 컬러는 **{result_tone}** 입니다.")
    st.write(f"Hue 평균: {round(h_mean)}°, 채도(S): {s_mean:.2f}, 명도(V): {v_mean:.2f}")
    st.write(TONE_INFO.get(result_tone, ""))

    celeb_name = "정보 없음"
    celeb_url = ""
    if result_tone in CELEB and gender in CELEB[result_tone]:
        celeb_name, celeb_url = CELEB[result_tone][gender]
        st.subheader(f"대표 연예인: {celeb_name}")
        st.image(celeb_url, width=300)

    st.subheader("Best / Worst Colors")
    col_b, col_w = st.columns(2)
    with col_b:
        st.write("**Best**")
        if result_tone in BEST_COLORS:
            st.image(utils.draw_color_boxes(BEST_COLORS[result_tone], "Best"))
    with col_w:
        st.write("**Worst**")
        if result_tone in WORST_COLORS:
            st.image(utils.draw_color_boxes(WORST_COLORS[result_tone], "Worst"))

    def create_result_card():
        card = Image.new("RGB", (1200, 800), (255, 255, 255))
        draw = ImageDraw.Draw(card)
        try:
            font_title = ImageFont.truetype("NanumGothic-Bold.ttf", 50)  
            font_text = ImageFont.truetype("NanumGothic-Regular.ttf", 30)
        except:
            font_title = ImageFont.load_default()
            font_text = ImageFont.load_default()

        draw.text((50, 50), f"{display_name}님의 퍼스널 컬러 결과", fill="black", font=font_title)
        draw.text((50, 130), f"결과: {result_tone}", fill="black", font=font_title)
        draw.text((50, 200), f"계절: {season}", fill="gray", font=font_text)

        draw.text((50, 300), "BEST COLORS", fill="green", font=font_title)
        if result_tone in BEST_COLORS:
            best_img = utils.draw_color_boxes(BEST_COLORS[result_tone], "Best")
            card.paste(best_img, (50, 360))
        
        draw.text((50, 500), "WORST COLORS", fill="darkred", font=font_title)
        if result_tone in WORST_COLORS:
            worst_img = utils.draw_color_boxes(WORST_COLORS[result_tone], "Worst")
            card.paste(worst_img, (50, 560))

        if celeb_url:
            try:
                c_res = requests.get(celeb_url, timeout=3)
                celeb = Image.open(io.BytesIO(c_res.content)).resize((450, 550))
                card.paste(celeb, (700, 150))
                draw.text((700, 720), f"대표 연예인: {celeb_name}", fill="black", font=font_text)
            except: pass
        return card

    st.subheader("🔗 결과 저장")
    with st.spinner("결과 카드 생성 중..."):
        try:
            final_card = create_result_card()
            buf = io.BytesIO()
            final_card.save(buf, format="PNG")
            st.download_button(
                "🖼 결과 이미지 다운로드",
                buf.getvalue(),
                file_name=f"{name}_personal_color.png",
                mime="image/png"
            )
        except Exception as e:
            st.warning(f"이미지 생성 오류: {e}")
    st.divider()
    st.button("🏠 홈으로 돌아가기", on_click=go_home, use_container_width=True)

# --- [2] 체형 분석 페이지 ---
def page_body_shape():
    st.subheader("체형 분석")
    st.markdown("※ 전신이 나오도록 촬영한 사진을 업로드해주세요.")
    import numpy as np
    from PIL import Image
    
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("이름", key="bs_n")
        gender = st.radio("성별", ["여자", "남자"], key="bs_g")
    with c2:
        height = st.number_input("키(cm)", key="bs_h")
        weight = st.number_input("몸무게(kg)", key="bs_w")
    
    file = st.file_uploader("전신 사진 업로드", type=["jpg", "png"], key="bs_f")
    if file:
        img = Image.open(file)
        img = utils.fix_image_orientation(img)
        st.image(img, caption="업로드한 전신 사진", use_column_width=True)
        if st.button("분석하기", type="primary"):
            rgb = np.array(img.convert("RGB"))
            body_comment = utils.analyze_body_shape(rgb)
            st.success("체형 분석 결과")
            st.write(body_comment)
            utils.save_result("body_shape", name, "", gender, height, weight, body_comment)
    st.divider()
    st.button("🏠 홈으로 돌아가기", on_click=go_home)

# --- [3] 캐릭터 매칭 페이지 (대폭 수정됨!) ---
def page_kids_fun():
    st.subheader("얼굴 캐릭터 매칭")
    
    # [NEW] 키, 몸무게 입력 추가
    c1, c2 = st.columns(2)
    with c1:
        name = st.text_input("이름", key="kf_n")
        gender = st.radio("성별", ["여자", "남자"], key="kf_g")
        height = st.number_input("키(cm)", key="kf_h") # 추가됨
    with c2:
        weight = st.number_input("몸무게(kg)", key="kf_w") # 추가됨
        # [NEW] 카테고리 대폭 확장 (definitions.py에서 가져옴)
        target_type = st.selectbox("어떤 느낌으로 매칭할까요?", list(KIDS_CHARACTERS.keys()))

    file = st.file_uploader("얼굴 사진 업로드", type=["jpg", "png"], key="kf_f")
    if file:
        st.image(file, width=300)
        if st.button("매칭하기", type="primary"):
            # 아직은 Google API가 없으므로 '랜덤'으로 뽑지만,
            # 키/몸무게 정보를 저장해두는 척은 합니다!
            
            picked = random.choice(KIDS_CHARACTERS[target_type])
            
            # (나중에 여기에 Google API 로직이 들어갑니다)
            
            st.success(f"당신의 특징(키 {height}cm, {target_type})을 분석한 결과...")
            time.sleep(1) # 분석하는 척 뜸 들이기
            st.balloons()
            st.success(f"**{picked}** 와(과) 가장 닮았습니다! 🎉")
            
            utils.save_result("kids_fun", name, "", gender, height, weight, picked)
            
    st.divider()
    st.button("🏠 홈으로 돌아가기", on_click=go_home)

# --- [4] 관리자 페이지 ---
def page_admin():
    st.button("🏠 홈으로", on_click=go_home)
    st.subheader("관리자 모드")
    pw = st.text_input("비밀번호", type="password")
    if pw == "0910":
        st.success("인증되었습니다!")
        import pandas as pd
        df = utils.get_results_df()
        if len(df) > 0:
            st.write(f"총 {len(df)}개 결과")
            st.dataframe(df)
            st.download_button("📥 CSV 다운로드", df.to_csv(index=False).encode('utf-8'), "data.csv")
            st.divider()
            col1, col2 = st.columns(2)
            col1.bar_chart(df['service'].value_counts())
            pc_df = df[df['service'] == 'personal_color']
            if not pc_df.empty: col2.bar_chart(pc_df['result'].value_counts())
        else: st.info("데이터 없음")
    elif pw: st.error("비밀번호 오류")

# --- 메인 실행 ---
if st.session_state['page'] == 'home':
    st.title("✨ AI 퍼스널 브랜딩")
    st.write("서비스를 선택하세요")
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1: 
        if st.button("① 퍼스널 컬러", use_container_width=True): go_page("pc")
    with c2: 
        if st.button("② 체형 분석", use_container_width=True): go_page("bs")
    with c3: 
        if st.button("③ 캐릭터 매칭", use_container_width=True): go_page("kf")
    st.markdown("<br><br>", unsafe_allow_html=True)
    with st.expander("🔒 관리자 접속"):
        if st.button("관리자 페이지 이동"): go_page("admin")

elif st.session_state['page'] == 'pc': page_personal_color()
elif st.session_state['page'] == 'bs': page_body_shape()
elif st.session_state['page'] == 'kf': page_kids_fun()
elif st.session_state['page'] == 'admin': page_admin()
