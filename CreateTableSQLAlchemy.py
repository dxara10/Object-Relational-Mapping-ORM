from sqlalchemy import create_engine

engine = create_engine('mysql+mysqlconnector://seu_usuario:sua_senha@localhost/seu_banco_de_dados')

Base.metadata.create_all(engine)
