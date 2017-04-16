def input_int(prompt = "enter someting:", default = None):
	"""error proof int reader with default
		
		read user input for a int, require a default value
		input: 
			arg1 <str> is from raw_input
			arg2 <tbd> is default value
		output:
			return1 <int> normal output 
			return2 <int> take default value
			return3 None error message when no default value 
	"""
	#accept input
	try:
		return int(raw_input(prompt))
	except ValueError:
		if default != None:
			print "Note: Not an integer. Take the default value %d" % default
			return default
		else:
			print "Error! No default value provided."
			return None
		
def fibonacci_serie(n=None, max=None):
	"""Fibonacci serie generator
	
		generate Fibonacci serie 
		input: 2-member tuple
			arg1 n <int> is the element amount, default 30
			arg2 max <int> is the max amount, default 1E6
				note: a30 < 1E6 < a31
		output: a 3-element list 
			return1 <list> is the collection of fibonacci series in int
			return2 <str> is the brief intro of the series
			return3 <str> is the report of the operating message
	"""
	#output information
	intro = "\nFibonacci serie: \n\ta(0) = 0,\n\ta(1) = 1,\n\ta(n)=a(n-1)+a(n-2)\n"
	print intro

	
	#innitialize parameters
	default_n, default_max = 30, 1000000 # must be int
	if n == None:
		n = input_int("element number n (default %d): " % default_n, default_n)
	if max == None:
		max = input_int("maximum value (default %d): " % default_max, default_max)
		
	report = "n = %d, max = %d" % (n, max)
	error = ""
	error1 = """\n
		Warning! \n
		Only partial results below max number %d is recorded!
		""" % max	
	
	#main
	a, b = 0, 1
	result = [] # list to store result
	for i in range(1,n+1):
		a,b=b,a+b
		if a <= max:
			result.append(a)
		else: 
			error += error1 #append error 1 message to report
			break
	if error == "":
		report += "\nSuccessful!"  # normal report
	else:
		report += error
	return [result, intro, report]


def serie_print(s, info =[True, True], format = [20, 10,"- "]):
	"""serie printer + format
		
		print out serie in a eye plesant format
		required 
		arg1 s is required 2-element list 
			arg1.1 serie is the content itself
			arg1.2 rpt is the report from function
		arg2 info is a switch display info from funcion
			arg 2.1 is the introdution switch
			arg 2.2 is the the report switch 
		arg3 format is a parameter list 
			arg3.1 wid is the width of separating line default 20
			arg3.2 v is the separatnig line 
			arg3.3 spr is the type of separater
		later version may display the serie introduction
	"""
	
	serie,intro,rpt = s[:] #copy the input serie
	wid,vt,spr=format #unpack formatting list
	half_w = wid / 2 #define width of separting line
	
	#print serie
	if info[0]: print intro #intro from function
	print "=" * half_w,"start","=" * half_w #starting line
	for elm in enumerate(serie,1):
		print "a(%d)\t\b\b=" % elm[0], elm[1]
		if elm[0] % 10 == 0: print spr * half_w #separating line 
	print "=" * half_w, "end", "=" * half_w
	if info[1]: print rpt #report from function


# main
while 1:
	serie_print(fibonacci_serie())
	if raw_input("\npress 'enter' to continue, or type 'quit' to exit\n") == "quit": break
		


