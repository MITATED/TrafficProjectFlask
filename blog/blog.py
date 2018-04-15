from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_security import login_required

from app import db

from .forms import PostForm
from models import Post


blog = Blueprint('blog', __name__, template_folder="templates")


@blog.route('/create', methods=["POST", "GET"])
@login_required
def create_post():
	if request.method == "POST":
		title = request.form.get('title')
		body = request.form.get('body')

		post = Post(title=title, body=body)
		db.session.add(post)
		db.session.commit()
		return redirect(url_for('blog.post', slug=post.slug))

	form = PostForm()
	return render_template('blog/create.html', form=form)


@blog.route('/<slug>/update', methods=["POST", "GET"])
@login_required
def update_post(slug):
	post = Post.query.filter(Post.slug==slug).first_or_404()

	if request.method == "POST":
		form = PostForm(formdata=request.form, obj=post)
		form.populate_obj(post)
		db.session.commit()
		return redirect(url_for('blog.post', slug=slug))
	form = PostForm(obj=post)
	return render_template('blog/update.html', post=post, form=form)


@blog.route("/")
def posts():
	page = request.args.get('page')
	page = int(page) if page and page.isdigit() else 1
	print(page)

	if request.args and request.args.get("q", None):
		q = request.args.get("q")
		posts = Post.query.filter(Post.title.contains(q) | Post.body.contains(q)) #.all()
	else:
		posts = Post.query.order_by(Post.created.desc())

	pages = posts.paginate(page=page, per_page=3)
	return render_template('blog/posts.html', pages=pages)


@blog.route('/<slug>')
def post(slug):
	post = Post.query.filter(Post.slug == slug).first_or_404()	
	return render_template('blog/post.html', post=post)


