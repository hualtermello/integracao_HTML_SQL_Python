from flask import Flask, render_template, redirect, url_for, request
import mysql.connector

app = Flask (__name__)

bd_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'escola',
    'database': 'cadastro'
}

@app.route('/')
def buscar_index():
  try:
    conectar = mysql.connector.connect(**bd_config)
    cursor = conectar.cursor(dictionary=True)

    cursor.execute("select * from produtos")
    lista_produtos = cursor.fetchall()

    return render_template('index.html', produtos = lista_produtos)
  
  except mysql.connector.Error as erro:
    return f"Erro ao carregar a tabela: {erro}"

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
  nome_produto = request.form['nome_produto']
  descricao = request.form['descricao']
  preco = request.form['preco']

  try:
    conectar =  mysql.connector.connect(**bd_config)
    cursor = conectar.cursor()

    queue = "insert into produtos(nome_produto, descricao, preco) values (%s, %s, %s)"
    cursor.execute(queue, (nome_produto, descricao, preco))
    
    conectar.commit()
    cursor.close()
    conectar.close()
    
    return f"<h3>Produto {nome_produto} salvo com sucesso!</h3> <a href='/'> Voltar </a>"
    
  except mysql.connector.Error as erro:
    return f"Erro ao gravar no banco: {erro}"


@app.route('/excluir/<cod_produto>') #Verificar
def excluir(cod_produto):
    try:

        conectar = mysql.connector.connect(**bd_config)
        cursor = conectar.cursor()

        cursor.execute("DELETE FROM produtos WHERE cod_produto = %s", [cod_produto])

        conectar.commit()
        cursor.close()
        conectar.close()

        return redirect(url_for('buscar_index'))
    except mysql.connector.Error as erro:
        return f"Erro ao excluir: {erro}"

if __name__ == '__main__':
  app.run(debug=True)
