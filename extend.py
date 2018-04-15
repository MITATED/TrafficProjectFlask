from app import app
from app import db

from flask_security import SQLAlchemyUserDatastore
from flask_security import Security

from models import *
from flask import redirect, url_for, request

from flask_ckeditor import CKEditor
ckeditor = CKEditor(app)

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


def url_for_other_page(page):
    args = request.args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page
