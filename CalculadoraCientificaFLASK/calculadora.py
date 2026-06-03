import requests
from flask import Flask, render_template, request

def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']
    
    # inserir as operações da calculadora
    
    return render_template('calculadora.html', etapas=etapas, resultados=resultado)
