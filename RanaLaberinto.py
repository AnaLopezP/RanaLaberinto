laberinto = [
    ['I', 'X', 'X', 'B', 'X', 'X'],
    [' ', 'X', ' ', ' ', ' ', ' '],
    [' ', 'B', ' ', 'B', 'T2', ' '],
    [' ', ' ', ' ', 'X', ' ', ' '],
    [' ', ' ', ' ', 'X', ' ', ' ']
    ['T2', 'T1', ' ', 'T1', ' ','S']
]

inicio = 'I'
salida = 'S'
bomba = 'B'
muro = 'X'
teletransporte_1 = 'T1'
teletransporte_2 = 'T2'


muro = ((0,1), (0,2), (0,4), (0,5), (1,1), (3,3), (4,3))
bomba = ((0,3),(2,1),(2,3))
teletransporte_1 = ((5,1), (5,3))
teletransporte_2 = ((5,0), (2,4)) 
# maze shape
#maze1 = [" ","X","X","X","X"]
#maze2 = [" ","X"," "," "," "]
#maze3 = [" ","X"," ","X"," "]
#maze4 = [" "," "," ","X"," "]
#maze5 = ["X","X","X","X"," "]


lab =[]
def creacionlab():
        fila = []
        for i in range(0,6): #line
                for j in range(0,6): #column
                                      
                        if tuple([i,j]) in muro:
                                fia.append("X")
                        elif tuple([i,j]) in bomba:
                                fila.append("B")
                        elif tuple([i,j]) in teletransporte_1:
                                fila.append("T1")
                        elif tuple([i,j]) in teletransporte_2:
                                fila.append("T2")    
                        else:
                                fila.append(" ")
                lab.append (fila)
                fila = []
creacionlab()
  
for x in lab:
    print(" ".join(x))

        