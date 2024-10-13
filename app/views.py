
import os
from app import app
from app import app,db
from app.models import Usuario,Ocorrencia
from werkzeug.utils import secure_filename
from flask import render_template,url_for,request,redirect,flash,session
from werkzeug.security import generate_password_hash, check_password_hash



# PRINCIPAL 

@app.route('/')
def index():
    return render_template('index.html')

# LOGIN USUARIO 

@app.route('/login/', methods=['GET', 'POST'])
def login_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        senha = request.form.get('senha')
        user = Usuario.query.filter_by(nome=nome).first()
        
        if user and check_password_hash(user.senha, senha):
            session['nome'] = nome
            session['usuario_id'] = user.id
            flash('Login bem-sucedido!', 'success')
            return redirect(url_for('index')) 
        else:
            flash('Nome de usuário ou senha incorretos. Tente novamente.', 'error')
    return render_template('login.html')

# SAIR
@app.route('/logout/')
def sair():
    session.pop('nome', None)
    session.pop('usuario_id', None)
    flash('Logout realizado com sucesso!', 'success')
    return redirect(url_for('login_usuario'))


#CADASTRO USUARIO

@app.route('/cadastro/', methods=['GET', 'POST'])
def cadastro_usuario():
    if request.method == 'POST':
        nome = request.form.get('nome')  
        senha = request.form.get('senha')
        email = request.form.get('email')
        cpf = request.form.get('cpf')
        sobrenome = request.form.get("sobrenome")
        rua = request.form.get("rua")
        numero_casa = request.form.get("numero_casa")
        bairro = request.form.get("bairro")
        cripto_senha = generate_password_hash(senha)
        novo_usuario = Usuario (
            nome=nome,
            senha=cripto_senha,
            email=email, 
            cpf=cpf,
            sobrenome = sobrenome,
            rua=rua,
            numero_casa = numero_casa,
            bairro = bairro
            )

        db.session.add(novo_usuario)
        db.session.commit()

        flash('Cadastro realizado com sucesso! Faça login agora.', 'success')
        return redirect(url_for('login_usuario'))
    return render_template('cadastro.html')


#REGISTRA OCORRENCIA 

@app.route('/registrar_ocorrencia/', methods=['GET', 'POST'])
def registrar_ocorrencia():
    if request.method == 'POST':
        usuario_id = session.get('usuario_id') 
        localizacao = request.form.get('localizacao')
        tipo_problema = request.form.get('tipo_problema')
        descricao = request.form.get('descricao')
        imagem = request.files['imagem'] 
        nome_seguro = secure_filename(imagem.filename)
        
        nova_ocorrencia = Ocorrencia(
            usuario_id=usuario_id,
            localizacao=localizacao,
            tipo_problema=tipo_problema,
            descricao=descricao,
            imagem=nome_seguro
        )

        caminho = os.path.join(
            os.path.abspath(os.path.dirname(__file__)),
            app.config['UPLOAD_FILES'],
            'imagens_ocorrencia',
            nome_seguro 
        )
         
        imagem.save(caminho)
        db.session.add(nova_ocorrencia)
        db.session.commit()
        
        flash('Ocorrência registrada com sucesso!', 'success')
        return redirect(url_for('index'))
    return render_template('registrar_ocorrencia.html')

# LISTA OCORRENCIA

@app.route('/ocorrencias/', methods=['GET'])
def listar_ocorrencias():
    ocorrencias = db.session.query(Ocorrencia, Usuario).join(Usuario, Ocorrencia.usuario_id == Usuario.id).all()
    return render_template('listar_ocorrencias.html', ocorrencias=ocorrencias)


