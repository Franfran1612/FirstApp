from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker, declarative_base, scoped_session

# configurar banco
# criando conexão
engine = create_engine('sqlite:///base_biblioteca(1).sqlite3')
# db_session = scoped_session(sessionmaker(bind=engine))
db_session = scoped_session(sessionmaker(bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

class Livro(Base):
    __tablename__ = 'TAB_LIVRO'
    id = Column(Integer, primary_key=True)
    titulo_livro = Column(String(25), nullable=False, index=True)
    autor = Column(String(25), nullable=False, index=True)
    categoria = Column(String(11), nullable=True, index=True)
    descricao = Column(String(11), nullable=False, index=True)


    # representação classe
    def __repr__(self):
        return '<Livro: {} {} {} {}>'.format(self.titulo_livro, self.autor,
                                             self.categoria,self.descricao, self.id )

    def save(self):

        db_session.add(self)
        db_session.commit()



    def serialize_livro(self):
        dados_livro = {
            "id": self.id,
            "titulo_livro": self.titulo_livro,
            "autor": self.autor,
            "descricao": self.descricao,
            "categoria": self.categoria
        }
        return dados_livro

class Usuario(Base):
    __tablename__ = 'TAB_USUARIO'
    id_usuario = Column(Integer, primary_key=True)
    nome = Column(String(25), nullable=False, index=True)
    salario = Column(String(25), nullable=False, index=True)
    profissao = Column(String(11), nullable=False, index=True)

    # representação classe
    def __repr__(self):
        return '<Livro: {} {} {} {}>'.format(self.nome, self.salario,
                                             self.profissao, self.id_usuario)

    def save(self):
        db_session.add(self)
        db_session.commit()

    def serialize_livro(self):
        dados_usuario = {
            "id_usuario": self.id_usuario,
            "nome": self.nome,
            "salario": self.salario,
            "profissão": self.profissao,
        }
        return dados_usuario


def init_db():
    Base.metadata.create_all(bind=engine)


if __name__ == '__main__':
    init_db()


