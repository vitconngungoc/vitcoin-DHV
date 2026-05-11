# Nhật Ký Thiết Lập Môi Trường (Setup Log)

**1. Lỗi gặp phải:**
Sau khi tạo thành công môi trường ảo `dataviz` bằng Anaconda và cài đặt đủ các thư viện. Tôi mở file `setup_test.ipynb` bằng VS Code và chạy thử lệnh `import pandas as pd` thì nhận được thông báo lỗi: 
`ModuleNotFoundError: No module named 'pandas'`

**2. Quá trình tìm giải pháp và Cách khắc phục:**
* **Nguyên nhân:** Tôi phát hiện ra rằng dù thư viện đã cài trong môi trường `dataviz`, nhưng VS Code đang tự động sử dụng trình thông dịch (Interpreter/Kernel) của môi trường Python gốc trên máy.
* **Giải pháp:** 1. Nhìn lên góc trên cùng bên phải của giao diện file notebook trong VS Code.
    2. Click vào mục chọn Kernel (thường đang hiện chữ `Python 3.x.x`).
    3. Chọn "Select Another Kernel..." -> "Python Environments" -> Chọn môi trường `dataviz` mà tôi đã tạo.
    4. Chạy lại cell code và các thư viện đã được import thành công.

**3. Link nguồn tham khảo:**
* Tài liệu chính thức của VS Code về Jupyter: https://code.visualstudio.com/docs/datascience/jupyter-notebooks#_work-with-python-environments