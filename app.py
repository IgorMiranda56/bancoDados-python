import os
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import sessionmaker, declarative_base

MEU_BANCO_ALUNO = create_engine("sqlite:///meubancoaluno.db")

Session = sessionmaker(bind=MEU_BANCO_ALUNO)
session = Session()

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"

    ra = Column("ra", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    sobrenome = Column("sobrenome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, sobrenome: str, email: str, senha: str):
        self.nome = nome
        self.sobrenome = sobrenome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=MEU_BANCO_ALUNO)

os.system("cls || clear")
def create_aluno():
    inserir_nome = input("Digite seu nome: ")
    inserir_sobrenome = input("Digite seu sobrenome: ")
    inserir_email = input("Digite seu e-mail: ")
    inserir_senha = input("Digite sua senha: ")

    aluno = Aluno(nome=inserir_nome, sobrenome=inserir_sobrenome, email=inserir_email, senha=inserir_senha)
    session.add(aluno)
    session.commit() 

    return create_aluno

def read_aluno():
    lista_alunos = session.query(Aluno).all()

    for aluno in lista_alunos:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} - {aluno.email} - {aluno.senha}")

    return read_aluno

def update_aluno():
    email_aluno = input("digite o e-mail do aluno que será atualizado: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        aluno.nome = input("Digite seu nome: ")
        aluno.sobrenome = input("Digite seu sobrenome: ")
        aluno.email = input("Digite seu e-mail: ")
        aluno.senha = input("Digite sua senha: ")

        session.commit()
    else:
        print("Aluno não encontrado. ")
    return update_aluno

def delete_aluno():
    email_aluno = input("Digite o e-mail do aluno que será excluído: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        session.delete(aluno)
        session.commit()
        print(f"Aluno {aluno.nome} excluído com sucesso! ")
    else:
        print("Aluno não encontrado. ")
    return delete_aluno

def consultar_aluno():
    email_aluno = input("digite o e-mail do aluno: ")

    aluno = session.query(Aluno).filter_by(email = email_aluno).first()

    if aluno:
        print(f"{aluno.ra} - {aluno.nome} - {aluno.sobrenome} -{aluno.email} - {aluno.senha}")
    else:
        print("Aluno não encontrado. ")
    return consultar_aluno
    

print("Solicitando dados para o aluno. ")
create_aluno()

print("\nExibindo dados de todos os alunos.")
read_aluno()

print("\nAtualizando dados do aluno. ")
update_aluno()

print("\nExibindo dados de todos os alunos.")
read_aluno()

print("\nExcluindo os dados de um aluno. ")
delete_aluno()

print("\nExibindo dados de todos os alunos.")
read_aluno()

print("Consultando os dados de apenas um aluno. ")
consultar_aluno()

session.close()