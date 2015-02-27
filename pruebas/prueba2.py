stringraw = raw_input("Introduce un numero: ")

try:
    ival =int(stringraw)
except:
    ival=-1

if ival>0:
    print "Buen trabajo"
else:
    print "No es un numero HIJODEPUTA"
    
