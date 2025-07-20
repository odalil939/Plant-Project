import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

class FruitVegetableModel:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.classes = ['Apple_Apple_scab', 'Apple_Cedar_apple_rust', 'Apple_healthy',
                        'Grape_Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape_healthy',
                        'Grape_Leaf_blight_(Isariopsis_Leaf_Spot)', 'Strawberry_healthy',
                        'Strawberry_Leaf_scorch']
    
    def load_and_prepare_image(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet.preprocess_input(img_array)
        return img_array
    
    def predict_image(self, img_path):
        img_array = self.load_and_prepare_image(img_path)
        predictions = self.model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = self.classes[predicted_class_index]
        confidence = predictions[0][predicted_class_index] * 100
        return predicted_class, confidence

class TomatoPotatoPepperModel:
    def __init__(self, model_path):
        self.model = tf.keras.models.load_model(model_path)
        self.classes = ['Tomato_Bacterial_spot', 'Tomato_Early_blight', 'Tomato_healthy',
                        'Tomato_Late_blight', 'Tomato_Leaf_Mold', 'Tomato_Septoria_leaf_spot',
                        'Tomato_Spider_mites_Two-spotted_spider_mite', 'Tomato_Target_Spot',
                        'Tomato_Tomato_mosaic_virus', 'Tomato_Tomato_Yellow_Leaf_Curl_Virus',
                        'Potato_Early_blight', 'Potato_healthy', 'Potato_Late_blight',
                        'Pepper_bell_Bacterial_spot', 'Pepper_bell_healthy']
    
    def load_and_prepare_image(self, img_path):
        img = image.load_img(img_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = tf.keras.applications.mobilenet.preprocess_input(img_array)
        return img_array
    
    def predict_image(self, img_path):
        img_array = self.load_and_prepare_image(img_path)
        predictions = self.model.predict(img_array)
        predicted_class_index = np.argmax(predictions[0])
        predicted_class = self.classes[predicted_class_index]
        confidence = predictions[0][predicted_class_index] * 100
        return predicted_class, confidence
