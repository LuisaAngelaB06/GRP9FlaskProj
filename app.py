from flask import Flask, render_template
import os

app = Flask(__name__)

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