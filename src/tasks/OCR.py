import cv2
import pytesseract
import numpy as np
import streamlit as st
from PIL import Image
import time

class OCRApp:
    """
    Lớp Ứng dụng OCR cho phép nhận dạng ký tự trên hình ảnh.
    Attributes:
        tessdata_dir_config (str): Cấu hình thư mục tessdata cho thư viện pytesseract.
        image (PIL.Image): Hình ảnh được tải lên cho OCR.
    Methods:
        __init__(): Khởi tạo ứng dụng OCR và thiết lập các thuộc tính cần thiết.
        refresh(): Làm mới biến self.image thành None.
        display_interface(): Hiển thị giao diện người dùng và thực hiện OCR khi người dùng tải lên hình ảnh.
        howtouse(): Hiển thị hướng dẫn sử dụng chức năng OCR.
        perform_ocr(image: PIL.Image, language: str): Thực hiện OCR trên hình ảnh.
        run(): Chạy ứng dụng OCR.
    """

    def __init__(self):
        """
        Khởi tạo ứng dụng OCR.
        Thiết lập đường dẫn tesseract_cmd và tessdata_dir_config để sử dụng thư viện pytesseract.
        """
        pytesseract.pytesseract.tesseract_cmd = './Tesseract-OCR/tesseract.exe'
        self.tessdata_dir_config = '--tessdata-dir "./Tesseract-OCR/tessdata" --psm 6'
        self.image = None

    def refresh(self):
        """
        Làm mới biến self.image thành None.
        """
        self.image = None

    def display_interface(self):
        """
        Hiển thị giao diện người dùng.
        Hiển thị tiêu đề và chọn ngôn ngữ. Cho phép người dùng tải lên hình ảnh và thực hiện OCR.
        """
        st.title(":red[Optical Character Recognition]")
        self.howtouse()
        language = st.selectbox("Select language:", ("English", "VietNamese", "Korean", "Japanese", "Chinese"))
        language = {"English": 'eng', "VietNamese": 'vie', "Korean": 'kor', "Japanese": 'jpn', "Chinese": 'chi_sim'}[language]
        uploaded_file = st.file_uploader("Upload an image (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])
        
        if uploaded_file is not None:
            self.image = Image.open(uploaded_file)
            st.image(self.image)
            
            if st.button("Start"):
                with st.spinner('Wait for it...'):
                    time.sleep(3)
                result = self.perform_ocr(self.image, language)
                st.write(result)

    def howtouse(self):
        """
        Hiển thị hướng dẫn sử dụng chức năng OCR.
        """
        st.markdown("**Hướng dẫn sử dụng chức năng OCR:**")
        st.markdown("Bước 1: Chọn ngôn ngữ bạn muốn phát hiện bên trong ảnh.")
        st.markdown("Bước 2: Tải ảnh từ máy bạn lên web bằng cách nhấn **Browse files**.")
        st.markdown("Bước 3: Nhấn **Start** để xem kết quả")
        st.markdown("""**Lưu ý: Chức năng này hoạt động tốt với những hình ảnh chứa ký tự đánh máy, 
                        những ký tự viết tay sẽ không được nhận diện chính xác.**""")

    def perform_ocr(self, image, language):
        """
        Thực hiện OCR trên hình ảnh.
        Parameters:
            - image: Hình ảnh để thực hiện OCR.
            - language: Ngôn ngữ được sử dụng cho OCR.
        Returns:
            Kết quả văn bản từ OCR.
        """
        image = np.array(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        gray = cv2.medianBlur(gray, 3)
        text = pytesseract.image_to_string(gray, lang=language, config=self.tessdata_dir_config)
        return text

    def run(self):
        """
        Chạy ứng dụng OCR.
        Hiển thị giao diện người dùng và xử lý OCR khi người dùng tải lên hình ảnh.
        """
        self.refresh()
        self.display_interface()

if __name__ == '__main__':
    app = OCRApp()
    app.run()
