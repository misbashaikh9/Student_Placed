from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return "Placement Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    # Extract features
    features = [
        data['cgpa'],
        data['aptitude'],
        data['communication'],
        data['projects']
    ]

    # Prediction
    prediction = model.predict([features])[0]

    return jsonify({
        'placement_prediction': int(prediction)
    })

if __name__ == '__main__':
    port=int(os.environ.get("PORT",3000))
    app.run(host="0.0.0.0",port=port)