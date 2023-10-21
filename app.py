from flask import Flask, render_template, request, flash, session, redirect, url_for
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "supersecretkey"

users_db = []

notes_db = []


@app.route("/")
def index():
    return render_template("index.html", notes=notes_db)


@app.route("/add_note", methods=["POST"])
def add_note():
    if request.method == "POST":
        if "user" not in session:
            flash("Você precisa estar logado para adicionar notas.")
            return redirect(url_for("login"))

        title = request.form["title"]
        content = request.form["content"]

        notes_db.append({"title": title, "content": content})
        flash("Nota adicionada com sucesso!")
        return redirect(url_for("notes"))


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
            session["user"] = username  # Adicione o usuário à sessão
            flash("Login bem-sucedido!")
            return redirect(url_for("notes"))

        flash("Credenciais inválidas. Tente novamente.")

    return render_template("login.html")


@app.route("/notes")
def notes():
    if "user" not in session:
        flash("Você precisa estar logado para adicionar notas.")
        return redirect(url_for("login"))

    return render_template("notes.html", notes=notes_db)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
