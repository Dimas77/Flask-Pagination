from app import app, db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post = db.Column(db.String(500))

    def __repr__(self):
        return self.post
