from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Text,DateTime,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
Base = declarative_base()

class User(Base):
    """User account."""

    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement="auto")
    username = Column(String(255), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255))
    last_name = Column(String(255))
    bio = Column(Text)
    avatar_url = Column(Text)
    role = Column(String(255))
    last_seen = Column(DateTime)
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, onupdate=func.now())

    def __repr__(self):
        return f"<User {self.username}>"


class Comment(Base):
    """User-generated comment on a blog post."""

    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("user.id"))  # FK added
    post_id = Column(Integer, ForeignKey("post.id"), index=True)  # FK added
    body = Column(Text)
    upvotes = Column(Integer, default=1)
    removed = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    # Relationships
    user = relationship("User")

    def __repr__(self):
        return f"<Comment {self.id}>"


class Post(Base):
    """Blog post/article."""

    __tablename__ = "post"

    id = Column(Integer, primary_key=True, index=True)
    author_id = Column(Integer, ForeignKey("user.id"))  # FK added
    slug = Column(String(255), nullable=False, unique=True)
    title = Column(String(255), nullable=False)
    summary = Column(String(400))
    feature_image = Column(String(300))
    body = Column(Text)
    status = Column(String(255), nullable=False, default="unpublished")
    created_at = Column(DateTime, server_default=func.now())
    updated_at = Column(DateTime, server_default=func.now())

    # Relationships
    author = relationship("User")
    comments = relationship("Comment")

    def __repr__(self):
        return f"<Post {self.id}>"