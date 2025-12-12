# -----------------------------------------------------------
# 파일 경로: data/definitions.py
# 설명: 데이터 창고 (캐릭터 종류 대폭 추가!)
# -----------------------------------------------------------

# [1] 퍼스널 컬러 기본 데이터 (유지)
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
    "봄 라이트": {"여자": ("윤아", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTM1/MDAxNzYyNDM5MzA3NDI1.T2rxWI6y8G0KOX-pdK4BcAXgCEUl-2UUOHU9WVgtZCMg.uI3ecF_zdMm_guc5BmRIwcZldTBYdPBzu3u5rqqj2J8g.JPEG/IMG％EF％BC％BF1192.JPG?type=w966"), "남자": ("이종석", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNzUg/MDAxNzYyNDM5MzA4MzU2.sgx5YYgOJeH6tIQ-dfmq6Zt-u_LoLhWvFeNpUvvnHhEg.3Mwa48B-biz1QudsFRHSsLPkcuXJJIkbHWwf-aYegiAg.JPEG/IMG％EF％BC％BF1225.JPG?type=w966")},
    "봄 브라이트": {"여자": ("나연", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjAz/MDAxNzYyNDM5MzA3Nzk1.gmEqXNzB37B2wBTgrVx4w6JDMlcaCNtqIFSnr5T8UCwg.VjDPhKIS95U1AB33R8KfuleDxyRQ_ZB9CZefvdTNSpsg.JPEG/IMG％EF％BC％BF1206.JPG?type=w966"), "남자": ("강다니엘", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjY1/MDAxNzYyNDM5MzA4MjU3.f0OZ-_VnhEI33cm0IcEuUITdmX6X8HORMrUzWCv1d7Ug.8iSY5eGRrAfNUEhvH0KehClXPBPUKeKnZEF79olvxNYg.JPEG/IMG％EF％BC％BF1227.JPG?type=w966")},
    "여름 라이트": {"여자": ("장원영", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjc1/MDAxNzYyNDM5MzA4MTQ5.ewVz5OQExgMd60ij3x5v1IJTSFIpA9syFeb7_hi3I1kg.ZV73W-Lvr8U2bh-C31jX_kZjdKvcrkNGkw9bhsDHesgg.JPEG/IMG％EF％BC％BF1222.JPG?type=w966"), "남자": ("정해인", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNTMg/MDAxNzYyNDM5MzA3Nzgz.GO7RDL060ifLkDNT0xixz1kD9tHebrfG1ONvQhfmU8sg.321vBWpCBZuZGURaIJM69c0KWgwYMGBsPSuHsNbgaYcg.JPEG/IMG％EF％BC％BF1230.JPG?type=w966")},
    "여름 브라이트": {"여자": ("은하", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTc1/MDAxNzYyNDM5MzA4OTk3.XyRCgDMBrhObmZydV-7E8XWWBytUp7_7ta2l3XREYOUg.MrkWtbrcCdX0wZ3g-xKerOWoAVDJot8wEe3j7E45T_Mg.JPEG/IMG％EF％BC％BF1224.JPG?type=w966"), "남자": ("뷔", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTYz/MDAxNzYyNDM5MzA4NDE1.NA54xC6oQosEfDWvfgmvnltIvdpYa_Z9klksZELld6wg.J262fp66ywuKByMfaaYNFqFPSZKQu89N0QSEA8GuLuog.JPEG/IMG％EF％BC％BF1236.JPG?type=w966")},
    "여름 뮤트": {"여자": ("문채원", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjgg/MDAxNzYyNDM5MzA3NDg0.YIstb7sU0wswDpygeoQIMwVh9vVkMuhrI41ndLMqPkIg.HHcvHaCoKnMGbQ7irGsYEe6PEtDV5ye2Nc53GC5a5Iwg.JPEG/IMG％EF％BC％BF1198.JPG?type=w966"), "남자": ("송강", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjYw/MDAxNzYyNDM5MzA4OTIz.vBmWxVKj7Dco3PTkrigIXG3R2N_Dj-4QVpQtFiE_-q4g.GVzu4Lw-QZTCjKe_GHcupZ6TEmKAPRkXN0ihWi1kBPMg.JPEG/IMG％EF％BC％BF1201.JPG?type=w966")},
    "가을 뮤트": {"여자": ("제니", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfODYg/MDAxNzYyNDM5MzA3OTA1.NLvRSbc3iZzDH_aKTbQfBBovpza2OvEFEOgZcXubatwg.Kfs2Empot5CsxTb_nCOJz4_VWHB53mDVkfRTtvFqBB8g.JPEG/IMG％EF％BC％BF1221.JPG?type=w966"), "남자": ("서강준", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNDYg/MDAxNzYyNDM5MzA3NDQ6.EVmfObIqUCqbIgkLv0mcIHQsTIljnLb2gdRXGitKdnog.FeE4c0NscxPFePQ4Qhj6LUGsvQPE6y2TrkX8Qc3HThIg.JPEG/IMG％EF％BC％BF1237.JPG?type=w966")},
    "가을 스트롱": {"여자": ("조이", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjE1/MDAxNzYyNDM5MzA8NTE2.AGNHRbZMl93a6NwjTt76N9EBBZ8rzVZTEbt3mn5-BRYg.CCSBsMGuO3E4BfInjwoNWn6fAl85PhNn-kWRgPC6p1Qg.JPEG/output％EF％BC％BF3817396647.jpg?type=w966"), "남자": ("강태오", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjY6/MDAxNzYyNDM5MzA7NDg7.nM3UvJAe4uPo3Pc1HT40vYbzRk7cCefKLFUZRpBjOHcg.22tuUdmI-mklIm793R8Sw0smpnqebyt5QgHzu0kUK0Eg.JPEG/output％EF％BC％BF2543490798.jpg?type=w966")},
    "가을 딥": {"여자": ("김유정", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfNiAg/MDAxNzYyNDM5MzA8OTg6.SLp61r-OMfbkn0euIMLhk2o2ZYGANT9fKoHE2S5B6lAg.umJC53HxGvx0kDdsZEL6jeZD5gLfuWPy9A3ce9tgIfAg.JPEG/IMG％EF％BC％BF1212.JPG?type=w966"), "남자": ("공유", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTU1/MDAxNzYyNDM5MzA8Nzk8.xN33tfvJjPbOHU13TZhzBf8FM0G1yCLp2oFSSHGyqZAg.3mlA7xcK21r6p7rdfl1UXf1fr_8nkjVi0h6rzeaGvH0g.JPEG/IMG％EF％BC％BF1238.JPG?type=w966")},
    "겨울 브라이트": {"여자": ("카리나", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjkg/MDAxNzYyNDM5MzA7N7I0.vmX-1402X4TAKcSD1DtyrGBqAbFDBsYS5GottDNPMj0g.xsjf_Hcyax48NNMp_VhE10ICNjCLPbcDMK3GFSIYroUg.JPEG/IMG％EF％BC％BF1217.JPG?type=w966"), "남자": ("조정석", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTY6/MDAxNzYyNDM5MzA5MTI4.-ohQnzHZ8xK8fnjgWQU1wg9Yxcr0tJwxy6CrV10Hpl4g.wmGPYOHyE-c7Fgh60uye6fuSujLGUcQ4BSMQJRR7PP0g.JPEG/IMG％EF％BC％BF1244.JPG?type=w966")},
    "겨울 딥": {"여자": ("지수", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMTIz/MDAxNzYyNDM5MzA4OTM4.3sc7OS-eHnjtSQ-8JRgjVFVDxzGihBNxhKqgZtZifdcg.sG6vJqOREgXxvXQeD7Acb9LEzxSYM98r7PoElLlgQpUg.JPEG/IMG％EF％BC％BF1209.JPG?type=w966"), "남자": ("이수혁", "https://mblogthumb-phinf.pstatic.net/MjAyNTExMDZfMjc0/MDAxNzYyNDM5MzA8ODM7._qzsWliOJ9QxBy8Co8KdQOwR6oj8l7ePdot8o99kx2gg.jvtnAbBjBxUajgXjAQSJkNqinB8Eibdfu5DMcTdAt4cg.JPEG/IMG％EF％BC％BF1231.JPG?type=w966")},
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

# [NEW] 캐릭터 매칭 데이터 (대폭 확장!)
# ※ 이미지 주소는 샘플 URL입니다. 나중에 실제 주소로 하나씩 채워주세요!
TEMP_IMG = "https://via.placeholder.com/300?text=Check+Image+URL"

KIDS_CHARACTERS = {
    "한국 애니메이션": {
        "뽀로로": {"img": "https://i.namu.wiki/i/qF6l1tVz8gq5x7v6u4wX5y7z9a1b2c3d4e5f6g7h8i9j0k.webp", "reason": "동글동글한 얼굴과 호기심 가득한 눈빛이 뽀로로와 똑 닮았어요! 🤓"},
        "루피 (잔망루피)": {"img": "https://mblogthumb-phinf.pstatic.net/MjAyMjAzMjhfMjYy/MDAxNjQ4NDQwNjYyNzM4.3-1s5-k5y6z7A8b9C0d1E2f3g4h5i6j7k8l9m0n.png?type=w800", "reason": "귀여운 볼살과 부드러운 인상이 잔망루피를 연상시켜요! 🌸"},
        "하츄핑 (티니핑)": {"img": TEMP_IMG, "reason": "사랑스럽고 애교 넘치는 분위기가 캐치 티니핑의 하츄핑 같아요! 💖"},
        "크롱": {"img": "https://i.namu.wiki/i/2a3b4c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9r0s.webp", "reason": "장난기 넘치는 표정과 활발한 에너지가 크롱과 찰떡입니다! 🦖"},
        "타요": {"img": "https://i.namu.wiki/i/1a2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s.webp", "reason": "믿음직스럽고 긍정적인 눈빛이 꼬마버스 타요와 닮았어요! 🚌"},
        "자두": {"img": "https://i.namu.wiki/i/9a8b7c6d5e4f3g2h1i0j9k8l7m6n5o4p3q2r1s.webp", "reason": "명랑하고 쾌활한 분위기가 안녕 자두야의 자두 같아요! 🍒"},
        "둘리": {"img": "https://i.namu.wiki/i/5a6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s.webp", "reason": "개구쟁이 같으면서도 친근한 인상이 둘리를 닮았네요! 🦕"},
        "신비 (신비아파트)": {"img": TEMP_IMG, "reason": "개성 넘치고 유쾌한 표정이 신비아파트의 신비를 닮았어요! 👻"},
        "라바 (옐로우)": {"img": TEMP_IMG, "reason": "익살스럽고 재미있는 표정이 라바 옐로우랑 비슷해요! 🐛"}
    },
    "일본 애니메이션": {
        "루피 (원피스)": {"img": "https://i.namu.wiki/i/3a4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s.webp", "reason": "시원시원한 미소와 열정적인 눈빛이 해적왕 루피를 닮았어요! 🏴‍☠️"},
        "나루토": {"img": "https://i.namu.wiki/i/4a5b6c7d8e9f0g1h2i3j4k5l6m7n8o9p0q1r2s.webp", "reason": "장난기 있으면서도 의지가 강해 보이는 눈매가 나루토 같아요! 🍥"},
        "피카츄": {"img": "https://i.namu.wiki/i/6a7b8c9d0e1f2g3h4i5j6k7l8m9n0o1p2q3r4s.webp", "reason": "귀엽고 사랑스러운 분위기가 피카츄와 싱크로율 100%! ⚡"},
        "토토로": {"img": "https://i.namu.wiki/i/7a8b9c0d1e2f3g4h5i6j7k8l9m0n1o2p3q4r5s.webp", "reason": "푸근하고 듬직한 인상이 이웃집 토토로를 닮았어요! 🌳"},
        "짱구": {"img": TEMP_IMG, "reason": "장난기 가득한 눈썹과 볼살이 못말리는 짱구 같아요! 🍪"},
        "도라에몽": {"img": TEMP_IMG, "reason": "둥글둥글하고 친근한 얼굴이 도라에몽을 쏙 빼닮았네요! 🔔"},
        "하울": {"img": "https://i.namu.wiki/i/8a9b0c1d2e3f4g5h6i7j8k9l0m1n2o3p4q5r6s.webp", "reason": "신비롭고 매력적인 분위기가 하울과 비슷하네요! ✨"},
        "코난": {"img": "https://i.namu.wiki/i/0a1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s.webp", "reason": "지적이고 예리한 눈빛이 명탐정 코난을 연상시켜요! 👓"},
        "아냐 (스파이패밀리)": {"img": "https://i.namu.wiki/i/1b2c3d4e5f6g7h8i9j0k1l2m3n4o5p6q7r8s9t.webp", "reason": "큰 눈과 다양한 표정이 아냐와 정말 비슷해요! 🥜"},
        "탄지로 (귀멸의 칼날)": {"img": TEMP_IMG, "reason": "선하고 올곧은 눈빛이 탄지로를 닮았어요! 🌊"}
    },
    "미국 애니메이션 (디즈니/픽사)": {
        "엘사": {"img": "https://i.namu.wiki/i/2b3c4d5e6f7g8h9i0j1k2l3m4n5o6p7q8r9s0t.webp", "reason": "우아하고 차분한 분위기가 겨울왕국 엘사를 닮았어요! ❄️"},
        "우디": {"img": "https://i.namu.wiki/i/3b4c5d6e7f8g9h0i1j2k3l4m5n6o7p8q9r0s1t.webp", "reason": "길쭉한 얼굴형과 선한 인상이 토이스토리 우디와 비슷해요! 🤠"},
        "버즈": {"img": "https://i.namu.wiki/i/4b5c6d7e8f9g0h1i2j3k4l5m6n7o8p9q0r1s2t.webp", "reason": "강인한 턱선과 자신감 넘치는 표정이 버즈 라이트이어 같아요! 🚀"},
        "미키마우스": {"img": "https://upload.wikimedia.org/wikipedia/en/thumb/d/d4/Mickey_Mouse.png/220px-Mickey_Mouse.png", "reason": "밝게 웃는 모습과 긍정적인 에너지가 미키마우스 같아요! 🐭"},
        "심바": {"img": "https://i.namu.wiki/i/5b6c7d8e9f0g1h2i3j4k5l6m7n8o9p0q1r2s3t.webp", "reason": "당당하고 용맹한 기운이 라이온킹 심바를 닮았네요! 🦁"},
        "라푼젤": {"img": "https://i.namu.wiki/i/6b7c8d9e0f1g2h3i4j5k6l7m8n9o0p1q2r3s4t.webp", "reason": "호기심 많고 큰 눈망울이 라푼젤과 똑 닮았어요! 🍳"},
        "미니언즈": {"img": TEMP_IMG, "reason": "유쾌하고 엉뚱한 매력이 미니언즈를 닮았어요! 🍌"},
        "주디 (주토피아)": {"img": TEMP_IMG, "reason": "초롱초롱한 눈망울과 토끼 같은 이미지가 주디 홉스 같아요! 🐰👮‍♀️"},
        "닉 (주토피아)": {"img": TEMP_IMG, "reason": "능글맞으면서도 매력적인 눈매가 여우 닉 와일드를 닮았어요! 🦊"},
        "올라프": {"img": TEMP_IMG, "reason": "밝은 미소와 튀어나온 앞니가 사랑스러운 올라프 같아요! ⛄"}
    },
    "동물": {
        "강아지": {"img": "https://cdn.pixabay.com/photo/2016/12/13/05/15/puppy-1903313_1280.jpg", "reason": "순하고 쳐진 눈매가 사랑스러운 강아지상이에요! 🐶"},
        "고양이": {"img": "https://cdn.pixabay.com/photo/2017/02/20/18/03/cat-2083492_1280.jpg", "reason": "도도하고 매력적인 눈매가 전형적인 고양이상입니다! 🐱"},
        "여우": {"img": "https://cdn.pixabay.com/photo/2015/04/10/01/41/fox-715588_1280.jpg", "reason": "가로로 긴 눈과 날렵한 턱선이 매력적인 여우상이에요! 🦊"},
        "토끼": {"img": "https://cdn.pixabay.com/photo/2016/10/26/13/43/rabbit-1771714_1280.jpg", "reason": "하얀 피부와 귀여운 앞니가 토끼를 연상케 해요! 🐰"},
        "곰": {"img": "https://cdn.pixabay.com/photo/2015/07/28/22/08/teddy-bear-865063_1280.jpg", "reason": "둥글둥글하고 푸근한 인상이 듬직한 곰상입니다! 🐻"},
        "공룡": {"img": "https://cdn.pixabay.com/photo/2014/10/22/16/47/dinosaur-498263_1280.jpg", "reason": "이목구비가 뚜렷하고 남성적인 매력이 넘치는 공룡상이에요! 🦖"},
        "햄스터": {"img": TEMP_IMG, "reason": "볼이 빵빵하고 귀여운 이미지가 햄스터를 닮았어요! 🐹"},
        "사슴": {"img": TEMP_IMG, "reason": "목이 길고 눈망울이 깊은 사슴상이에요! 🦌"},
        "늑대": {"img": TEMP_IMG, "reason": "날카롭고 차가운 도시적인 분위기가 늑대 같아요! 🐺"},
        "쿼카": {"img": TEMP_IMG, "reason": "항상 웃는 듯한 입꼬리가 세상 행복한 쿼카를 닮았어요! 🐻"}
    },
    "연예인 닮은꼴": {
        "아이유": {"img": "https://i.namu.wiki/i/IU_Image.webp", "reason": "청순하고 귀여운 이미지가 아이유와 비슷해요! 🎤"},
        "수지": {"img": "https://i.namu.wiki/i/Suzy_Image.webp", "reason": "국민 첫사랑 같은 청초한 분위기가 수지를 닮았네요! 🌸"},
        "차은우": {"img": "https://i.namu.wiki/i/Eunwoo_Image.webp", "reason": "조각 같은 이목구비가 얼굴 천재 차은우를 연상시켜요! ✨"},
        "송강": {"img": "https://i.namu.wiki/i/Songkang_Image.webp", "reason": "소년미와 멍뭉미가 공존하는 매력이 송강과 닮았어요! 🦋"},
        "제니": {"img": "https://i.namu.wiki/i/Jennie_Image.webp", "reason": "고급스럽고 힙한 분위기가 제니와 똑 닮았네요! 👑"},
        "박보검": {"img": "https://i.namu.wiki/i/Bogum_Image.webp", "reason": "선하고 반듯한 이미지가 박보검을 닮았어요! 🦌"},
        "장원영": {"img": TEMP_IMG, "reason": "인형 같은 비율과 화려한 이목구비가 장원영을 닮았어요! 🎀"},
        "카리나": {"img": TEMP_IMG, "reason": "CG보다 더 CG 같은 비현실적인 외모가 카리나 같아요! 💜"},
        "뷔 (BTS)": {"img": TEMP_IMG, "reason": "세계 미남 1위의 아우라가 느껴지는 뷔 닮은꼴! 🐯"},
        "손석구": {"img": TEMP_IMG, "reason": "치명적이고 섹시한 어른미가 손석구를 닮았네요! 🥃"}
    }
}
