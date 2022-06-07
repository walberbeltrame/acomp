import networkx as nx
import structout as so
from bintrees import FastRBTree

T = FastRBTree()
G = nx.Graph()

def vertex():
  v=str(input('''
  Digite um ponto: '''))
  return v

def edge():
  e=float(input('''
  Digite uma ligação: '''))
  return e

def add():
  v1 = vertex()
  v2 = vertex()
  e = edge()
  T.insert(v1+v2, e)
  G.add_node(v1)
  G.add_node(v2)
  G.add_edge(v1, v2, weight=e)

def search():
  return

def remove():
  return

def foo(k, v):
  print(k + ": " + str(v))

def view():
  so.gprint(G)
  T.foreach(foo, 0)

def short():
  return

def min():
  return
  
def menu():
  while True:
    opt=int(input('''
      Escolha uma opção
  1 - Cadastrar ligação
  2 - Buscar ligação
  3 - Excluir ligação
  4 - Imprimir rede
  5 - Caminho mais curto
  6 - Rede mínima
  0 - Sair
  Escolha: '''))
    if opt == 1:
      add()
    elif opt == 2:
      search()
    elif opt == 3:
      remove()
    elif opt == 4:
      view()
    elif opt == 5:
      short()
    elif opt == 6:
      min()
    elif opt == 0:
      break

def main(*args):
  menu()

if __name__ == '__main__':
  main()