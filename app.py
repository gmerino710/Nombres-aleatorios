import random 
#importar cosas del istema

import os
#cras archivos y lo llenas de texo
def archivos(name,texto):
    file = open(name+".txt", "w")
    MyList=map(lambda x:x+'\n', texto)
    file.writelines(MyList)
    file.close()

#variables
archivo = open('datos.txt','r');
personas =[];
#aqui asignas los valores del archivo a una lista 
for linea in archivo:
    personas.append(linea.rstrip("\n")) 

# contador
#es el numero de datos del array
value =len(personas);
#contador para bombre de archivo
contador =0;     
  
#-----------------------Desarrollo------------------------------------  
while value >0:
    removido =(random.sample(personas,k=5));
   # print(value);
    print(removido);
    #choice = input("would you like to play again? y/n: ")
    if removido:
        print ("descuento")
        value = value-len(removido)
        print('resta esto',value);
        contador += 1
        print(contador);
        #Crea el archivo
        archivos(str(contador),removido);
     



