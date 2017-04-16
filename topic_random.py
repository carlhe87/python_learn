import random

def devide(people=2,mode="r"):
	share,devide=[],[]
	if mode =="r":
		for i in range(people-1):
			devide.append(random.uniform(0, 1))

		devide =sorted(devide)
		#print "sorted devide=", devide

		share.append(devide[0])
		for i in range(1, people-1):
			share.append(devide[i]-devide[i-1])
		share.append(1-devide[people-2])

		return share
		
	elif mode == "e":
		for i in range(people):
			share.append(1.0/(people))	
		return share
	else: return ValueError
	

def deliver(people,mode,total):
	actual=[]
	for item in devide(people,mode)[:]:
		actual.append(round((total * item),2))
	return actual

def input_interface():
	people,mode,total = 3,"r",1
	people=int(raw_input("please input num of people:"))
	#mode=raw_input("random mode? default random")
	total=int(raw_input("please input total amount of money:"))
	return (people,mode,total)

	
list = deliver(*input_interface())

print "\n"*10,"Here is the list"
for item in list:
	print item

