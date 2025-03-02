from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from CreateUser import createuser
from Login import loginuser
import requests
import os

app = Flask(__name__)

# Allow cross-origin resource sharing
CORS(app)

# Load environment variables
load_dotenv()
api_key = os.getenv("API_KEY")

# Register blueprints
app.register_blueprint(createuser, url_prefix='/createuser')
app.register_blueprint(loginuser, url_prefix='/loginuser')

if __name__ == '__main__':
    # Clear the environment
    url = f"http://api.nessieisreal.com/data?type=Customers&key={api_key}"
    response = requests.delete(
        url,
        headers={'Content-Type': 'application/json'}
    )
    app.run(debug=True)