import pandas as pd
import pickle
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score
from src.preprocessing import transform_text

MODEL_PATH = 'model.pkl'

def train_model(data_path='data/spam.csv'):
    try:
        df = pd.read_csv(data_path, encoding='latin-1')
        df = df.iloc[:, :2]
        df.columns = ['target', 'text']
        
        df['target'] = df['target'].map({'ham': 0, 'spam': 1})
        
        df['transformed_text'] = df['text'].apply(transform_text)
        
        X = df['transformed_text']
        y = df['target']
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        model = Pipeline([
            ('tfidf', TfidfVectorizer(max_features=3000)),
            ('svm', SVC(kernel='sigmoid', gamma=1.0, probability=True)) 
        ])
        
        model.fit(X_train, y_train)
        
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, zero_division=0)
        
        with open(MODEL_PATH, 'wb') as f:
            pickle.dump(model, f)
        
        return accuracy, precision
        
    except Exception as e:
        raise e

def predict_message(text):
    if not os.path.exists(MODEL_PATH):
        raise Exception("Model not found.")
        
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
        
    transformed_text = transform_text(text)
    prediction = model.predict([transformed_text])[0]
    proba = model.predict_proba([transformed_text])[0]
    
    return prediction, proba

if __name__ == "__main__":
    train_model()
