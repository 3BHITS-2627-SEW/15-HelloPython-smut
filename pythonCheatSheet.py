# Cheatsheet für python

# Variablen

eineVariable = 13

print("eineVariable: ", eineVariable)

eineVariable = "blablabla"

print("eineVariable: ", eineVariable)

# Typisierung in Py: Ducktyping

# Daher: bitte immer nach Möglichkeit typisieren

eineZweiteVariable : int = 14

print("eineZweiteVariable: ", eineZweiteVariable*3)

eineZweiteVariable = "text"
#Gibt aus: texttexttext
print("eineZweiteVariable: ", eineZweiteVariable*3)

# Datentyp von variable bekommen
datentyp = type(eineVariable)
print("Datentyp von eineVariable:", datentyp)

eineVariable = 15

datentyp = type(eineVariable)
print("Datentyp von eineVariable:", datentyp)

# formatierte Ausgabe:
print(f"")

einText = f"{eineVariable} Hilft mit nicht viel weiter"


# eingaben von der command line

einedritteVariable = input("Geb einne Zahl ein: ")

# Stringumwandlung 
einString = str(einedritteVariable)

alternativText = "Die Zahl ist: " + einString

print(alternativText)