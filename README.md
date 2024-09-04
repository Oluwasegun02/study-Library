###### Overview of the Library Web App
# Back-End (Python with Flask):
- Flask will be used to handle HTTP requests, manage routes, and interact with a database.
- SQLite will be used as the database to store book information.

# Front-End (HTML, CSS, JavaScript):
- The front-end will use HTML for structure, CSS for styling, and JavaScript for dynamic functionality.
- We'll use Bootstrap for responsive design.

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install Flask
pip install Flask


library-web-app/
│
├── app/
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── scripts.js
│   └── templates/
│       ├── layout.html
│       ├── index.html
│       ├── search.html
│       └── book_detail.html
├── library.db
├── run.py
└── requirements.txt


#Migrate the Database
flask db current
flask db init
flask db migrate -m "Add is_admin field to User model."
flask db upgrade
flask run

# Run the Script Again
python create_db.py

python create_admin.py
# Create Admin User via Flask Shell
You can also create the admin user via the Flask shell:


flask shell
Then, in the Flask shell:

python
Copy code
from app import db
from app.models import User

admin = User(username='admin', email='admin@example.com', is_admin=True)
admin.set_password('your_secure_password')
db.session.add(admin)
db.session.commit()

python run.py



pip install --upgrade werkzeug

pip install Flask-Migrate

pip install Flask-Uploads PyMuPDF python-docx

pip install Flask-Login Flask-Bcrypt

pip freeze > requirements.txt





Step 7: Prepare for Deployment
To deploy your app, consider using a platform like Heroku, PythonAnywhere, or AWS.

# Create a Procfile for Heroku deployment:
web: gunicorn app:app
# Create a .gitignore file to exclude unnecessary files:
__pycache__/
*.pyc
instance/
.env
.venv/
### Deploy to Heroku:
# Initialize a Git repository:
git init
git add .
git commit -m "Initial commit"
## Login to Heroku and create a new app:
heroku login
heroku create your-app-name
## Push your code to Heroku:
git push heroku master
## Set up the database on Heroku:
heroku run python
>>> from app import db
>>> db.create_all()
>>> exit()