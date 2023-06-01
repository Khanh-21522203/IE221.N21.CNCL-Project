import streamlit as st
from googletrans import Translator

class TranslatorApp:
    """
    Ứng dụng dịch ngôn ngữ sử dụng thư viện Translator.
    Attributes:
        translator (Translator): Đối tượng Translator để thực hiện việc dịch.
        languages (dict): Một từ điển chứa các ngôn ngữ hỗ trợ và mã tương ứng của chúng.
    Methods:
        __init__(): Khởi tạo đối tượng TranslatorApp và thiết lập các thuộc tính cần thiết.
        detect_language(text: str): Phát hiện ngôn ngữ của văn bản đầu vào.
        translate(input_text: str, src_lang: str, dest_lang: str): Dịch văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích.
        display_interface(): Hiển thị giao diện người dùng.
        run(): Chạy ứng dụng dịch ngôn ngữ.
    """

    def __init__(self):
        """
        Khởi tạo đối tượng TranslatorApp.
        Thiết lập đối tượng Translator và từ điển các ngôn ngữ hỗ trợ.
        """
        self.translator = Translator(service_urls=['translate.google.com'])
        self.languages = {
            'Detect Language': 'detect',
            'Afrikaans': 'af',
            'Albanian': 'sq',
            'Amharic': 'am',
            'Arabic': 'ar',
            'Armenian': 'hy',
            'Azerbaijani': 'az',
            'Basque': 'eu',
            'Belarusian': 'be',
            'Bengali': 'bn',
            'Bosnian': 'bs',
            'Bulgarian': 'bg',
            'Catalan': 'ca',
            'Cebuano': 'ceb',
            'Chichewa': 'ny',
            'Chinese (simplified)': 'zh-cn',
            'Chinese (traditional)': 'zh-tw',
            'Corsican': 'co',
            'Croatian': 'hr',
            'Czech': 'cs',
            'Danish': 'da',
            'Dutch': 'nl',
            'English': 'en',
            'Esperanto': 'eo',
            'Estonian': 'et',
            'Filipino': 'tl',
            'Finnish': 'fi',
            'French': 'fr',
            'Frisian': 'fy',
            'Galician': 'gl',
            'Georgian': 'ka',
            'German': 'de',
            'Greek': 'el',
            'Gujarati': 'gu',
            'Haitian creole': 'ht',
            'Hausa': 'ha',
            'Hawaiian': 'haw',
            'Hebrew': 'he',
            'Hindi': 'hi',
            'Hmong': 'hmn',
            'Hungarian': 'hu',
            'Icelandic': 'is',
            'Igbo': 'ig',
            'Indonesian': 'id',
            'Irish': 'ga',
            'Italian': 'it',
            'Japanese': 'ja',
            'Javanese': 'jw',
            'Kannada': 'kn',
            'Kazakh': 'kk',
            'Khmer': 'km',
            'Korean': 'ko',
            'Kurdish (kurmanji)': 'ku',
            'Kyrgyz': 'ky',
            'Lao': 'lo',
            'Latin': 'la',
            'Latvian': 'lv',
            'Lithuanian': 'lt',
            'Luxembourgish': 'lb',
            'Macedonian': 'mk',
            'Malagasy': 'mg',
            'Malay': 'ms',
            'Malayalam': 'ml',
            'Maltese': 'mt',
            'Maori': 'mi',
            'Marathi': 'mr',
            'Mongolian': 'mn',
            'Myanmar (burmese)': 'my',
            'Nepali': 'ne',
            'Norwegian': 'no',
            'Odia': 'or',
            'Pashto': 'ps',
            'Persian': 'fa',
            'Polish': 'pl',
            'Portuguese': 'pt',
            'Punjabi': 'pa',
            'Romanian': 'ro',
            'Russian': 'ru',
            'Samoan': 'sm',
            'Scots gaelic': 'gd',
            'Serbian': 'sr',
            'Sesotho': 'st',
            'Shona': 'sn',
            'Sindhi': 'sd',
            'Sinhala': 'si',
            'Slovak': 'sk',
            'Slovenian': 'sl',
            'Somali': 'so',
            'Spanish': 'es',
            'Sundanese': 'su',
            'Swahili': 'sw',
            'Swedish': 'sv',
            'Tajik': 'tg',
            'Tamil': 'ta',
            'Telugu': 'te',
            'Thai': 'th',
            'Turkish': 'tr',
            'Ukrainian': 'uk',
            'Urdu': 'ur',
            'Uyghur': 'ug',
            'Uzbek': 'uz',
            'Vietnamese': 'vi',
            'Welsh': 'cy',
            'Xhosa': 'xh',
            'Yiddish': 'yi',
            'Yoruba': 'yo',
            'Zulu': 'zu'
        }

    def detect_language(self, text):
        """
        Phát hiện ngôn ngữ của văn bản đầu vào.
        Args:
            text (str): Văn bản cần phát hiện ngôn ngữ.
        Returns:
            str: Mã ngôn ngữ của văn bản được phát hiện.
        """
        result = self.translator.detect(text)
        return result.lang

    def translate(self, input_text, src_lang, dest_lang):
        """
        Dịch văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích.
        Args:
            input_text (str): Văn bản cần dịch.
            src_lang (str): Mã ngôn ngữ của văn bản nguồn.
            dest_lang (str): Mã ngôn ngữ của văn bản đích.
        Returns:
            str: Văn bản đã được dịch.
        """
        if src_lang == "detect":
            src_lang = self.detect_language(input_text)
        output = self.translator.translate(input_text, src=src_lang, dest=dest_lang).text
        return output

    def display_interface(self):
        """
        Hiển thị giao diện người dùng cho chức năng dịch văn bản
        """
        st.title(":violet[Translation]")
        col1, col2 = st.columns(2)
        with col1:
            src_lang = st.selectbox("Chọn ngôn ngữ nguồn", self.languages.keys())
            input_text = st.text_area("Nhập văn bản cần dịch")
        with col2:
            dest_lang = st.selectbox("Chọn ngôn ngữ đích", list(self.languages.keys())[1:])
            if input_text and src_lang and dest_lang:
                out_text = self.translate(input_text, self.languages[src_lang], self.languages[dest_lang])
                st.text_area("Kết quả", value=out_text)

    def run(self):
        """
        Chạy ứng dụng dịch ngôn ngữ.
        """
        self.display_interface()

if __name__ == '__main__':
    trans = TranslatorApp()
    trans.run()