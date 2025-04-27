from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    mensagem = "Essa mensagem veio do Python!"
    return render_template('index.html', mensagem=mensagem)

@app.route('/obg')
def obg():
    return render_template('obg.html')

@app.route('/enviar', methods=['POST']) 
def enviar ():
    nome = request.form.get("nome")
    email = request.form.get("email")
    telefone = request.form.get("telefone")
    assunto = request.form.get("assunto")
    mensagem = request.form.get("mensagem")
    
    #salvando o arquivo
    with open('contatos.txt', 'a', encoding='utf-8') as f:
        f.write(f"""
================= NOVA MENSAGEM =================
Nome: {nome}
Email: {email}
Telefone: {telefone}
Assunto: {assunto}
Mensagem:
{mensagem}
=================================================

""")

    return redirect(url_for('index'))



@app.route('/buscar', methods=['GET', 'POST'])
def buscar():
    resultados = ''
    if request.method == 'POST':
        termo = request.form.get('termo')
        with open('contatos.txt', 'r', encoding='utf-8') as f:
            dados = f.read()
            if termo.lower() in dados.lower():
                resultados = dados.split('================= NOVA MENSAGEM =================')
                resultados = [r for r in resultados if termo.lower() in r.lower()]
    return render_template('buscar.html', resultados=resultados)

import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Render define a porta
    app.run(host='0.0.0.0', port=port)
