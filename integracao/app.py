#import do flask para criação do servidor
#render_template para criar uma "ponte" com html
#request para capturar os dados digitados
from flask import Flask, render_template, redirect, url_for, request
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
    #Cria conexão com MySQL e permite adicionar comando SQL
    conectar = mysql.connector.connect(**bd_config)
    cursor = conectar.cursor(dictionary=True)

    #Selecao da tabela
    cursor.execute("select cpf, primeiro_nome, sobrenome, idade from cliente")
    lista_clientes = cursor.fetchall()

    return render_template('index.html', clientes = lista_clientes)
  
  except mysql.connector.Error as erro:
    return f"Erro ao carregar a tabela: {erro}"

#Cria uma rota para acessar o formulário
@app.route('/cadastrar', methods=['POST'])
def cadastrar():
  #Bloco para armazenar os dados digitados
  cpf = request.form['cpf']
  primeiro_nome = request.form['primeiro_nome']
  sobrenome = request.form['sobrenome']
  idade = request.form['idade']
  
  try:
    #verificando conexão com MySQL
    conectar =  mysql.connector.connect(**bd_config)
    #Variável que permite a escrever SQL
    cursor = conectar.cursor()

    queue = "insert into cliente(cpf, primeiro_nome, sobrenome, idade) values (%s, %s, %s, %s)"
    cursor.execute(queue, (cpf, primeiro_nome, sobrenome, idade))
    
    #Atualiza as alterações e fecha as conexões
    conectar.commit()
    cursor.close()
    conectar.close()
    
    return redirect(url_for('buscar_index'))
    
  except mysql.connector.Error as erro:
    return f"Erro ao gravar no banco: {erro}"

#Cria a rota para exclusão
@app.route('/excluir/<cpf>')
def excluir(cpf):
    try:

        conectar = mysql.connector.connect(**bd_config)
        cursor = conectar.cursor()

        cursor.execute("DELETE FROM cliente WHERE CPF = %s", [cpf])

        conectar.commit()
        cursor.close()
        conectar.close()

        return redirect(url_for('buscar_index'))
    except mysql.connector.Error as erro:
        return f"Erro ao excluir: {erro}"

if __name__ == '__main__':
  app.run(debug=True)

