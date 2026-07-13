import os
import re

kb_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
md_link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')

def validate_links():
    print("--- BẮT ĐẦU KIỂM TRA LIÊN KẾT NỘI BỘ KNOWLEDGE BASE ---")
    has_error = False
    
    for root, dirs, files in os.walk(kb_root):
        # Bỏ qua thư mục ẩn
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        
        for file in files:
            if not file.lower().endswith(".md"):
                continue
                
            file_path = os.path.join(root, file)
            rel_file_path = os.path.relpath(file_path, kb_root)
            
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                
            links = md_link_pattern.findall(content)
            for text, link in links:
                # Chỉ kiểm tra liên kết cục bộ (local links), bỏ qua các liên kết ngoài (http/https/file://)
                if link.startswith(("http://", "https://", "mailto:", "file://", "#")):
                    continue
                    
                # Phân tách phần neo (anchor) nếu có (ví dụ: path/to/file.md#section)
                clean_link = link.split("#")[0]
                if not clean_link:
                    continue
                    
                # Tính toán đường dẫn tuyệt đối của liên kết đích
                target_path = os.path.abspath(os.path.join(root, clean_link))
                
                if not os.path.exists(target_path):
                    has_error = True
                    print(f"❌ LỖI LIÊN KẾT HỎNG ở file: {rel_file_path}")
                    print(f"   -> Link đích không tồn tại: '{link}' (Đường dẫn thử nghiệm: {target_path})")
                    print()
                    
    if not has_error:
        print("✅ THÀNH CÔNG: Tất cả các liên kết nội bộ trong Knowledge Base đều hợp lệ!")
    else:
        print("❌ THẤT BẠI: Phát hiện có liên kết hỏng trong Knowledge Base!")

if __name__ == "__main__":
    validate_links()
