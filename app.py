from flask import Flask,render_template
app = Flask(__name__)
app.secret_key = 'SuperSecretKey'

#login page
@app.route('/login')
def home():
    return render_template('login.html') 

#register page
@app.route('/register')
def registration():
    return render_template('registration.html')

#dashboard page
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

#allows to refresh without closing out virtual environment
if __name__ == '__main__':
    app.run(debug=True)

