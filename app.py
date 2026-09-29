import streamlit as st
from main import Bank


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="centered"
)


# ---------------- BANK OBJECT ----------------

bank = Bank()


# ---------------- TITLE ----------------

st.title("🏦 Bank Management System")

st.write("Manage your bank account easily using the options below.")


# ---------------- SIDEBAR ----------------

st.sidebar.title("Bank Menu")

option = st.sidebar.radio(
    "Choose an option",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Update Details",
        "Delete Account"
    ]
)


# ==================================================
# CREATE ACCOUNT
# ==================================================

if option == "Create Account":

    st.header("📝 Create New Account")

    name = st.text_input("Enter your name")

    age = st.number_input(
        "Enter your age",
        min_value=1,
        max_value=100,
        step=1
    )

    email = st.text_input("Enter your email")

    pin = st.text_input(
        "Create 4-digit PIN",
        type="password",
        max_chars=4
    )

    if st.button("Create Account"):

        if not pin.isdigit():

            st.error("PIN must contain only numbers.")

        elif len(pin) != 4:

            st.error("PIN must contain exactly 4 digits.")

        else:

            success, result = bank.create_account(
                name=name,
                age=age,
                email=email,
                pin=int(pin)
            )

            if success:

                st.success("🎉 Account created successfully!")

                st.info(
                    f"Your Account Number is: **{result}**"
                )

                st.warning(
                    "Please save your account number safely."
                )

            else:

                st.error(result)


# ==================================================
# DEPOSIT MONEY
# ==================================================

elif option == "Deposit Money":

    st.header("💰 Deposit Money")

    account_number = st.text_input(
        "Enter account number"
    )

    pin = st.text_input(
        "Enter PIN",
        type="password",
        max_chars=4
    )

    amount = st.number_input(
        "Enter amount",
        min_value=0.0,
        step=100.0
    )

    if st.button("Deposit Money"):

        if not pin.isdigit():

            st.error("Invalid PIN.")

        else:

            success, message = bank.deposit_money(
                account_number,
                int(pin),
                amount
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# WITHDRAW MONEY
# ==================================================

elif option == "Withdraw Money":

    st.header("💸 Withdraw Money")

    account_number = st.text_input(
        "Enter account number"
    )

    pin = st.text_input(
        "Enter PIN",
        type="password",
        max_chars=4
    )

    amount = st.number_input(
        "Enter amount",
        min_value=0.0,
        step=100.0
    )

    if st.button("Withdraw Money"):

        if not pin.isdigit():

            st.error("Invalid PIN.")

        else:

            success, message = bank.withdraw_money(
                account_number,
                int(pin),
                amount
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# SHOW DETAILS
# ==================================================

elif option == "Show Details":

    st.header("👤 Account Details")

    account_number = st.text_input(
        "Enter account number"
    )

    pin = st.text_input(
        "Enter PIN",
        type="password",
        max_chars=4
    )

    if st.button("Show Details"):

        if not pin.isdigit():

            st.error("Invalid PIN.")

        else:

            user = bank.show_details(
                account_number,
                int(pin)
            )

            if user:

                st.success("Account found!")

                st.write("### Personal Information")

                st.write(
                    f"**Name:** {user['name']}"
                )

                st.write(
                    f"**Age:** {user['age']}"
                )

                st.write(
                    f"**Email:** {user['email']}"
                )

                st.write(
                    f"**Account Number:** {user['account no.']}"
                )

                st.write("### Account Balance")

                st.metric(
                    "Current Balance",
                    f"₹{user['balance']}"
                )

            else:

                st.error(
                    "Invalid account number or PIN."
                )


# ==================================================
# UPDATE DETAILS
# ==================================================

elif option == "Update Details":

    st.header("✏️ Update Account Details")

    account_number = st.text_input(
        "Enter account number"
    )

    pin = st.text_input(
        "Current PIN",
        type="password",
        max_chars=4
    )

    st.write(
        "Leave any field empty if you don't want to change it."
    )

    new_name = st.text_input(
        "New Name"
    )

    new_email = st.text_input(
        "New Email"
    )

    new_pin = st.text_input(
        "New PIN",
        type="password",
        max_chars=4
    )

    if st.button("Update Details"):

        if not pin.isdigit():

            st.error("Invalid current PIN.")

        elif new_pin and (
            not new_pin.isdigit()
            or len(new_pin) != 4
        ):

            st.error(
                "New PIN must contain exactly 4 digits."
            )

        else:

            success, message = bank.update_details(
                account_number=account_number,
                pin=int(pin),
                name=new_name if new_name else None,
                email=new_email if new_email else None,
                new_pin=int(new_pin) if new_pin else None
            )

            if success:
                st.success(message)

            else:
                st.error(message)


# ==================================================
# DELETE ACCOUNT
# ==================================================

elif option == "Delete Account":

    st.header("🗑️ Delete Account")

    st.warning(
        "⚠️ This action cannot be undone."
    )

    account_number = st.text_input(
        "Enter account number"
    )

    pin = st.text_input(
        "Enter PIN",
        type="password",
        max_chars=4
    )

    confirmation = st.checkbox(
        "I understand that I want to delete this account."
    )

    if st.button("Delete Account"):

        if not confirmation:

            st.error(
                "Please confirm account deletion."
            )

        elif not pin.isdigit():

            st.error("Invalid PIN.")

        else:

            success, message = bank.delete_account(
                account_number,
                int(pin)
            )

            if success:
                st.success(message)

            else:
                st.error(message)