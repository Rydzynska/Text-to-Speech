import festival
import time

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
     'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
     'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
     's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey', 
     'x':'x-ray', 'y':'yankee', 'z':'zulu', '.':'dot', ',':'comma', '!':'exclamation mark', 
     '?':"question mark"}

def speak_ICAO():
    target = raw_input("Enter a file name: ")
    fhand = open(target)
    text = fhand.read().lower()

    for char in text:
        speech = ""
        speech = d.get(char, char)

        festival.sayText(speech)

        if char == " ":
            time.sleep(1.5)
        else:
            time.sleep(0.5)

    return speech

speak_ICAO()