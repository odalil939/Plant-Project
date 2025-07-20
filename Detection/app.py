from flask import Flask, render_template, request, redirect, url_for
from models import FruitVegetableModel, TomatoPotatoPepperModel

app = Flask(__name__)

# Define paths to your models
fruit_vegetable_model_path = r"D:/Arwa/Tomatoes_potatoes_pepperMODEL.h5"
fruit_vegetable_model = FruitVegetableModel(fruit_vegetable_model_path)

tomato_potato_pepper_model_path = r"D:/Arwa/Apples_strawberries_grapesMODEL.h5"
tomato_potato_pepper_model = TomatoPotatoPepperModel(tomato_potato_pepper_model_path)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        model_type = request.form['model_type']  
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file and model_type == 'fruit_vegetable':
            img_path = 'uploads/' + file.filename
            file.save(img_path)
            predicted_class, confidence = fruit_vegetable_model.predict_image(img_path)
            return render_template('result.html', predicted_class=predicted_class, confidence=confidence, img_path=img_path)
        elif file and model_type == 'tomato_potato_pepper':
            img_path = 'uploads/' + file.filename
            file.save(img_path)
            predicted_class, confidence = tomato_potato_pepper_model.predict_image(img_path)
            return render_template('result.html', predicted_class=predicted_class, confidence=confidence, img_path=img_path)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=5002)
