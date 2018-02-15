from flask import Flask, render_template, redirect, url_for, request
from config import POSTS_PER_PAGE
from app import app, db
from app.models import Post
from app.forms import PostForm

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
def index(): 
    form = PostForm()
    if form.validate_on_submit():
        posts = Post(post=form.post.data)
        db.session.add(posts)
        db.session.commit()
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = Post.query.order_by(Post.post.asc()).paginate(page, POSTS_PER_PAGE, False) 
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None 	
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None 
    return render_template("index.html", title="Flask - Pagination", form=form, posts=posts.items, next_url=next_url, prev_url=prev_url) 

