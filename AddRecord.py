from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
session = Session()

nova_pessoa = Pessoa(nome='Alice', idade=30)
session.add(nova_pessoa)
session.commit()
