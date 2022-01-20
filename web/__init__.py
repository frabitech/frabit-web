# (c) 2021 frabit-web Project maintained and limited by FrabiTech < blylei.info@gmail.com >
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
#
# This file is part of frabit-web

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_pagedown import PageDown
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()
pagedown = PageDown()

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    pagedown.init_app(app)

    if app.config['SSL_REDIRECT']:
        from flask_sslify import SSLify
        sslify = SSLify(app)

    # register all blueprint at this point
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint, url_prefix='/api/v1')

    from .backup import backup as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/backup')

    from .config import config as config_blueprint
    app.register_blueprint(config_blueprint, url_prefix='/config')

    from .display import display as display_blueprint
    app.register_blueprint(display_blueprint, url_prefix='/display')

    from .login import login as login_blueprint
    app.register_blueprint(login_blueprint, url_prefix='/login')

    from .manager import manager as manager_blueprint
    app.register_blueprint(manager_blueprint, url_prefix='/manager')

    from .pitr import pitr as pitr_blueprint
    app.register_blueprint(pitr_blueprint, url_prefix='/pitr')

    from .restore import restore as restore_blueprint
    app.register_blueprint(restore_blueprint, url_prefix='/restore')

    from .schedule import schedule as schedule_blueprint
    app.register_blueprint(schedule_blueprint, url_prefix='/schedule')

    from .upload import upload as upload_blueprint
    app.register_blueprint(upload_blueprint, url_prefix='/upload')






    return app
