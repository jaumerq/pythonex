inp = raw_input ("Introduce las horas que has trabajado: ")
try:
	inp = float(inp)
except:
	inp = -1
if inp>0:
	print "Buen trabajo, prosigamos . "
else:
	print "No es un numero. "
	
hours = float(inp)

if hours>=40:
	hours=40+((hours-40)*1.5)
	
inp = raw_input("Introduce euros hora ")

try:
	inp = float(inp)
except:
	inp = -1
if inp>0:
	print "Buen trabajo ahora te lo calculamos. "
else:
	print "No es un numero. "

rate = inp
pay = rate*hours
print pay
