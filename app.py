from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Lista de perguntas e respostas
questions = [
    {
        "pergunta": "o que é meio ambiente?",
        "opcoes": ["O desenvolvimento que visa suprir as necessidades geração atuais", "Tudo que faz parte do meio em que vive o ser humano, os seres vivos e/ou as coisas.", "Uma das formas de reaproveitamento de resíduos", "é o fenômeno responsável pelo aumento da temperatura da terra."],
        "resposta": "Tudo que faz parte do meio em que vive o ser humano, os seres vivos e/ou as coisas."
    },
    {
        "pergunta": "O que é coleta seletiva?",
        "opcoes": ["Processo de separação e recolhimento dos resíduos para o reaproveitamento por meio de reciclagem.", "Destinação de resíduos para lixões e aterros.", "Processo de envio de todo lixo produzido para cooperativas ou entrega para catadores de rua.", "A escolha aleatória do melhor lixo produzido."],
        "resposta": "Processo de separação e recolhimento dos resíduos para o reaproveitamento por meio de reciclagem"
    },
    {
        "pergunta": "Como consumir de forma consciente?",
        "opcoes": ["Trocando todos os nossos objetos sempre que um novo do mesmo tipo for lançado.", "Usar a mangueira para lavar o quintal e o carro.", "Utilizando os recursos naturais para satisfazer nossas necessidades e das gerações futuras.", "Adquirindo qualquer tipo de produto se for barato."],
        "resposta": "Utilizando os recursos naturais para satisfazer nossas necessidades e das gerações futuras."
    }
]

# Lista para armazenar respostas do usuário
respostas_usuario = []

# ... (código anterior)

pontuacao = 0

@app.route('/verificar_resposta', methods=['POST'])
def verificar_resposta():
    resposta_usuario = request.form.get('resposta')
    respostas_usuario.append(resposta_usuario)

    proxima_pergunta = len(respostas_usuario)

    # Verificar se a resposta está correta e atribuir pontos
    if resposta_usuario == questions[proxima_pergunta - 1]["resposta"]:
        global pontuacao
        pontuacao += 1

    if proxima_pergunta < len(questions):
        return render_template('index.html', question=questions[proxima_pergunta])
    else:
        total_perguntas = 3
        pontuacao_final = pontuacao  / 3
          # Pontuação final
        return render_template('fim.html', respostas=respostas_usuario, pontuacao_final=pontuacao_final, total_perguntas=len(questions))

# ... (restante do código)

@app.route('/')
def index():
    return render_template('index.html', question=questions[0])



if __name__ == '__main__':
    app.run(debug=True)


