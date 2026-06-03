from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Página Inicial</h1><p>Vá para <a href="/curriculo">/curriculo</a> para ver o currículo.</p>'

@app.route('/curriculo')
def exibir_curriculo():
    texto_explicacao = """
    <!DOCTYPE html>
    <html lang="pt-BR">
    <head>
        <meta charset="UTF-8">
        <title>Currículo - Bernardo Magalhães Santos</title>
        <style>
            body { font-family: Arial, sans-serif; line-height: 1.6; margin: 40px; color: #333; }
            h1 { color: #0056b3; margin-bottom: 5px; }
            h3 { color: #0056b3; border-bottom: 1px solid #ddd; padding-bottom: 5px; margin-top: 20px; }
            p, ul { margin: 5px 0; }
            ul { padding-left: 20px; }
            .contato { italic; color: #555; margin-bottom: 20px; }
        </style>
    </head>
    <body>

        <h1>Bernardo Magalhães Santos</h1>
        <p class="contato">
            Rua Oliveiro Marciano, 315 - Diamante - Belo Horizonte – MG <br>
            Telefone: 31 98424-6642 | E-mail: bernardo.maga2009@gmail.com
        </p>

        <h3>RESUMO PROFISSIONAL</h3>
        <p>Estudante de Tecnologia da Informação, com boa comunicação, organização e facilidade para trabalhar em equipe. Tenho interesse em aprendizado contínuo, responsabilidade no cumprimento de tarefas e postura profissional no ambiente de trabalho.</p>

        <h3>OBJETIVO</h3>
        <p>Atuar como estagiário na área de Tecnologia da Informação, com foco no desenvolvimento de habilidades técnicas, aprendizado prático e contribuição responsável para a equipe.</p>

        <h3>FORMAÇÃO ACADÊMICA</h3>
        <p><strong>Curso de Tecnologia da Informação</strong><br>
        Colégio Cotemig – Belo Horizonte (Início: 2024 – Em andamento)</p>

        <h3>CURSOS COMPLEMENTARES</h3>
        <ul>
            <li><strong>Cisco Networking Academy</strong> - Introdução à Cibersegurança (Concluído)</li>
            <li><strong>Cisco Networking Academy</strong> - Fundamentos do Hardware do Computador (Concluído)</li>
        </ul>

        <h3>HABILIDADES TÉCNICAS</h3>
        <ul>
            <li>Montagem e Manutenção de Computadores</li>
            <li>Google Workspace (Docs, Planilhas, Drive, etc.)</li>
            <li>HTML, CSS, JavaScript e C#</li>
            <li>Desenvolvimento web</li>
        </ul>

        <h3>HABILIDADES</h3>
        <ul>
            <li>Comunicação clara e objetiva</li>
            <li>Trabalho em equipe e bom relacionamento interpessoal</li>
            <li>Organização e cumprimento de prazos</li>
            <li>Proatividade e disposição para aprender</li>
            <li>Noções de informática e tecnologia</li>
        </ul>

        <h3>IDIOMAS</h3>
        <ul>
            <li>Inglês básico (leitura e escrita)</li>
            <li>Espanhol básico (leitura e escrita)</li>
        </ul>

    </body>
    </html>
    """
    return texto_explicacao

if __name__ == '__main__':
    app.run(debug=True)
