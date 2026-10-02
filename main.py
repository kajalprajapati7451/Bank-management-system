import json
import random
import string
from pathlib import Path


class Bank:

    database = "data.json"

    def __init__(self):
        self.data = self.load_data()

    # ---------------- LOAD DATA ----------------
    def load_data(self):

        if not Path(self.database).exists():
            return []

        try:
            with open(self.database, "r", encoding="utf-8") as fs:
                return json.load(fs)

        except (json.JSONDecodeError, FileNotFoundError):
            return []

    # ---------------- SAVE DATA ----------------
    def update(self):

        with open(self.database, "w", encoding="utf-8") as fs:
            json.dump(self.data, fs, indent=4)

    # ---------------- GENERATE ACCOUNT NUMBER ----------------
    @staticmethod
    def account_generate():

        while True:

            alphabets = random.choices(
                string.ascii_uppercase,
                k=3
            )

            numbers = random.choices(
                string.digits,
                k=3
            )

            special = random.choices(
                "!@#$%^&*",
                k=3
            )

            account = alphabets + numbers + special

            random.shuffle(account)

            account_number = "".join(account)

            if not Path("data.json").exists():
                return account_number

            try:
                with open(
                    "data.json",
                    "r",
                    encoding="utf-8"
                ) as fs:
                    data = json.load(fs)

            except (json.JSONDecodeError, FileNotFoundError):
                data = []

            if not any(
                user["account no."] == account_number
                for user in data
            ):
                return account_number

    # ---------------- FIND ACCOUNT ----------------
    def find_account(self, account_number, pin):

        for user in self.data:

            if (
                user["account no."] == account_number
                and user["pin"] == pin
            ):
                return user

        return None

    # ---------------- CREATE ACCOUNT ----------------
    def create_account(self, name, age, email, pin):

        if not name:
            return False, "Name cannot be empty."

        if age < 18:
            return False, "You must be at least 18 years old."

        if not email:
            return False, "Email cannot be empty."

        if len(str(pin)) != 4:
            return False, "PIN must contain exactly 4 digits."

        account_number = self.account_generate()

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "account no.": account_number,
            "balance": 0
        }

        self.data.append(info)

        self.update()

        return True, account_number

    # ---------------- DEPOSIT MONEY ----------------
    def deposit_money(self, account_number, pin, amount):

        user = self.find_account(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > 10000:
            return False, "You can deposit maximum ₹10,000 at a time."

        user["balance"] += amount

        self.update()

        return True, f"₹{amount} deposited successfully."

    # ---------------- WITHDRAW MONEY ----------------
    def withdraw_money(self, account_number, pin, amount):

        user = self.find_account(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if amount <= 0:
            return False, "Amount must be greater than 0."

        if amount > user["balance"]:
            return False, "Insufficient balance."

        user["balance"] -= amount

        self.update()

        return True, f"₹{amount} withdrawn successfully."

    # ---------------- SHOW DETAILS ----------------
    def show_details(self, account_number, pin):

        user = self.find_account(
            account_number,
            pin
        )

        if not user:
            return None

        return user

    # ---------------- UPDATE DETAILS ----------------
    def update_details(
        self,
        account_number,
        pin,
        name=None,
        email=None,
        new_pin=None
    ):

        user = self.find_account(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if name:
            user["name"] = name

        if email:
            user["email"] = email

        if new_pin:

            if len(str(new_pin)) != 4:
                return False, "New PIN must contain exactly 4 digits."

            user["pin"] = new_pin

        self.update()

        return True, "Details updated successfully."

    # ---------------- DELETE ACCOUNT ----------------
    def delete_account(self, account_number, pin):

        user = self.find_account(
            account_number,
            pin
        )

        if not user:
            return False, "Invalid account number or PIN."

        if user["balance"] > 0:
            return False, (
                "Please withdraw your remaining balance "
                "before deleting the account."
            )

        self.data.remove(user)

        self.update()

        return True, "Account deleted successfully."
