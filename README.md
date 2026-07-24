# Loan Approval ML Deployment

A complete Machine Learning deployment project that predicts loan approval using applicant financial information.

The project contains:

- Machine Learning Model
- FastAPI Backend
- Docker Containerization
- AWS EC2 Deployment
- Nginx Reverse Proxy
- Streamlit Frontend


## Project Architecture


User
 |
 |
Streamlit Frontend
 |
 |
FastAPI API
 |
 |
ML Pipeline
 |
 |
Prediction



## Features Used

The model uses:

- Number of Dependents
- Education
- Self Employment Status
- Annual Income
- Loan Amount
- Loan Term
- CIBIL Score
- Residential Assets
- Commercial Assets
- Luxury Assets
- Bank Assets


Feature Engineering:

- Total Assets Value
- Loan to Income Ratio
- Asset to Loan Ratio
- Approx Monthly Installment
- CIBIL Score Bucket


## Backend

Backend is developed using:

- FastAPI
- Scikit-learn
- Pandas
- Joblib


### Run Backend Locally


Create environment:

```bash
python -m venv venv
