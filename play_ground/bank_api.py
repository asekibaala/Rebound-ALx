from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import requests
import logging
from datetime import datetime

# Setup logging
log_filename = f"{__name__}_{datetime.now().strftime('%Y-%m-%d')}.log"
logging.basicConfig(
    filename=log_filename,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


# Initialize Flask app
app = Flask(__name__)

# Configure SQLite database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the database
db = SQLAlchemy(app)

# Define Bank Account model
class BankAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    account_number = db.Column(db.String(20), unique=True, nullable=False)
    balance = db.Column(db.Float, default=0.0)

# Create tables
with app.app_context():
    db.create_all()

# Authentication API URL
AUTH_API_URL = "http://127.0.0.1:5004/validate-token"

# Helper function to validate JWT token
def validate_token(token):
    response = requests.post(AUTH_API_URL, json={"token": token})
    if response.status_code == 200 and response.json().get("valid"):
        return response.json().get("user_id")
    return None

# Create a New Bank Account
@app.route('/create-account', methods=['POST'])
def create_account():
    logging.info("Create-account endpoint hit: Headers=%s, Body=%s", dict(request.headers), request.json)
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token required"}), 401

    user_id = validate_token(token.replace("Bearer ", ""))
    if not user_id:
        return jsonify({"message": "Invalid or expired token"}), 401

    data = request.json
    account_number = data.get('account_number')

    if BankAccount.query.filter_by(account_number=account_number).first():
        return jsonify({"message": "Account already exists"}), 400

    new_account = BankAccount(user_id=user_id, account_number=account_number, balance=0.0)
    db.session.add(new_account)
    db.session.commit()

    return jsonify({"message": "Bank account created successfully"}), 201

# Deposit Money
@app.route('/deposit', methods=['POST'])
def deposit():
    logging.info("Deposit endpoint hit: Headers=%s, Body=%s", dict(request.headers), request.json)
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token required"}), 401

    user_id = validate_token(token.replace("Bearer ", ""))
    if not user_id:
        return jsonify({"message": "Invalid or expired token"}), 401

    data = request.json
    account_number = data.get('account_number')
    amount = data.get('amount')

    account = BankAccount.query.filter_by(user_id=user_id, account_number=account_number).first()
    if not account:
        return jsonify({"message": "Account not found"}), 404

    account.balance += amount
    db.session.commit()

    return jsonify({"message": "Deposit successful", "new_balance": account.balance}), 200

# Withdraw Money
@app.route('/withdraw', methods=['POST'])
def withdraw():
    logging.info("Withdraw endpoint hit: Headers=%s, Body=%s", dict(request.headers), request.json)
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token required"}), 401

    user_id = validate_token(token.replace("Bearer ", ""))
    if not user_id:
        return jsonify({"message": "Invalid or expired token"}), 401

    data = request.json
    account_number = data.get('account_number')
    amount = data.get('amount')

    account = BankAccount.query.filter_by(user_id=user_id, account_number=account_number).first()
    if not account:
        return jsonify({"message": "Account not found"}), 404

    if account.balance < amount:
        return jsonify({"message": "Insufficient funds"}), 400

    account.balance -= amount
    db.session.commit()

    return jsonify({"message": "Withdrawal successful", "new_balance": account.balance}), 200

# Get Account Balance
@app.route('/balance', methods=['GET'])
def balance():
    logging.info("Balance endpoint hit: Headers=%s, Params=%s", dict(request.headers), request.args)
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"message": "Token required"}), 401

    user_id = validate_token(token.replace("Bearer ", ""))
    if not user_id:
        return jsonify({"message": "Invalid or expired token"}), 401

    account_number = request.args.get('account_number')

    account = BankAccount.query.filter_by(user_id=user_id, account_number=account_number).first()
    if not account:
        return jsonify({"message": "Account not found"}), 404

    return jsonify({"account_number": account.account_number, "balance": account.balance}), 200

# Run the banking API
if __name__ == '__main__':
    app.run(port=5005, debug=True)
