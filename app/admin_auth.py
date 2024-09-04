from app import db
from app.models import User

user = User.query.filter_by(username='admin_user').first()
user.is_admin = True
db.session.commit()
