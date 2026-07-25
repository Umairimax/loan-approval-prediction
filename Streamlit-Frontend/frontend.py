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

# ---------------- Validation ---------------- #

validation_errors = []

if len(name.strip()) < 2:
    validation_errors.append("Name must contain at least 2 characters.")

if income_annum <= 0:
    validation_errors.append("Annual Income must be greater than 0.")

if loan_amount <= 0:
    validation_errors.append("Loan Amount must be greater than 0.")

if loan_term <= 0:
    validation_errors.append("Loan Term must be greater than 0.")

if cibil_score < 300 or cibil_score > 900:
    validation_errors.append("CIBIL Score must be between 300 and 900.")


if validation_errors:

    st.warning("Please fix the following before predicting:")

    for error in validation_errors:
        st.write(f"• {error}")


predict_clicked = st.button(
    "🔍 Predict Loan",
    disabled=len(validation_errors) > 0,
    use_container_width=True
)


# ---------------- Prediction ---------------- #

if predict_clicked:

    payload = {

        "name": name.strip(),

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

        with st.spinner("Predicting..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=15
            )

        if response.status_code == 200:

            result = response.json()

            st.divider()

            if result["prediction"] == "Approved":

                st.success("✅ Loan Approved")

            else:

                st.error("❌ Loan Rejected")

            st.metric(
                label="Approval Probability",
                value=f"{result['approval_probability'] * 100:.2f}%"
            )

        else:

            try:

                error = response.json()

                if "message" in error:

                    st.error(error["message"])

                else:

                    st.error("Prediction failed.")

            except:

                st.error("Unable to process your request.")

    except requests.exceptions.ConnectionError:

        st.error("Unable to connect to the backend server.")

    except requests.exceptions.Timeout:

        st.error("Request timed out. Please try again.")

    except Exception as e:

        st.error(f"Unexpected Error: {e}")


























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