from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

class Restaurant():
    
    __instance__ = None
    __connectionString = "mssql://DESKTOP-DC7ADPP\\PP2/Restaurant?driver=ODBC+Driver+17+for+SQL+Server"
    
    def __init__(self):
        if Restaurant.__instance__ is None:
            Restaurant.__instance__ = self
            self.engine = create_engine(self.__connectionString)
            self.DBSession = sessionmaker(self.engine)
            self.session = self.DBSession()
           
        else:
            raise Exception("Error: Utilizar metodo getInstance() para inicializar un objeto Restaurant")  
  
    @staticmethod  
    def getInstance():  
        if not Restaurant.__instance__:  
            Restaurant()  
        return Restaurant.__instance__


    @staticmethod  
    def getConnectionString():  
        if not Restaurant.__instance__:  
            Restaurant()  
        return Restaurant.__connectionString
        