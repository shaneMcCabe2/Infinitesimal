from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate # uses Alembic migration template

app = Flask(__name__) # creates the application object as an instance of class Flask
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models # routes imported at bottom to workaround circular imports
