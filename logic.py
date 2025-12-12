# -----------------------------------------------------------
# 파일명: logic.py (기능 완전 복구 + 안전 모드)
# -----------------------------------------------------------
import os
import csv
import json
from datetime import datetime

# [중요] 상단 import에는 무거운 라이브러리(Pandas, PIL, CV2) 없음!

RESULTS_CSV = "user_results.csv"

def fix_image_orientation(img):
    from PIL import Image, ExifTags # 필요할 때 로딩
    try:
        exif = img._getexif()
        if exif is not None:
            for k, v in ExifTags.TAGS.items():
                if v == "Orientation":
                    orientation = exif.get(k)
                    if orientation == 3: img = img.rotate(180, expand=True)
                    elif orientation == 6: img = img.rotate(270, expand=True)
                    elif orientation == 8: img = img.rotate(90, expand=True)
                    break
    except: pass
    return img

def draw_color_boxes(colors, title):
    from PIL import Image, ImageDraw # 필요할 때 로딩
    box_size = 180; height = 60
    img = Image.new("RGB", (box_size * len(colors), height), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for i, rgb in enumerate(colors):
        draw.rectangle([i * box_size, 0, (i+1) * box_size, height], fill=rgb)
    return img

def circular_mean_hue(h_deg_values):
    import numpy as np
    rad = np.deg2rad(h_deg_values)
    xbar = np.mean(np.cos(rad)); ybar = np.mean(np.sin(rad))
    return float((np.rad2deg(np.arctan2(ybar, xbar)) + 360) % 360)

def map_to_pccs_10(h, s, v):
    is_warm = (0 <= h <= 70) or (330 <= h <= 360)
    is_cool = (170 <= h <= 260)
    if is_warm:
        if v >= 0.75: return "봄 브라이트" if s >= 0.55 else "봄 라이트"
        else: return "가을 뮤트" if s <= 0.4 else "가을 딥" if v <= 0.55 else "가을 스트롱"
    if is_cool:
        if v >= 0.75: return "여름 브라이트" if s >= 0.55 else "여름 라이트"
        else: return "여름 뮤트" if s <= 0.4 else "겨울 딥" if v <= 0.5 else "겨울 브라이트"
    if v >= 0.75 and s < 0.5: return "여름 라이트"
    if s < 0.4: return "여름 뮤트"
    if v < 0.5: return "겨울 딥"
    return "겨울 브라이트"

def tone_to_season(tone): return tone.split()[0]

def analyze_body_shape(img_array):
    h, w, _ = img_array.shape
    ratio = h / w if w > 0 else 1
    if ratio >= 1.9: return "전체적으로 세로 비율이 길게 느껴지는 체형입니다. 롱실루엣이 잘 어울릴 수 있어요."
    elif ratio >= 1.6: return "균형 잡힌 표준적인 비율에 가까운 체형입니다. 대부분의 기본 핏이 잘 어울릴 수 있어요."
    else: return "상체와 하체 비율이 안정적으로 느껴지는 체형입니다. 상·하의 비율을 나누는 코디가 잘 어울릴 수 있어요."

def save_result(service, name, byear, gender, h, w, res, extra=None):
    row = {"timestamp": datetime.now().isoformat(), "service": service, "name": name, "birth_year": byear, "gender": gender, "height": h, "weight": w, "result": res, "extra": json.dumps(extra or {})}
    exists = os.path.exists(RESULTS_CSV)
    with open(RESULTS_CSV, "a", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        if not exists: writer.writeheader()
        writer.writerow(row)

def get_results_df():
    if not os.path.exists(RESULTS_CSV): return []
    try:
        import pandas as pd # 여기서 판다스 로딩
        return pd.read_csv(RESULTS_CSV)
    except: return []