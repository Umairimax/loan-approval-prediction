import pandas as pd
from schemas import LoanRequest


def get_cibil_bucket(score: int):

    if score < 550:
        return 0   # poor
    elif score < 650:
        return 1   # fair
    elif score < 750:
        return 2   # good
    else:
        return 3   # excellent



def prepare_features(request: LoanRequest):

    total_assets_value = (
        request.residential_assets_value
        + request.commercial_assets_value
        + request.luxury_assets_value
        + request.bank_asset_value
    )


    loan_to_income_ratio = (
        request.loan_amount /
        request.income_annum
    )


    asset_to_loan_ratio = (
        total_assets_value /
        request.loan_amount
    )


    # Assuming loan_term is in months
    approx_monthly_installment = (
        request.loan_amount /
        request.loan_term
    )


    cibil_score_bucket = get_cibil_bucket(
        request.cibil_score
    )


    data = pd.DataFrame([{

        "no_of_dependents": request.no_of_dependents,

        "education": request.education,

        "self_employed": request.self_employed,

        "income_annum": request.income_annum,

        "loan_amount": request.loan_amount,

        "loan_term": request.loan_term,

        "cibil_score": request.cibil_score,

        "residential_assets_value":
            request.residential_assets_value,

        "commercial_assets_value":
            request.commercial_assets_value,

        "luxury_assets_value":
            request.luxury_assets_value,

        "bank_asset_value":
            request.bank_asset_value,

        "total_assets_value":
            total_assets_value,

        "loan_to_income_ratio":
            loan_to_income_ratio,

        "asset_to_loan_ratio":
            asset_to_loan_ratio,

        "approx_monthly_installment":
            approx_monthly_installment,

        "cibil_score_bucket":
            cibil_score_bucket
    }])


    return data