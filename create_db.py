# create_db.py
from app import app, db

# This ensures we are working within the application context
with app.app_context():
    db.create_all()  # This will create all tables defined in your SQLAlchemy models
    
    print("Database and tables created successfully!")
