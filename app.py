import streamlit as st
import base64

# ── Page config ──────────────────────────────────────────────────
st.set_page_config(
    page_title="Email signature generator",
    page_icon="✉️",
    layout="wide",
)

# ── Logo (embedded as base64 so the app is fully self-contained) ─
LOGO_B64 = "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"

LOGO_FULLCOLOR_B64 = "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"

# ── Styles ───────────────────────────────────────────────────────
st.markdown("""
<style>
  /* Hide Streamlit branding */
  #MainMenu, footer, header { visibility: hidden; }

  /* Page background */
  .stApp { background-color: #D3D9DB; }

  /* Tighten up spacing */
  .block-container { padding-top: 2rem; padding-bottom: 2rem; }

  /* Section title */
  h1 { color: #79B55B !important; font-size: 2.2rem !important; font-weight: 400 !important; }

  /* Signature preview box */
  .sig-box {
    background: white;
    border: 1px solid #e5e7eb;
    border-radius: 12px;
    padding: 24px 28px;
    margin-bottom: 16px;
  }
  .sig-label {
    font-weight: 700;
    color: #1B454D;
    font-size: 0.95rem;
    margin-bottom: 4px;
  }
  .sig-hint {
    color: #9AAAAB;
    font-size: 0.85rem;
    margin-bottom: 16px;
  }
</style>
""", unsafe_allow_html=True)

# ── Layout: two columns ──────────────────────────────────────────
col_form, col_preview = st.columns(2, gap="large")

# ── LEFT: Form ───────────────────────────────────────────────────
with col_form:
    st.markdown('<div style="background:white; border-radius:24px; padding:32px;">', unsafe_allow_html=True)
    st.title("Email signature generator")

    logo_choice = st.radio(
        "Logo",
        ["Green", "Full colour"],
        horizontal=True,
    )

    name     = st.text_input("Name",            placeholder="Joe Bloggs")
    jobtitle = st.text_input("Job title",        placeholder="Account Executive")
    pronouns = st.text_input("Pronouns",         placeholder="Optional")
    email    = st.text_input("Email address",    placeholder="joe.bloggs@enable.com")

    tel_options = [
        "+1 628-251-1057",
        "+1 416-628-1921",
        "+44 330 3112 808",
        "Other",
        "No phone number",
    ]
    tel1 = st.selectbox("Main or office telephone number", tel_options)
    tel1other = ""
    if tel1 == "Other":
        tel1other = st.text_input("Enter telephone number", placeholder="e.g. +353 1 234 5678")

    tel2 = st.text_input("Mobile telephone number", placeholder="Optional")

    office_options = [
        "535 Mission St. Floor 14, San Francisco, CA 94105",
        "545 King St. W. Toronto, ON M5V 1M1, Canada",
        "9-12 The Courtyard, Stratford-upon-Avon, CV37 9NP, UK",
        "120 Spencer St. Melbourne, VIC 3000, Australia",
        "333 George St. Sydney, NSW 2000, Australia",
        "B:HIVE Building, Smales Farm, 74 Taharoto Road, Takapuna Auckland, 0622",
        "No address",
    ]
    street = st.selectbox("Enable office location closest to you", office_options)

    generate = st.button("Generate signatures", type="primary", use_container_width=False)

    st.markdown("""
    <p style="color:#9AAAAB; font-size:0.85rem; margin-top:2rem;">
      Use this tool to generate your email signature. Then take a look at the instructions for
      how to set up a signature in Outlook
      <a href="https://support.microsoft.com/en-us/office/create-an-email-signature-in-outlook-for-mac-637c3b77-3d2a-4610-9cea-e3ad622aa54e" target="_blank">for Mac</a> and
      <a href="https://support.microsoft.com/en-us/office/create-an-email-signature-31fb24f9-e698-4789-b92a-f0e777f774ca" target="_blank">for PC</a>.
    </p>
    """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# ── RIGHT: Preview ───────────────────────────────────────────────
with col_preview:
    st.markdown('<div style="background:white; border-radius:24px; padding:32px; min-height:400px;">', unsafe_allow_html=True)

    # Resolve the phone number
    if tel1 == "Other":
        tel = tel1other
    elif tel1 == "No phone number":
        tel = ""
    else:
        tel = tel1

    has_data = bool(name and email)

    if not has_data:
        st.markdown("""
        <div style="display:flex; align-items:center; justify-content:center; min-height:320px;">
          <p style="color:#9AAAAB; text-align:center; max-width:32ch;">
            Once you fill in the form your signatures will be displayed here.
          </p>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Build the name line (with optional pronouns)
        name_display = name
        if pronouns:
            name_display += f" ({pronouns})"

        # Pick logo based on user selection
        active_logo = LOGO_FULLCOLOR_B64 if logo_choice == "Full colour" else LOGO_B64

        # Build the shared signature table HTML
        def sig_table(include_street=False):
            tel2_line = f'<br><span style="font-family:Arial,sans-serif;font-size:14px;color:#000;">{tel2}</span>' if tel2 else ""
            show_street = include_street and street != "No address"
            street_line = f'<br><span style="font-family:Arial,sans-serif;font-size:14px;color:#000;">{street}</span>' if show_street else ""
            # Phone + email line: omit bullet if no phone number
            # Wrap phone in a styled <a> to prevent email clients auto-linking it
            if tel:
                tel_span = f'<a href="#" style="font-family:Arial,sans-serif;font-size:14px;color:#000000;text-decoration:none;cursor:text;" x-apple-data-detectors="false">{tel}</a>'
                contact_line = f'{tel_span}<span style="font-family:Arial,sans-serif;font-size:14px;color:#000;"> &bull; </span><a href="mailto:{email}" style="font-family:Arial,sans-serif;font-size:14px;color:#0B8F43;text-decoration:underline;">{email}</a>'
            else:
                contact_line = f'<a href="mailto:{email}" style="font-family:Arial,sans-serif;font-size:14px;color:#0B8F43;text-decoration:underline;">{email}</a>'
            return f"""
            <table cellspacing="0" cellpadding="0" border="0" style="border-collapse:collapse;">
              <tr>
                <td style="padding-right:14px;border-right:2px solid #00A74C;vertical-align:middle;">
                  <a href="https://www.enable.com" target="_blank" style="display:block;"><img src="data:image/png;base64,{active_logo}" width="128" height="31" alt="Enable" style="display:block;border:0;"></a>
                </td>
                <td style="width:14px;"></td>
                <td style="vertical-align:middle;font-family:Arial,sans-serif;font-size:14px;color:#000;line-height:1.5;">
                  <span style="font-family:Arial,sans-serif;font-size:14px;color:#000;">{name_display}</span><br>
                  <span style="font-family:Arial,sans-serif;font-size:14px;color:#000;">{jobtitle}, </span><a href="https://www.enable.com" target="_blank" style="font-family:Arial,sans-serif;font-size:14px;color:#0B8F43;text-decoration:underline;">Enable</a><br>
                  {contact_line}{tel2_line}{street_line}
                </td>
              </tr>
            </table>
            """

        # ── Option 1 ──
        st.markdown('<p class="sig-label">Option 1, recommended version for most roles</p>', unsafe_allow_html=True)
        st.markdown('<p class="sig-hint">Select all below (Ctrl+A / Cmd+A), then copy (Ctrl+C / Cmd+C)</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="sig-box">{sig_table(include_street=False)}</div>', unsafe_allow_html=True)

        # ── Download Option 1 ──
        def wrap_htm(sig_html):
            return f"""<!DOCTYPE html>
<html><head>
<meta charset="UTF-8">
<meta name="format-detection" content="telephone=no, date=no, address=no, email=no">
</head><body>
{sig_html.strip()}
</body></html>"""

        st.download_button(
            "⬇ Download Option 1 as .htm",
            data=wrap_htm(sig_table(include_street=False)),
            file_name="signature-option1.htm",
            mime="text/html",
            key="dl1"
        )

        st.markdown("<hr style='border:none;border-top:2px solid #EBF0F5;margin:24px 0;'>", unsafe_allow_html=True)

        # ── Option 2 ──
        st.markdown('<p class="sig-label">Option 2, includes street address, required for field AEs</p>', unsafe_allow_html=True)
        st.markdown('<p class="sig-hint">Select all below (Ctrl+A / Cmd+A), then copy (Ctrl+C / Cmd+C)</p>', unsafe_allow_html=True)
        st.markdown(f'<div class="sig-box">{sig_table(include_street=True)}</div>', unsafe_allow_html=True)

        # ── Download Option 2 ──
        st.download_button(
            "⬇ Download Option 2 as .htm",
            data=wrap_htm(sig_table(include_street=True)),
            file_name="signature-option2.htm",
            mime="text/html",
            key="dl2"
        )

    st.markdown('</div>', unsafe_allow_html=True)
