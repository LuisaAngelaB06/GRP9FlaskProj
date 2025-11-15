from flask import Flask, render_template
from config import Config
<<<<<<< HEAD
from models.db import db

=======
>>>>>>> acdde8ebb56e77efbcbb4f2aeebf0449466726f4
import os

app = Flask(__name__)

app.config.from_object(Config)

<<<<<<< HEAD
db.init_app(app)

=======
>>>>>>> acdde8ebb56e77efbcbb4f2aeebf0449466726f4
# Login page route
@app.route('/')
def login():
    return render_template('login.html')

# Register page route
@app.route('/signup')
def register():
    return render_template('signup.html')

if __name__ == "__main__":
    port = int(os.getenv('PORT', 5055))
    app.run(debug=True, port=port)