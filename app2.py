from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import check_password_hash, generate_password_hash
import subprocess
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Secret key for session

# Predefined login credentials
login_id = "21271A6606"
password_hash = generate_password_hash("iompbatch1")  # Hashed password

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        login_input = request.form['login_id']
        password_input = request.form['password']
        
        # Check if login ID matches and password hash is correct
        if login_input == login_id and check_password_hash(password_hash, password_input):
            flash("Login Successful!", "success")
            return redirect(url_for('dashboard'))
        else:
            flash("Invalid credentials, please try again.", "danger")
    
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    # Define the full path to test3.py
    test3_script = r'C:\Users\akshi\OneDrive\Desktop\(IOMP)\PresencePro\PresencePro\test3.py'
    
    # Use subprocess to launch test3.py
    subprocess.Popen(['python', test3_script])
    
    return "Welcome to the Dashboard! The interface is now launching."

if __name__ == '__main__':
    app.run(debug=True)
