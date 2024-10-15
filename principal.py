import os 
from sqlalchemy import create_engine, Column, String, Integer 
from sqlalchemy.orm import sessionmaker, declarative_base


# Criando Banco de dados 
MEU_BANCO = create_engine("sqlite:///meubancozinho.db")

# Criando conexão com banco de dados 
Session = sessionmaker(bind=MEU_BANCO)
session = Session()

# Criando tabela 
Base = declarative_base() #Característica que irá acontecer para a classe 

# Quando trazemos uma classe, criamos um objeto
class Cliente(Base):
    # Tabela 
    __tablename__ = "clientes"

    #Definindo campos de tabela 
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    email = Column("email", String)
    senha = Column("senha", String)

    def __init__(self, nome: str, email: str, senha: str):
        self.nome = nome
        self.email = email
        self.senha = senha


Base.metadata.create_all(bind=MEU_BANCO)


#CRUD
os.system("cls || clear")
print("Solicitando dados do usuário:")
inserir_nome = input("Digite seu nome:")
inserir_email = input("Digite seu email:")
inserir_senha = input("Digite sua senha:")

cliente = Cliente(nome= inserir_nome, email= inserir_email, senha= inserir_senha)
session.add(cliente)
session.commit()

#Read - Select  - Consulta
print("\nExibindo dados dos clientes")
lista_clientes = session.query(Cliente).all()

for cliente in lista_clientes:
    print(f"{cliente.id} - {cliente.nome} - {cliente.email} - {cliente.senha}")

#U - UPDATE - Atualizar 
print("Atualizando dados do usuário")
email_cliente = input("Digite o email do cliente que será atualizado:")
