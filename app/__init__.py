from flask import Flask
from dotenv import load_dotenv
import os
import bcrypt

# load environment variables in .env file, if available
load_dotenv()

password_hash = os.getenv('HASH', '')
password_salt = os.getenv('SALT', '')

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
