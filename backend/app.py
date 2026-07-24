from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, Field
from routes import router

app=FastAPI(
    title="Loan Approval Prediction API",
    description="API for predicting loan approval decisions"
    )


app.include_router(router)