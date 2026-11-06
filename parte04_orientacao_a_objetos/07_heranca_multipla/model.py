# superclasses
class Carro:
    def __init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapameto):
        self.__cambio = cambio
        self.__estepe = estepe
        self.__porta_malas = porta_malas
        self.__volante = volante
        self.__retrovisor = retrovisor
        self.__buzina = buzina
        self.__escapamento = escapameto

# métodos set e get
    @property # método get
    def cambio(self):
        return self.__cambio

    @cambio.setter # método set
    def cambio(self,cambio):
        self.__cambio = cambio

    @property # método get
    def estepe(self):
        return self.__estepe
    
    @estepe.setter # método set
    def estepe(self,estepe):
        self.__estepe = estepe

    @property # método get
    def porta_malas(self):
        return self.__porta_malas
    
    @porta_malas.setter # método set
    def porta_malas(self,porta_malas):
        self.__porta_malas = porta_malas

    @property # método get
    def volante(self):
        return self.__volante
    
    @volante.setter # método set
    def volante(self,volante):
        self.__volante = volante

    @property # método get
    def retrovisor(self):
        return self.__retrovisor
    
    @retrovisor.setter # método set
    def retrovisor(self,retrovisor):
        self.__retrovisor = retrovisor

    @property # método get
    def buzina(self):
        return self.__buzina
    
    @buzina.setter # método set
    def buzina(self,buzina):
        self.__buzina = buzina

    @property # método get
    def escapamento(self):
        return self.__escapamento
    
    @escapamento.setter # método set
    def escapamento(self,escapamento):
        self.__escapamento = escapamento

class Aviao:
    def __init__(self,asa,turbina,aerofolio,cauda,manche,caixa_preta):
        self.__asa = asa
        self.__turbina = turbina
        self.__aerofolio = aerofolio
        self.__cauda = cauda
        self.__manche = manche
        self.__caixa_preta = caixa_preta

    # métodos set e get
    @property # método get
    def asa(self):
        return self.__asa

    @asa.setter # método set
    def asa(self,asa):
        self.__asa = asa

    # métodos set e get
    @property # método get
    def turbina(self):
        return self.__turbina

    @turbina.setter # método set
    def turbina(self,turbina):
        self.__turbina = turbina

    # métodos set e get
    @property # método get
    def aerofolio(self):
        return self.__aerofolio

    @aerofolio.setter # método set
    def aerofolio(self,aerofolio):
        self.__aerofolio = aerofolio

    # métodos set e get
    @property # método get
    def cauda(self):
        return self.__cauda

    @cauda.setter # método set
    def cauda(self,cauda):
        self.__cauda = cauda

    # métodos set e get
    @property # método get
    def manche(self):
        return self.__manche

    @manche.setter # método set
    def manche(self,manche):
        self.__manche = manche

    # métodos set e get
    @property # método get
    def caixa_preta(self):
        return self.__caixa_preta

    @caixa_preta.setter # método set
    def caixa_preta(self,caixa_preta):
        self.__caixa_preta = caixa_preta

class CarroVoador(Carro, Aviao):
    def __init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapameto,asa,turbina,aerofolio,cauda,manche,caixa_preta):
        Carro.__init__(self,cambio,estepe,porta_malas,volante,retrovisor,buzina,escapameto)
        Aviao.__init__(self,asa,turbina,aerofolio,cauda,manche,caixa_preta)