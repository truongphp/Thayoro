import json
import os

FILE_NAME = "quy_nhom.json"

# 1. Đọc dữ liệu cũ nếu đã tồn tại file
if os.path.exists(FILE_NAME):
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        ds_chi_tieu = json.load(f)
    print("📂 Đã tìm thấy dữ liệu cũ:")
    for muc in ds_chi_tieu:
        print(f" - {muc['ten']}: {muc['tien']:,} đ")
else:
    print("✨ Chưa có file dữ liệu, tạo danh sách mới hoàn toàn!")
    ds_chi_tieu = [{"ten": "Liên hoan", "tien": 600000}]

# 2. Nhập thêm khoản chi mới
ten_moi = input("\n👉 Nhập tên khoản chi mới: ")
tien_moi = int(input("👉 Nhập số tiền: "))

ds_chi_tieu.append({"ten": ten_moi, "tien": tien_moi})

# 3. Ghi đè toàn bộ danh sách xuống ổ đĩa
with open(FILE_NAME, "w", encoding="utf-8") as f:
    json.dump(ds_chi_tieu, f, ensure_ascii=False, indent=2)

print(f"\n💾 Đã lưu thành công vào file '{FILE_NAME}'!")
