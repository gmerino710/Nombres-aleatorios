import random 
#importar cosas del istema

import os
#cras archivos y lo llenas de texo
def archivos(name,texto,contador):
    file = open("Grupo-"+name+".txt", "w",encoding="utf-8")
    MyList=map(lambda x:x+'\n',texto)
    file.writelines("Grupo-"+contador+'\n')
    file.writelines(MyList)
    file.close()



#variables
archivo = open('datos.txt','r',encoding="utf-8");
personas =[];
#aqui asignas los valores del archivo a una lista 
for linea in archivo:
    personas.append(linea.rstrip("\n")) 

print('primer array')
print(personas);
print('----------------------------------------------')
print('')
print('Algoritmo')

# contador
#es el numero de datos del array
value =len(personas);
#contador para bombre de archivo
contador =0;     
  
#-----------------------Desarrollo------------------------------------  
while value >0:
    if len(personas)<5:
        removido =(random.sample(personas,k=len(personas)));
        print('vuelta');
    # print(value);
        print(removido);
        #choice = input("would you like to play again? y/n: ")
        if removido:
            print ("descuento")
            value = value-len(removido)
            print('resta esto',value);
            contador += 1
            print(contador);
            #crea nueva lista
            print('')
            print('Nueva lista')
            #esta es uba lista de compresion creas un array nuevo de esta forma
            personas = [ elem for elem in personas if elem not in removido];
            print(personas); 
            #Crea el archivo
            archivos(str(contador),removido,str(contador));
            print('')
    else:    
        removido =(random.sample(personas,k=5));
        print('vuelta');
    # print(value);
        print(removido);
        #choice = input("would you like to play again? y/n: ")
        if removido:
            print ("descuento")
            value = value-len(removido)
            print('resta esto',value);
            contador += 1
            print(contador);
            #crea nueva lista
            print('')
            print('Nueva lista')
            #esta es uba lista de compresion creas un array nuevo de esta forma
            personas = [ elem for elem in personas if elem not in removido];
            print(personas); 
            #Crea el archivo
            archivos(str(contador),removido,str(contador));
            print('')
     

