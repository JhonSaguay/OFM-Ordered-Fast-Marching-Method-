from math import *
#insert MergeSort
def sortmethod(lista,celda,indiceinicial=0):
    
    n=len(lista)
    if celda.tiempo<=lista[0].tiempo:
        return (indiceinicial)
    elif celda.tiempo>=lista[n-1].tiempo:
        indiceinicial=n+indiceinicial
        return (indiceinicial)
    else:
        #reducir tamaño de la lista en cuatro
        listareduced=lista[1:len(lista)-1]
        indiceinicial+=1
        division=len(listareduced)//4
        #Vamos a formar las 4 listas
        #cuadrante F->entra en el primero , T entra en el segudno
        if celda.tiempo<lista[n//2].tiempo:
            Cuadrant=True
        else:
            Cuadrant=False

        
        if Cuadrant:

            cuadrante1=listareduced[:division]
            
            if len(cuadrante1)>0:
                
                indexcuadrante1=indiceinicial
                inicio=cuadrante1[0].tiempo
                fin=cuadrante1[len(cuadrante1)-1].tiempo
                if celda.tiempo>inicio and celda.tiempo<=fin:
                    if len(cuadrante1)>=30000:
                        indiceinicial=sortmethod(cuadrante1,celda,indexcuadrante1)
                    else:
                        indiceinicial=mergesort(cuadrante1,celda,indexcuadrante1)
                    return (indiceinicial)
                elif celda.tiempo<=inicio:
                    indiceinicial=indexcuadrante1
                    return (indiceinicial)

            cuadrante2=listareduced[division:division*2]
            if len(cuadrante2)>0:
                indexcuadrante2=indexcuadrante1+len(cuadrante1)
                inicio=cuadrante2[0].tiempo
                fin=cuadrante2[len(cuadrante2)-1].tiempo
                if celda.tiempo>inicio and celda.tiempo<=fin:
                    if len(cuadrante2)>=30000:
                        indiceinicial=sortmethod(cuadrante2,celda,indexcuadrante2)
                    else:
                        indiceinicial=mergesort(cuadrante2,celda,indexcuadrante2)
                    return (indiceinicial)
                elif celda.tiempo<=inicio:
                    indiceinicial=indexcuadrante2
                    return (indiceinicial)
                elif celda.tiempo>fin:
                    indiceinicial=indiceinicial+(division*2)
                    return (indiceinicial)
        else:
        
            cuadrante3=listareduced[division*2:division*3]
            if len(cuadrante3)>0:
                # indexcuadrante3=indexcuadrante2+len(cuadrante2)
                indexcuadrante3=(division*2)+1
                inicio=cuadrante3[0].tiempo
                fin=cuadrante3[len(cuadrante3)-1].tiempo
                if celda.tiempo>inicio and celda.tiempo<=fin:
                    if len(cuadrante3)>=30000:
                        indiceinicial=sortmethod(cuadrante3,celda,indexcuadrante3)
                    else:
                        indiceinicial=mergesort(cuadrante3,celda,indexcuadrante3)
                    return (indiceinicial)
                elif celda.tiempo<=inicio:
                    indiceinicial=indexcuadrante3
                    return (indiceinicial)
            
            cuadrante4=listareduced[division*3:]
            if len(cuadrante4)>0:
                
                indexcuadrante4=len(listareduced)-len(cuadrante4)+indiceinicial
                inicio=cuadrante4[0].tiempo
                fin=cuadrante4[len(cuadrante4)-1].tiempo
                if celda.tiempo>inicio and celda.tiempo<=fin:
                    if len(cuadrante4)>=30000:
                        
                        indiceinicial=sortmethod(cuadrante4,celda,indexcuadrante4)
                    else:
                        indiceinicial=mergesort(cuadrante4,celda,indexcuadrante4)
                    return (indiceinicial)
                elif celda.tiempo<=inicio:
                    indiceinicial=indexcuadrante4
                    return (indiceinicial)

                elif celda.tiempo>fin:
                    indiceinicial=indiceinicial+n-2
                    return (indiceinicial)

        
        
def mergesortprincipal(lista,celda,indiceinicial=0):
    if len(lista)>=30000:
        # print('entro 2')
        index=sortmethod(lista,celda,indiceinicial)
    else:
        # print('entro 1')
        index=mergesort(lista,celda,indiceinicial)
    
    return index

def mergesort(lista,celda,indiceinicial=0):
    #ingresar o no a la recursion
    n=len(lista)
    if celda.tiempo<=lista[0].tiempo:
        return (indiceinicial)
        #print("Se insertara en la posicion 1:",indiceinicial)
    elif celda.tiempo>=lista[n-1].tiempo:
        indiceinicial=n+indiceinicial
        return (indiceinicial)
        #print("Se insertara en la posicion 2:",n+indiceinicial)
    else:
        
        if len(lista)>5:
            Left=lista[1:(len(lista)//2)]
            Right=lista[(len(lista)//2):len(lista)-1]
            indiceinicial+=1
        else:
            Left=lista[0:(len(lista)//2)]
            Right=lista[(len(lista)//2):len(lista)]
            indiceinicial=indiceinicial 
        
        if len(Right)>0:
            indexRight=indiceinicial+len(Left)
            inicio=Right[0].tiempo
            fin=Right[len(Right)-1].tiempo
            if celda.tiempo>inicio and celda.tiempo<=fin:
                indiceinicial=mergesort(Right,celda,indexRight)
                return (indiceinicial)
            elif celda.tiempo<=inicio:
              
                indiceinicial=indexRight
                return (indiceinicial)
                
            elif celda.tiempo>fin:
                indiceinicial=indiceinicial+n-2
                return (indiceinicial)

        if len(Left)>0:
            indexLeft=indiceinicial
            inicio=Left[0].tiempo
            fin=Left[len(Left)-1].tiempo
            if celda.tiempo>inicio and celda.tiempo<=fin:
                indiceinicial=mergesort(Left,celda,indexLeft)
                return (indiceinicial)
            elif celda.tiempo<=inicio:

                indiceinicial=indexLeft
                return (indiceinicial)

        
        
        
        
        

    
    return(indiceinicial)

def sortmethodoriginal(lista,celda,indiceinicial=0):
    #ingresar o no a la recursion
    n=len(lista)
    if celda.tiempo<=lista[0].tiempo:
        return (indiceinicial)
        #print("Se insertara en la posicion 1:",indiceinicial)
    elif celda.tiempo>=lista[n-1].tiempo:
        indiceinicial=n+indiceinicial
        return (indiceinicial)
        #print("Se insertara en la posicion 2:",n+indiceinicial)
    else:
        if celda.tiempo<lista[n//2].tiempo:
            Cuadrant=False
        else:
            Cuadrant=True
        Left=lista[0:(len(lista)//2)]
        Right=lista[(len(lista)//2):len(lista)]
        indiceinicial=indiceinicial
        if len(Left)>0:
            
            indexLeft=indiceinicial
            inicio=Left[0].tiempo
            fin=Left[len(Left)-1].tiempo
            if celda.tiempo>inicio and celda.tiempo<=fin:
                if (Cuadrant):
                    print(inicio)
                    print(fin)
                    print(Right[0].tiempo)
                    print(Right[-1].tiempo)
                    print(lista[n//2].tiempo)
                    print(celda.tiempo)
                    
                    print('no debia entrar')
                indiceinicial=sortmethodoriginal(Left,celda,indexLeft)
                return (indiceinicial)
            elif celda.tiempo<=inicio:
                indiceinicial=indexLeft
                return (indiceinicial)

        
        if len(Right)>0:
            
            indexRight=indiceinicial+len(Left)
            inicio=Right[0].tiempo
            fin=Right[len(Right)-1].tiempo
            if celda.tiempo>inicio and celda.tiempo<=fin:
                indiceinicial=sortmethodoriginal(Right,celda,indexRight)
                return (indiceinicial)
            elif celda.tiempo<=inicio:
            
                indiceinicial=indexRight
                return (indiceinicial)
            elif celda.tiempo>fin:
                indiceinicial=indiceinicial+n
                return (indiceinicial)
    
    return(indiceinicial)


#Merge sort complete
def merge_sort_complete(lista): 
    """
    Lo primero que se ve en el psudocódigo es un if que
    comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
    ¿Por que? Ya esta ordenada. 
    """
    if len(lista) < 2:
        return lista
    
    # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        right = merge_sort_complete(lista[:middle])
        left = merge_sort_complete(lista[middle:])
        return merge(right,left)
    


#Merge
def merge(lista1, lista2):
    """
    merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
 
   # Intercalar ordenadamente
    while(i < len(lista1) and j < len(lista2)):
        if (lista1[i].tiempo < lista2[j].tiempo):
            result.append(lista1[i])

            i += 1
        else:
            result.append(lista2[j])
            j += 1
 
    # Agregamos los resultados a la lista
    result += lista1[i:]
    result += lista2[j:]

    # Retornamos los resultados
    return result

#Bucket sort

    #insert
def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j].tiempo > up.tiempo:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up    
    return b    
    #Bucket
def bucketSort(x,maximum):
    B=[]
    bucket=10
    divider=ceil((maximum+1)/bucket)
    for i in range(bucket):
        B.append([])
    for element in x:
        j=floor(element.tiempo/divider)
        B[j].append(element)
    for i in range(len(B)):
        B[i] = insertionSort(B[i])

    k = 0
    for i in range(len(B)):
        for j in range(len(B[i])):
            x[k] = B[i][j]
            k += 1
    return x


    

