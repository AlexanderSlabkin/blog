from webapp import app
from flask import render_template, flash, redirect
from webapp.forms import LoginForm

@app.route('/')
@app.route('/home')
@app.route('/index')
def Hello():
    title = 'Homepage'
    user = {'name': 'Alex',
            'age' : '23'}
    posts = [
            {'author': {'name': 'Nik', 'age': '24'},
                'body': {'text': 'string', 'time': '22:00'}},
            {'author': {'name': 'Mike', 'age': '22'},
                'body': {'text': 'longer string', 'time': '21:15'}}
            ]   
    return render_template('home.html', **locals())

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/index')
    return render_template('login.html', **locals())
