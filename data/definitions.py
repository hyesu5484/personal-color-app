# -----------------------------------------------------------
# 파일 경로: data/definitions.py
# 설명: 프로그램에서 사용하는 고정된 데이터(텍스트, URL, 색상값)를 모아둔 창고입니다.
# -----------------------------------------------------------

# 톤 설명
TONE_INFO = {
    "봄 라이트": "고명도의 밝은 느낌이지만 저채도의 파스텔톤이 잘 어울려요. 복숭아·코랄·살구처럼 맑고 연한 립을 바르면 얼굴이 따뜻하고 청순하게 보입니다.",
    "봄 브라이트": "고채도의 따뜻하고 발랄한 느낌, 고명도의 밝고 쨍한 컬러가 잘 어울려요. 봄처럼 화사하게 피어나는 인상이 강해서 ‘봄의 정석’이라고도 불려요.",
    "여름 라이트": "고명도의 밝고 은은한 파스텔톤이 잘 어울려요. 싱그럽고 투명한 느낌이 있고, 봄 라이트보다 흰 기가 조금 더 많아요.",
    "여름 브라이트": "고명도·고채도 계열이라 채도가 높은 원색 계열도 잘 받아요. 쨍한 여름 컬러가 잘 어울립니다.",
    "여름 뮤트": "탁기가 있는 톤다운 파스텔 계열이 어울려요. 자연스럽고 부드러운 느낌이 특징입니다.",
    "가을 뮤트": "톤 다운된 따뜻한 브라운·카키·올리브 계열이 잘 어울려요. 분위기 있고 고급스러운 인상을 줍니다.",
    "가을 스트롱": "중명도·고채도 웜톤이 잘 어울려요. 테라코타·머스타드처럼 선명한 색이 잘 받습니다.",
    "가을 딥": "저명도의 어둡고 깊이 있는 컬러가 잘 어울려요. 버건디·다크브라운 계열이 찰떡입니다.",
    "겨울 브라이트": "고채도의 비비드한 쿨톤이 잘 어울려요. 선명한 푸시아·코발트 블루가 잘 받습니다.",
    "겨울 딥": "저명도·저채도의 어두운 쿨톤이 어울려요. 블랙 계열이 가장 잘 어울리는 타입입니다.",
}

# 시즌 팔레트 이미지 URL
SEASON_PALETTE = {
    "봄": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_봄.png",
    "여름": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_여름.png",
    "가을": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_가을.png",
    "겨울": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_겨울.png",
}
DEFAULT_PALETTE = "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccsMain.png"

# 연예인 데이터 (app.py에 있던 내용 전체 이동)
CELEB = {
    "봄 라이트": {
        "여자": ("윤아", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTM1/MDAxNzYyNDM5MzA3NDI1.T2rxWI6y8G0KOX-pdK4BcAXgCEUl-2UUOHU9WVgtZCMg.uI3ecF_zdMm_guc5BmRIwcZldTBYdPBzu3u5rqqj2J8g.JPEG/IMG％EF％BC％BF1192.JPG?type=w966"),
        "남자": ("이종석", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNzUg/MDAxNzYyNDM5MzA4MzU2.sgx5YYgOJeH6tIQ-dfmq6Zt-u_LoLhWvFeNpUvvnHhEg.3Mwa48B-biz1QudsFRHSsLPkcuXJJIkbHWwf-aYegiAg.JPEG/IMG％EF％BC％BF1225.JPG?type=w966")
    },
    "봄 브라이트": {
        "여자": ("나연", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjAz/MDAxNzYyNDM5MzA3Nzk1.gmEqXNzB37B2wBTgrVx4w6JDMlcaCNtqIFSnr5T8UCwg.VjDPhKIS95U1AB33R8KfuleDxyRQ_ZB9CZefvdTNSpsg.JPEG/IMG％EF％BC％BF1206.JPG?type=w966"),
        "남자": ("강다니엘", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjY1/MDAxNzYyNDM5MzA4MjU3.f0OZ-_VnhEI33cm0IcEuUITdmX6X8HORMrUzWCv1d7Ug.8iSY5eGRrAfNUEhvH0KehClXPBPUKeKnZEF79olvxNYg.JPEG/IMG％EF％BC％BF1227.JPG?type=w966")
    },
    # ... (나머지 연예인 데이터도 여기에 그대로 붙여넣기 해주세요) ...
    # 지면상 생략했지만, app.py의 CELEB 전체를 여기에 넣습니다.
}

# Best 색상칩
BEST_COLORS = {
    "봄 라이트": [(255, 229, 204), (255, 205, 178), (255, 183, 197)],
    "봄 브라이트": [(255, 85, 125), (255, 180, 60), (255, 135, 0)],
    "여름 라이트": [(210, 225, 255), (245, 230, 250), (235, 240, 255)],
    "여름 브라이트": [(60, 90, 255), (255, 70, 140), (80, 200, 255)],
    "여름 뮤트": [(180, 185, 195), (210, 200, 215), (160, 170, 185)],
    "가을 뮤트": [(165, 140, 120), (150, 130, 100), (180, 155, 135)],
    "가을 스트롱": [(200, 100, 20), (160, 80, 20), (220, 130, 30)],
    "가을 딥": [(95, 60, 45), (75, 40, 30), (120, 70, 60)],
    "겨울 브라이트": [(40, 20, 255), (255, 30, 90), (20, 200, 255)],
    "겨울 딥": [(30, 20, 50), (60, 0, 90), (0, 0, 0)]
}

# Worst 색상칩
WORST_COLORS = {
    "봄 라이트": [(120, 120, 120), (0, 0, 0), (50, 50, 150)],
    "봄 브라이트": [(150, 150, 150), (50, 50, 180), (0, 0, 70)],
    "여름 라이트": [(80, 60, 40), (40, 30, 20), (0, 0, 0)],
    "여름 브라이트": [(100, 80, 50), (40, 20, 0), (0, 0, 0)],
    "여름 뮤트": [(240, 240, 240), (255, 255, 200), (255, 190, 200)],
    "가을 뮤트": [(240, 240, 255), (180, 210, 255), (200, 230, 255)],
    "가을 스트롱": [(240, 240, 240), (200, 210, 255), (180, 220, 255)],
    "가을 딥": [(240, 240, 240), (200, 230, 255), (190, 220, 255)],
    "겨울 브라이트": [(255, 235, 200), (255, 225, 180), (200, 180, 150)],
    "겨울 딥": [(255, 235, 205), (255, 240, 220), (200, 180, 150)],
}

# 아이용 캐릭터 매칭 데이터
KIDS_CHARACTERS = {
    "사람 캐릭터": ["스폰지밥", "도라에몽 속 노진구", "짱구", "엘사(겨울왕국)", "안나(겨울왕국)"],
    "동물 캐릭터": ["푸우(곰돌이 푸)", "톰(톰과 제리)", "주토피아 주디", "라이온킹 심바"],
    "연예인": ["아이유", "유재석", "정국", "장원영", "카리나"],
}