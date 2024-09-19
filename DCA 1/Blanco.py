'''
Problema 1
'''
class persona:
    def __init__(self, *args):
        if len(args) == 0:
            self.nombre = " "
    distancia_recorrida = '2kms'

    def caminar(self, *args):
        if len(args) == 1:
            self.kms -= args[0] / 2
        elif len(args) == 2:
            if (args[1] == "entrenamiento_calorias"):
                self.kms += args[0] / 500 
            else:
                self.kms += args[0] / 750
        else:
            self.kms -= 0.5
    def entrenar_sin_argumentos(self):
        self.kms -= 10
    def competir_sin_argumentos(self):
        self.kms -= 20
    def __str__(self):
        return 'Persona (nombre={}, entrenamiento={})'.format( self.nombre, self.caminar)

"""
Atleta
"""    
class Atleta():
    def __init__(self, *args):
        super().__init__(args[0], args[1])  # super se refiere a la clase Persona
        if len(args) == 3:          
            self.entrenamiento = args[2]
        else:
            self.competicion = 0.0
       

    def calcular_imc(self):  
        if self.calorias == 0:
            return 'No se puede calcular, calorias = 0'     
        return self.kms / (self.entrenamiento * self.competicion)
    
    def __str__(self): # Permite obtener una cadena con todos los valores
        return 'Atleta (nombre={}, entrenamiento={}, competicion={})'.format(
            self.nombre, self.sin_argumentos, self.sin_argumentos)
