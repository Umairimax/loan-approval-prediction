# 🏦 Loan Approval Prediction System

An end-to-end Machine Learning project that predicts loan approval status using applicant financial and personal information. The project includes ML development, FastAPI backend, Docker deployment, AWS EC2 hosting, and Streamlit frontend.

## 📌 Dataset

Kaggle Dataset:  
https://www.kaggle.com/datasets/taweilo/loan-approval-classification-data

## 🤖 Machine Learning

Built a classification pipeline to predict:

- Approved
- Rejected

### Feature Engineering

Created additional financial features:

- Total Assets Value
- Loan to Income Ratio
- Asset to Loan Ratio
- Approx Monthly Installment
- CIBIL Score Bucket

### Features Used

- Income
- Loan Amount
- Loan Term
- CIBIL Score
- Education
- Self Employment
- Dependents
- Asset Values
- Engineered Financial Features

### Models Trained

- Logistic Regression
- Random Forest Classifier
- Gradient Boosting Classifier

Final Model Used:

✅ Gradient Boosting Classifier

The complete preprocessing + model pipeline was saved using Joblib.

## ⚡ FastAPI Backend

Developed a production API using FastAPI.

Features:

- Input validation with Pydantic
- ML model inference
- Approval probability prediction


## 🐳 Docker & Deployment

The FastAPI backend was containerized using Docker and pushed to Docker Hub.

Deployment stack:

- Docker
- AWS EC2
- Nginx Reverse Proxy

## 🎨 Streamlit Frontend

Created an interactive Streamlit web interface where users can enter applicant details and get instant loan approval predictions.

Frontend deployed on:

✅ Streamlit Cloud

Backend deployed on:

✅ AWS EC2


## 🛠️ Tech Stack

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Docker
- AWS EC2
- Nginx
