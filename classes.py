class Pokemon:
    def __init__(self, nombre:str):
        self.nombre = nombre
class Entrenador:
    def __init__(self, nombre:str, pkmLista:list):
        self.nombre = nombre
        self.pokemones = pkmLista
    @property
    def pokemones(self):
        return self._pokemones
    @pokemones.setter
    def pokemones(self, pkmLista:list):
        if len(pkmLista) != 3:
            raise ValueError('Wrong List Length')
        if not any([not isinstance(pkm, Pokemon) for pkm in pkmLista]):
            self._pokemones = pkmLista
        else:
            raise TypeError('Wrong Datatype')