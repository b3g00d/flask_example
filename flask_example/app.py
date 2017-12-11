import os
import click

from flask import Flask
from flask_example.extensions import (
    migrate,
    db
)


def create_app(env_name=None, blueprints=None):
    SETTINGS_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'config.py'
    )
    if blueprints is None:
        blueprints = []

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile(SETTINGS_PATH)
    if env_name:
        filename = os.path.join(
            app.root_path, 'config-' + env_name)
        app.config.from_pyfile(filename)

    configure_extensions(app)
    configure_blueprints(app, blueprints)
    configure_hook(app)
    configure_error_handlers(app)
    return app


def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db=db)
    configure_migrate_commands(app)


def configure_commands(app):
    @app.cli.command()
    def seed():
        click.echo("Not implement seeding")

    @app.cli.command()
    def dropdb():
        click.echo("Not implement dropdb")


def configure_blueprints(app, blueprints):
    for blueprint in blueprints:
        app.register_blueprint(blueprint)


def configure_migrate_commands(app):
    from flask_migrate import MigrateCommand
    app.cli.add_command('db', MigrateCommand)


def configure_hook(app):
    @app.before_request
    def before_request():
        pass

    @app.after_request
    def after_request():
        pass


def configure_error_handlers(app):
    @app.errorhandler(500)
    def server_error_page(error):
        return "ERROR PAGE"
