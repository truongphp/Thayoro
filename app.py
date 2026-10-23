import streamlit as st
import json
import os

FILE_NAME = "quy_nhom.json"

# Cấu hình tiêu đề trang web
st.set_page_config(page_title="Sổ Quỹ Nhóm 6 Người", page_icon="💰", layout="centered")

# 1. ĐỌC DỮ LIỆU TỪ FILE JSON (Trí nhớ vĩnh cửu)
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        ds_chi_tieu = json.load(f)
else:
    ds_chi_tieu = [{"ten": "Liên hoan", "tien": 600000}]

# 2. GIAO DIỆN WEB: TIÊU ĐỀ & 3 Ô TỔNG QUAN
st.title("📊 Sổ Chi Tiêu Nhóm 6 Người")
st.caption("Ứng dụng chạy 100% bằng Python trên Web")

# Tính toán số liệu
tong_chi = sum(item["tien"] for item in ds_chi_tieu)
moi_nguoi = int(tong_chi / 6)

col1, col2, col3 = st.columns(3)
col1.metric("📌 Số khoản chi", f"{len(ds_chi_tieu)} mục")
col2.metric("💸 Tổng tiền chi", f"{tong_chi:,} đ")
col3.metric("👤 Mỗi người (÷6)", f"{moi_nguoi:,} đ")

st.divider()

# 3. GIAO DIỆN WEB: FORM NHẬP THÊM KHOẢN CHI MỚI
st.subheader("➕ Thêm Khoản Chi Mới")
with st.form("form_nhap", clear_on_submit=True):
    ten_moi = st.text_input("Tên khoản chi (VD: Ăn lẩu, Cầu lông):")
    tien_moi = st.number_input("Số tiền chi (VNĐ):", min_value=0, step=10000, value=0)
    nut_luu = st.form_submit_button("💾 Lưu Vào Quỹ")

    if nut_luu:
        if ten_moi.strip() != "" and tien_moi > 0:
            # Nhét vào danh sách
            ds_chi_tieu.append({"ten": ten_moi.strip(), "tien": int(tien_moi)})
            # Lưu thẳng vào file JSON
            with open(FILE_NAME, "w", encoding="utf-8") as f:
                json.dump(ds_chi_tieu, f, ensure_ascii=False, indent=2)
            st.success(f"✔ Đã thêm khoản '{ten_moi}' thành công!")
            st.rerun()
        else:
            st.error("✖ Vui lòng nhập đầy đủ tên và số tiền lớn hơn 0!")

# 4. GIAO DIỆN WEB: BẢNG KÊ CHI TIẾT
st.subheader("📋 Danh Sách Các Khoản Đã Chi")
for idx, item in enumerate(ds_chi_tieu, 1):
    chia_deu = int(item["tien"] / 6)
    st.write(f"**#{idx}. {item['ten']}** — Tổng: `{item['tien']:,} đ` ➔ *Mỗi người: {chia_deu:,} đ*")
