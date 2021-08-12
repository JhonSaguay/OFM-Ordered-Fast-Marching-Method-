import numpy as np
import math
import time
import cv2 as cv
import tratamiento_imagenes as Timage
import contourfunctions as contour
import routeconstruction as route
#variables globales
listavecinos=[]
listavecinosvalues=[]
list_initialvalues=[]
matriz2object=[]
maxval=math.inf
#--------------------
class Celdas():
    def __init__(self,coordenadas,tiempo=maxval,tipo="open",velocidad=1.0,tail=None):

        self.coordenadas=coordenadas
        self.tiempo = tiempo
        self.tipo = tipo
        self.velocidad = velocidad
        self.tail=tail


def contruct_initial(n,m,initial_points):
    initial_matrix=np.zeros(n*m).reshape(n,m)
    for point in initial_points:
        initial_matrix[point[0]][point[1]]=1
    return (initial_matrix)

def contruct_time(n,m):
    matrixtime=np.zeros(n*m).reshape(n,m)
    return(matrixtime)

def imprimirtiempo():
    for fila in matriz2object:
        for columna in fila:
            print("{0:.2f}".format(columna.tiempo), end="    ")
        print("")
        print("")

# sort function here
  
def constructmatrix(matrix_initialvalues,matrix_velocity):
    matrizobjetos=[]
    i=0
    for fila in matrix_initialvalues:
        filaobjetos=[]
        j=0
        for columna in fila:
            if columna==1:
                celdaobjeto=Celdas((i,j),0,"frozen",matrix_velocity[i][j])
                list_initialvalues.append(celdaobjeto)
            else:
                celdaobjeto=Celdas((i,j),maxval,"open",matrix_velocity[i][j])
            filaobjetos.append(celdaobjeto)
            j+=1
        i+=1
        matrizobjetos.append(filaobjetos)
    matriz2=np.array(matrizobjetos)
    return (matriz2)

def recorreriniciales():
    for inicial in list_initialvalues:
        reconocervecinos(inicial)
        #main_loop()


def reconocervecinos(i):

    x=i.coordenadas[0]
    y=i.coordenadas[1]
    von_neuman_list=[]
    if (y+1<=len(matriz2object[0])-1):
        von_neuman_list.append(matriz2object[x][y+1])
    if (x+1<=len(matriz2object)-1):
        von_neuman_list.append(matriz2object[x+1][y])
    if (y-1>=0):
        von_neuman_list.append(matriz2object[x][y-1])
    if (x-1>=0):
        von_neuman_list.append(matriz2object[x-1][y])

    for celda in von_neuman_list:
        x=celda.coordenadas[0]
        y=celda.coordenadas[1]
        if (celda.velocidad!=0):
            if (celda.tipo!="frozen"):
                #aumentar padding left,right,up and bottom
                enter=True
                if (padding!=0):
                    if (y+padding<=len(matriz2object[0])-1) and (x+padding<=len(matriz2object)-1) and (y-padding>=0) and (x-padding>=0) :         
                        leftceld=matriz2object[x-padding][y]
                        rightceld=matriz2object[x+padding][y]
                        upceld=matriz2object[x][y+padding]
                        bottomceld=matriz2object[x][y-padding]
                        if (leftceld.velocidad==0 or rightceld.velocidad==0 or upceld.velocidad==0 or bottomceld.velocidad==0):
                            enter=False
                        else:
                            enter=True
                if (enter):
                    value=eikonalequation(celda,i)
                    if celda.tipo=="open":
                        celda.tipo="narrow"
                        listavecinos.append(celda)
                        celda.tiempo=value
                        celda.tail=i
                        listavecinosvalues.append(celda.tiempo)
                    elif celda.tipo=="narrow":
                        if value<celda.tiempo:
                            #agregado
                            celda.tiempo=value
                            celda.tail=i
                            indice=listavecinos.index(celda)
                            listavecinosvalues[indice]=celda.tiempo
                else:
                    celda.tail=None
                    celda.tiempo=0
                    celda.tipo="frozen"
        else:
            celda.tail=None
            celda.tiempo=0
            celda.tipo="frozen"    

def eikonalequation(vecino,celdacontigua):
    x=vecino.coordenadas[0]
    y=vecino.coordenadas[1]
    t1=maxval
    t2=maxval
    if ((x+1<=len(matriz2object)-1) and (x-1>=0)):
        t1=min(matriz2object[x-1][y].tiempo,matriz2object[x+1][y].tiempo)
    elif(x+1<=len(matriz2object)-1):
        t1=matriz2object[x+1][y].tiempo
    elif (x-1>=0):
        t1=matriz2object[x-1][y].tiempo
    if ((y+1<=len(matriz2object[0])-1) and (y-1>=0)):
        t2=min(matriz2object[x][y-1].tiempo,matriz2object[x][y+1].tiempo)
    elif(y+1<=len(matriz2object[0])-1):
        t2=matriz2object[x][y+1].tiempo
    elif (y-1>=0):
        t2=matriz2object[x][y-1].tiempo
    #calculo previo para sacar raiz
    a=2
    b=(-2)*(t1+t2)
    if (vecino.velocidad!=0):
        c=pow(t1,2)+pow(t2,2)-(1/(pow(vecino.velocidad,2)))
    else:
        c=pow(t1,2)+pow(t2,2)
    discriminante=pow(b,2)-4*a*c
    if discriminante>=0:
        T=quadraticfunction(a,b,c)
    else:
        if (vecino.velocidad!=0):
            T=celdacontigua.tiempo+(1/vecino.velocidad)
        else:
            T=celdacontigua.tiempo
    return(T)

def quadraticfunction(a,b,c):

    discriminante=pow(b,2)-4*a*c
    T=((-b)+math.sqrt(discriminante))/(2*a)
    return(T)
#encuentra el vecino min  
def find_min_neighborlist():
    minvecino=maxval
    mincoordenadas=(-1,-1)
    for celda in listavecinos:
        x=celda.coordenadas[0]
        y=celda.coordenadas[1]
        if celda.tiempo<minvecino:
            minvecino=celda.tiempo
            mincoordenadas=celda.coordenadas
    return (mincoordenadas)
#first min found
def find_first_min_neighborlist():
    indice=listavecinosvalues.index(min(listavecinosvalues))
    listavecinosvalues.pop(indice)
    mincoordenadas=listavecinos[indice].coordenadas
    return (mincoordenadas)
def main_loop():
    cont=0
    while len(listavecinos)>0:
        cont+=1
        coordenadasvecino=find_first_min_neighborlist()
        x=coordenadasvecino[0]
        y=coordenadasvecino[1]
        matriz2object[x][y].tipo="frozen"
        matrixtime[x][y]=matriz2object[x][y].tiempo
        listavecinos.remove(matriz2object[x][y])
        matriz[x][y]=1
        # print("Paso  ",cont)
        # print(matriz)
        # imprimirtiempo()
        vecino=matriz2object[x][y]
        reconocervecinos(vecino)

#repeticion
repetition=5
listrepetition=[]

for i in range(repetition):
    # A = np.loadtxt('imagennew1.txt',dtype=float)
    A = Timage.conversion_image('laberinto3.jpg')
    # Timage.show_results_two(A,A)
    #A = Timage.conversion_image('imagen_400x400.png')
    # matplotlib.image.imsave('D:\\Documents\\noveno\\tesis\\Classic FMM\\Ruta_Original2.jpg',A)
    # img=cv.imread('D:\\Documents\\noveno\\tesis\\Classic FMM\\Ruta_Original2.jpg',1)
    # cv.imshow('imagen',img)
    # cv.waitKey(0)
    n=len(A)
    m=len(A[0])
    print(n,",",m)
    #initial_points=[(n//2,1)]
    #initial_points=[(n//2,m//2)]
    initial_points=[(15,15)]
    # initial_points=[(190,210)]
    #punto_final=(510,450)
    punto_final=(725,545)
    # punto_final=(n-1,m-1)
    #adding anchor and padding
    # padding=5
    # anchor=2
    padding=3
    anchor=2

    matriz=contruct_initial(n,m,initial_points)
    matrixtime=contruct_time(n,m)
    start_time=time.time()
    matriz2object=constructmatrix(matriz,A)
    recorreriniciales()
    main_loop()
    # imprimirtiempo()
    fast_execution_time=(time.time() - start_time)
    listrepetition.append(fast_execution_time)
    print("size matrix: ",n, "," , m)
    print("---Fast Marching execution  %s seconds ---" % (fast_execution_time))

print('Average')
print(sum(listrepetition)/repetition)
print('Min')
print(min(listrepetition))
print('Max')
print(max(listrepetition))
contour.contourgraph(matrixtime)
contour.contour3dgraph(matrixtime)
