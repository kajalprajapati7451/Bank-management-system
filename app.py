import streamlit as st
import html
from main import Bank


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="NovaBank",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

    /* ---------- GLOBAL ---------- */

    * {
        box-sizing: border-box;
    }

    .stApp {
        background: #f5f7fb;
    }

    .main .block-container {
        max-width: 1200px;
        padding: 2rem 2.5rem 1rem;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        background: transparent !important;
    }


    /* ---------- SIDEBAR ---------- */

    [data-testid="stSidebar"] {
        background: #101828;
        border-right: 1px solid #1f2937;
    }

    [data-testid="stSidebar"] > div:first-child {
        padding: 1.5rem 1rem;
    }

    .sidebar-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        padding: 8px 10px 25px;
    }

    .sidebar-logo {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        background: #ffffff;
        color: #101828;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 21px;
        font-weight: 700;
    }

    .sidebar-brand-name {
        color: white;
        font-size: 20px;
        font-weight: 700;
        letter-spacing: -0.5px;
    }

    .sidebar-subtitle {
        color: #98a2b3;
        font-size: 11px;
        margin-top: 2px;
    }

    .nav-label {
        color: #667085;
        font-size: 10px;
        font-weight: 700;
        letter-spacing: 1px;
        padding: 8px 10px;
        margin-top: 10px;
    }

    /* Sidebar radio */

    [data-testid="stSidebar"] .stRadio > div {
        gap: 4px;
    }

    [data-testid="stSidebar"] .stRadio label {
        color: #d0d5dd !important;
        border-radius: 9px;
        padding: 9px 10px;
        margin: 0;
        font-size: 13px;
        transition: 0.2s;
    }

    [data-testid="stSidebar"] .stRadio label:hover {
        background: #1d2939;
        color: white !important;
    }

    [data-testid="stSidebar"] .stRadio label[data-checked="true"] {
        background: #1d2939;
        color: white !important;
    }

    [data-testid="stSidebar"] .stRadio div[role="radiogroup"] {
        gap: 3px;
    }

    .sidebar-bottom {
        margin-top: 35px;
        padding: 15px;
        border: 1px solid #1f2937;
        border-radius: 12px;
        background: #172033;
    }

    .sidebar-bottom-title {
        color: white;
        font-size: 12px;
        font-weight: 600;
    }

    .sidebar-bottom-text {
        color: #98a2b3;
        font-size: 11px;
        margin-top: 4px;
        line-height: 1.5;
    }


    /* ---------- TOP HEADER ---------- */

    .top-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        margin-bottom: 35px;
        padding-bottom: 18px;
        border-bottom: 1px solid #e4e7ec;
    }

    .top-title {
        font-size: 13px;
        color: #667085;
    }

    .secure-badge {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        background: #ecfdf3;
        color: #027a48;
        border: 1px solid #abefc6;
        border-radius: 30px;
        padding: 6px 12px;
        font-size: 11px;
        font-weight: 600;
    }

    .secure-dot {
        width: 6px;
        height: 6px;
        background: #12b76a;
        border-radius: 50%;
    }


    /* ---------- PAGE HEADER ---------- */

    .page-eyebrow {
        color: #667085;
        font-size: 11px;
        font-weight: 700;
        letter-spacing: 1px;
        margin-bottom: 7px;
    }

    .page-title {
        color: #101828;
        font-size: 32px;
        font-weight: 700;
        letter-spacing: -1px;
        margin: 0;
    }

    .page-description {
        color: #667085;
        font-size: 14px;
        margin-top: 7px;
        margin-bottom: 28px;
    }


    /* ---------- HOME ---------- */

    .welcome-section {
        background: #101828;
        border-radius: 18px;
        padding: 38px;
        color: white;
        margin-bottom: 22px;
    }

    .welcome-small {
        color: #98a2b3;
        font-size: 12px;
        font-weight: 600;
        letter-spacing: 1px;
        margin-bottom: 8px;
    }

    .welcome-title {
        font-size: 36px;
        font-weight: 700;
        letter-spacing: -1.2px;
        margin: 0;
    }

    .welcome-text {
        color: #d0d5dd;
        font-size: 14px;
        margin-top: 10px;
        max-width: 600px;
        line-height: 1.6;
    }

    .welcome-icon {
        font-size: 70px;
        text-align: center;
        opacity: 0.9;
    }


    /* ---------- FEATURE CARDS ---------- */

    .feature-card {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 14px;
        padding: 22px;
        height: 100%;
    }

    .feature-icon {
        width: 40px;
        height: 40px;
        border-radius: 10px;
        background: #f2f4f7;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
        margin-bottom: 17px;
    }

    .feature-title {
        font-size: 15px;
        font-weight: 700;
        color: #101828;
        margin-bottom: 6px;
    }

    .feature-text {
        font-size: 12px;
        color: #667085;
        line-height: 1.6;
    }


    /* ---------- FORM PANEL ---------- */

    .form-panel {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 16px;
        padding: 30px;
        max-width: 850px;
        margin: 0 auto;
        box-shadow: 0 2px 8px rgba(16, 24, 40, 0.03);
    }

    .form-panel-title {
        font-size: 19px;
        color: #101828;
        font-weight: 700;
        margin-bottom: 4px;
    }

    .form-panel-description {
        font-size: 12px;
        color: #667085;
        margin-bottom: 25px;
    }


    /* ---------- INPUTS ---------- */

    .stTextInput label,
    .stNumberInput label {
        color: #344054 !important;
        font-size: 12px !important;
        font-weight: 600 !important;
    }

    .stTextInput input,
    .stNumberInput input {
        border: 1px solid #d0d5dd !important;
        border-radius: 9px !important;
        background: white !important;
        color: #101828 !important;
        min-height: 43px;
    }

    .stTextInput input:focus,
    .stNumberInput input:focus {
        border-color: #667085 !important;
        box-shadow: 0 0 0 2px rgba(16, 24, 40, 0.05) !important;
    }

    /* ---------- BUTTON ---------- */

    .stButton > button {
        width: 100%;
        min-height: 43px;
        border-radius: 9px;
        border: 1px solid #101828;
        background: #101828;
        color: white;
        font-size: 13px;
        font-weight: 600;
        transition: 0.2s;
    }

    .stButton > button:hover {
        background: #1d2939;
        border-color: #1d2939;
        color: white;
    }


    /* ---------- BANK CARD ---------- */

    .bank-card {
        background: linear-gradient(135deg, #172033 0%, #101828 100%);
        border-radius: 18px;
        padding: 28px;
        color: white;
        min-height: 245px;
        position: relative;
        overflow: hidden;
        box-shadow: 0 12px 30px rgba(16, 24, 40, 0.15);
    }

    .bank-card::after {
        content: "";
        position: absolute;
        width: 210px;
        height: 210px;
        border-radius: 50%;
        border: 1px solid rgba(255,255,255,0.08);
        right: -80px;
        top: -70px;
    }

    .bank-card-top {
        display: flex;
        justify-content: space-between;
        align-items: center;
    }

    .bank-name {
        font-size: 17px;
        font-weight: 700;
        letter-spacing: 1px;
    }

    .card-status {
        font-size: 9px;
        letter-spacing: 1px;
        color: #98a2b3;
    }

    .chip {
        width: 42px;
        height: 31px;
        border-radius: 6px;
        background: #d0d5dd;
        margin-top: 38px;
        position: relative;
    }

    .chip::before {
        content: "";
        position: absolute;
        left: 19px;
        top: 0;
        width: 1px;
        height: 100%;
        background: #98a2b3;
    }

    .chip::after {
        content: "";
        position: absolute;
        left: 0;
        top: 14px;
        width: 100%;
        height: 1px;
        background: #98a2b3;
    }

    .card-number {
        font-size: 22px;
        letter-spacing: 3px;
        margin-top: 22px;
        font-weight: 500;
    }

    .card-bottom {
        display: flex;
        justify-content: space-between;
        align-items: end;
        margin-top: 24px;
    }

    .card-label {
        font-size: 8px;
        color: #98a2b3;
        letter-spacing: 1px;
        margin-bottom: 4px;
    }

    .card-value {
        font-size: 12px;
        font-weight: 600;
    }


    /* ---------- ACCOUNT INFO ---------- */

    .info-panel {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 16px;
        padding: 25px;
        height: 100%;
    }

    .info-title {
        font-size: 15px;
        font-weight: 700;
        color: #101828;
        margin-bottom: 22px;
    }

    .info-row {
        padding: 13px 0;
        border-bottom: 1px solid #f2f4f7;
    }

    .info-row:last-child {
        border-bottom: none;
    }

    .info-label {
        color: #667085;
        font-size: 11px;
        margin-bottom: 3px;
    }

    .info-value {
        color: #101828;
        font-size: 14px;
        font-weight: 600;
    }


    /* ---------- BALANCE ---------- */

    .balance-panel {
        background: white;
        border: 1px solid #eaecf0;
        border-radius: 16px;
        padding: 25px;
        margin-top: 20px;
    }

    .balance-label {
        font-size: 11px;
        color: #667085;
    }

    .balance-value {
        font-size: 30px;
        font-weight: 700;
        color: #101828;
        margin-top: 5px;
    }


    /* ---------- SUCCESS ---------- */

    .success-box {
        background: #ecfdf3;
        border: 1px solid #abefc6;
        border-radius: 12px;
        padding: 18px 20px;
        margin-top: 20px;
    }

    .success-title {
        color: #027a48;
        font-size: 14px;
        font-weight: 700;
    }

    .success-text {
        color: #05603a;
        font-size: 12px;
        margin-top: 4px;
    }


    /* ---------- WARNING ---------- */

    .danger-box {
        background: #fef3f2;
        border: 1px solid #fecdca;
        border-radius: 12px;
        padding: 17px 20px;
        color: #b42318;
        font-size: 12px;
        margin-bottom: 20px;
    }


    /* ---------- FOOTER ---------- */

    .custom-footer {
        margin-top: 65px;
        padding: 25px 0 10px;
        border-top: 1px solid #e4e7ec;
        display: flex;
        justify-content: space-between;
        gap: 20px;
        color: #667085;
        font-size: 11px;
    }

    .footer-brand {
        color: #101828;
        font-weight: 700;
        font-size: 13px;
    }

    .footer-tech {
        text-align: right;
    }


    /* ---------- RESPONSIVE ---------- */

    @media (max-width: 900px) {

        .main .block-container {
            padding: 1.5rem 1.2rem;
        }

        .welcome-section {
            padding: 28px;
        }

        .welcome-title {
            font-size: 29px;
        }

        .welcome-icon {
            display: none;
        }

        .page-title {
            font-size: 27px;
        }

        .bank-card {
            margin-bottom: 20px;
        }
    }


    @media (max-width: 600px) {

        .main .block-container {
            padding: 1rem 0.8rem;
        }

        .top-header {
            margin-bottom: 25px;
        }

        .secure-badge {
            font-size: 9px;
            padding: 5px 8px;
        }

        .welcome-section {
            padding: 24px 20px;
            border-radius: 14px;
        }

        .welcome-title {
            font-size: 25px;
        }

        .page-title {
            font-size: 24px;
        }

        .form-panel {
            padding: 20px 16px;
            border-radius: 13px;
        }

        .bank-card {
            padding: 22px;
            min-height: 220px;
        }

        .card-number {
            font-size: 16px;
            letter-spacing: 2px;
        }

        .custom-footer {
            flex-direction: column;
        }

        .footer-tech {
            text-align: left;
        }
    }

</style>
""", unsafe_allow_html=True)


# =========================================================
# BANK OBJECT
# =========================================================

bank = Bank()


# =========================================================
# HELPER FUNCTIONS
# =========================================================

def page_header(section, title, description):

    st.markdown(
        f"""
        <div class="page-eyebrow">{section.upper()}</div>
        <h1 class="page-title">{title}</h1>
        <div class="page-description">{description}</div>
        """,
        unsafe_allow_html=True
    )


def footer():

    st.markdown(
        """
        <div class="custom-footer">

            <div>
                <div class="footer-brand">🏦 NovaBank</div>
                <div>Smart • Secure • Simple Banking</div>
            </div>

            <div class="footer-tech">
                Python • Streamlit • JSON<br>
                © 2026 NovaBank
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-brand">

            <div class="sidebar-logo">🏦</div>

            <div>
                <div class="sidebar-brand-name">NovaBank</div>
                <div class="sidebar-subtitle">Banking Management System</div>
            </div>

        </div>

        <div class="nav-label">MAIN MENU</div>
        """,
        unsafe_allow_html=True
    )

    page = st.radio(
        "Navigation",
        [
            "🏠  Dashboard",
            "📝  Create Account",
            "💰  Deposit Money",
            "💸  Withdraw Money",
            "👤  Account Details",
            "✏️  Update Details",
            "🗑️  Delete Account"
        ],
        label_visibility="collapsed"
    )

    st.markdown(
        """
        <div class="sidebar-bottom">
            <div class="sidebar-bottom-title">🔒 Secure Banking</div>
            <div class="sidebar-bottom-text">
                Your account data is managed locally
                using Python and JSON.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# TOP HEADER
# =========================================================

st.markdown(
    """
    <div class="top-header">

        <div class="top-title">
            NovaBank / Banking Management System
        </div>

        <div class="secure-badge">
            <span class="secure-dot"></span>
            System Online
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# DASHBOARD
# =========================================================

if page == "🏠  Dashboard":

    page_header(
        "Dashboard",
        "Welcome to NovaBank",
        "A simple and secure banking management system built with Python."
    )

    st.markdown(
        """
        <div class="welcome-section">

            <div class="welcome-small">
                NOVABANK DIGITAL BANKING
            </div>

            <div class="welcome-title">
                Banking made simple.
            </div>

            <div class="welcome-text">
                Create accounts, manage balances and update your
                banking details from one clean interface.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">📝</div>

                <div class="feature-title">
                    Create Account
                </div>

                <div class="feature-text">
                    Open a new NovaBank account with your
                    basic personal details.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">💳</div>

                <div class="feature-title">
                    Manage Money
                </div>

                <div class="feature-text">
                    Deposit or withdraw money while keeping
                    your account balance updated.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="feature-card">

                <div class="feature-icon">🔐</div>

                <div class="feature-title">
                    Account Security
                </div>

                <div class="feature-text">
                    Your account operations require the correct
                    account number and PIN.
                </div>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================================================
# CREATE ACCOUNT
# =========================================================

elif page == "📝  Create Account":

    page_header(
        "Accounts",
        "Create Account",
        "Open a new NovaBank account in a few simple steps."
    )

    st.markdown(
        """
        <div class="form-panel">

            <div class="form-panel-title">
                Account Information
            </div>

            <div class="form-panel-description">
                Enter your details below. You must be 18 or older.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("create_account_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "Age",
                min_value=1,
                max_value=100,
                value=18
            )

        with col2:

            email = st.text_input(
                "Email Address",
                placeholder="example@email.com"
            )

            pin = st.text_input(
                "4-Digit PIN",
                type="password",
                max_chars=4,
                placeholder="Enter 4 digit PIN"
            )

        st.markdown("<br>", unsafe_allow_html=True)

        submitted = st.form_submit_button(
            "Create Account"
        )

    if submitted:

        if not pin.isdigit() or len(pin) != 4:

            st.error("PIN must contain exactly 4 digits.")

        else:

            success, result = bank.create_account(
                name.strip(),
                age,
                email.strip(),
                int(pin)
            )

            if success:

                st.markdown(
                    f"""
                    <div class="success-box">

                        <div class="success-title">
                            ✓ Account Created Successfully
                        </div>

                        <div class="success-text">
                            Welcome, {html.escape(name)}.
                        </div>

                        <div style="
                            margin-top:10px;
                            font-size:18px;
                            font-weight:700;
                            color:#101828;
                        ">
                            Account Number: {html.escape(str(result))}
                        </div>

                        <div class="success-text">
                            Your initial account balance is ₹0.00.
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.error(result)


# =========================================================
# DEPOSIT MONEY
# =========================================================

elif page == "💰  Deposit Money":

    page_header(
        "Transactions",
        "Deposit Money",
        "Add money to your NovaBank account."
    )

    st.markdown(
        """
        <div class="form-panel">
            <div class="form-panel-title">Deposit Funds</div>
            <div class="form-panel-description">
                Enter your account credentials and deposit amount.
                Maximum deposit is ₹10,000 per transaction.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("deposit_form"):

        col1, col2 = st.columns(2)

        with col1:

            account_number = st.text_input(
                "Account Number",
                placeholder="Enter account number"
            )

            pin = st.text_input(
                "PIN",
                type="password",
                max_chars=4,
                placeholder="Enter 4 digit PIN"
            )

        with col2:

            amount = st.number_input(
                "Deposit Amount",
                min_value=1,
                max_value=10000,
                value=1000,
                step=100
            )

        st.markdown("<br>", unsafe_allow_html=True)

        submitted = st.form_submit_button(
            "Deposit Money"
        )

    if submitted:

        if not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        else:

            success, message = bank.deposit_money(
                account_number.strip(),
                int(pin),
                amount
            )

            if success:
                st.success(message)
            else:
                st.error(message)


# =========================================================
# WITHDRAW MONEY
# =========================================================

elif page == "💸  Withdraw Money":

    page_header(
        "Transactions",
        "Withdraw Money",
        "Withdraw money from your NovaBank account."
    )

    st.markdown(
        """
        <div class="form-panel">
            <div class="form-panel-title">Withdraw Funds</div>
            <div class="form-panel-description">
                Verify your account and enter the amount you want
                to withdraw.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("withdraw_form"):

        col1, col2 = st.columns(2)

        with col1:

            account_number = st.text_input(
                "Account Number",
                placeholder="Enter account number"
            )

            pin = st.text_input(
                "PIN",
                type="password",
                max_chars=4,
                placeholder="Enter 4 digit PIN"
            )

        with col2:

            amount = st.number_input(
                "Withdrawal Amount",
                min_value=1,
                value=1000,
                step=100
            )

        st.markdown("<br>", unsafe_allow_html=True)

        submitted = st.form_submit_button(
            "Withdraw Money"
        )

    if submitted:

        if not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        else:

            success, message = bank.withdraw_money(
                account_number.strip(),
                int(pin),
                amount
            )

            if success:
                st.success(message)
            else:
                st.error(message)


# =========================================================
# ACCOUNT DETAILS
# =========================================================

elif page == "👤  Account Details":

    page_header(
        "Account",
        "Account Details",
        "View your account information and available balance."
    )

    col1, col2 = st.columns([1.15, 0.85])

    with col1:

        account_number = st.text_input(
            "Account Number",
            placeholder="Enter account number"
        )

    with col2:

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            placeholder="Enter 4 digit PIN"
        )

    if st.button("View Account"):

        if not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        else:

            user = bank.show_details(
                account_number.strip(),
                int(pin)
            )

            if user:

                name = html.escape(str(user["name"]))
                email = html.escape(str(user["email"]))
                account_no = html.escape(
                    str(user["account no."])
                )

                col1, col2 = st.columns([1.1, 0.9])

                with col1:

                    st.markdown(
                        f"""
                        <div class="bank-card">

                            <div class="bank-card-top">

                                <div class="bank-name">
                                    NOVABANK
                                </div>

                                <div class="card-status">
                                    ACTIVE ACCOUNT
                                </div>

                            </div>

                            <div class="chip"></div>

                            <div class="card-number">
                                {account_no}
                            </div>

                            <div class="card-bottom">

                                <div>
                                    <div class="card-label">
                                        ACCOUNT HOLDER
                                    </div>

                                    <div class="card-value">
                                        {name.upper()}
                                    </div>
                                </div>

                                <div>
                                    <div class="card-label">
                                        ACCOUNT TYPE
                                    </div>

                                    <div class="card-value">
                                        SAVINGS
                                    </div>
                                </div>

                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                with col2:

                    st.markdown(
                        f"""
                        <div class="info-panel">

                            <div class="info-title">
                                Personal Information
                            </div>

                            <div class="info-row">
                                <div class="info-label">
                                    ACCOUNT HOLDER
                                </div>
                                <div class="info-value">
                                    {name}
                                </div>
                            </div>

                            <div class="info-row">
                                <div class="info-label">
                                    AGE
                                </div>
                                <div class="info-value">
                                    {user["age"]}
                                </div>
                            </div>

                            <div class="info-row">
                                <div class="info-label">
                                    EMAIL
                                </div>
                                <div class="info-value">
                                    {email}
                                </div>
                            </div>

                            <div class="info-row">
                                <div class="info-label">
                                    ACCOUNT NUMBER
                                </div>
                                <div class="info-value">
                                    {account_no}
                                </div>
                            </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                st.markdown(
                    f"""
                    <div class="balance-panel">

                        <div class="balance-label">
                            AVAILABLE BALANCE
                        </div>

                        <div class="balance-value">
                            ₹{user["balance"]:,.2f}
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.error("Invalid account number or PIN.")


# =========================================================
# UPDATE DETAILS
# =========================================================

elif page == "✏️  Update Details":

    page_header(
        "Account",
        "Update Details",
        "Update your name, email address or account PIN."
    )

    st.markdown(
        """
        <div class="form-panel">
            <div class="form-panel-title">
                Update Account
            </div>

            <div class="form-panel-description">
                Your current account number and PIN are required
                to make changes.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("update_form"):

        col1, col2 = st.columns(2)

        with col1:

            account_number = st.text_input(
                "Account Number",
                placeholder="Enter account number"
            )

            pin = st.text_input(
                "Current PIN",
                type="password",
                max_chars=4,
                placeholder="Current PIN"
            )

        with col2:

            new_name = st.text_input(
                "New Name",
                placeholder="Leave empty to keep current name"
            )

            new_email = st.text_input(
                "New Email",
                placeholder="Leave empty to keep current email"
            )

        new_pin = st.text_input(
            "New 4-Digit PIN",
            type="password",
            max_chars=4,
            placeholder="Leave empty to keep current PIN"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        submitted = st.form_submit_button(
            "Update Details"
        )

    if submitted:

        if not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid current 4-digit PIN.")

        elif new_pin and (
            not new_pin.isdigit() or len(new_pin) != 4
        ):

            st.error("New PIN must contain exactly 4 digits.")

        else:

            success, message = bank.update_details(
                account_number=account_number.strip(),
                pin=int(pin),
                name=new_name.strip() or None,
                email=new_email.strip() or None,
                new_pin=int(new_pin) if new_pin else None
            )

            if success:
                st.success(message)
            else:
                st.error(message)


# =========================================================
# DELETE ACCOUNT
# =========================================================

elif page == "🗑️  Delete Account":

    page_header(
        "Account",
        "Delete Account",
        "Permanently remove your NovaBank account."
    )

    st.markdown(
        """
        <div class="danger-box">
            ⚠️ <b>Important:</b> Account deletion is permanent.
            You must withdraw your remaining balance before
            deleting the account.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="form-panel">

            <div class="form-panel-title">
                Delete Account
            </div>

            <div class="form-panel-description">
                Verify your account credentials to continue.
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

    with st.form("delete_form"):

        account_number = st.text_input(
            "Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "PIN",
            type="password",
            max_chars=4,
            placeholder="Enter 4 digit PIN"
        )

        st.markdown("<br>", unsafe_allow_html=True)

        submitted = st.form_submit_button(
            "Delete Account"
        )

    if submitted:

        if not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        else:

            success, message = bank.delete_account(
                account_number.strip(),
                int(pin)
            )

            if success:
                st.success(message)
                st.info(
                    "Your account has been removed from NovaBank."
                )
            else:
                st.error(message)


# =========================================================
# FOOTER
# =========================================================

footer()