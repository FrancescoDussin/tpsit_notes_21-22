# Realizzare un programma che, utilizzando la libreria os, svolga le seguenti funzioni:

#     Stampare il pid del processo corrente
#     Stampare il pid del processo padre
#     Stampare il nome del sistema operativo in uso
#     Stampare la directory corrente, tornare indietro di una cartella e stampare nuovamente la directory corrente
#     Crea una directory con nome "prova"
#     Stampare i file presenti nella cartella home
#     Aprire un file nuovo in scrittura chiamato "testo.txt" e inserire il nome della cartella corrente

import multiprocessing
import random
import time
import sys
import os
  

# def create_directory():
c_directory = "prova"
parent_dir = "/home/local/FERMI/s01689/Scrivania"
path = os.path.join(parent_dir, c_directory)
os.mkdir('path')
print("Directory '% s' created" % c_directory)

print(os.startfile(path, operation = 'print'))