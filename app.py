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


#get and post requests
#login
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
     print("User authenticated successfully")
    # Fetch the user's ID based on their role
    user_id = None
    if user[0]['role'] == 'patient':
        mysql = connectToMySQL('clinic_manage')
        query = "SELECT patientID FROM patients WHERE userID = %(user_id)s"
        data = {'user_id': user[0]['id']}
        result = mysql.query_db(query, data)

        if result:
            user_id = result[0]['userID']
            print(f"Patient ID: {user_id}")
    else:
        user_id = user[0]['id']
        print(f"User ID: {user_id}")

    # Set the session variable with the correct user ID
    if user_id:
        session['user_id'] = user_id
        return redirect('/dashboard')
    else:
        flash("Invalid email or password!")
        return redirect('/login')

        
#profile
@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('Must be logged in to access profile')
        return redirect('/login')

    if request.method == 'GET':
        # Get patient first name and last name if available
        mysql = connectToMySQL('clinic_manage')
        query = "SELECT FName, LName FROM patients WHERE userID = %(user_id)s"
        data = {'user_id': session['user_id']}
        patient_info = mysql.query_db(query, data)

        # Render profile template with patient info
        return render_template('profile.html', patient_info=patient_info[0] if patient_info else None)

    elif request.method == 'POST':
        # Update patient info
        gender = request.form['gender']
        birthday = request.form['birthday']
        contactPhone = request.form['contactPhone']
        medicalHistory = request.form['medicalHistory']
        notes = request.form['notes']

        mysql = connectToMySQL('clinic_manage')
        query = "UPDATE patients SET gender=%(gender)s, birthday = %(birthday)s, contactPhone = %(contactPhone)s, medicalHistory = %(medicalHistory)s, notes = %(notes)s WHERE userID = %(user_id)s"
        data = {
            'gender': gender,
            'birthday': birthday,
            'contactPhone': contactPhone,
            'medicalHistory': medicalHistory,
            'notes': notes,
            'user_id': session['user_id']
        }
        mysql.query_db(query, data)

        flash('Profile updated successfully!')
        return redirect('/dashboard')
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'GET':
        return render_template('registration.html')
    elif request.method == 'POST':
        is_valid = True
    
        # Registration form validation 
        role = request.form['form_role']

        if role not in ['patient', 'staff', 'admin']:
            flash("Invalid role")
            return redirect('/register')
        
        if len(request.form['form_FName']) < 2:
            flash('First Name is required')
            is_valid = False
        
        if len(request.form['form_LName']) < 2:
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
            query = "INSERT INTO users (FName, LName, email, password, role) VALUES (%(f_name)s, %(l_name)s, %(email)s, %(hashed_pw)s, %(role)s);"
            data={
                'f_name': request.form['form_FName'],
                'l_name': request.form['form_LName'],
                'email': request.form['form_email'],
                'hashed_pw': pw_hash,
                'role': role
            }


            # Insert user into users table
           
            new_user_id = mysql.query_db(query, data)


         

            if new_user_id: 
            # If user is a patient, insert into patients table with userID
                #flash('We have reached checkpoint 1')
                print(type(new_user_id))
                print(new_user_id)
                print('The role is :: ' + role)
            
                if role == 'patient':
                    #flash('We have reached checkpoint 2')
                    mysql = connectToMySQL('clinic_manage')
                    
                    
                    
                    insert_query = "INSERT INTO patients (userID, FName, LName) VALUES (%(user_ID)s, %(first_name)s, %(last_name)s);"

                    patient_data = {
                        'user_ID': new_user_id,
                        'first_name': request.form['form_FName'],
                        'last_name': request.form['form_LName']
                    }
                       
                    print(patient_data)
                    
                    mysql.query_db(insert_query, patient_data)

                    # Set user_id session variable
                    session['user_id'] = new_user_id
                    #flash('We have reached checkpoint 3')
                    #flash('Patient registration successful')


            # Redirect based on user's role
            if role == 'patient':
                return redirect('/dashboard')
            elif role == 'staff':
                return redirect('/dashboard')
            elif role == 'admin':
                return redirect('/admin_dashboard')
            else:
                flash("Failed to register user")
                return redirect('/register')
#dashboard route
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        flash('Must be logged in to access dashboard')
        return redirect('/login')
    
    user_id = session['user_id']

    
    #Get login info
    mysql = connectToMySQL('clinic_manage')
    query = "SELECT FName FROM patients WHERE userID= %(user_id)s"
    data={'user_id': user_id}
    user = mysql.query_db(query,data)
    
    if user:
        user_FName = user[0]['FName']
        welcome_message = f"Hello, {user_FName}!"
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
