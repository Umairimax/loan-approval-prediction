# import streamlit as st
# import requests


# API_URL = "http://100.57.3.53/predict"


# st.set_page_config(
#     page_title="Loan Approval Predictor",
#     page_icon="🏦",
#     layout="centered"
# )


# st.title("🏦 Loan Approval Prediction")
# st.write("Enter applicant details to predict loan approval")


# # Personal Information

# st.subheader("Applicant Information")

# name = st.text_input(
#     "Name"
# )

# gender = st.selectbox(
#     "Gender",
#     ["Male", "Female", "Other"]
# )


# no_of_dependents = st.number_input(
#     "Number of Dependents",
#     min_value=0,
#     value=0,
#     step=1
# )


# education = st.selectbox(
#     "Education",
#     [
#         "Graduate",
#         "Not Graduate"
#     ]
# )


# self_employed = st.selectbox(
#     "Self Employed",
#     [
#         "Yes",
#         "No"
#     ]
# )


# # Financial Information

# st.subheader("Financial Information")


# income_annum = st.number_input(
#     "Annual Income",
#     min_value=0.0,
#     value=0.0,
#     step=10000.0
# )


# loan_amount = st.number_input(
#     "Loan Amount",
#     min_value=0.0,
#     value=0.0,
#     step=10000.0
# )


# loan_term = st.number_input(
#     "Loan Term (Months)",
#     min_value=1,
#     value=12,
#     step=1
# )


# cibil_score = st.number_input(
#     "CIBIL Score",
#     min_value=300,
#     max_value=900,
#     value=300,
#     step=1
# )



# # Assets

# st.subheader("Assets")


# residential_assets_value = st.number_input(
#     "Residential Assets Value",
#     min_value=0.0,
#     value=0.0,
#     step=10000.0
# )


# commercial_assets_value = st.number_input(
#     "Commercial Assets Value",
#     min_value=0.0,
#     value=0.0,
#     step=10000.0
# )


# luxury_assets_value = st.number_input(
#     "Luxury Assets Value",
#     min_value=0.0,
#     value=0.0,
#     step=10000.0
# )


# bank_asset_value = st.number_input(
#     "Bank Assets Value",
#     min_value=0.0,
#     value=0.0,
#     step=10000.0
# )



# if st.button("Predict Loan"):

#     payload = {

#         "name": name,
#         "gender": gender,

#         "no_of_dependents": no_of_dependents,

#         "education": education,

#         "self_employed": self_employed,

#         "income_annum": income_annum,

#         "loan_amount": loan_amount,

#         "loan_term": loan_term,

#         "cibil_score": cibil_score,

#         "residential_assets_value": residential_assets_value,

#         "commercial_assets_value": commercial_assets_value,

#         "luxury_assets_value": luxury_assets_value,

#         "bank_asset_value": bank_asset_value
#     }


#     try:

#         response = requests.post(
#             API_URL,
#             json=payload
#         )


#         if response.status_code == 200:

#             result = response.json()


#             st.success(
#                 f"Prediction: {result['prediction']}"
#             )


#             st.metric(
#                 "Approval Probability",
#                 f"{result['approval_probability']*100:.2f}%"
#             )


#         else:

#             st.error(response.json())


#     except Exception as e:

#         st.error(
#             f"API Error: {e}"
#         )











import streamlit as st
import requests


API_URL = "http://100.57.3.53/predict"


st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)


st.title("🏦 Loan Approval Prediction")
st.write("Enter applicant details to predict loan approval")


# Personal Information

st.subheader("Applicant Information")

name = st.text_input(
    "Name"
)

gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)


no_of_dependents = st.number_input(
    "Number of Dependents",
    min_value=0,
    value=0,
    step=1
)


education = st.selectbox(
    "Education",
    [
        "Graduate",
        "Not Graduate"
    ]
)


self_employed = st.selectbox(
    "Self Employed",
    [
        "Yes",
        "No"
    ]
)


# Financial Information

st.subheader("Financial Information")


income_annum = st.number_input(
    "Annual Income",
    min_value=0.0,
    value=0.0,
    step=10000.0
)


loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=0.0,
    step=10000.0
)


loan_term = st.number_input(
    "Loan Term (Months)",
    min_value=1,
    value=12,
    step=1
)


cibil_score = st.number_input(
    "CIBIL Score",
    min_value=300,
    max_value=900,
    value=300,
    step=1
)



# Assets

st.subheader("Assets")


residential_assets_value = st.number_input(
    "Residential Assets Value",
    min_value=0.0,
    value=0.0,
    step=10000.0
)


commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    min_value=0.0,
    value=0.0,
    step=10000.0
)


luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    min_value=0.0,
    value=0.0,
    step=10000.0
)


bank_asset_value = st.number_input(
    "Bank Assets Value",
    min_value=0.0,
    value=0.0,
    step=10000.0
)



if st.button("Predict Loan"):

    payload = {

        "name": name,
        "gender": gender,

        "no_of_dependents": no_of_dependents,

        "education": education,

        "self_employed": self_employed,

        "income_annum": income_annum,

        "loan_amount": loan_amount,

        "loan_term": loan_term,

        "cibil_score": cibil_score,

        "residential_assets_value": residential_assets_value,

        "commercial_assets_value": commercial_assets_value,

        "luxury_assets_value": luxury_assets_value,

        "bank_asset_value": bank_asset_value
    }


    try:

        response = requests.post(
            API_URL,
            json=payload
        )


        if response.status_code == 200:

            result = response.json()


            st.success(
                f"Prediction: {result['prediction']}"
            )


            st.metric(
                "Approval Probability",
                f"{result['approval_probability']*100:.2f}%"
            )


        else:

            st.error(response.json())


    except Exception as e:

        st.error(
            f"API Error: {e}"
        )