import numpy as np
import cv2
from tensorflow.keras.models import load_model
from patient_entity import Patient

class ImageAnalysis:
    def __init__(self, model_path):
        self.model = load_model(model_path)

    def analyze_image(self, image_path, patient: Patient):
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))
        image = image / 255.0
        image = np.expand_dims(image, axis=0)

        prediction = self.model.predict(image)
        diagnosis = np.argmax(prediction)

        if diagnosis == 0:
            return "Normal"
        elif diagnosis == 1:
            return "Abnormal"
        else:
            return "Unknown"

    def analyze_images(self, image_paths, patient: Patient):
        diagnoses = []
        for image_path in image_paths:
            diagnosis = self.analyze_image(image_path, patient)
            diagnoses.append(diagnosis)
        return diagnoses

    def save_analysis(self, image_path, diagnosis, patient: Patient):
        # Implement saving logic here
        pass

    def load_analysis(self, image_path, patient: Patient):
        # Implement loading logic here
        pass
