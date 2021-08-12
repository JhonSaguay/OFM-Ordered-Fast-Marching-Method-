from functools import update_wrapper
import math
import tratamiento_imagenes as Timage
maxval=math.inf
def find_neigbord_min(matriz2object,initial_points,x,y):
    neighbors_list=[]
    min_value_list=maxval
    node_min_value=None
    #diagonals
    if (x+1<=len(matriz2object)-1 and y+1<=len(matriz2object[0])-1):
        value=matriz2object[x+1][y+1]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    if (x-1>=0  and y-1>=0 ):
        value=matriz2object[x-1][y-1]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    if (x-1>=0 and y+1<=len(matriz2object[0])-1):
        value=matriz2object[x-1][y+1]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    if (x+1<=len(matriz2object)-1 and y-1>=0):
        value=matriz2object[x+1][y-1]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    #von-neuman
    if (y+1<=len(matriz2object[0])-1):
        value=matriz2object[x][y+1]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    if (x+1<=len(matriz2object)-1):
        value=matriz2object[x+1][y]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    if (y-1>=0):
        value=matriz2object[x][y-1]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    if (x-1>=0):
        value=matriz2object[x-1][y]
        neighbors_list.append(value)
        if (value.coordenadas in initial_points):
            return value
        if (value.tiempo<min_value_list and value.tiempo>0 and value.velocidad>0.0):
            node_min_value=value
            min_value_list=node_min_value.tiempo
    return(node_min_value)

#ruta con diagonales

def constructroutediagonal(initial_points,matriz2object,matrixroutediagonal,punto_final,anchor):
    cont=0
    flag=True
    x=punto_final[0]
    y=punto_final[1]
    matrixroutediagonal[x][y]=0
    pasos=0
    directory="D:\\Documents\\noveno\\tesis\\Classic FMM\\Individual\\"
    while (flag):
        
        name='Img_diagonal_'+str(pasos)+'.jpg'
        # Timage.save_individual_image(directory,name,matrixroutediagonal)
        node_min_value=find_neigbord_min(matriz2object,initial_points,x,y)
        
        x=node_min_value.coordenadas[0]
        y=node_min_value.coordenadas[1]
        pasos+=1
        if (anchor):
            matrixroutediagonal=completeroute(matrixroutediagonal,x,y,anchor)
        
        if (node_min_value.coordenadas in initial_points):
            flag=False
        
        matrixroutediagonal[x][y]=0
    print('-- Ruta nueva --')
    print("Distancia recorrida: ",pasos)

def completeroute(matrixroute,x,y,anchor):
    for i in range(anchor):
        matrixroute[x-i][y]=0
        matrixroute[x+i][y]=0
        matrixroute[x][y+i]=0
        matrixroute[x][y-i]=0
    return (matrixroute)

# ruta sin diagonales
def constructroute(matriz2object,matrixroute,punto_final,anchor):
    flag=True
    x=punto_final[0]
    y=punto_final[1]
    pasos=0
    while (flag):
        pasos+=1
        matrixroute[x][y]=0
        before_node=matriz2object[x][y].tail
        if (anchor):
            matrixroute=completeroute(matrixroute,x,y,anchor)
        if (before_node!=None):
            x=before_node.coordenadas[0]
            y=before_node.coordenadas[1]
        else:
            flag=False
    print('-- Ruta original --')
    print("Distancia recorrida: ",pasos)