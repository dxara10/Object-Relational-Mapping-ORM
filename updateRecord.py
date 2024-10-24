pessoa = session.query(Pessoa).filter_by(nome='Alice').first()
pessoa.idade = 31
session.commit()
