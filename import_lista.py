import networkx as nx
import matplotlib as mat
import pandas
import numpy
lista_nodos=pandas.read_excel("lista_nodos.xlsx").to_numpy()
lista_aristas=pandas.read_excel("lista_aristas.xlsx").to_numpy()
lista_nodos=(lista_nodos[0:,0:2])
lista_aristas=(lista_aristas[0:,0:3])
g=nx.Graph()

for x in lista_nodos:
    g.add_node(x[0],h=0,g=0,f=0)
    
for y in lista_aristas:
    g.add_edge(y[0],y[1],peso=y[2])
    
for x in lista_nodos:     ### Estaciones que pertenecen a más de una linea
    if lista_nodos.degree(x) > 2:
        print(x)
    

def fg(nodo1,nodo2):
    return g[nodo1][nodo2]["peso"] 
def fh(nodo1):
    return g[nodo1]["h"]
def get_vecinos(nodo1):
    lista_vecinos=set([])
    for x in nx.neighbors(g,nodo1):
        lista_vecinos.add(x)
    return lista_vecinos
def actualizar_peso(nodo1,nodo2):
    g[nodo2]["g"]=g[nodo1][nodo2]["peso"]+g[nodo1]["g"]
def calc_h(nodo):
    g[nodo]["f"]=g[nodo]["g"]+g[nodo]["h"]
def astar(nodo_inicial,nodo_final):
    abierta=([])
    cerrada=([])
    nodo_actual=nodo_inicial
    peso_actual=0
    cerrada.append(nodo_actual)
    while(nodo_actual != nodo_final):
        vecinos=get_vecinos(nodo_actual)
        for x in vecinos:
            actualizar_peso(nodo_actual,x)
            calc_h(x)
            cerrada.append(x)
        
        cerrada.sort()
        nodo_actual=cerrada.pop()
        