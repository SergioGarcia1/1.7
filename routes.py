from app import app

@app.route('/')
@app.route('/iindex')
def index():
    return "Hello, World!"

from app import app

@app.route('/')
@app.route('/iindex')
def index():
    user = {'username': 'Miguel'}
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + user['username'] + '''!</h1>
    </body>
</html>'''



from flask import render_template
from app import app

@app.route('/')
@app.route('/iindex')
def index():
    user = {'username': 'Miguel'}
    return render_template('iindex.html', title='Home', user=user)


from flask import render_template
from app import app

@app.route('/')
@app.route('/iindex')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('iindex.html', title='Home', user=user, posts=posts)


from flask import render_template
from app import app
from app.forms import LoginForm

# ...

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)


from flask import render_template, flash, redirect


from flask import render_template, flash, redirect

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect('/iindex')
    return render_template('login.html', title='Sign In', form=form)

