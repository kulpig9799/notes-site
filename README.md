# Notes Site (MkDocs + GitHub Pages)

Website ghi chú cá nhân chia thành 6 mục: DBA, SQL, Linux, Tối ưu SQL, Python, Data Engineer.

## Yêu cầu
- Python 3.8+
- pip

## Cài đặt
```bash
pip install -r requirements.txt
```

## Chạy dev
```bash
mkdocs serve    # http://127.0.0.1:8000
```

## Deploy lên GitHub Pages
```bash
git init
git remote add origin https://github.com/<username>/notes-site.git
git add .
git commit -m "first commit"
git branch -M main
git push -u origin main

mkdocs gh-deploy --force
```
Sau khi deploy, mở Settings → Pages để lấy link, dạng: `https://<username>.github.io/notes-site/`

## Thêm ghi chú mới
1. Tạo file `.md` trong `docs/<muc>/` (ví dụ `docs/sql/join.md`)
2. Mở `mkdocs.yml` thêm đường dẫn vào `nav` để hiển thị trên menu
3. Chạy `mkdocs serve` để xem kết quả
4. Push và `mkdocs gh-deploy --force` để cập nhật website online

## Nhập hàng loạt file .txt
```bash
python scripts/convert_txt_to_md.py /path/den/thu_muc_txt
```
Script sẽ tạo file `.md` tương ứng trong `docs/notes/` (nếu chưa có sẽ tạo) và in gợi ý `nav` để bạn copy vào `mkdocs.yml`.

## Nhập .docx
- Khuyến nghị dùng **Pandoc** (cài từ https://pandoc.org/installing.html), sau đó:
```bash
pandoc "your.docx" -f docx -t markdown -o docs/<muc>/your.md
```
- Hoặc dùng script `scripts/convert_docx_to_md.py` (cần `pip install python-docx`):
```bash
python scripts/convert_docx_to_md.py /path/den/thu_muc_docx docs/<muc>
```