# -*- coding: utf-8 -*-

class Evento():
    """Isso é a classe do Evento"""
    def __init__(self, titulo, data):
        """Isso é o metodo de inicialização da class"""
        self.titulo = titulo
        self.data = data
        self.organizador = ""


festa_no_ap = Evento("festa no ap", "01/01/2019")

festa_no_ap.organizador = "pseudonerds"


print(festa_no_ap.titulo)

