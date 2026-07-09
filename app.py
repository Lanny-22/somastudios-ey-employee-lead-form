import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="EY Employee Submission Form",
    page_icon="📋",
    layout="centered",
)

st.markdown(
    """
    <style>
      .stApp,
      [data-testid="stAppViewContainer"],
      [data-testid="stMain"],
      [data-testid="block-container"],
      [data-testid="stHeader"],
      [data-testid="stBottom"],
      [data-testid="stMainBlockContainer"] {
        background-color: #fcf1eb !important;
      }
      iframe[title="streamlit_components_v1.components.html"] {
        background-color: #fcf1eb;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

st.title("EY Employee Submission Form")
st.caption(
    "Register to gain exclusive EY employee discounts."
)

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
  <style>
    :root {
      --momenceColorBackground: #fcf1eb;
      --momenceColorPrimary: 16, 89, 95;
      --momenceColorBlack: 3, 1, 13;
    }
    html {
      background: #fcf1eb;
    }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 0;
      background: #fcf1eb;
      min-height: 100%;
    }
    .momence-lead_form-success {
      padding: 12px 0;
      font-size: 16px;
      line-height: 1.5;
      color: #0d8050;
      font-weight: 600;
    }
  </style>
</head>
<body>
  <div id="momence-plugin-lead-form"></div>
  <script
    async
    type="module"
    id="momence-plugin-lead-form-src"
    host_id="81008"
    fields="firstName,lastName,email,phoneNumber"
    token="DOjMdWLXQ5"
    country_code="mt"
    source_id="221834"
    data_collect_consent="required"
    data-on-success-msg="Thank you! We have received your submission and will email you within the next 24–48 hours with your unique EY discount code."
    data-field-def='{"firstName":{"type":"text","label":"First name","required":true},"lastName":{"type":"text","label":"Last name","required":true},"email":{"type":"email","label":"Email","required":true},"phoneNumber":{"type":"phone-number","label":"Phone number","required":true}}'
    src="https://momence.com/plugin/lead-form/lead-form.js"
  ></script>
</body>
</html>
"""

components.html(FORM_HTML, height=620, scrolling=False)
