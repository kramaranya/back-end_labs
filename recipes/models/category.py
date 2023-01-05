from sqlalchemy import ForeignKey

from recipes.db import db


class CategoryModel(db.Model):
    __tablename__ = "category"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)

    note = db.relationship(
        "NoteModel",
        back_populates="category",
        lazy="dynamic",
    )

    user_id = db.Column(
        db.Integer,
        ForeignKey("user.id", ondelete="CASCADE"),
        unique=False,
        nullable=False
    )

    is_private = db.Column(db.Boolean, unique=False, nullable=False, default=False)
