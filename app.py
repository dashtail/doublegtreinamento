# -*- coding: utf-8 -*-
import json 

class Evento():
    """Isso é a classe do Evento"""
    def __init__(self, titulo, data):
        """Isso é o metodo de inicialização da class"""
        self.titulo = titulo
        self.data = data
        self.organizador = ""


festa_no_ap = Evento("festa no ap", "01/01/2019")
festa_no_ap.organizador = "pseudonerds"

#__dict__ pq sim
json_festa = json.dumps(festa_no_ap.__dict__)

print(json_festa)

#exibo a classe
#print(festa_no_ap)

