from flask import  current_app, render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User,Post
from flaskblog.forms import Loginform, Registrationform


    



posts = [
    {
        'author': 'Jad Shakra',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 19, 2023'
    },
    {
        'author': 'Jason Stone',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 14, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def Registration():
    form = Registrationform()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('registration.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def Login():
    form = Loginform()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
