# 📦 Smart Spam Classifier – Refactored Project Structure (Aligned with DD Bank Style)

This document contains the **fully rewritten and reorganized structure** for the *Smart Spam Classifier* project, now made consistent with the style, depth, and format of the **DD Bank Management System** project.

---

# 🧠 Smart Spam Classifier – Machine Learning SMS/Email Filtering System

A clean, professional, fully structured ML project designed to classify messages as **Spam** or **Ham** using NLP + SVM. This version follows the **DD Bank documentation style** with a strict project structure, clarity, and modular organization.

---

## 📌 Overview

The Smart Spam Classifier uses Natural Language Processing (NLP) and Support Vector Machine (SVM) models to identify whether a message is spam. This refactored version includes:

* Proper folder hierarchy
* Modular Python files
* A clean "src" directory like DD Bank
* JSON/log-based history storage
* Streamlit UI moved into dedicated module
* Testing folder and docs folder added
* Full professional README structure

---

## ✨ Features

### **1. Real-Time Message Classification**

* Users can input SMS or email text
* Model predicts **Spam** or **Ham** instantly
* Confidence score displayed

### **2. Dataset Insights Dashboard**

* Spam/Ham distribution
* WordClouds for spam keywords
* Frequency charts

### **3. User Query History (JSON-based)**

* Stores recent classifications
* Auto-generates timestamps

### **4. Model Pipeline**

* Text cleaning (NLTK)
* TF-IDF vectorizer
* SVM classifier
* Modular ML pipeline like `bank_management.py` structure

### **5. Premium UI**

* Built with Streamlit
* Dark + Light modes
* Clean minimal layout

---

## 🏗️ Technologies Used

* **Python 3**
* **Scikit-learn** (ML model)
* **NLTK** (NLP preprocessing)
* **Streamlit** (UI)
* **Pandas & NumPy**
* **Matplotlib & WordCloud** (visualizations)
* **JSON** (for storing query history)

---

## 📂 Project Structure

```
smart-spam-classifier/
├── src/
│   ├── app.py                 # Main Streamlit app
│   ├── classifier.py          # Model loading, prediction functions
│   ├── preprocessing.py       # Text cleaning, NLP pipeline
│   ├── train_model.py         # Script to train & save SVM model
│   ├── visuals.py             # Dashboard charts + wordclouds
│   ├── history_manager.py     # JSON-based log/history system
│   └── utils.py               # Helper utilities
│
├── models/
│   └── svm_model.pkl
│
├── data/
│   ├── spam.csv               # Dataset
│   └── history.json           # User logs
│
├── tests/
│   ├── test_classifier.py
│   ├── test_preprocessing.py
│   └── test_history.py
│
├── docs/
│   └── report.pdf             # To be added later (parallel to DD Bank)
│
├── README.md
├── requirements.txt
└── statement.md
```

---

## ⚙️ Installation & Running the Project

### **1. Clone the Repository**

```
git clone <repo-url>
cd smart-spam-classifier
```

### **2. Install Dependencies**

```
pip install -r requirements.txt
```

### **3. Run the App**

```
streamlit run src/app.py
```

---

## 📊 Testing Instructions

Test individual modules using:

```
python -m unittest discover tests
```

You can manually test:

* Entering long spam messages
* Testing random ham messages
* Changing inputs rapidly
* Checking JSON logs

---

## 📸 Screenshots (Optional Future Section)

* Dashboard view
* Classification UI
* WordClouds
* History JSON preview

---

## 👤 Author

**Name:** Dhrrishit V. Deka

---

## 📄 License

This project is for academic and learning purposes.
