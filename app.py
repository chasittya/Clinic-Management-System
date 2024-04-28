from flask import Flask,render_template
app = Flask(__name__)
app.secret_key = 'SuperSecretKey'


@app.route('/login')
def home():
    return render_template('login.html') # pass data to our template

@app.route('/register')
def registration():
    return render_template('registration.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)

