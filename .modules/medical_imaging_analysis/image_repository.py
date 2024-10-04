from typing import List
from image_analysis import ImageAnalysis

class ImageRepository:
    def __init__(self):
        self.images = []
        self.analysis = ImageAnalysis("model.h5")

    def add_image(self, image_path, patient: Patient):
        self.images.append((image_path, patient))

    def get_image(self, image_path) -> str:
        for image, patient in self.images:
            if image == image_path:
                return patient
        return None

    def update_image(self, image_path, patient: Patient):
        for i, (image, existing_patient) in enumerate(self.images):
            if image == image_path:
                self.images[i] = (image_path, patient)
                break

    def delete_image(self, image_path):
        for i, (image, patient) in enumerate(self.images):
            if image == image_path:
                del self.images[i]
                break

    def get_all_images(self) -> List[str]:
        return [image for image, patient in self.images]

    def analyze_images(self, image_paths, patient: Patient):
        return self.analysis.analyze_images(image_paths, patient)

    def save_analysis(self, image_path, diagnosis, patient: Patient):
        self.analysis.save_analysis(image_path, diagnosis, patient)

    def load_analysis(self, image_path, patient: Patient):
        return self.analysis.load_analysis(image_path, patient)
