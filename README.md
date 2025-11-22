# Smart Spam Classifier

## Overview
The **Smart Spam Classifier** is a machine learning-based application designed to filter SMS and email messages as either "Spam" or "Ham". It uses NLP techniques and an SVM classifier to provide accurate predictions through a user-friendly web interface.

## Features
-   **Real-time Classification**: Instantly classify messages.
-   **Analytics Dashboard**: Visualize dataset distribution and common spam words.
-   **History Log**: Track your recent queries.
-   **Premium UI**: Modern, responsive interface.

## Technologies Used
-   **Language**: Python
-   **ML**: Scikit-learn (SVM)
-   **Web**: Streamlit
-   **Data**: Pandas, NLTK

## Installation
1.  Clone the repo:
    ```bash
    git clone <repo-url>
    ```
2.  Install requirements:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the app:
    ```bash
    streamlit run src/app.py
    ```

## Testing
Run unit tests:
```bash
python -m unittest discover tests
```
