from PIL import Image, ImageChops

class ImageComparisonUtil:
    @staticmethod
    def check_match(image1_path, image2_path):
        
        img1 = Image.open(image1_path).convert("RGB")
        img2 = Image.open(image2_path).convert("RGB")

        diff = ImageChops.difference(img1, img2)

        return not diff.getbbox()  
