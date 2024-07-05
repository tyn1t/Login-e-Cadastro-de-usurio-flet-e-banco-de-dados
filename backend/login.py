import sqlite3 as sql 
import bcrypt 

class Login:
    def __init__(self) -> None:
        self.conn = None
        self.cursor = None
        self.usuario = None 
        self.senha = None
        
    def verificar_cadastro(self):
        try:          
            self.conn = sql.connect("cadastro.db") 
            self.cursor = self.conn.cursor()
            self.cursor.execute("SELECT usuario, senha FROM cadastro WHERE usuario = ?", (self.usuario,))
            resultado = self.cursor.fetchone()
            if resultado:
                usuario_cadastro, senha_hash = resultado
                if bcrypt.checkpw(self.senha.encode(), senha_hash.encode()):
                    return True 
            return False
        except Exception as e:
            print(f"Erro na verificação: {e}")
            return False 
        finally:
            if self.conn: 
                self.conn.close()
                
    def login_usuario(self, usuario, senha):
        try:
            self.usuario = usuario 
            self.senha = senha
            if self.verificar_cadastro(): 
                print("Login efetuado com sucesso!")
                return True
            else: 
                print("Usuário ou senha inválidos.")
                return False
        except Exception as e:
            print(f'Erro no login {e}')