import streamlit as st
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

/* ---------- MAIN BACKGROUND ---------- */

.stApp {
    background: #f5f7fb;
}


/* ---------- SIDEBAR ---------- */

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0f172a, #172554);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}


/* ---------- HERO ---------- */

.hero {
    background: linear-gradient(135deg, #0f172a, #2563eb);
    padding: 45px 30px;
    border-radius: 25px;
    text-align: center;
    color: white;
    margin-bottom: 30px;
    box-shadow: 0 12px 35px rgba(37, 99, 235, 0.25);
}

.hero h1 {
    font-size: 48px;
    font-weight: 800;
    margin: 0;
}

.hero p {
    font-size: 19px;
    margin: 12px 0;
    opacity: 0.95;
}

.hero span {
    font-size: 14px;
    opacity: 0.75;
}


/* ---------- SECTION TITLE ---------- */

.section-title {
    font-size: 32px;
    font-weight: 750;
    color: #0f172a;
    margin-bottom: 5px;
}

.section-subtitle {
    font-size: 16px;
    color: #64748b;
    margin-bottom: 25px;
}


/* ---------- FEATURE CARDS ---------- */

.card {
    background: white;
    padding: 28px;
    border-radius: 20px;
    min-height: 190px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 8px 25px rgba(15, 23, 42, 0.07);
}

.card h2 {
    font-size: 35px;
    margin: 0;
}

.card h3 {
    color: #0f172a;
    margin: 10px 0;
}

.card p {
    color: #64748b;
    line-height: 1.6;
}


/* ---------- ACCOUNT CARD ---------- */

.account-card {
    background: linear-gradient(135deg, #0f172a, #1d4ed8);
    color: white;
    padding: 32px;
    border-radius: 22px;
    margin-top: 25px;
    box-shadow: 0 12px 30px rgba(15, 23, 42, 0.18);
}

.account-card small {
    opacity: 0.7;
    letter-spacing: 1px;
}

.account-card h2 {
    margin-top: 8px;
}

.account-number {
    font-size: 29px;
    font-weight: 700;
    letter-spacing: 3px;
    margin: 10px 0 22px;
}


/* ---------- QUICK ACTION ---------- */

.quick-card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    border: 1px solid #e2e8f0;
    box-shadow: 0 6px 20px rgba(15, 23, 42, 0.06);
}


/* ---------- FOOTER ---------- */

.footer {
    text-align: center;
    color: #64748b;
    padding: 35px 10px;
    margin-top: 50px;
    border-top: 1px solid #e2e8f0;
}


/* ---------- BUTTON ---------- */

.stButton > button,
.stFormSubmitButton > button {
    border-radius: 10px;
    font-weight: 600;
}


/* ---------- INPUTS ---------- */

div[data-baseweb="input"] {
    border-radius: 10px;
}


/* ---------- METRICS ---------- */

div[data-testid="stMetric"] {
    background: white;
    padding: 20px;
    border-radius: 16px;
    border: 1px solid #e2e8f0;
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
    <p>Smart • Secure • Simple Banking Management System</p>
    <span>Python • Streamlit • JSON</span>
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
        '<div class="section-title">Welcome to NovaBank 👋</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="section-subtitle">'
        'Your simple and secure digital banking management system.'
        '</div>',
        unsafe_allow_html=True
    )

    # FEATURE CARDS

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
        '<div class="section-title">📝 Create New Account</div>',
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

                st.markdown(
                    f"""
                    <div class="account-card">

                        <small>ACCOUNT CREATED</small>

                        <h2>Welcome, {name} 👋</h2>

                        <small>YOUR ACCOUNT NUMBER</small>

                        <div class="account-number">
                            {result}
                        </div>

                        <small>INITIAL BALANCE</small>

                        <h2>₹0.00</h2>

                        <small>
                            ⚠️ Please save your account number safely.
                        </small>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:

                st.error(result)
            else:

                st.error(result)


# =========================================================
# DEPOSIT
# =========================================================

elif option == "💰 Deposit Money":

    st.markdown(
        '<div class="section-title">💰 Deposit Money</div>',
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
        '<div class="section-title">💸 Withdraw Money</div>',
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
        '<div class="section-title">👤 Account Details</div>',
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

                st.success("✅ Account verified successfully!")

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

                st.markdown(
                    f"""
                    <div class="account-card">

                        <small>ACCOUNT HOLDER</small>
                        <h2>{user['name']}</h2>

                        <small>ACCOUNT NUMBER</small>

                        <div class="account-number">
                            {user['account no.']}
                        </div>

                        <small>EMAIL</small>
                        <p>{user['email']}</p>

                        <small>AVAILABLE BALANCE</small>
                        <h2>₹{user['balance']:,.2f}</h2>

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
        '<div class="section-title">✏️ Update Details</div>',
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

            st.error("Please enter a valid current PIN.")

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
                name=new_name.strip() if new_name.strip() else None,
                email=new_email.strip() if new_email.strip() else None,
                new_pin=int(new_pin) if new_pin else None
            )

            if success:

                st.success(f"✅ {message}")

            else:

                st.error(message)


# =========================================================
# DELETE ACCOUNT
# =========================================================

elif option == "🗑️ Delete Account":

    st.markdown(
        '<div class="section-title">🗑️ Delete Account</div>',
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
</p> <b>NovaBank</b> 
 
<br> 
 
Python • Streamlit • JSON

    Secure Banking Management System © 2026

</div>
""", unsafe_allow_html=True)
