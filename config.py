#Framework ORM: FLASK-SQLALCHEMY

#site oficial
#https://flask-sqlalchemy.palletsprojects.com/

#No terminal do pycharm digita:
#pip install Flask Flask-SQLAlchemy

#caso ocorra erro de segurança no terminal do pycharm, é necessário
#mudar a política de segurança do powershell
#A. Executar PowerShell no modo administrador
#B. Set-ExecutionPolicy RemoteSigned
#C. A (all)

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

#Configurando o acesso ao banco de dados do SQLAlchemy
#basedir = 'D:\Curso Python\projeto_Alchemy'
basedir = os.path.abspath(os.path.dirname(__file__))

uri = 'sqlite:///' + os.path.join(basedir, 'database.db')

#para Mysql
#mysql://username:password@host:port/database_name
#exemplo: 'mysql://root:senha@localhost:3306/nome_banco'

#cria o app onde roda o banco de dados
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = uri
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#cria o banco de dados do app
db = SQLAlchemy(app)
