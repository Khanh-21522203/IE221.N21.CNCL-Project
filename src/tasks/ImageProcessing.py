import streamlit as st
from PIL import Image, ImageEnhance, ImageFilter
import io

class ImageProcess:
    """
    Lớp để tăng cường ảnh bằng cách điều chỉnh độ tương phản, độ sáng, đổ bóng và áp dụng bộ lọc khung.
    Attributes:
        image (PIL.Image.Image): Ảnh đầu vào.
        prev_contrast_factor (float): Giá trị hệ số tương phản trước đó.
        prev_bright_factor (float): Giá trị hệ số độ sáng trước đó.
        prev_shadow_factor (float): Giá trị hệ số đổ bóng trước đó.
        prev_color_factor (float): Giá trị hệ số màu sắc trước đó.
        prev_frame_factor (float): Giá trị hệ số khung trước đó.
    Methods:
        __init__(): Khởi tạo đối tượng ImageProcess và thiết lập thuộc tính image.
        refresh(): Làm mới biến self.image thành None.
        change_contrast(image, factor): Điều chỉnh độ tương phản của ảnh cho trước theo hệ số đã cho.
        change_brightness(image, factor): Điều chỉnh độ sáng của ảnh cho trước theo hệ số đã cho.
        change_shadow(image, factor): Điều chỉnh đổ bóng của ảnh cho trước theo hệ số đã cho.
        color_change(image, factor): Điều chỉnh màu sắc của ảnh cho trước theo hệ số đã cho.
        frame_change(image, factor): Áp dụng bộ lọc khung vào ảnh cho trước.
        view(): Hiển thị giao diện của chức năng.
        howtouse(): Hiển thị hướng dẫn sử dụng chức năng Chỉnh sửa hình ảnh.
        update_image(enhanced_image, contrast_factor, bright_factor, shadow_factor, color_factor, frame_factor): Cập nhật hình ảnh sau khi áp dụng các chỉnh sửa độ tương phản, độ sáng, đổ bóng, màu sắc và khung.
        run(): Chạy ứng dụng Chỉnh sửa hình ảnh.
    """

    def __init__(self):
        """
        Khởi tạo đối tượng ImageProcess và thiết lập thuộc tính image,
        Thiết lập thuộc tính prev_contrast_factor, prev_bright_factor, prev_shadow_factor, prev_color_factor, prev_frame_factor.
        """
        self.image = None
        self.prev_contrast_factor = None
        self.prev_bright_factor = None
        self.prev_shadow_factor = None
        self.prev_color_factor = None
        self.prev_frame_factor = None

    def refresh(self):
        """
        Làm mới biến self.image thành None.
        """
        self.image = None

    def change_contrast(self, image, factor):
        """
        Điều chỉnh độ tương phản của ảnh cho trước theo hệ số đã cho.
        Args:
            image (PIL.Image.Image): Ảnh đầu vào.
            factor (float): Hệ số tương phản để áp dụng.
        Returns:
            PIL.Image.Image: Ảnh với độ tương phản đã điều chỉnh.
        """
        enhancer = ImageEnhance.Contrast(image)
        enhanced_image = enhancer.enhance(factor)
        return enhanced_image

    def change_brightness(self, image, factor):
        """
        Điều chỉnh độ sáng của ảnh cho trước theo hệ số đã cho.
        Args:
            image (PIL.Image.Image): Ảnh đầu vào.
            factor (float): Hệ số độ sáng để áp dụng.
        Returns:
            PIL.Image.Image: Ảnh với độ sáng đã điều chỉnh.
        """
        enhancer = ImageEnhance.Brightness(image)
        enhanced_image = enhancer.enhance(factor)
        return enhanced_image

    def change_shadow(self, image, factor):
        """
        Điều chỉnh đổ bóng của ảnh cho trước theo hệ số đã cho.
        Args:
            image (PIL.Image.Image): Ảnh đầu vào.
            factor (float): Hệ số đổ bóng để áp dụng.
        Returns:
            PIL.Image.Image: Ảnh với đổ bóng đã điều chỉnh.
        """
        enhancer = ImageEnhance.Sharpness(image)
        enhanced_image = enhancer.enhance(factor)
        return enhanced_image

    def color_change(self, image, factor):
        """
        Điều chỉnh màu sắc của ảnh cho trước theo hệ số đã cho.
        Args:
            image (PIL.Image.Image): Ảnh đầu vào.
            factor (float): Hệ số màu sắc để áp dụng.
        Returns:
            PIL.Image.Image: Ảnh với màu sắc đã điều chỉnh.
        """
        enhancer = ImageEnhance.Color(image)
        enhanced_image = enhancer.enhance(factor)
        return enhanced_image
    
    def frame_change(self, image, factor):
        """
        Áp dụng bộ lọc khung vào ảnh cho trước.
        Args:
            image (PIL.Image.Image): Ảnh đầu vào.
        Returns:
            PIL.Image.Image: Ảnh với khung đã áp dụng.
        """
        height, weight = image.size[0], image.size[1]
        background = image.copy().resize((int(height*factor), int(weight*factor)), Image.ANTIALIAS)
        # Tạo bộ lọc Gaussian Blur
        gaussian_blur_filter = ImageFilter.GaussianBlur(radius=5)
        # Áp dụng bộ lọc lên ảnh
        background = background.filter(gaussian_blur_filter)
        x = int(height*(factor-1)/2)
        y = int(weight*(factor-1)/2)
        background.paste(image, (x,y))
        return background

    def view(self):
        """
        Hiện giao diện của chức năng
        """
        st.title(":orange[Image Processing]")
        self.howtouse()
        uploaded_file = st.file_uploader("Upload an image (.jpg, .jpeg, .png)", type=["jpg", "jpeg", "png"])

        if uploaded_file is not None:
            self.image = Image.open(uploaded_file)
            # Hiển thị ảnh gốc
            if self.image is not None:
                col1, col2 = st.columns(2)
                with col1:
                    # Sử dụng st.slider để chọn factor
                    contrast_factor = st.slider("Độ tương phản", 0.0, 2.0, 1.0, 0.1, key='contrast')
                    bright_factor = st.slider("Độ sáng", 0.0, 2.0, 1.0, 0.1, key='bright')
                    shadow_factor = st.slider("Độ đổ bóng", 0.0, 10.0, 5.0, 0.1, key='shadow')
                    color_factor = st.slider("Màu sắc", 0.0, 5.0, 1.0, 0.1, key='color')
                    frame_factor = st.slider("Frame", 1.0, 2.0, 1.0, 0.05, key='frame')
                    # Thay đổi ảnh
                    enhanced_image = self.image.copy()
                    enhanced_image = self.update_image(enhanced_image,contrast_factor,bright_factor,shadow_factor,color_factor,frame_factor)
                with col2:
                    # Hiển thị ảnh đã thay đổi độ tương phản
                    st.image(enhanced_image)
                    img_bytes = io.BytesIO()
                    enhanced_image.save(img_bytes, format='JPEG')
                    download = st.download_button(label="Download", 
                                                data=img_bytes.getvalue(), 
                                                file_name="enhancedimage.jpg")
                    
    def howtouse(self):
        """
        Hiển thị hướng dẫn sử dụng chức năng Chỉnh sửa hình ảnh.
        """
        st.markdown("**Hướng dẫn sử dụng chức năng :orange[Chỉnh sửa hình ảnh]:**")
        st.markdown("""Bước 1: Tải file bạn muốn chỉnh sửa lên bằng cách nhấn vào **Browse files**""")
        st.markdown("""Bước 2: Sau khi tải ảnh lên, giao diện sẽ hiện cho bạn những lựa chọn trong 
                        việc chỉnh sửa ảnh.""")
        st.markdown("Bước 3: Sau khi chỉnh sửa ảnh xong, nhấn **Download** để tải về")   
        st.markdown("**Lưu ý: văn bản và câu hỏi phải cùng ngôn ngữ.**")

    def update_image(self, enhanced_image,contrast_factor,bright_factor,shadow_factor,color_factor,frame_factor):
        """
        Cập nhật hình ảnh sau khi áp dụng các chỉnh sửa độ tương phản, độ sáng, đổ bóng, màu sắc và khung.
        Args:
            enhanced_image (PIL.Image.Image): Ảnh đầu vào đã được cải thiện.
            contrast_factor (float): Hệ số tương phản.
            bright_factor (float): Hệ số độ sáng.
            shadow_factor (float): Hệ số đổ bóng.
            color_factor (float): Hệ số màu sắc.
            frame_factor (float): Hệ số khung.
        Returns:
            PIL.Image.Image: Ảnh đã được cập nhật sau khi áp dụng các chỉnh sửa.
        """
        if contrast_factor != self.prev_contrast_factor:
            enhanced_image = self.change_contrast(self.image, contrast_factor)
            # Cập nhật hình ảnh sau khi thay đổi độ tương phản
            self.prev_contrast_factor = contrast_factor
        if bright_factor != self.prev_bright_factor:
            enhanced_image = self.change_brightness(enhanced_image, bright_factor)
            # Cập nhật hình ảnh sau khi thay đổi độ sáng
            self.prev_bright_factor = bright_factor
        if shadow_factor != self.prev_shadow_factor:
            enhanced_image = self.change_shadow(enhanced_image, shadow_factor)
            # Cập nhật hình ảnh sau khi thay đổi độ đổ bóng
            self.prev_shadow_factor = shadow_factor
        if color_factor != self.prev_color_factor:
            enhanced_image = self.color_change(enhanced_image, color_factor)
            # Cập nhật hình ảnh sau khi thay đổi màu sắc
            self.prev_color_factor = color_factor
        if frame_factor != self.prev_frame_factor:
            enhanced_image = self.frame_change(enhanced_image, frame_factor)
            # Cập nhật hình ảnh sau khi thay đổi khung
            self.prev_frame_factor = frame_factor

        return enhanced_image
    
    def run(self):
        self.refresh()
        self.view()

if __name__ == '__main__':
    app = ImageProcess()
    app.run()