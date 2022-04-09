from time import sleep
from sys import stdout

output = ""
for c in "Mordor Gandalf,|| is it left| or right?":
    sleep(0.05)
    if (c == "|"):
        sleep(0.5)
    else:
        output += c
        stdout.write("\r" + output)
sleep(3)
stdout.write("\r" + (" " * len(output)) + "\r")