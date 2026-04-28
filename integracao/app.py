#import do flask para criação do servidor
#render_template para criar uma "ponte" com html
#request para capturar os dados digitados
from flask import Flask, render_template, request
import mysql.connector

#Permite o Flask localizar o caminho dos arquivos
app = Flask(__name__)

bd_config = {
  'host': 'localhost',
  'user': 'root',
  'password': 'escola',
  'database': 'cadastro' 
}
#Criando a rota para acessar o arquivo html
@app.route('/')
def buscar_index(): 
  return render_template('index.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
  #Bloco para armazenar
  cpf = request.form['cpf']
  primeiro_nome = request.form['primeiro_nome']
  sobrenome = request.form['sobrenome']
  idade = request.form['idade']
  
  
  
