from flask import Flask, render_template, request, redirect, url_for, flash
from config import config
from supabase import Client, create_client

app = Flask(__name__)

supabase: Client = create_client(config['development'].SUPABASE_URL, config['development'].SUPABASE_KEY)

db = create_client(config['development'].SUPABASE_URL, config['development'].SUPABASE_KEY)



@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        try:
            
            db.auth.sign_in_with_password({"email": username, "password": password})
            return render_template('index.html')
        except Exception as e:
            print('Error: ' + str(e))
    else:     
        return render_template('auth/login.html')
    return render_template('auth/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = db.auth.sign_up({'email':username,'password':password})
        if error:
            flash('Usuario registrado')
            return render_template('auth/login.html')
        else:
            flash('Registro fallido')
            return render_template('auth/register.html')
    
    else:     
        return render_template('auth/register.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.run()
