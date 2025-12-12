# -----------------------------------------------------------
# 파일 경로: data/definitions.py
# 설명: 데이터 창고 (진짜 이미지 URL 탑재 완료!)
# -----------------------------------------------------------

# 톤 설명 사전
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
    "여름 뮤트": {"여자": ("문채원", "
