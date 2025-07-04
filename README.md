# Fake-News-Detection-App
# 📰 Fake News Detection App

A machine learning web application that classifies whether a news article is **Fake** or **Real** using NLP techniques and a trained model.

---

## 🚀 Demo

🔗 **Live App** 
https://fake-news-detection-app-u6nr.onrender.com
---

## 🧠 Models Used

This project evaluates three models:

- Logistic Regression ✅ *(final model)*
- Naive Bayes ✅
- Random Forest ✅

All models were trained and tested. The best-performing model was saved as `fake_news_model.pkl`.

---

## 🧾 Dataset

**Source**: [Kaggle - Fake and Real News Dataset](https://www.kaggle.com/clmentbisaillon/fake-and-real-news-dataset)

Due to GitHub's 25MB file limit, data is hosted externally:

📥 Download from Google Drive:

- [Fake.csv](https://drive.google.com/your-fake-link)
- [True.csv](https://drive.google.com/your-true-link)

📁 Place these files inside the `data/` folder:
fake-news-detection-app/
└── data/
├── Fake.csv
└── True.csv


---

## 📁 Project Structure

fake-news-detection-app/
│
├── app.py # Flask web app
├── model/
│ └──fake_news_model.pkl # Trained ML model
├── templates/
│ ├── home.html # Input form
│ └── result.html # Prediction output
├── data/ # Contains dataset (local)
├── requirements.txt # All dependencies
└── README.md # Project documentation


---

## 📦 Tech Stack

- Python 3.x
- Pandas, Numpy
- Scikit-learn
- Flask
- HTML (Jinja2 templating)
- Git, GitHub

---

## ⚙️ How to Run Locally

1. **Clone the repo**

```bash
git clone https://github.com/Rovil70/fake-news-detection-app.git
cd fake-news-detection-app
pip install -r requirements.txt
python app.py-- # Run the app


✅ Features
Predicts if a news article is real or fake

Clean UI using Flask & HTML

Trained with real-world news dataset

Uses NLP (TF-IDF vectorizer)

🙌 Author
Made with ❤️ by Rovil Katariya




