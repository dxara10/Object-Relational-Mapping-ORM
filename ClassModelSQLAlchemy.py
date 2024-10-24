from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Pessoa(Base):
    __tablename__ = 'pessoas'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50))
    idade = Column(Integer)

    def __repr__(self):
        return f"<Pessoa(nome='{self.nome}', idade={self.idade})>"
