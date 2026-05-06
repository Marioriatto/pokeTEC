class Pokemon:
    def __init__(self, datos:dict):
        self.nombre = datos['nombre']
        self.ataques = datos['ataques']
        self.defensas = datos['defensas']
        self.vida = datos['vida']
        self.power = datos['power']
        self.defendiendo = 0
class Entrenador:
    def __init__(self, datos:dict, ):
        self.nombre = datos['nombre']
        self.avatar = datos['avatar']
        self.pokemones = datos['pokemones']