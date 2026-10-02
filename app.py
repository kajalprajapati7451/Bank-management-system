import streamlit as st
from main import Bank
import html


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

/* =========================================================
   MAIN BACKGROUND
========================================================= */

.stApp {
    background: #f4f7fb;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    max-width: 1400px;
}


/* =========================================================
   SIDEBAR
========================================================= */

section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #0b1220 0%,
        #111c35 50%,
        #172554 100%
    );
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

section[data-testid="stSidebar"] hr {
    border-color: rgba(255,255,255,0.15);
}

section[data-testid="stSidebar"] .stRadio label {
    padding: 8px 10px;
    border-radius: 10px;
    transition: 0.2s;
}

section[data-testid="stSidebar"] .stRadio label:hover {
    background: rgba(255,255,255,0.10);
}


/* =========================================================
   HERO
========================================================= */

.hero {
    background:
        radial-gradient(
            circle at top right,
            rgba(96,165,250,0.35),
            transparent 35%
        ),
        linear-gradient(
            135deg,
            #0f172a,
            #2563eb
        );

    padding: 50px 35px;

    border-radius: 28px;

    text-align: center;

    color: white;

    margin-bottom: 35px;

    box-shadow:
        0 20px 45px rgba(15,23,42,0.18);

    border: 1px solid rgba(255,255,255,0.10);
}

.hero h1 {
    font-size: 50px;
    font-weight: 800;
    letter-spacing: -1px;
    margin: 0;
}

.hero p {
    font-size: 19px;
    margin: 12px 0;
    opacity: 0.95;
}

.hero span {
    font-size: 13px;
    opacity: 0.70;
    letter-spacing: 1px;
}


/* =========================================================
   SECTION TITLE
========================================================= */

.section-title {
    font-size: 32px;
    font-weight: 800;
    color: #0f172a;
    margin-bottom: 4px;
}

.section-subtitle {
    font-size: 16px;
    color: #64748b;
    margin-bottom: 28px;
}


/* =========================================================
   FEATURE CARDS
========================================================= */

.card {
    background: white;

    padding: 28px;

    border-radius: 22px;

    min-height: 190px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 10px 30px rgba(15,23,42,0.07);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}

.card:hover {
    transform: translateY(-5px);

    box-shadow:
        0 18px 40px rgba(15,23,42,0.12);
}

.card h2 {
    font-size: 36px;
    margin: 0 0 5px 0;
}

.card h3 {
    color: #0f172a;
    margin: 10px 0;
    font-size: 21px;
}

.card p {
    color: #64748b;
    line-height: 1.7;
}


/* =========================================================
   ACCOUNT CARD
========================================================= */

.account-card {

    position: relative;

    background:
        radial-gradient(
            circle at 90% 10%,
            rgba(96,165,250,0.35),
            transparent 30%
        ),
        linear-gradient(
            135deg,
            #0b1220,
            #1d4ed8 70%,
            #2563eb
        );

    color: white;

    padding: 35px;

    border-radius: 25px;

    margin-top: 28px;

    min-height: 280px;

    overflow: hidden;

    box-shadow:
        0 18px 40px rgba(15,23,42,0.22);

    border: 1px solid rgba(255,255,255,0.12);
}


/* Decorative circle */

.account-card::after {

    content: "";

    position: absolute;

    width: 190px;
    height: 190px;

    right: -75px;
    bottom: -80px;

    border-radius: 50%;

    background: rgba(255,255,255,0.08);
}


/* Account labels */

.account-card small {

    display: block;

    color: rgba(255,255,255,0.65);

    font-size: 11px;

    font-weight: 600;

    letter-spacing: 1.5px;

    margin-top: 10px;
}


/* Account heading */

.account-card h2 {

    color: white;

    font-size: 28px;

    font-weight: 750;

    margin: 6px 0 28px;
}


/* Account number */

.account-number {

    display: inline-block;

    background: rgba(255,255,255,0.10);

    border: 1px solid rgba(255,255,255,0.18);

    padding: 14px 20px;

    border-radius: 12px;

    font-family: monospace;

    font-size: 25px;

    font-weight: 700;

    letter-spacing: 4px;

    margin: 8px 0 25px;

    color: white;

    position: relative;

    z-index: 1;
}


/* Email */

.account-card p {

    color: rgba(255,255,255,0.88);

    font-size: 15px;

    margin: 6px 0 25px;
}


/* Balance */

.account-card .balance {

    color: white;

    font-size: 30px;

    font-weight: 750;

    margin: 5px 0 25px;
}


/* Warning */

.account-card .warning {

    display: inline-block;

    padding: 10px 14px;

    border-radius: 10px;

    background: rgba(255,255,255,0.08);

    color: rgba(255,255,255,0.85);

    font-size: 13px;

    position: relative;

    z-index: 2;
}


/* =========================================================
   QUICK ACTION
========================================================= */

.quick-card {

    background: white;

    padding: 25px;

    border-radius: 20px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.06);
}


/* =========================================================
   FORMS
========================================================= */

div[data-testid="stForm"] {

    background: white;

    padding: 25px;

    border-radius: 20px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 8px 25px rgba(15,23,42,0.05);
}


/* =========================================================
   INPUTS
========================================================= */

div[data-baseweb="input"] {
    border-radius: 12px;
}

div[data-baseweb="input"] > div {
    border-radius: 12px;
}


/* =========================================================
   BUTTONS
========================================================= */

.stButton > button,
.stFormSubmitButton > button {

    border-radius: 12px;

    font-weight: 700;

    min-height: 45px;

    border: none;

    transition:
        transform 0.2s ease,
        box-shadow 0.2s ease;
}

.stButton > button:hover,
.stFormSubmitButton > button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 8px 20px rgba(37,99,235,0.20);
}


/* =========================================================
   METRICS
========================================================= */

div[data-testid="stMetric"] {

    background: white;

    padding: 22px;

    border-radius: 18px;

    border: 1px solid #e2e8f0;

    box-shadow:
        0 8px 22px rgba(15,23,42,0.06);
}

div[data-testid="stMetricLabel"] {
    color: #64748b !important;
}

div[data-testid="stMetricValue"] {
    color: #0f172a !important;
    font-weight: 750;
}


/* =========================================================
   ALERTS
========================================================= */

div[data-testid="stAlert"] {

    border-radius: 14px;

    border: none;

    box-shadow:
        0 5px 18px rgba(15,23,42,0.05);
}


/* =========================================================
   FOOTER
========================================================= */

.footer {

    text-align: center;

    color: #64748b;

    padding: 40px 10px 20px;

    margin-top: 60px;

    border-top: 1px solid #e2e8f0;
}

.footer h1 {

    color: #0f172a;

    font-size: 24px;

    margin-bottom: 5px;
}

.footer p {

    font-size: 14px;

    margin: 5px;
}

.footer small {

    color: #94a3b8;
}


/* =========================================================
   MOBILE
========================================================= */

@media (max-width: 768px) {

    .hero {
        padding: 35px 20px;
    }

    .hero h1 {
        font-size: 36px;
    }

    .hero p {
        font-size: 16px;
    }

    .section-title {
        font-size: 26px;
    }

    .account-card {
        padding: 25px;
    }

    .account-number {
        font-size: 20px;
        letter-spacing: 2px;
    }

}

</style>
""", unsafe_allow_html=True)


# =========================================================
# BANK OBJECT
# =========================================================

bank = Bank()


# =========================================================
# HERO HEADER
# =========================================================

st.markdown("""
<div class="hero">

    <h1>🏦 NovaBank</h1>

    <p>
        Smart • Secure • Simple Banking Management System
    </p>

    <span>
        Python • Streamlit • JSON
    </span>

</div>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown("# 🏦 NovaBank")

    st.caption("Digital Banking Management System")

    st.markdown("---")

    option = st.radio(
        "Navigation",
        [
            "🏠 Home",
            "📝 Create Account",
            "💰 Deposit Money",
            "💸 Withdraw Money",
            "👤 Account Details",
            "✏️ Update Details",
            "🗑️ Delete Account"
        ]
    )

    st.markdown("---")

    st.caption("🔐 Secure Banking")
    st.caption("🐍 Python + Streamlit")
    st.caption("💾 JSON Database")


# =========================================================
# HOME
# =========================================================

if option == "🏠 Home":

    st.markdown(
        '<div class="section-title">'
        'Welcome to NovaBank 👋'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Your simple and secure digital banking management system.'
        '</div>',
        unsafe_allow_html=True
    )


    # =====================================================
    # FEATURE CARDS
    # =====================================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown("""
        <div class="card">

            <h2>🔐</h2>

            <h3>Secure</h3>

            <p>
                Account number and PIN authentication
                keeps your banking information protected.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col2:

        st.markdown("""
        <div class="card">

            <h2>💰</h2>

            <h3>Easy Banking</h3>

            <p>
                Deposit and withdraw money using
                simple and user-friendly controls.
            </p>

        </div>
        """, unsafe_allow_html=True)


    with col3:

        st.markdown("""
        <div class="card">

            <h2>⚡</h2>

            <h3>Fast Management</h3>

            <p>
                Create, update, view and manage
                your account from one dashboard.
            </p>

        </div>
        """, unsafe_allow_html=True)


    # =====================================================
    # QUICK ACTIONS
    # =====================================================

    st.markdown("## 🚀 Quick Actions")

    col1, col2 = st.columns(2)

    with col1:

        st.info(
            "📝 **Create Account**\n\n"
            "Open a new NovaBank account."
        )

    with col2:

        st.info(
            "💰 **Manage Money**\n\n"
            "Deposit or withdraw money securely."
        )


# =========================================================
# CREATE ACCOUNT
# =========================================================

elif option == "📝 Create Account":

    st.markdown(
        '<div class="section-title">'
        '📝 Create New Account'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Open your new NovaBank account in a few seconds.'
        '</div>',
        unsafe_allow_html=True
    )


    with st.form("create_account_form"):

        col1, col2 = st.columns(2)

        with col1:

            name = st.text_input(
                "👤 Full Name",
                placeholder="Enter your full name"
            )

            age = st.number_input(
                "🎂 Age",
                min_value=1,
                max_value=100,
                value=18
            )


        with col2:

            email = st.text_input(
                "📧 Email",
                placeholder="example@gmail.com"
            )

            pin = st.text_input(
                "🔐 Create 4-Digit PIN",
                type="password",
                max_chars=4
            )


        submitted = st.form_submit_button(
            "🚀 Create Account",
            use_container_width=True
        )


    if submitted:

        if not name.strip():

            st.error("Please enter your name.")

        elif age < 18:

            st.error("You must be at least 18 years old.")

        elif not email.strip():

            st.error("Please enter your email.")

        elif not pin.isdigit():

            st.error("PIN must contain only numbers.")

        elif len(pin) != 4:

            st.error("PIN must contain exactly 4 digits.")

        else:

            success, result = bank.create_account(
                name=name.strip(),
                age=age,
                email=email.strip(),
                pin=int(pin)
            )


            if success:

                st.success(
                    "🎉 Account created successfully!"
                )


                # Escape account number safely
                safe_result = html.escape(str(result))

                safe_name = html.escape(str(name))


                st.markdown(
                    f"""
                    <div class="account-card">

                        <small>
                            ✓ ACCOUNT CREATED
                        </small>

                        <h2>
                            Welcome, {safe_name} 👋
                        </h2>

                        <small>
                            YOUR ACCOUNT NUMBER
                        </small>

                        <div class="account-number">
                            {safe_result}
                        </div>

                        <small>
                            INITIAL BALANCE
                        </small>

                        <div class="balance">
                            ₹0.00
                        </div>

                        <div class="warning">
                            ⚠️ Please save your account number safely.
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            else:

                st.error(result)


# =========================================================
# DEPOSIT
# =========================================================

elif option == "💰 Deposit Money":

    st.markdown(
        '<div class="section-title">'
        '💰 Deposit Money'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Add money securely to your NovaBank account.'
        '</div>',
        unsafe_allow_html=True
    )


    with st.form("deposit_form"):

        account_number = st.text_input(
            "🏦 Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "💵 Deposit Amount",
            min_value=0.0,
            step=100.0
        )


        submitted = st.form_submit_button(
            "💰 Deposit Money",
            use_container_width=True
        )


    if submitted:

        if not account_number.strip():

            st.error("Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        elif amount <= 0:

            st.error("Amount must be greater than ₹0.")

        else:

            success, message = bank.deposit_money(
                account_number.strip(),
                int(pin),
                amount
            )

            if success:

                st.success(f"✅ {message}")

            else:

                st.error(message)


# =========================================================
# WITHDRAW
# =========================================================

elif option == "💸 Withdraw Money":

    st.markdown(
        '<div class="section-title">'
        '💸 Withdraw Money'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Withdraw money securely from your account.'
        '</div>',
        unsafe_allow_html=True
    )


    with st.form("withdraw_form"):

        account_number = st.text_input(
            "🏦 Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        amount = st.number_input(
            "💵 Withdrawal Amount",
            min_value=0.0,
            step=100.0
        )


        submitted = st.form_submit_button(
            "💸 Withdraw Money",
            use_container_width=True
        )


    if submitted:

        if not account_number.strip():

            st.error("Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        elif amount <= 0:

            st.error("Amount must be greater than ₹0.")

        else:

            success, message = bank.withdraw_money(
                account_number.strip(),
                int(pin),
                amount
            )

            if success:

                st.success(f"✅ {message}")

            else:

                st.error(message)


# =========================================================
# ACCOUNT DETAILS
# =========================================================

elif option == "👤 Account Details":

    st.markdown(
        '<div class="section-title">'
        '👤 Account Details'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'View your personal and account information securely.'
        '</div>',
        unsafe_allow_html=True
    )


    with st.form("details_form"):

        account_number = st.text_input(
            "🏦 Account Number",
            placeholder="Enter account number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )


        submitted = st.form_submit_button(
            "🔎 View Account",
            use_container_width=True
        )


    if submitted:

        if not account_number.strip():

            st.error("Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            st.error("Please enter a valid 4-digit PIN.")

        else:

            user = bank.show_details(
                account_number.strip(),
                int(pin)
            )


            if user:

                st.success(
                    "✅ Account verified successfully!"
                )


                # =================================================
                # ACCOUNT SUMMARY
                # =================================================

                col1, col2, col3 = st.columns(3)


                with col1:

                    st.metric(
                        "💰 Balance",
                        f"₹{user['balance']:,.2f}"
                    )


                with col2:

                    st.metric(
                        "🎂 Age",
                        user["age"]
                    )


                with col3:

                    st.metric(
                        "🏦 Status",
                        "Active"
                    )


                # =================================================
                # ACCOUNT CARD
                # =================================================

                safe_name = html.escape(
                    str(user["name"])
                )

                safe_account = html.escape(
                    str(user["account no."])
                )

                safe_email = html.escape(
                    str(user["email"])
                )


                st.markdown(
                    f"""
                    <div class="account-card">

                        <small>
                            ✓ ACCOUNT VERIFIED
                        </small>

                        <h2>
                            Welcome, {safe_name} 👋
                        </h2>

                        <small>
                            ACCOUNT NUMBER
                        </small>

                        <div class="account-number">
                            {safe_account}
                        </div>

                        <small>
                            EMAIL
                        </small>

                        <p>
                            📧 {safe_email}
                        </p>

                        <small>
                            AVAILABLE BALANCE
                        </small>

                        <div class="balance">
                            ₹{user['balance']:,.2f}
                        </div>

                        <div class="warning">
                            🏦 NovaBank • Account Status: Active
                        </div>

                    </div>
                    """,
                    unsafe_allow_html=True
                )


            else:

                st.error(
                    "❌ Invalid account number or PIN."
                )


# =========================================================
# UPDATE DETAILS
# =========================================================

elif option == "✏️ Update Details":

    st.markdown(
        '<div class="section-title">'
        '✏️ Update Details'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Change your name, email or PIN.'
        '</div>',
        unsafe_allow_html=True
    )


    with st.form("update_form"):

        account_number = st.text_input(
            "🏦 Account Number"
        )

        pin = st.text_input(
            "🔐 Current PIN",
            type="password",
            max_chars=4
        )


        st.markdown("### 📝 New Information")


        new_name = st.text_input(
            "👤 New Name",
            placeholder="Leave empty to keep current name"
        )

        new_email = st.text_input(
            "📧 New Email",
            placeholder="Leave empty to keep current email"
        )

        new_pin = st.text_input(
            "🔐 New PIN",
            type="password",
            max_chars=4,
            placeholder="Leave empty to keep current PIN"
        )


        submitted = st.form_submit_button(
            "💾 Update Details",
            use_container_width=True
        )


    if submitted:

        if not account_number.strip():

            st.error("Please enter account number.")

        elif not pin.isdigit() or len(pin) != 4:

            st.error(
                "Please enter a valid current PIN."
            )

        elif new_pin and (
            not new_pin.isdigit()
            or len(new_pin) != 4
        ):

            st.error(
                "New PIN must contain exactly 4 digits."
            )

        else:

            success, message = bank.update_details(
                account_number=account_number.strip(),
                pin=int(pin),
                name=(
                    new_name.strip()
                    if new_name.strip()
                    else None
                ),
                email=(
                    new_email.strip()
                    if new_email.strip()
                    else None
                ),
                new_pin=(
                    int(new_pin)
                    if new_pin
                    else None
                )
            )


            if success:

                st.success(
                    f"✅ {message}"
                )

            else:

                st.error(message)


# =========================================================
# DELETE ACCOUNT
# =========================================================

elif option == "🗑️ Delete Account":

    st.markdown(
        '<div class="section-title">'
        '🗑️ Delete Account'
        '</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Permanently remove your NovaBank account.'
        '</div>',
        unsafe_allow_html=True
    )


    st.error(
        "⚠️ Warning: Account deletion is permanent."
    )


    with st.form("delete_form"):

        account_number = st.text_input(
            "🏦 Account Number"
        )

        pin = st.text_input(
            "🔐 PIN",
            type="password",
            max_chars=4
        )

        confirmation = st.checkbox(
            "I understand that this account will be permanently deleted."
        )


        submitted = st.form_submit_button(
            "🗑️ Delete Account",
            use_container_width=True
        )


    if submitted:

        if not confirmation:

            st.error(
                "Please confirm account deletion."
            )

        elif not account_number.strip():

            st.error(
                "Please enter account number."
            )

        elif not pin.isdigit() or len(pin) != 4:

            st.error(
                "Please enter a valid 4-digit PIN."
            )

        else:

            success, message = bank.delete_account(
                account_number.strip(),
                int(pin)
            )


            if success:

                st.success(
                    f"✅ {message}"
                )

                st.balloons()

            else:

                st.error(message)


# =========================================================
# FOOTER
# =========================================================

st.markdown("""
<div class="footer">

    <h1>🏦 NovaBank</h1>

    <p>
        Smart • Secure • Simple Banking Management System
    </p>

    <b>NovaBank</b>

    <br><br>

    <small>
        Python • Streamlit • JSON
    </small>

    <br>

    <small>
        Secure Banking Management System © 2026
    </small>

</div>
""", unsafe_allow_html=True)