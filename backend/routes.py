from fastapi import APIRouter
from schemas import LoanRequest, LoanResponse
from utils import prepare_features
from model.model import model

router = APIRouter()

@router.get("/")
def home():
    return {"message": "Loan Approval Classification API"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}

@router.post("/predict", response_model=LoanResponse)
def predict(request: LoanRequest):
    features = prepare_features(request)
    prediction = model.predict(features)[0]
    approval_probability = model.predict_proba(features)[0][1]

    return LoanResponse(
        name=request.name,
        gender=request.gender,
        prediction="Approved" if prediction == 1 else "Rejected",
        approval_probability=approval_probability
    )