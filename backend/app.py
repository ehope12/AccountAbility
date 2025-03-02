from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from CreateUser import createuser

app = Flask(__name__)

# Allow cross-origin resource sharing
CORS(app)

# Load environment variables
load_dotenv()

# Register blueprints
app.register_blueprint(createuser, url_prefix='/createuser')

if __name__ == '__main__':
    app.run(debug=True)