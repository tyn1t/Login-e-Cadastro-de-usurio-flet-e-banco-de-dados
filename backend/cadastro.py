import sqlite3
import bcrypt

class Cadastra:
    def __init__(self, usuario, email, senha, confirmar_senha):
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.confirmar_senha = confirmar_senha
        self.conn = None
        self.cursor = None 
    
    # Cria a tabela 'cadastro' no banco de dados se ela não existir.  
    def criar_tabelas(self):
        try:
            self.conn = sqlite3.connect('cadastro.db')
            self.cursor = self.conn.cursor()

            self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS cadastro (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario TEXT UNIQUE,
                    email TEXT UNIQUE,
                    senha TEXT
                )
            """)

            self.conn.commit()
        except Exception as e:
            print(f'Erro ao criar Tabela: {e}')
            self.conn.close()
        
            
    # VALIDAR SENHA 
    def valida_senha(self):
        if self.senha != self.confirmar_senha:
            print('As senhas não coincidem')
            return False
        
        if len(self.senha) < 10:
            print("A senha deve ter pelo menos 10 caracteres.")
            return False

        # Verificando se a senha tem pelo menos um número, uma letra e um caractere especial
        if not any(c.isdigit() for c in self.senha):
            print("A senha deve conter pelo menos um número.")
            return False
        if not any(c.isalpha() for c in self.senha):
            print("A senha deve conter pelo menos uma letra.")
            return False
        
        if not any(not c.isalnum() for c in self.senha):
            return False

        return True
    
    # Valida o formato do email do usuário.
    def validar_email(self):
        if "@" not in self.email or "." not in self.email:
            return None
        return  True    
    
    # CADASTRA USUARIO 
    def cadastra_usuario(self):
        try:
            self.criar_tabelas()
            if self.valida_senha() and self.validar_email():
                self.conn = sqlite3.connect('cadastro.db')
                self.cursor = self.conn.cursor()
                
                senha_hash = bcrypt.hashpw(self.senha.encode(), bcrypt.gensalt())
                # Use execute para inserir um único usuário
                self.cursor.execute("""
                    INSERT INTO cadastro (usuario, email, senha)
                    VALUES (?, ?, ?)
                """, (self.usuario, self.email, senha_hash.decode()))
                self.conn.commit()

                print("Usuário inserido com sucesso!")
        except ValueError as e:
            print(f"Erro de validação: {e}")
        except Exception as e:
            print(f"Erro ao inserir usuário: {e}")
        finally:
            self.conn.close() 