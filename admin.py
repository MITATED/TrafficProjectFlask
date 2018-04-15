from app import app
from app import db
from flask_admin import Admin
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_security import current_user

from models import *

class AdminMixin:
	def is_accessible(self):
		return current_user.has_role('admin')

	def inaccessible_callback(self, name, **kwargs):
		return redirect(url_for('security.login', next=request.url))


class BaseModelView(ModelView):
	def on_model_change(self, form, model, is_created):
		model.generate_slug()
		return super(BaseModelView, self).on_model_change(form, model, is_created)


class HomeAdminView(AdminMixin, AdminIndexView): 
	pass

class PostAdminView(AdminMixin, BaseModelView):
	form_columns = ['title', 'body']

class UserAdminView(AdminMixin, ModelView):
	pass

class RoleAdminView(AdminMixin, ModelView):
	pass

admin = Admin(app, 'FlaskApp', url='/', index_view=HomeAdminView(name="Home"))
admin.add_view(PostAdminView(Post, db.session))
admin.add_view(UserAdminView(User, db.session))
admin.add_view(RoleAdminView(Role, db.session))
