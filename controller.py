from model import AccionesBd as abd
from dotenv import load_dotenv
import os

class Controller(abd):
    
    def __init__(self):
        try:
            load_dotenv()
            host = os.getenv("HOST")
            user = os.getenv("USER")
            password = os.getenv("PASS")
            database = os.getenv("DATABASE")
            super().__init__(host,user,password,database)
            self.set_table("holaa")
        except:
            print("No hay conexion")
       
    def buscar_valores(self):
        datos= self.select_all()
        if datos:
            print(datos)
        else:
            print("No hay")
        
        
    



         



