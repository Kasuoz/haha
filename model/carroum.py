from model.carro import Carro

<<<<<<< HEAD:model/carroum.py
class carroum(Carro):
=======
class pessoaJuridica(Carro):
>>>>>>> 3075a411379ae433745f13aff223818975cbf28d:model/pessoajur.py
    __marca = ""
    __modelo = ""
    __placa = ""
    __cor = ""
    __ano = ""

    @property
    def marca(self):
        return self.__marca
    @marca.setter
    def marca(self, marca):
        self.__marca = marca

    @property
    def modelo(self):
        return self.__modelo
    @modelo.setter
    def modelo(self, modelo):
        self.__modelo = modelo  

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, placa):
        self.__placa = placa  

    @property
    def cor(self):
        return self.__cor
    @cor.setter
    def cor(self, cor):
        self.__cor = cor    

    @property
    def ano(self):
        return self.__ano
    @ano.setter
    def ano(self, ano):
        self.__ano = ano

    def __str__(self):
        return f'{super().__str__()}; {self.marca}; {self.modelo}; {self.placa}; {self.cor}; {self.ano}; '