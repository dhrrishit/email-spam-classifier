import pandas as pd
import os
from datetime import datetime

HISTORY_FILE = 'history.csv'

def log_query(text, prediction, confidence):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    label = "Spam" if prediction == 1 else "Ham"
    
    new_data = pd.DataFrame({
        'Timestamp': [timestamp],
        'Message': [text],
        'Prediction': [label],
        'Confidence': [confidence]
    })
    
    if not os.path.exists(HISTORY_FILE):
        new_data.to_csv(HISTORY_FILE, index=False)
    else:
        new_data.to_csv(HISTORY_FILE, mode='a', header=False, index=False)

def get_history():
    if os.path.exists(HISTORY_FILE):
        return pd.read_csv(HISTORY_FILE).sort_values(by='Timestamp', ascending=False)
    return pd.DataFrame(columns=['Timestamp', 'Message', 'Prediction', 'Confidence'])
