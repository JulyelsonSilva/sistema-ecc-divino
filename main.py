from flask import Flask, render_template, request, redirect, url_for, session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecc.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Encontrista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_ele = db.Column(db.String(100))
    nome_ela = db.Column(db.String(100))
    nome_usual_ele = db.Column(db.String(100))
    nome_usual_ela = db.Column(db.String(100))
    telefone_ele = db.Column(db.String(50))
    telefone_ela = db.Column(db.String(50))
    endereco = db.Column(db.String(200))
    numero_encontro = db.Column(db.String(20))
    ano_encontro = db.Column(db.String(10))
    data_casamento = db.Column(db.String(20))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True, host='0.0.0.0', port=3000)

@app.route('/')
def index():
    if 'user' not in session:
        return redirect(url_for('login'))
    encontristas = Encontrista.query.all()
    return render_template('index.html', encontristas=encontristas)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form['email'] == 'admin@ecc.local' and request.form['senha'] == 'Teste1234':
            session['user'] = 'admin'
            return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=3000)
