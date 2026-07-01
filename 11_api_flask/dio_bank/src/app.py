import os

from flask import Flask, current_app
import click
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy as sa
from datetime import datetime

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class User(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(sa.String, unique=True, nullable=False)
    password: Mapped[str] = mapped_column(sa.String, nullable=False)

class Post(db.Model):
    id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    author_id: Mapped[int] = mapped_column(sa.ForeignKey("user.id"))
    created: Mapped[datetime] = mapped_column(sa.DateTime, nullable=False, server_default=sa.func.now())
    title: Mapped[str] = mapped_column(sa.String, nullable=False)
    body: Mapped[str] = mapped_column(sa.String, nullable=False)



@click.command('init-db')
def init_db_command():
    """Clear the existing data and create new tables."""
    global db
    with current_app.app_context():
        db.create_all()
    click.echo('Initialized the database.')

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        SQLALCHEMY_DATABASE_URI='sqlite:///dio_bank.db',
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)


    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.cli.add_command(init_db_command)
    
    db.init_app(app)

    from src.controllers import user, post

    app.register_blueprint(user.app)

    return app