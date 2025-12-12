# -----------------------------------------------------------
# 파일 경로: data/definitions.py
# 설명: 데이터 창고 & 이미지 필터링 로직 통합 (제출용)
# -----------------------------------------------------------

# ==========================================================
# 1. 퍼스널 컬러 및 연예인 데이터 (기존 데이터 유지)
# ==========================================================

TONE_INFO = {
    "봄 라이트": "고명도의 밝은 느낌이지만 저채도의 파스텔톤이 잘 어울려요.",
    "봄 브라이트": "고채도의 따뜻하고 발랄한 느낌, 고명도의 밝고 쨍한 컬러가 잘 어울려요.",
    "여름 라이트": "고명도의 밝고 은은한 파스텔톤이 잘 어울려요.",
    "여름 브라이트": "고명도·고채도 계열이라 채도가 높은 원색 계열도 잘 받아요.",
    "여름 뮤트": "탁기가 있는 톤다운 파스텔 계열이 어울려요.",
    "가을 뮤트": "톤 다운된 따뜻한 브라운·카키·올리브 계열이 잘 어울려요.",
    "가을 스트롱": "중명도·고채도 웜톤이 잘 어울려요.",
    "가을 딥": "저명도의 어둡고 깊이 있는 컬러가 잘 어울려요.",
    "겨울 브라이트": "고채도의 비비드한 쿨톤이 잘 어울려요.",
    "겨울 딥": "저명도·저채도의 어두운 쿨톤이 어울려요."
}

SEASON_PALETTE = {
    "봄": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_봄.png",
    "여름": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_여름.png",
    "가을": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_가을.png",
    "겨울": "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccs_겨울.png",
}
DEFAULT_PALETTE = "https://cdn.jsdelivr.net/gh/thesimplegithub/mycolor-hosting/images/pccsMain.png"

CELEB = {
    "봄 라이트": {"여자": ("윤아", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTM1/MDAxNzYyNDM5MzA3NDI1.T2rxWI6y8G0KOX-pdK4BcAXgCEUl-2UUOHU9WVgtZCMg.uI3ecF_zdMm_guc5BmRIwcZldTBYdPBzu3u5rqqj2J8g.JPEG/IMG%EF%BC%BF1192.JPG?type=w966"), "남자": ("이종석", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNzUg/MDAxNzYyNDM5MzA4MzU2.sgx5YYgOJeH6tIQ-dfmq6Zt-u_LoLhWvFeNpUvvnHhEg.3Mwa48B-biz1QudsFRHSsLPkcuXJJIkbHWwf-aYegiAg.JPEG/IMG%EF%BC%BF1225.JPG?type=w966")},
    "봄 브라이트": {"여자": ("나연", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjAz/MDAxNzYyNDM5MzA3Nzk1.gmEqXNzB37B2wBTgrVx4w6JDMlcaCNtqIFSnr5T8UCwg.VjDPhKIS95U1AB33R8KfuleDxyRQ_ZB9CZefvdTNSpsg.JPEG/IMG%EF%BC%BF1206.JPG?type=w966"), "남자": ("강다니엘", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjY1/MDAxNzYyNDM5MzA4MjU3.f0OZ-_VnhEI33cm0IcEuUITdmX6X8HORMrUzWCv1d7Ug.8iSY5eGRrAfNUEhvH0KehClXPBPUKeKnZEF79olvxNYg.JPEG/IMG%EF%BC%BF1227.JPG?type=w966")},
    "여름 라이트": {"여자": ("장원영", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjc1/MDAxNzYyNDM5MzA4MTQ5.ewVz5OQExgMd60ij3x5v1IJTSFIpA9syFeb7_hi3I1kg.ZV73W-Lvr8U2bh-C31jX_kZjdKvcrkNGkw9bhsDHesgg.JPEG/IMG%EF%BC%BF1222.JPG?type=w966"), "남자": ("정해인", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNTMg/MDAxNzYyNDM5MzA3Nzgz.GO7RDL060ifLkDNT0xixz1kD9tHebrfG1ONvQhfmU8sg.321vBWpCBZuZGURaIJM69c0KWgwYMGBsPSuHsNbgaYcg.JPEG/IMG%EF%BC%BF1230.JPG?type=w966")},
    "여름 브라이트": {"여자": ("은하", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTc1/MDAxNzYyNDM5MzA4OTk3.XyRCgDMBrhObmZydV-7E8XWWBytUp7_7ta2l3XREYOUg.MrkWtbrcCdX0wZ3g-xKerOWoAVDJot8wEe3j7E45T_Mg.JPEG/IMG%EF%BC%BF1224.JPG?type=w966"), "남자": ("뷔", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTYz/MDAxNzYyNDM5MzA4NDE1.NA54xC6oQosEfDWvfgmvnltIvdpYa_Z9klksZELld6wg.J262fp66ywuKByMfaaYNFqFPSZKQu89N0QSEA8GuLuog.JPEG/IMG%EF%BC%BF1236.JPG?type=w966")},
    "여름 뮤트": {"여자": ("문채원", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjgg/MDAxNzYyNDM5MzA3NDg0.YIstb7sU0wswDpygeoQIMwVh9vVkMuhrI41ndLMqPkIg.HHcvHaCoKnMGbQ7irGsYEe6PEtDV5ye2Nc53GC5a5Iwg.JPEG/IMG%EF%BC%BF1198.JPG?type=w966"), "남자": ("송강", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjYw/MDAxNzYyNDM5MzA4OTIz.vBmWxVKj7Dco3PTkrigIXG3R2N_Dj-4QVpQtFiE_-q4g.GVzu4Lw-QZTCjKe_GHcupZ6TEmKAPRkXN0ihWi1kBPMg.JPEG/IMG%EF%BC%BF1201.JPG?type=w966")},
    "가을 뮤트": {"여자": ("제니", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfODYg/MDAxNzYyNDM5MzA3OTA1.NLvRSbc3iZzDH_aKTbQfBBovpza2OvEFEOgZcXubatwg.Kfs2Empot5CsxTb_nCOJz4_VWHB53mDVkfRTtvFqBB8g.JPEG/IMG%EF%BC%BF1221.JPG?type=w966"), "남자": ("서강준", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNDYg/MDAxNzYyNDM5MzA3NDQ6.EVmfObIqUCqbIgkLv0mcIHQsTIljnLb2gdRXGitKdnog.FeE4c0NscxPFePQ4Qhj6LUGsvQPE6y2TrkX8Qc3HThIg.JPEG/IMG%EF%BC%BF1237.JPG?type=w966")},
    "가을 스트롱": {"여자": ("조이", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjE1/MDAxNzYyNDM5MzA8NTE2.AGNHRbZMl93a6NwjTt76N9EBBZ8rzVZTEbt3mn5-BRYg.CCSBsMGuO3E4BfInjwoNWn6fAl85PhNn-kWRgPC6p1Qg.JPEG/output%EF%BC%BF3817396647.jpg?type=w966"), "남자": ("강태오", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjY6/MDAxNzYyNDM5MzA7NDg7.nM3UvJAe4uPo3Pc1HT40vYbzRk7cCefKLFUZRpBjOHcg.22tuUdmI-mklIm793R8Sw0smpnqebyt5QgHzu0kUK0Eg.JPEG/output%EF%BC%BF2543490798.jpg?type=w966")},
    "가을 딥": {"여자": ("김유정", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNiAg/MDAxNzYyNDM5MzA8OTg6.SLp61r-OMfbkn0euIMLhk2o2ZYGANT9fKoHE2S5B6lAg.umJC53HxGvx0kDdsZEL6jeZD5gLfuWPy9A3ce9tgIfAg.JPEG/IMG%EF%BC%BF1212.JPG?type=w966"), "남자": ("공유", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTU1/MDAxNzYyNDM5MzA8Nzk8.xN33tfvJjPbOHU13TZhzBf8FM0G1yCLp2oFSSHGyqZAg.3mlA7xcK21r6p7rdfl1UXf1fr_8nkjVi0h6rzeaGvH0g.JPEG/IMG%EF%BC%BF1238.JPG?type=w966")},
    "겨울 브라이트": {"여자": ("카리나", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjkg/MDAxNzYyNDM5MzA7N7I0.vmX-1402X4TAKcSD1DtyrGBqAbFDBsYS5GottDNPMj0g.xsjf_Hcyax48NNMp_VhE10ICNjCLPbcDMK3GFSIYroUg.JPEG/IMG%EF%BC%BF1217.JPG?type=w966"), "남자": ("조정석", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTY6/MDAxNzYyNDM5MzA5MTI4.-ohQnzHZ8xK8fnjgWQU1wg9Yxcr0tJwxy6CrV10Hpl4g.wmGPYOHyE-c7Fgh60uye6fuSujLGUcQ4BSMQJRR7PP0g.JPEG/IMG%EF%BC%BF1244.JPG?type=w966")},
    "겨울 딥": {"여자": ("지수", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTIz/MDAxNzYyNDM5MzA4OTM4.3sc7OS-eHnjtSQ-8JRgjVFVDxzGihBNxhKqgZtZifdcg.sG6vJqOREgXxvXQeD7Acb9LEzxSYM98r7PoElLlgQpUg.JPEG/IMG%EF%BC%BF1209.JPG?type=w966"), "남자": ("이수혁", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjc0/MDAxNzYyNDM5MzA8ODM7._qzsWliOJ9QxBy8Co8KdQOwR6oj8l7ePdot8o99kx2gg.jvtnAbBjBxUajgXjAQSJkNqinB8Eibdfu5DMcTdAt4cg.JPEG/IMG%EF%BC%BF1231.JPG?type=w966")},
}

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

# ==========================================================
# 2. 캐릭터 매칭 데이터 (기존 데이터 유지)
# ==========================================================
TEMP_IMG = "https://via.placeholder.com/300?text=Image+Coming+Soon"

KIDS_CHARACTERS = {
    "한국 애니메이션": {
        "뽀로로": {"img": "https://upload.wikimedia.org/wikipedia/en/2/23/Pororo_the_Little_Penguin.png", "reason": "동글동글한 얼굴과 호기심 가득한 눈빛이 뽀로로와 똑 닮았어요! 🤓"},
        "루피": {"img": "https://upload.wikimedia.org/wikipedia/en/thumb/c/c3/Zanmang_Loopy.png/220px-Zanmang_Loopy.png", "reason": "귀여운 볼살과 부드러운 인상이 잔망루피를 연상시켜요! 🌸"},
        "크롱": {"img": "https://i.pinimg.com/736x/8f/33/c9/8f33c9233075c330df3200924409392e.jpg", "reason": "장난기 넘치는 표정과 활발한 에너지가 크롱과 찰떡입니다! 🦖"},
        "타요": {"img": "https://upload.wikimedia.org/wikipedia/ko/6/62/%EA%BC%AC%EB%A7%88%EB%B2%84%EC%8A%A4_%ED%83%80%EC%9A%94.png", "reason": "믿음직스럽고 긍정적인 눈빛이 타요와 닮았어요! 🚌"},
        "둘리": {"img": "https://upload.wikimedia.org/wikipedia/ko/thumb/5/52/%EC%95%84%EA%B8%B0%EA%B3%B5%EB%A3%A1_%EB%91%98%EB%A6%AC_%282009%29.jpg/250px-%EC%95%84%EA%B8%B0%EA%B3%B5%EB%A3%A1_%EB%91%98%EB%A6%AC_%282009%29.jpg", "reason": "개구쟁이 같으면서도 친근한 인상이 둘리를 닮았네요! 🦕"}
    },
    "일본 애니메이션": {
        "피카츄": {"img": "https://upload.wikimedia.org/wikipedia/en/a/a6/Pok%C3%A9mon_Pikachu_art.png", "reason": "귀엽고 사랑스러운 분위기가 피카츄와 싱크로율 100%! ⚡"},
        "토토로": {"img": "https://upload.wikimedia.org/wikipedia/en/0/02/My_Neighbor_Totoro_-_Tonari_no_Totoro_%28Movie_Poster%29.jpg", "reason": "푸근하고 듬직한 인상이 이웃집 토토로를 닮았어요! 🌳"},
        "나루토": {"img": "https://upload.wikimedia.org/wikipedia/en/9/9a/Naruto_Uzumaki.png", "reason": "의지가 강해 보이는 눈매가 나루토 같아요! 🍥"},
        "아냐 (스파이패밀리)": {"img": "https://upload.wikimedia.org/wikipedia/en/2/25/Anya_Forger.jpg", "reason": "큰 눈과 귀여운 표정이 아냐와 정말 비슷해요! 🥜"}
    },
    "미국 애니메이션 (디즈니/픽사)": {
        "엘사": {"img": "https://upload.wikimedia.org/wikipedia/en/thumb/5/5e/Elsa_from_Disney%27s_Frozen.png/220px-Elsa_from_Disney%27s_Frozen.png", "reason": "우아하고 차분한 분위기가 겨울왕국 엘사를 닮았어요! ❄️"},
        "미키마우스": {"img": "https://upload.wikimedia.org/wikipedia/en/d/d4/Mickey_Mouse.png", "reason": "밝게 웃는 모습과 긍정적인 에너지가 미키마우스 같아요! 🐭"},
        "올라프": {"img": "https://upload.wikimedia.org/wikipedia/en/thumb/7/7d/Olaf_from_Disney%27s_Frozen.png/220px-Olaf_from_Disney%27s_Frozen.png", "reason": "밝은 미소와 튀어나온 앞니가 사랑스러운 올라프 같아요! ⛄"}
    },
    "동물": {
        "강아지": {"img": "https://cdn.pixabay.com/photo/2016/12/13/05/15/puppy-1903313_1280.jpg", "reason": "순하고 쳐진 눈매가 사랑스러운 강아지상이에요! 🐶"},
        "고양이": {"img": "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg", "reason": "도도하고 매력적인 눈매가 전형적인 고양이상입니다! 🐱"},
        "토끼": {"img": "https://cdn.pixabay.com/photo/2016/10/26/13/43/rabbit-1771714_1280.jpg", "reason": "하얀 피부와 귀여운 앞니가 토끼를 연상케 해요! 🐰"},
        "곰": {"img": "https://cdn.pixabay.com/photo/2015/07/28/22/08/teddy-bear-865063_1280.jpg", "reason": "둥글둥글하고 푸근한 인상이 듬직한 곰상입니다! 🐻"}
    },
    "연예인 닮은꼴": {
        "아이유": {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/IU_for_Chamisul_advertising_campaign_2020_%281%29.png/220px-IU_for_Chamisul_advertising_campaign_2020_%281%29.png", "reason": "청순하고 귀여운 이미지가 아이유와 비슷해요! 🎤"},
        "수지": {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Suzy_at_Blue_Dragon_Series_Awards_Handprinting_Event_in_June_2023_02.jpg/220px-Suzy_at_Blue_Dragon_Series_Awards_Handprinting_Event_in_June_2023_02.jpg", "reason": "국민 첫사랑 같은 청초한 분위기가 수지를 닮았네요! 🌸"},
        "차은우": {"img": "https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Cha_Eun-woo_in_2024.jpg/220px-Cha_Eun-woo_in_2024.jpg", "reason": "조각 같은 이목구비가 얼굴 천재 차은우를 연상시켜요! ✨"}
    }
}

# ==========================================================
# 3. [NEW] 이미지 결과 처리 서비스 클래스 (타요 필터링 로직 포함)
# ==========================================================

class ImageFilterService:
    """
    이미지 분석 결과를 처리하고 필터링하는 서비스 클래스입니다.
    객체지향적 설계를 통해 관리와 수정이 용이하도록 구성했습니다.
    """

    # [관리 포인트] 단독으로 보여주고 싶은 캐릭터 키워드 리스트
    # 나중에 다른 캐릭터를 추가하고 싶으면 여기에 콤마(,)로 구분해 추가하면 됩니다.
    SPECIAL_CHARACTERS = ["Tayo", "타요", "The Little Bus", "Little Bus Tayo"]

    def process_results(self, results):
        """
        API 결과를 받아 비즈니스 로직(타요 필터링 등)을 수행합니다.
        
        :param results: [{'description': 'Tayo', 'score': 0.95}, ...] 형태의 리스트
        :return: 필터링된 결과 리스트
        """
        if not results:
            return []

        # 1. 점수(score) 기준 내림차순 정렬 (유사도가 높은 순서대로)
        # 데이터에 'score' 키가 없으면 에러 방지를 위해 0으로 처리
        sorted_results = sorted(results, key=lambda x: x.get('score', 0), reverse=True)
        
        # 가장 유사도가 높은 1순위 결과 가져오기
        top_match = sorted_results[0]
        
        # Google Vision 결과는 보통 'description'이나 'label'에 이름이 들어감
        # 안전하게 가져오기 위해 get 사용
        top_name = top_match.get('description') or top_match.get('name') or top_match.get('label') or ""

        # [수정 핵심 로직]: 1순위가 타겟 캐릭터(타요)인지 확인
        if self._is_target_character(top_name):
            # 타요가 맞다면 -> 리스트에 타요(1순위) 하나만 남기고 나머지 제거
            return [top_match]
        
        # 타요가 아니라면 -> 원래 리스트(정렬됨) 전체 반환
        return sorted_results

    def _is_target_character(self, name):
        """
        이름이 특별 키워드 리스트에 포함되는지 확인하는 내부 메서드
        """
        if not name:
            return False
        
        # 대소문자 구분 없이 키워드가 포함되어 있는지 확인
        # 예: "tayo" in "The Little Bus Tayo" -> True
        return any(keyword.lower() in name.lower() for keyword in self.SPECIAL_CHARACTERS)

# ---------------------------------------------------------
# [사용 편의성] 외부에서 바로 사용할 수 있도록 객체 생성
# ---------------------------------------------------------
image_filter = ImageFilterService()
# data/definitions.py (수정 버전)

# ... (위쪽 데이터는 그대로 두세요) ...

class ImageFilterService:
    SPECIAL_CHARACTERS = ["Tayo", "타요", "The Little Bus", "Little Bus Tayo"]

    def process_results(self, results):
        print(f"DEBUG: 필터링 전 데이터 개수: {len(results)}") # 확인용 로그
        if not results:
            return []

        # 1. 데이터 형태 정규화 (딕셔너리든 객체든 'score'와 'name'을 뽑아냄)
        refined_list = []
        for item in results:
            # 딕셔너리인 경우 vs 객체(속성)인 경우 모두 처리
            score = getattr(item, 'score', None) or item.get('score') or 0
            name = getattr(item, 'description', None) or item.get('description') or \
                   getattr(item, 'name', None) or item.get('name') or \
                   getattr(item, 'label', None) or item.get('label') or ""
            
            # 다루기 쉽게 딕셔너리로 변환해서 저장
            refined_list.append({'name': name, 'score': score, 'original': item})

        # 2. 점수순 정렬
        sorted_results = sorted(refined_list, key=lambda x: x['score'], reverse=True)
        top_match = sorted_results[0]
        
        print(f"DEBUG: 1순위 감지 결과: {top_match['name']} (점수: {top_match['score']})") # 확인용 로그

        # 3. 타요 필터링 로직
        if self._is_target_character(top_match['name']):
            print("DEBUG: 타요 감지됨! 단독 노출 처리합니다.")
            # 원본 객체 형태를 유지해서 반환
            return [top_match['original']]
        
        print("DEBUG: 타요 아님. 전체 결과 반환.")
        # 원본 객체 리스트 반환
        return [item['original'] for item in sorted_results]

    def _is_target_character(self, name):
        if not name: return False
        return any(keyword.lower() in name.lower() for keyword in self.SPECIAL_CHARACTERS)

image_filter = ImageFilterService()
