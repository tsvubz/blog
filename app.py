from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)
