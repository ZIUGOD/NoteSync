from flask import Flask, flash, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from NoteSync import (
    db,
)  # Substitua 'your_app_name' pelo nome real do seu aplicativo
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "OrzQhJX6Uk8ThBMaARjqCjoGfqcXdfYa"  # Troque por uma chave secreta mais segura em produção

# Simulando um banco de dados temporário
users_db = []
notes_db = []


@app.route("/")
def index():
    # Recuperando todas as notas do banco de dados
    notes = notes_db  # Usando a lista de notas simulada
    return render_template("index.html", notes=notes)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        hashed_password = generate_password_hash(password, method="sha256")
        users_db.append({"username": username, "password": hashed_password})

        flash("Registro bem-sucedido! Faça login agora.")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = next((u for u in users_db if u["username"] == username), None)
        if user and check_password_hash(user["password"], password):
            flash("Login bem-sucedido!")
            return redirect(url_for("notes"))

        flash("Credenciais inválidas. Tente novamente.")

    return render_template("login.html")


@app.route("/notes")
def notes():
    return render_template("notes.html", notes=notes_db)


@app.route("/add_note", methods=["GET", "POST"])
@login_required  # Adicione este decorator para proteger a rota
def add_note():
    if request.method == "POST":
        note_text = request.form["note_text"]

        # Salve a nota no banco de dados associando-a ao usuário logado
        note = Note(text=note_text, user_id=current_user.id)
        db.session.add(note)
        db.session.commit()

        flash("Nota adicionada com sucesso!", "success")
        return redirect(url_for("index"))

    return render_template("add_notes.html")


if __name__ == "__main__":
    app.run(debug=True, port=4999)
