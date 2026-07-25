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


# ---------------- Applicant Information ---------------- #

st.subheader("Applicant Information")


name = st.text_input("Name")

name_error = len(name.strip()) < 3

if name_error:
    st.error("Name must contain at least 3 characters.")


gender = st.selectbox(
    "Gender",
    ["Male", "Female", "Other"]
)


no_of_dependents = st.number_input(
    "Number of Dependents",
    value=0,
    step=1
)

dependents_error = no_of_dependents < 0

if dependents_error:
    st.error("Number of Dependents cannot be negative.")


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


# ---------------- Financial Information ---------------- #

st.subheader("Financial Information")


income_annum = st.number_input(
    "Annual Income",
    value=0.0,
    step=10000.0
)

income_error = income_annum <= 0

if income_error:
    st.error("Annual Income must be greater than 0.")



loan_amount = st.number_input(
    "Loan Amount",
    value=0.0,
    step=10000.0
)

loan_error = loan_amount <= 0

if loan_error:
    st.error("Loan Amount must be greater than 0.")



loan_term = st.number_input(
    "Loan Term (Months)",
    value=12,
    step=1
)

loan_term_error = loan_term <= 0

if loan_term_error:
    st.error("Loan Term must be a positive number.")



cibil_score = st.number_input(
    "CIBIL Score",
    value=300,
    step=1
)

cibil_error = cibil_score <= 0 or cibil_score > 900

if cibil_error:
    st.error("CIBIL Score must be positive and between 1 and 900.")



# ---------------- Assets ---------------- #

st.subheader("Assets")


residential_assets_value = st.number_input(
    "Residential Assets Value",
    value=0.0,
    step=10000.0
)

residential_error = residential_assets_value < 0

if residential_error:
    st.error("Residential Assets Value cannot be negative.")



commercial_assets_value = st.number_input(
    "Commercial Assets Value",
    value=0.0,
    step=10000.0
)

commercial_error = commercial_assets_value < 0

if commercial_error:
    st.error("Commercial Assets Value cannot be negative.")



luxury_assets_value = st.number_input(
    "Luxury Assets Value",
    value=0.0,
    step=10000.0
)

luxury_error = luxury_assets_value < 0

if luxury_error:
    st.error("Luxury Assets Value cannot be negative.")



bank_asset_value = st.number_input(
    "Bank Assets Value",
    value=0.0,
    step=10000.0
)

bank_error = bank_asset_value < 0

if bank_error:
    st.error("Bank Assets Value cannot be negative.")


# ---------------- Final Validation Status ---------------- #

has_errors = any([
    name_error,
    dependents_error,
    income_error,
    loan_error,
    loan_term_error,
    cibil_error,
    residential_error,
    commercial_error,
    luxury_error,
    bank_error
])



# ---------------- Prediction Button ---------------- #

predict_clicked = st.button(
    "🔍 Predict Loan",
    disabled=has_errors,
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