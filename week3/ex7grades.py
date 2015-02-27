#Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

nota = raw_input ("Introduce tu nota: ")
try:
	nota = float(nota)
except:
	nota = -1
	print "No es un numero"
	exit()

if nota>float(1) or nota<float(0.0):
	print "No es un formato valido, introduce un rango del 0.0 al 1.0"	
	exit ()
	
if nota>=0.9:	
	print "A. "
elif   nota>=0.8:
	print "B "
elif   nota>=0.7:
	print "C. "
elif   nota>=0.6:
	print "D. "
elif   nota<0.6:
	print "F. "
  

	
