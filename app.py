from flask import Flask, render_template, request
import joblib

# Initialize Flask app
app = Flask(__name__)

# Load trained model and vectorizer
model = joblib.load(r"D:\Practice+Learning\Fake_news App\Models\fake_news_model.pkl")
vectorizer = joblib.load(r"D:\Practice+Learning\Fake_news App\Models\tfidf_vectorizer.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        news_text = request.form['news']
        clean_input = news_text.lower()
        vectorized_input = vectorizer.transform([clean_input])
        prediction = model.predict(vectorized_input)[0]

        label = "🔴 FAKE NEWS" if prediction == 0 else "🟢 REAL NEWS"
        return render_template('result.html', prediction=label, input_text=news_text)

if __name__ == '__main__':
    app.run(debug=True)
