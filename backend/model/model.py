import joblib
from pathlib import Path


MODEL_PATH = Path(__file__).parent / "loan_approval_pipeline1.pkl"

model = joblib.load(MODEL_PATH)
