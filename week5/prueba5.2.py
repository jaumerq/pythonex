largest = None
smallest = None
while True:
    num = raw_input("Enter a number: ")
    if num == "done" : break
    try:
		num = int(num)
	except:
		num = -1
    print num

print "Maximum", largest
