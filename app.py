from flask import Flask, render_template, url_for
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'e9a3c75a6cf3e587b7648f9440749256'

posts = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'date': '2023-10-01',
        'content': 'This is the content of the first post.',
    },
    {
        'author': 'Jane Smith',
        'title': 'Second Post',
        'date': '2023-10-02',
        'content': 'This is the content of the second post.',
    },
    {
        'author': 'Alice Johnson',
        'title': 'Third Post',
        'date': '2023-10-03',
        'content': 'This is the content of the third post.',
    }
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True)
