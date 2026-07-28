from contextlib import contextmanager

from flask import render_template, request, redirect, url_for, abort, jsonify
from sqlalchemy import select

from app.routes import main_bp
from app.database import SessionLocal
from app.database.models import User


@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def user_to_dict(user: User):
    return {
        "id": user.id,
        "dni": user.dni,
        "given_name": user.given_name,
        "family_name": user.family_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "address": user.address,
        "created_at": user.created_at.isoformat() if user.created_at else None,
        "updated_at": user.updated_at.isoformat() if user.updated_at else None,
    }


def get_user_or_404(db, user_id: int):
    user = db.get(User, user_id)
    if user is None:
        abort(404)
    return user


@main_bp.route("/")
def home():
    return render_template("index.html")


@main_bp.route("/users/api")
def api_client():
    return render_template("users/api_client.html")


@main_bp.route("/users")
def list_users():
    with get_db() as db:
        users = db.scalars(select(User).order_by(User.id)).all()
        return render_template("users/list.html", users=users)


@main_bp.route("/users/new")
def new_user():
    return render_template("users/form.html", user=None, action=url_for("main.create_user"), title="Crear usuario")


@main_bp.route("/users", methods=["POST"])
def create_user():
    with get_db() as db:
        user = User(
            dni=request.form.get("dni", ""),
            given_name=request.form.get("given_name", ""),
            family_name=request.form.get("family_name", ""),
            email=request.form.get("email", ""),
            phone_number=request.form.get("phone_number", ""),
            address=request.form.get("address", ""),
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return redirect(url_for("main.user_detail", user_id=user.id))


@main_bp.route("/users/<int:user_id>")
def user_detail(user_id):
    with get_db() as db:
        user = get_user_or_404(db, user_id)
        return render_template("users/detail.html", user=user)


@main_bp.route("/users/<int:user_id>/edit")
def edit_user(user_id):
    with get_db() as db:
        user = get_user_or_404(db, user_id)
        return render_template("users/form.html", user=user, action=url_for("main.update_user", user_id=user.id), title="Editar usuario")


@main_bp.route("/users/<int:user_id>", methods=["POST"])
def update_user(user_id):
    with get_db() as db:
        user = get_user_or_404(db, user_id)
        user.dni = request.form.get("dni", "")
        user.given_name = request.form.get("given_name", "")
        user.family_name = request.form.get("family_name", "")
        user.email = request.form.get("email", "")
        user.phone_number = request.form.get("phone_number", "")
        user.address = request.form.get("address", "")
        db.commit()
        db.refresh(user)
        return redirect(url_for("main.user_detail", user_id=user.id))


@main_bp.route("/users/<int:user_id>/delete", methods=["POST"])
def delete_user(user_id):
    with get_db() as db:
        user = get_user_or_404(db, user_id)
        db.delete(user)
        db.commit()
        return redirect(url_for("main.list_users"))


@main_bp.route("/api/users")
def api_list_users():
    with get_db() as db:
        users = db.scalars(select(User).order_by(User.id)).all()
        return jsonify([user_to_dict(user) for user in users])


@main_bp.route("/api/users/<int:user_id>")
def api_get_user(user_id):
    with get_db() as db:
        user = db.get(User, user_id)
        if user is None:
            return jsonify({"error": "User not found"})
        return jsonify(user_to_dict(user))


@main_bp.route("/api/users/search")
def api_search_users():
    given_name = request.args.get("given_name")
    if not given_name:
        return jsonify({"error": "given_name query parameter is required"})

    with get_db() as db:
        stmt = select(User).where(User.given_name == given_name).order_by(User.id)
        users = db.scalars(stmt).all()
        return jsonify([user_to_dict(user) for user in users])
