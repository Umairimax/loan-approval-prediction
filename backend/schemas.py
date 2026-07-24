from pydantic import BaseModel, Field
from typing import Literal


class LoanRequest(BaseModel):

    name: str = Field(
        ...,
        min_length=2,
        max_length=50,
        description="Applicant name"
    )

    gender: Literal["Male", "Female", "Other"] = Field(
        ...,
        description="Applicant gender"
    )

    no_of_dependents: int = Field(
        ...,
        ge=0,
        description="Number of dependents"
    )

    education: Literal["Graduate", "Not Graduate"] = Field(
        ...,
        description="Education status"
    )

    self_employed: Literal["Yes", "No"] = Field(
        ...,
        description="Self employment status"
    )

    income_annum: float = Field(
        ...,
        gt=0,
        description="Annual income"
    )

    loan_amount: float = Field(
        ...,
        gt=0,
        description="Requested loan amount"
    )

    loan_term: int = Field(
        ...,
        gt=0,
        le=600,
        description="Loan term in months"
    )

    cibil_score: int = Field(
        ...,
        ge=300,
        le=900,
        description="CIBIL score"
    )

    residential_assets_value: float = Field(
        0,
        ge=0,
        description="Residential assets value"
    )

    commercial_assets_value: float = Field(
        0,
        ge=0,
        description="Commercial assets value"
    )

    luxury_assets_value: float = Field(
        0,
        ge=0,
        description="Luxury assets value"
    )

    bank_asset_value: float = Field(
        0,
        ge=0,
        description="Bank assets value"
    )


class LoanResponse(BaseModel):

    name: str

    gender: Literal["Male", "Female", "Other"] = Field(
            ...,
            description="Applicant gender"
        )
    
    prediction: Literal[
        "Approved",
        "Rejected"
    ]

    approval_probability: float = Field(
        ...,
        ge=0,
        le=1
    )