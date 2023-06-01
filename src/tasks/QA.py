import streamlit as st
from transformers import pipeline
from docx import Document
from googletrans import Translator

class QuestionAnswering:
    """
    Ứng dụng Question Answering sử dụng mô hình 'deepset/roberta-base-squad2' và tokenizer tương ứng.
    Attributes:
        QApip (pipeline): Đối tượng pipeline để thực hiện trả lời câu hỏi dựa trên mô hình question-answering.
        translator (Translator): Đối tượng Translator để thực hiện dịch câu hỏi và văn bản ngữ cảnh (nếu cần).
    Methods:
        __init__(): Khởi tạo đối tượng QuestionAnswering và thiết lập các thuộc tính cần thiết.
        answer_question(context: str, question: str): Trả lời câu hỏi dựa trên văn bản ngữ cảnh bằng tiếng anh.
        answer(context: str, question: str): Trả về câu trả lời cho câu hỏi dựa trên văn bản ngữ cảnh và câu hỏi đã dịch (nếu cần).
        display_interface(): Hiển thị giao diện người dùng.
        read_docx_file(file: str): Đọc nội dung văn bản từ file .docx.
        howtouse(): Hiển thị hướng dẫn sử dụng chức năng Question Answer.
        run(): Chạy ứng dụng Question Answering.
    """

    def __init__(self):
        """
        Khởi tạo ứng dụng Question Answering.
        Sử dụng mô hình question-answering 'deepset/roberta-base-squad2' và tokenizer tương ứng.
        """
        self.QApip = pipeline('question-answering', model='deepset/roberta-base-squad2', tokenizer='deepset/roberta-base-squad2')
        self.translator = Translator(service_urls=['translate.google.com'])

    def answer_question(self, context, question):
        """
        Trả lời câu hỏi dựa trên văn bản ngữ cảnh.
        Parameters:
            - context: Văn bản ngữ cảnh.
            - question: Câu hỏi.
        Returns:
            Câu trả lời cho câu hỏi dựa trên văn bản ngữ cảnh.
        """
        question_set = {
            'question': question,
            'context': context
        }
        results = self.QApip(question_set)
        return results['answer']

    def answer(self, context, question):
        """
        Trả về câu trả lời cho câu hỏi dựa trên văn bản ngữ cảnh và câu hỏi được dịch (nếu cần).
        Parameters:
            - context: Văn bản ngữ cảnh.
            - question: Câu hỏi.
        Returns:
            Câu trả lời cho câu hỏi dựa trên văn bản ngữ cảnh và câu hỏi đã dịch (nếu cần).
        """
        lang_src = self.translator.detect(context).lang
        if lang_src != self.translator.detect(question).lang:
            return 'Context và Question phải cùng một ngôn ngữ.'
        if lang_src != 'en':
            context_eng = self.translator.translate(context, src=lang_src, dest='en').text
            question_eng = self.translator.translate(question, src=lang_src, dest='en').text
            answer = self.answer_question(context_eng, question_eng)
            answer = self.translator.translate(answer, src='en', dest=lang_src).text
        else:
            answer = self.answer_question(context_eng, question_eng)
        return answer
    
    def display_interface(self):
        """
        Hiển thị giao diện người dùng.
        Hiển thị tiêu đề và cho phép người dùng nhập văn bản ngữ cảnh và câu hỏi.
        Hiển thị kết quả câu trả lời khi người dùng nhấn nút Start.
        """
        st.title(":green[Question Answer Task]")
        self.howtouse()

        type = st.radio("", ('CopyPaste', 'Upload File'))
        if type == 'CopyPaste':
            context = st.text_area("Context: ")
        else:
            file = st.file_uploader("Chọn file .docx", type=".docx")
            if file is not None:
                context = self.read_docx_file(file)
        question = st.text_area("Question: ")
        
        if st.button('Start'):
            if context and question:
                answer = self.answer(context, question)
                st.text("Trả lời:")
                if answer:
                    st.text(answer)
                else:
                    st.text("Tôi không có câu trả lời cho câu hỏi của bạn, có thể thứ bạn hỏi không nằm trong văn bản ngữ cảnh.")
            else:
                if not context:
                    st.markdown("Mục **Context** còn trống hoặc bạn chưa upload file")
                if not question:
                    st.markdown("Mục **Question** còn trống")

    def read_docx_file(self, file):
        """
        Đọc nội dung văn bản từ file .docx.
        Parameters:
            - file: Đường dẫn tới file .docx.
        Returns:
            Văn bản trong file .docx dưới dạng một chuỗi.
        """
        doc = Document(file)
        result = []
        for paragraph in doc.paragraphs:
            result.append(paragraph.text)
        return '\n'.join(result)

    def howtouse(self):
        """
        Hiển thị hướng dẫn sử dụng chức năng Question Answer.
        """
        st.markdown("**Hướng dẫn sử dụng chức năng Question Answer:**")
        st.markdown("""Bước 1: Nhập văn bản bài viết mà bạn muốn hỏi về nội dung trong đó vào mục **Context**.
                        Bạn cũng có thể upload file word nếu cần.""")
        st.markdown("Bước 2: Nhập câu hỏi vào ô **Question**.")
        st.markdown("Bước 3: Nhấn **Start** để xem kết quả.")   
        st.markdown("**Lưu ý: văn bản và câu hỏi phải cùng ngôn ngữ.**")
    
    def run(self):
        """
        Chạy ứng dụng Question Answering.
        Hiển thị giao diện người dùng và gọi phương thức hiển thị kết quả câu trả lời khi người dùng nhập văn bản ngữ cảnh và câu hỏi.
        """
        self.display_interface()

if __name__ == '__main__':
    if 'qa' not in st.session_state:
        st.session_state.qa = QuestionAnswering()
    qa = st.session_state.qa
    qa.run()
