# Author: Dussin Francesco 5Ai

# Title: Miniserver con digestione GET e POST

# Started: Aperto giovedì, 14 ottobre 2021, 00:00
# DeadLine: Data limite giovedì, 21 ottobre 2021, 00:00

# Task: Realizzare un miniserver con il linguaggio di programmazione a propria scelta che implementi un mini server web.

# Limits: netcat va usato come interfaccia alla rete/socket.
# Il miniserver deve intercettare in chiamata http i parametri passati in GET e POST e riproporli in pagina di uscita.

############################ notes from yt: 
# https://www.youtube.com/watch?v=qriL9Qe8pJc
# https://zetcode.com/python/requests/
# http get request -> https://httpbin.org/
# NON devono essere utilizzate per informazioni/dati sensibili
# utilizzato per ricevere DATA da una lista

# query string = ? il (?) per iniziare il (=) per assegnare
# esempio -> https://httpbin.org/get?name=Francesco&lastname=Dussin
# http post request ->
# utilizzato per inviare data da un form html
# uploadare files
# designed per creare e inviare files e dati sensibili

# starting point ->

import requests as req
import sys
from typing import Counter
import os

if __name__ == '__main__':

    #load = { "firstName": "Francesco", "lastName": "Dussin"}
    #r = requests.get("https://httpbin.org/get", params=load)
    #resp = req.get("http://127.0.0.1:5500/tpsitgetpost/tpsitgetpostform.html")
    #print(resp.text)

    resp = req.request(method='GET', url="http://127.0.0.1:5500/tpsitgetpost/tpsitgetpostform.html")
    print(resp.text)


# #!/usr/bin/env python3

# import requests as req
# import re

# resp = req.get("http://www.webcode.me")

# content = resp.text

# stripped = re.sub('<[^<]+?>', '', content)
# print(stripped)

    # print(r.url) #print url
    # print(r.status_code) #200 succesful request
    # print(r.text) #la libreria requests 'decoda' returnera il 'body basandosi sugli headers http passati all'header http
    
    # r = requests.post("https://httpbin.org/post", params=load) #params/data
    # #la keyword data transformera la conversione del dictionary paylaod

    # # quando utiliziamo l'http post protocol, i parametri non sono url codificati come nella get
    # # il dictionary passato tramite la post request è inviata al nostro server e
    # # viene mostrata nel object FORM all'interno del body

    #!/bin/python3

import os
import sys
#!/bin/python3

import os
import sys
import fileinput

    #GET /?nome=fdjdfjfg HTTP/1.1
    #nc.traditional -l -v -p 7500 -c " python3 getpost.py"

print("HTTP/1.1 200 OK")
print("Content-Type: text/html")
print("Content-Type: text/plain")
print("Connection: keep-alive")
print()
print("<ul>")
print("")
print("</ul>")