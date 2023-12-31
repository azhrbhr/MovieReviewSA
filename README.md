# Movie Review Sentiment Analysis

This Flask application performs sentiment analysis on movie reviews using a machine learning model. It predicts whether a given review is positive or negative based on its sentiment.

## Getting Started

To get started with the Flask Movie Review Sentiment Analysis app, follow these instructions:

### Prerequisites

- Python 3.x
- pip

### Installation

1. Clone the repository:
git clone https://github.com/azhrbhr/MovieReviewSA.git


2. Navigate to the project directory:
```bash
cd MovieReviewSA
```


3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Usage

1. Run the Flask application:

```bash
flask run
```

2. Open your web browser and go to `http://localhost:5000` to access the application.

3. Enter a movie review in the provided form and submit it.

4. The application will analyze the sentiment of the review and display the predicted sentiment (positive or negative).

### Training the Model

To train the sentiment analysis model, you can use the following endpoint:

http://localhost:5000/train



- Make sure the `data.csv` file is present in the project directory before training the model. This CSV file contains movie reviews and their corresponding sentiments (positive or negative).

- Accessing the `/train` route will train a Logistic Regression model using the data from `data.csv`. The trained model will be stored as `sentiment_classifier.pkl`.

### Project Structure

- `app.py`: The main Flask application file containing the routes and sentiment analysis logic.
- `data.csv`: A CSV file containing movie reviews and their corresponding sentiments (positive or negative).
- `sentiment_classifier.pkl`: A trained machine learning model stored as a pickle file.
- `templates/`: A directory containing HTML templates for the web interface.

### Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request.




