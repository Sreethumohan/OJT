import pandas as pd
import re
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score

# Load the dataset
file_path = 'imb_dataset.csv'
imdb_data = pd.read_csv(file_path)

# Function to clean text without using NLTK
def simple_preprocess_text(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove special characters and digits
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    # Convert text to lowercase
    text = text.lower()
    return text

# Apply preprocessing to the reviews
imdb_data['cleaned_review'] = imdb_data['review'].apply(simple_preprocess_text)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(imdb_data['cleaned_review'], imdb_data['sentiment'], test_size=0.2, random_state=42)

# Vectorize the text data using TF-IDF
tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)

# Evaluate the model
y_pred = model.predict(X_test_tfidf)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Accuracy: {accuracy}')
print('Classification Report:')
print(report)

# Function to predict sentiment of new reviews
def predict_sentiment(reviews, model, vectorizer):
    cleaned_reviews = [simple_preprocess_text(review) for review in reviews]
    reviews_tfidf = vectorizer.transform(cleaned_reviews)
    predictions = model.predict(reviews_tfidf)
    return predictions

# Example new reviews
new_reviews = [
    "I absolutely loved this movie! The plot was great and the acting was superb.",
    "This movie was terrible. I wasted two hours of my life watching it.",
    "It was an okay movie. Not the best but not the worst either."
]

# Predict sentiment for new reviews
predicted_sentiments = predict_sentiment(new_reviews, model, tfidf_vectorizer)
for review, sentiment in zip(new_reviews, predicted_sentiments):
    print(f'Review: {review}\nPredicted Sentiment: {sentiment}\n')