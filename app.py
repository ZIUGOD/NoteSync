from flask import Flask, flash, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy  # Se você estiver usando SQLAlchemy
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    login_required,
    logout_user,
    current_user,
)
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"  # SQLite como exemplo
db = SQLAlchemy(app)
app.secret_key = "IGOA10pBEK2rqqPri7pzenhmw6DNosf3"
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    # Sua lógica para carregar o usuário com base no user_id aqui
    user = User.query.get(int(user_id))  # Exemplo usando SQLAlchemy

    return user


users = []


class User(UserMixin):
    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(
            password
        )  # Armazena a senha com hash
        self.email = email


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Realize validações e lógica de registro aqui
        # Certifique-se de verificar se as senhas coincidem e se o usuário ou e-mail já existem

        flash("Cadastro realizado com sucesso!", "success")
        return redirect(
            url_for("login")
        )  # Redireciona para a página de login após o cadastro

    return render_template("cadastro.html")  # Renderiza o formulário de cadastro


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user_id = request.form[
            "user_id"
        ]  # pode usar um formulário para obter o ID do usuário
        user = User(user_id)
        login_user(user)
        return redirect(url_for("profile"))
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


@app.route("/profile")
@login_required
def profile():
    return f"Bem-vindo, {current_user.id}!"


if __name__ == "__main__":
    app.run(debug=True, port=4999)
