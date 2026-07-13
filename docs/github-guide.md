# 🖥️ Hướng Dẫn Quản Trị & Đẩy Kho Tri Thức Lên GitHub

Kho tri thức này được thiết kế để lưu trữ dưới dạng một **GitHub Repository** độc lập. Dưới đây là các bước để khởi tạo Git, đẩy kho tri thức lên tài khoản GitHub của FinPeace và tích hợp nó.

---

## 1. Các Bước Đẩy Kho Tri Thức Lên GitHub Lần Đầu

Chạy các lệnh sau tại thư mục `/Users/tuananhnguyen/workspace-gravity/knowledge-base`:

```bash
# 1. Khởi tạo Git repository local
git init

# 2. Thêm tất cả các file vào Git theo dõi
git add .

# 3. Commit phiên bản đầu tiên
git commit -m "feat: init FinPeace knowledge base with core book and international references"

# 4. Thiết lập nhánh chính là main
git branch -M main

# 5. Thêm liên kết với repository trống được tạo trên GitHub của bạn
# (Thay thế URL bằng URL repository thực tế của bạn)
git remote add origin https://github.com/username/finpeace-knowledge-base.git

# 6. Đẩy toàn bộ tài liệu lên GitHub
git push -u origin main
```

---

## 2. Hướng Dẫn Tải Lên GitHub Wiki

Nếu bạn muốn biến kho tri thức này thành một trang **GitHub Wiki** tích hợp trực tiếp trong repository dự án chính của FinPeace:

1.  Truy cập vào repository chính trên GitHub, chọn tab **Wiki** ở thanh menu trên cùng.
2.  Nhấp vào nút **Create the first page** và tạo một trang trống bất kỳ.
3.  Sao chép URL clone của Wiki đó (thường có đuôi `.wiki.git`, ví dụ: `https://github.com/username/main-repo.wiki.git`).
4.  Clone Git Wiki đó về máy local của bạn.
5.  Sao chép toàn bộ các file `.md` và thư mục `docs/` trong thư mục `knowledge-base/` này vào trong thư mục Wiki vừa clone.
6.  Chạy lệnh `git add .`, `git commit -m "Update wiki docs"` và `git push` để đẩy lên trực tiếp. Giao diện GitHub Wiki sẽ tự động hiển thị cây thư mục tài liệu này của bạn.

---

## 3. Tích Hợp Vào Dự Án Chính Dưới Dạng Submodule

Nếu bạn muốn nhúng trực tiếp kho tri thức này vào trong repository dự án Web chính của FinPeace (`finpeace-web`) để chia sẻ tài nguyên sử dụng chung:

```bash
# Di chuyển vào thư mục dự án chính
cd /Users/tuananhnguyen/workspace-gravity/finpeace-web

# Thêm kho tri thức làm Git Submodule
git submodule add https://github.com/username/finpeace-knowledge-base.git src/knowledge-base

# Đồng bộ và cập nhật submodule
git submodule init
git submodule update
```
