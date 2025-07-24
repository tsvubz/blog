# BlogPy

BlogPy is a simple blogging platform built with Flask. It allows users to register, log in, create posts, edit their account, and reset their password. The project demonstrates user authentication, database management, and modular Flask application structure.

## Features

- User registration and authentication
- Create, edit, and delete blog posts
- Password reset via email
- User profile management
- Error handling pages
- Responsive design with Bootstrap

## Installation

1. **Clone the repository:**
    - git clone https://github.com/yourusername/BlogPy.git cd BlogPy

2. **Create a virtual environment and activate it:**
   ` python -m venv venv `

3. **Install dependencies:**
   ` pip install -r requirements.txt `

4. **Set environment variables for email (optional, for password reset):**
   - set EMAIL_USER=your_email@gmail.com 
   - set EMAIL_PASS=your_email_password

5. **Run the application:**
   ` python app.py `

## Usage

- Visit `http://localhost:5000` in your browser.
- Register a new account.
- Log in and create posts.
- Edit your profile and posts.
- Use the password reset feature if needed.

## Configuration

Configuration settings are in `app/config.py`. You can change the database URI, secret key, and mail server settings there.