from flask import Flask, render_template, request, redirect, flash, session
from mysqlconnection import connectToMySQL 
import re
from flask_bcrypt import Bcrypt        

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = 'SuperSecretKey'

#Get requests 
@app.route('/contactUs', methods= ['GET'])
def contactUs():
    return render_template('contactUs.html')

@app.route('/history', methods= ['GET'])
def history():
    return render_template('history.html')

@app.route('/profile',methods=['GET'])
def profile():
    return render_template('profile.html')

#get and post requests
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    elif request.method == 'POST':
        # Validate form 
        is_valid = True
        if not EMAIL_REGEX.match(request.form['form_email']):
            flash("Invalid email address!")
            is_valid = False
        #if not valid, redirect back to login screen
        if not is_valid:
            return redirect('/login')

        # Check if the user exists in the database
        mysql = connectToMySQL('clinic_manage')
        query = "SELECT * FROM users WHERE email = %(form_email)s"
        data = {'form_email': request.form['form_email']}
        user = mysql.query_db(query, data)

        # Validate password
        if len(user) > 0 and bcrypt.check_password_hash(user[0]['password'], request.form['form_password']):
            session['user_id'] = user[0]['id']
            return redirect('/dashboard')
        else:
            flash("Invalid email or password!")
            return redirect('/login')

    
#registration post and get route
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        is_valid = True
    
    #Registration form validation 
    if len(request.form['form_first_name']) < 2:
        flash('First Name is required')
        is_valid = False
    
    if len(request.form['form_last_name']) < 2:
        flash('Last Name is required')
        is_valid = False

    if not EMAIL_REGEX.match(request.form['form_email']):
        flash("Invalid email address!")
        is_valid = False
    else:
        mysql = connectToMySQL('clinic_manage')
        query = "SELECT * FROM users WHERE email = %(form_email)s"
        data={'form_email': request.form['form_email']}
        result= mysql.query_db(query,data)
        if result:
            flash('Email Already exists')
            is_valid = False
        
    if len(request.form['form_password']) < 8:
        flash('Password must be 8 characters long')
        is_valid = False

    if request.form['form_password'] != request.form['form_confirm_password']:
        flash("Passwords must match!")
        is_valid = False

    if not is_valid:
        return redirect('/register')
    else:
        pw_hash = bcrypt.generate_password_hash(request.form['form_password'])
        mysql = connectToMySQL('clinic_manage')
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(hashed_pw)s);"
        data={
            'f_name': request.form['form_first_name'],
            'l_name': request.form['form_last_name'],
            'email': request.form['form_email'],
            'hashed_pw': pw_hash
        }
        new_user_id = mysql.query_db(query,data)


        session['user_id']= new_user_id
        flash('Registration successful')
        return redirect('/dashboard')
    
#dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Must be logged in to access dashboard')
        return redirect('/login')
    
    user_id = session['user_id']
    #Get login info
    mysql = connectToMySQL('clinic_manage')
    query = "SELECT first_name FROM users WHERE id = %(user_id)s"
    data={'user_id': user_id}
    user = mysql.query_db(query,data)
    
    if user:
        user_first_name = user[0]['first_name']
        welcome_message = f"Hello, {user_first_name}!"
        return render_template('dashboard.html', welcome_message=welcome_message)
    else:
        flash('User not found')
        return redirect('/login')
    
#post requests
@app.route('/logout', methods = ['POST'])
def logout():
    session.clear()
    return redirect('/login')



if __name__ == '__main__':
    app.run(debug=True)

