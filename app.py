from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle

app = Flask(__name__)

data = pd.read_csv('data.csv')
reviews = data['review']
sentiments = data['sentiment']
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(reviews)
y = sentiments
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)


with open('sentiment_classifier.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        review = request.form.get('review')
        X = vectorizer.transform([review])
        prediction = model.predict(X)

        return render_template('analysis.html', prediction=prediction)

    return render_template('index.html')


@app.route('/train')
def train():
    model = LogisticRegression()
    model.fit(X_train, y_train)

    accuracy = model.score(X_test, y_test)

    with open('sentiment_classifier.pkl', 'wb') as file:
        pickle.dump(model, file)
    return 'Model trained successfully!'


if __name__ == '__main__':
    app.run(debug=True)
