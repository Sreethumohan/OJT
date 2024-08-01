import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Corrected data list
data = [
    ("I love NLP", "Positive"),
    ("I HATE This Technology", "Negative"),
    ("its okay, nothing special", "Neutral")
]

sentences, labels = zip(*data)

nltk.download('punkt')
nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

def preprocess(text):
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

preprocessed_sentences = [preprocess(sentence) for sentence in sentences]

vectorizer = TfidfVectorizer()
x = vectorizer.fit_transform(preprocessed_sentences)

x_train, x_test, y_train, y_test = train_test_split(x, labels, test_size=0.2, random_state=42)

classifier = MultinomialNB()
classifier.fit(x_train, y_train)

y_pred = classifier.predict(x_test)

accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f"Accuracy: {accuracy}")
print("Classification Report:")
print(report)
