from datetime import datetime, timedelta

from models import Filme, Sala, Sessao, db


def popular_dados():
    if Filme.query.count() > 0:
        return

    filmes = [
        Filme(titulo="Vingadores: Ultimato", duracao_min=181, classificacao="12"),
        Filme(titulo="Divertidamente 2", duracao_min=96, classificacao="L"),
    ]
    salas = [
        Sala(numero=1, capacidade=120),
        Sala(numero=2, capacidade=80),
    ]
    db.session.add_all(filmes + salas)
    db.session.commit()

    sessoes = [
        Sessao(
            filme_id=filmes[0].id,
            sala_id=salas[0].id,
            data_hora=datetime.now() + timedelta(days=1, hours=2),
            preco=25.0,
        ),
        Sessao(
            filme_id=filmes[1].id,
            sala_id=salas[1].id,
            data_hora=datetime.now() + timedelta(days=1, hours=5),
            preco=20.0,
        ),
    ]
    db.session.add_all(sessoes)
    db.session.commit()
