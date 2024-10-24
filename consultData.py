pessoas = session.query(Pessoa).all()

for pessoa in pessoas:
    print(pessoa)
