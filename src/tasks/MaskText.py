import requests
import streamlit as st

class MaskTextApp:
    """
    Lớp ứng dụng Mask Text cho phép gợi ý điền khuyết trong câu bằng cách sử dụng mô hình Masked Language Model.
    Attributes:
        API_URL (str): URL API để gọi mô hình từ xa sử dụng Hugging Face API.
        headers (dict): Headers để xác thực khi gọi API.
    Methods:
        __init__(): Khởi tạo ứng dụng Mask Text và thiết lập các thuộc tính cần thiết.
        mask_text(text: str): Gợi ý điền khuyết trong câu.
        display_interface(): Hiển thị giao diện người dùng và kết quả gợi ý khi người dùng nhập câu cần điền khuyết.
        HowToUse(): Hiển thị hướng dẫn sử dụng chức năng Mask Text.
        run(): Chạy ứng dụng Mask Text.
    """
    def __init__(self):
        """
        Khởi tạo ứng dụng Mask Text.
        Thiết lập URL API và headers để gọi mô hình từ xa sử dụng Hugging Face API.
        """
        self.API_URL = "https://api-inference.huggingface.co/models/bert-base-uncased"
        self.headers = {"Authorization": "Bearer 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"}

    def mask_text(self, text):
        """
        Gợi ý điền khuyết trong câu bằng cách sử dụng mô hình Masked Language Model.
        Parameters:
            - text: Câu cần điền khuyết.
        Returns:
            Kết quả gợi ý điền khuyết trong câu.
        """
        payload = {
            "inputs": text
        }
        response = requests.post(self.API_URL, headers=self.headers, json=payload)
        result = response.json()
        try:
            result = [result[i]["token_str"] for i in range(0,5)]
            return result
        except:
            return -1

    def display_interface(self):
        """
        Hiển thị giao diện người dùng.
        Hiển thị tiêu đề và cho phép người dùng nhập câu cần điền khuyết. Hiển thị gợi ý kết quả sau khi gọi phương thức mask_text.
        """
        st.title("Fill Masked Text")
        self.HowToUse()
        text_input = st.text_input('Nhập câu cần điền khuyết: ')
        
        if text_input:
            text_output = self.mask_text(text_input)
            if text_output != -1:
                st.write("Các gợi ý cho bạn:")
                for i in range(5):
                    st.write(f'*\tGợi ý {i}: **{text_output[i]}**')
            else:
                st.write("Câu của bạn không đúng cú pháp đã yêu cầu")
    
    def HowToUse(self):
        """
        Hiển thị hướng dẫn sử dụng chức năng Mask Text.
        """
        st.markdown("**Hướng dẫn sử dụng chức năng Mask Text:**")
        st.markdown("**Bước 1: Nhập câu cần điền khuyết**")
        st.markdown("""Trên giao diện, bạn sẽ thấy một ô văn bản. Hãy nhập câu cần điền khuyết vào ô đó.
                        Trong câu nhập vào, từ bạn cần điền khuyết được thay thế bằng **[MASK]** 
                        và câu nhập vào chỉ được phép có một **[MASK]**. Ví dụ:
                        \n\tI [MASK] to be a doctor""")
        st.markdown("**Bước 2: Nhấn Enter hoặc chờ kết quả**")
        st.markdown("**Bước 3: Xem gợi ý kết quả**")

    def run(self):
        """
        Chạy ứng dụng Mask Text.
        Hiển thị giao diện người dùng và gọi phương thức hiển thị gợi ý khi người dùng nhập câu cần điền khuyết.
        """
        self.display_interface()
    
if __name__ == '__main__':
    app = MaskTextApp()
    app.run()
