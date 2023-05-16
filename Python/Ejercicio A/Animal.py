class Animal:
    # def __init__(self,nombre_animal, pelo, plumas, huevos, leche, vuela, acuatico, depredador, dientes,
    #              espinazo, respira, venenoso, aletas, patas, cola, domestico, tamanio_gato, clase):
    def __init__(self, nombre_animal, patas, clase):
        self.nombre_animal = nombre_animal
        # self.pelo = pelo
        # self.plumas = plumas
        # self.huevos = huevos
        # self.leche = leche
        # self.vuela = vuela
        # self.acuatico = acuatico
        # self.depredador = depredador
        # self.dientes = dientes
        # self.espinazo = espinazo
        # self.respira = respira
        # self.venenoso = venenoso
        # self.aletas = aletas
        self.patas = patas
        # self.cola = cola
        # self.domestico = domestico
        # self.tamanio_gato = tamanio_gato
        self.clase = clase

    def __str__(self):
        return f'({self.nombre_animal})'