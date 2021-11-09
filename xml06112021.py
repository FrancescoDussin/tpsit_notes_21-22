#NOZIONI
    #xml -> (generalizzazione di hmtl e sgml) è un linguaggio gerarchico ( + padre - figli e niente nipoti)
        #alcuni tag non ammettono all'interno di essi specifici tag.
        #serializzazione = prende tutte le zone di memoria che riguardano l'oggetto e trasformarlo in XML
        #
    #sgml -> utilizza i tag come html (mark up language) ex. <b> ciao <i> da </b> duss </i> (blocchi compenetrati)
    #hmtl -> 
    #xhtml -> evoluzione di html (riformulazione di html 4.01 e xml 1.0)
    #html5 -> 
    #il DTD serve ad un parser per controllare la qualità del documento

#ESERCIZIO
    # Digestore xml di m0n0wall
    # Aperto sabato, 6 novembre 2021, 00:00
    # Data limite sabato, 13 novembre 2021, 00:00
    # Con il linguaggio di programmazione a propria scelta, strutturare un programma che permetta di avere:
    #     nome
    #     dominio
    #     elenco delle interfacce, con alcuni dettagli
    # da un file xml specificato come parametro da riga di comando
    # Consegnare solo il programma.

    #strutturare con un linguaggio a piacere, si deve poter estrarre le informazioni dal file di configurazione del monowall 
    #task: estrarre -> hostname - dominio - elenco interfacce
    #(si possono usare tutte le librerie predisposte alla manipolazione dei dati)

#AUTHOR
    #Francesco Dussin
    #5Ai
    #XML PARSER

#importing the library
import xml.etree.ElementTree as ET

#passing the xml file to the python program
#m0n0xml_file = 'xmlexample06112021.xml'

#reading the file with ElementTree
tree = ET.parse('/home/local/FERMI/s01689/Scrivania/tpsit/06112021/xmlconsegna/xmlexample06112021')
root = tree.getroot()

for i in root.findall('system'):
    for j in i.findall('hostname'):
       print("%s" % (j.text))
    for d in i.findall('domain'):
       print("%s" % (d.text))

for i in root.findall('interfaces'):
       print("%s" % (i.text))