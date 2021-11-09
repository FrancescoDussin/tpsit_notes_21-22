#TITLE: 2021-10-12: Miniserver http con netcat
#DEADLINE: Aperto martedì, 12 ottobre 2021, 00:00 Data limite sabato, 16 ottobre 2021, 14:00
#TASK: Realizzare un miniserver con il linguaggio di programmazione a propria scelta che implementi un mini server web.
# Si accetta lo standard out da un qualsiasi programma.
# Il modulo di aggiunta degli header va implementato.
# netcat va usato come interfaccia alla rete/socket.
#EXTRA: prevedere l'usita compressa e inserire nella pipe dei programmi gzip

#LIMITS: Consegnare massimo 3 file
#(shell script che compone tutto, programma personale, eventuale altro) -q 1

#COMMANDS TO USE:
# cowsay -SANDU- > filecs.txt
# cowsay -SANDU- | nc -l -p 7500
# date > filecs.txt | python3 cowsaypipehttp.py | nc -l -p 7500 

import sys
from typing import Counter
import os

if __name__ == '__main__':

#OPENING FILE

    my_file = open("filecs.txt","w+")

#WRITING TO FILE

    print("use command: cowsay -text- > filecs.txt")
    client_input = str(input())
    os.system(client_input)

#READ AND COUNT CHAR FROM FILE

    counter_input = my_file.read()
    counter_file = len(counter_input)
    print(counter_file)

#CLOSE FILE

    my_file.close()

#COMMAND PIPE PASSING TO BROWSER

    temp_var = 'HTTP/1.1, 200'
    print(temp_var)

    print(counter_input)