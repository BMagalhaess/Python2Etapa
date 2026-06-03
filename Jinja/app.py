from flask import Flask, request, render_template


app = Flask(__name__)

@app.route('/')
def filho1():
    nome = 'bernardo' 
    return render_template('filho1.html', nome = nome)

@app.route('/idade')
def filho2():
    nome = 'bernardo' 
    idade = '17' 
    return render_template('filho2.html', nome = nome, idade = idade)


if __name__ == "__main__":
    app.run(debug=True)