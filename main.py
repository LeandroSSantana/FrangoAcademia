from flask import Flask, render_template, request, redirect
from database.cadastro import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frangoAcademia.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route("/")
def homepage():
    sucesso = request.args.get("sucesso", default=False)
    return render_template("homepage.html", sucesso=sucesso)

with app.app_context():
    db.create_all()

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route('/create', methods=['POST'])
def create():
    name = request.form['name']
    telefone = request.form['telefone']
    email = request.form['email']
    objetivo = request.form['objetivo']
    # aluno = {'name': name, 'telefone': telefone, 'email': email, 'objetivo': objetivo}
    aluno = User(nome=name, telefone=telefone, email=email, objetivo=objetivo)
    db.session.add(aluno)
    db.session.commit()
    return redirect("/?sucesso=true")

@app.route("/usuarios")
def usuarios():
    alunos = User.query.all()
    return render_template("usuarios.html", alunos=alunos)

@app.route("/usuarios/excluir/<int:id>")
def excluir(id):
    aluno = User.query.get(id)
    db.session.delete(aluno)
    db.session.commit()
    return redirect("/usuarios")


@app.route("/usuarios/editar/<int:id>", methods=['POST'])
def editar(id):
    aluno = User.query.filter_by(id=id).first()

    if request.method == 'POST':
        if aluno:
            name = request.form['name']
            telefone = request.form['telefone']
            email = request.form['email']
            objetivo = request.form['objetivo']

            aluno = User(nome=name, telefone=telefone, email=email, objetivo=objetivo)

            db.session.edit(aluno)
            db.session.commit()
            return redirect("/create")

if __name__ == "__main__":
    app.run(debug=True)