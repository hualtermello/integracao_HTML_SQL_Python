
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
  try:
    #Cria conexão
    conectar = mysql.connector.connect(**bd_config)
    cursor = conectar.cursor(dictionary=True)

    #Selecao da tabela
    cursor.execute("select cpf, primeiro_nome, sobrenome, idade from cliente")
    lista_clientes = cursor.fetchall()

    return render_template('index.html', clientes = lista_clientes)
  
  except mysql.connector.Error as erro:
    return f"Erro ao carregar a tabela: {erro}"


@app.route('/cadastrar', methods=['POST'])
def cadastrar():
  #Bloco para armazenar
  cpf = request.form['cpf']
  primeiro_nome = request.form['primeiro_nome']
  sobrenome = request.form['sobrenome']
  idade = request.form['idade']
  
  try:
    conectar =  mysql.connector.connect(**bd_config)
    cursor = conectar.cursor()
    queue = "insert into cliente(cpf, primeiro_nome, sobrenome, idade) values (%s, %s, %s, %s)"
    cursor.execute(queue, (cpf, primeiro_nome, sobrenome, idade))
    
    conectar.commit()
    cursor.close()
    conectar.close()
    
    return f"<h3>Cliente {primeiro_nome} salvo com sucesso!</h3> <a href='/'> Voltar </a>"
    
  except mysql.connector.Error as erro:
    return f"Erro ao gravar no banco: {erro}"

if __name__ == '__main__':
  app.run(debug=True)

