from datetime import date

from sqlalchemy import Column, Date, Float, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

engine = create_engine("sqlite:///test.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Pessoa(Base):
    __tablename__ = "pessoas"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
    birthday = Column(Date)
    cpf = Column(String(11), unique=True)

    def __repr__(self) -> str:
        return f"Pessoa(name={self.name})"

class Categoria(Base):
    __tablename__ = "categorias"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    def __repr__(self) -> str:
        return f"Categoria(name={self.name})"

class Produto(Base):
    __tablename__ = "produtos"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    is_active = Column(Boolean, default=True)
    categoiay_id = Column(Integer, ForeignKey(Categoria.id))
    categoria = relationship("Categoria", backref="produtos")
    pessoa_id = Column(Integer, ForeignKey(Pessoa.id))
    pessoa = relationship("Pessoa", backref="produtos")

    def __repr__(self) -> str:
        return f"Produto(name={self.name})"

Base.metadata.create_all(engine)


p1 = Pessoa(name="Leonardo", age=25, birthday=date(2020, 1, 20), cpf="32233534534")
p2 = Pessoa(name="Val", age=22, birthday=date(2019, 3, 23), cpf="42422342344")
p3 = Pessoa(name="Hudson", age=29, birthday=date(1992, 3, 7), cpf="23243535345")
ctg1 = Categoria(name="Móveis")
ctg2 = Categoria(name="Eletrodomésticos")
ctg3 = Categoria(name="Eletrônicos")
pd1 = Produto(name="Sofá", description="Um sofá qualquer", price=10.50, pessoa=p1, categoria=ctg1)
pd2 = Produto(name="Microondas", description="Um microondas qualquer", price=20.50, pessoa=p2, categoria=ctg2)
pd3 = Produto(name="Alexa", description="fala pra caramba", price=30.50, pessoa=p3, categoria=ctg3)

session.add_all([p1, p2, p3, ctg1, ctg2, ctg3, pd1, pd2, pd3])

session.commit()

# result = select(pd1).all()
# print(result)