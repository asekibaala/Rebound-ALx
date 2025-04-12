from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, decode_token
import datetime
import logging
from datetime import datetime
from datetime import datetime, timedelta

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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'supersecretkey'  # Change this for production

# Initialize extensions
jwt = JWTManager(app)
db = SQLAlchemy(app)

# Define User model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Create tables
with app.app_context():
    db.create_all()

# User Registration
@app.route('/register', methods=['POST'])
def register():
    logging.info("Register endpoint hit: %s", request.json)
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# User Login and Token Issuance
@app.route('/login', methods=['POST'])
def login():
    logging.info("Login endpoint hit: %s", request.json)
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username, password=password).first()
    if not user:
        return jsonify({"message": "Invalid credentials"}), 401

    access_token = create_access_token(identity=user.id, expires_delta=timedelta(hours=1))
    return jsonify({"token": access_token}), 200

# Validate Token
@app.route('/validate-token', methods=['POST'])
def validate_token():
    logging.info("Validate-token endpoint hit: %s", request.json)
    data = request.json
    token = data.get('token')

    try:
        decoded_token = decode_token(token)
        return jsonify({"valid": True, "user_id": decoded_token["sub"]}), 200
    except:
        return jsonify({"valid": False, "message": "Invalid or expired token"}), 401

# Run authentication API
if __name__ == '__main__':
    app.run(port=5004, debug=True)
