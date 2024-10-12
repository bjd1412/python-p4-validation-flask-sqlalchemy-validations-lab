from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

class Author(db.Model):
    __tablename__ = 'authors'
    
    id = db.Column(db.Integer, primary_key=True)
    name= db.Column(db.String, unique=True, nullable=False)
    phone_number = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates('name')
    def valid_name(self, key, names):
        if names == "":
            raise ValueError("Value must have a name")
        elif Author.query.filter(Author.name == names).first():
            raise ValueError("Names must be unique")
        return names

    @validates('phone_number')
    def valid_number(self, key, number):
        if len(number) != 10 or not number.isdigit():
            raise ValueError("Numbers must be 10 digits.")
        return number
        



    

    def __repr__(self):
        return f'Author(id={self.id}, name={self.name})'

class Post(db.Model):
    __tablename__ = 'posts'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    content = db.Column(db.String)
    category = db.Column(db.String)
    summary = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    @validates("content")
    def validates_content(self, key, content):
        if len(content) < 250:
            raise ValueError("Content must be more than 250 characters.")
        return content

    @validates("title")
    def validates_title(self, key, title):
        titles = ["Won't Believe", "Secret", "Top", "Guess"]
        if title == "":
            raise ValueError
        elif  not any (words in title for words in titles):
            raise ValueError
        return title

    @validates("summary")
    def validates_summary(self, key, summary):
        if len(summary) > 250:
            raise ValueError
        return summary

    @validates("category")
    def validates_category(self, key, category):
        if category != "Fiction" and category != "Non-Fiction":
            raise ValueError
        return category


      


    def __repr__(self):
        return f'Post(id={self.id}, title={self.title} content={self.content}, summary={self.summary})'
