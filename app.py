import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="EY Lead Form",
    page_icon="📋",
    layout="centered",
)

st.title("EY Lead Form")
st.caption("Please use your EY work email (@mt.ey.com) to register.")

FORM_HTML = """
<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      margin: 0;
      padding: 0;
    }
    #ey-email-error {
      display: none;
      margin: 0 0 12px;
      padding: 10px 12px;
      border-radius: 8px;
      background: #fde8e8;
      color: #9b1c1c;
      font-size: 14px;
      font-weight: 600;
    }
    .momence-lead_form-success {
      padding: 12px 0;
      font-size: 16px;
      line-height: 1.5;
      color: #0d8050;
      font-weight: 600;
    }
  </style>
  <script>
    (function () {
      const ALLOWED_DOMAIN = "@mt.ey.com";
      const ERROR_MESSAGE =
        "Please use your EY work email (" + ALLOWED_DOMAIN + ").";

      function isValidEyEmail(email) {
        if (!email || typeof email !== "string") {
          return false;
        }
        return /^[^\\s@]+@mt\\.ey\\.com$/i.test(email.trim());
      }

      function getEmailFromPayload(body) {
        if (!body) {
          return "";
        }

        if (typeof body === "string") {
          try {
            return getEmailFromPayload(JSON.parse(body));
          } catch (error) {
            return "";
          }
        }

        if (typeof body === "object") {
          return String(body.email || body.Email || "").trim();
        }

        return "";
      }

      function showError(message) {
        const errorEl = document.getElementById("ey-email-error");
        if (errorEl) {
          errorEl.textContent = message;
          errorEl.style.display = "block";
        } else {
          alert(message);
        }
      }

      function hideError() {
        const errorEl = document.getElementById("ey-email-error");
        if (errorEl) {
          errorEl.style.display = "none";
          errorEl.textContent = "";
        }
      }

      function rejectLeadSubmission(message) {
        showError(message);
        return Promise.resolve(
          new Response(
            JSON.stringify({
              status: "fail",
              error: message,
            }),
            {
              status: 400,
              headers: { "Content-Type": "application/json" },
            }
          )
        );
      }

      function getEmailFromForm(form) {
        if (!form) {
          return "";
        }

        const emailInput =
          form.querySelector('input[type="email"]') ||
          form.querySelector('input[name="email"]') ||
          form.querySelector('input[id*="email" i]');

        return emailInput ? emailInput.value.trim() : "";
      }

      const originalFetch = window.fetch.bind(window);
      window.fetch = function (input, init) {
        const url = typeof input === "string" ? input : input.url;

        if (url && url.includes("/integrations/customer-leads/") && url.includes("/collect")) {
          const email = getEmailFromPayload(init && init.body);
          if (!isValidEyEmail(email)) {
            return rejectLeadSubmission(ERROR_MESSAGE);
          }
        }

        return originalFetch(input, init);
      };

      document.addEventListener(
        "submit",
        function (event) {
          const email = getEmailFromForm(event.target);
          if (!email) {
            return;
          }

          if (!isValidEyEmail(email)) {
            event.preventDefault();
            event.stopPropagation();
            event.stopImmediatePropagation();
            showError(ERROR_MESSAGE);
          } else {
            hideError();
          }
        },
        true
      );

      document.addEventListener(
        "input",
        function (event) {
          const target = event.target;
          if (
            target &&
            (target.type === "email" ||
              target.name === "email" ||
              /email/i.test(target.id || ""))
          ) {
            hideError();
          }
        },
        true
      );
    })();
  </script>
</head>
<body>
  <p id="ey-email-error"></p>
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
    data-on-success-msg="Thank you! Please check your email for your exclusive unique one-time use discount code."
    data-field-def='{"firstName":{"type":"text","label":"First name","required":true},"lastName":{"type":"text","label":"Last name","required":true},"email":{"type":"email","label":"Email (Work Email)","required":true,"hidden":false},"phoneNumber":{"type":"phone-number","label":"Phone number","required":true}}'
    src="https://momence.com/plugin/lead-form/lead-form.js"
  ></script>
</body>
</html>
"""

components.html(FORM_HTML, height=720, scrolling=True)
