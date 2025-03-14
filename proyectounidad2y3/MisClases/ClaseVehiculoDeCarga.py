class VehiculoDeCarga:
    def __init__(self,numero_de_vehiculo=0,tipo="", placas="",capmax=0.0, peso_del_producto=0.0, peso_tara=0.0):
        self.__numero_de_vehiculo=numero_de_vehiculo
        self.__tipo=tipo
        self.__placas=placas
        self.__capmax=capmax
        self.__peso_del_producto=peso_del_producto
        self.__peso_tara=peso_tara
    def get_numero_de_vehiculo(self):
        return self.__numero_de_vehiculo
    def set_numero_de_vehiculo(self,numero_de_vehiculo):
        self.__numero_de_vehiculo=numero_de_vehiculo
    def get_tipo(self):
        return self.__tipo
    def set_tipo(self,tipo):
        self.__tipo=tipo
    def get_placas(self):
        return self.__placas
    def set_placas(self,placas):
        self.__placas=placas
    def get_capmax(self):
        return self.__capmax
    def set_capmax(self,capmax):
        self.__capmax=capmax
    def get_peso_del_producto(self):
        return self.__peso_del_producto
    def set_peso_del_producto(self,peso_del_producto):
        self.__peso_del_producto=peso_del_producto
    def get_peso_tara(self):
        return self.__peso_tara
    def set_peso_tara(self,peso_tara):
        self.__peso_tara=peso_tara
    def __str__(self): 
        return f"Vehiculo tiene:\nnumero de vehiculo:{self.get_numero_de_vehiculo()},\
        \ntipo={self.get_tipo()},\
        \nplacas={self.get_placas()},\
        \ncapmax={self.get_capmax()}, \
        \npeso_del_producto=´{self.get_peso_del_producto()}, \
        \npeso_tara={self.get_peso_tara()})" 
     
    def __repr__(self): 
        return f"VehiculoDeCarga (numero_de_vehiculo={self.get_numero_de_vehiculo()}, \
        \ntipo={self.get_tipo()}, \
        \nplacas={self.get_placas()}, \
        \ncapmax={self.get_capmax()}, \
        \npeso_del_producto=´{self.get_peso_del_producto()}, \
        \npeso_tara={self.get_peso_tara()})" 
 



