from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base

# The db instance for Flask-SQLAlchemy
db = SQLAlchemy()

# Base class for the manual metadata binding requirement
Base = db.Model