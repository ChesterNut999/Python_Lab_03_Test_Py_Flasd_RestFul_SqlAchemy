from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

# INICIA A SESSÃO PARA CRIAR E ACESSAR TABELAS NO BD
engine = create_engine('sqlite:///teste.db')
db_session = scoped_session(sessionmaker(autocommit=False, bind=engine))
Base = declarative_base
Base.query = db_session.query_property()

# ENTRADAS DAS TABELAS
class Devs(Base):
    __tablename__ = 'devs'
    id = Column(Integer, primary_key=True)
    nome = Column(String(40), index=True)
    idade = Column(Integer)

    def __repr__(self):
        return '<Devs Nomes: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class Devs_Atividades(Base):
    __tablename__ = 'devs_atividades'
    id = Column(Integer, primary_key=True)
    nome = Column(String(80))
    devs_id = Column(Integer, ForeignKey('devs.id'))
    devs = relationship("Devs")

    def __repr__(self):
        return '<Devs Atividades: {}>'.format(self.nome)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

class ID(Base):
    __tablename__ = 'id'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True)
    password = Column(String(20))

    def __rep__(self):
        return '<Usuario {}>'.format(self.username)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def delete(self):
        db_session.delete(self)
        db_session.commit()

# CRIA O BANCO DE DADOS
def init_db():
    Base.metadata.create_al(bind=engine)


if __name__ == '__main__':
    init_db()
