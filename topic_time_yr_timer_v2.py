from datetime import datetime, timedelta
from mod_input_mtd import input_float, input_str
import time, winsound
from collections import deque #allow fast list.popleft

prgm_info =  "{:^35}\n\n{:^35}".format("Welcome to Yiran timer!","by Rabbit 2017 (c)")
sound_lib = {
	"cheer" : ["yr_cheerup.wav", "I Love You!", 7],
	"water" : ["yr_rabbit.wav", "Water yourself!", 10],
	"end" : ["yr_exercise.wav", "Move your body!", None],
	"add_ring" : ["filename.wav", "additional ring", 0],
	"sys_step" : [None, None, 1],
	"sys_period" : [None, None, 20],
	} #sound library
	
sound_queue = deque([]) # elms: 3-elm <tuple> ("file name","message",frequecy)

#set timing interval
def setting():
	"""take various parameters"""
	pg_clear(4)
	print "Do you wish to modify parameters? (Y/N)"
	print "\nEnter Y to set parameters"
	print "Press ENTER to skip (default)"

	if raw_input() == "Y":	
		#timer setting
		sound_lib["sys_period"][2] = input_float("\ntotal time [min]:", sound_lib["sys_period"][2])
		sound_lib["sys_step"][2] = input_float("\nrefresh frequency [sec]:", sound_lib["sys_step"][2])

		#ring setting
		sound_lib["cheer"][2] = input_float("\nset cheer frequency [min]:", sound_lib["cheer"][2])	
		sound_lib["water"][2] = input_float("\nset water frequency [min]:", sound_lib["water"][2])
	
	#additional ring setting
	add_ring = sound_lib["add_ring"][2]
	if not add_ring:
		print "\n\nDo you wish to Add an additional ring ? (Y/N)"
	if add_ring:
		print "\n\nDo you wish to Edit the additional ring ? (Y/N)"
	print "\nEnter Y to set new ring"
	print "Press ENTER to skip (default)"	
	if raw_input() == "Y":	
		try:
			tmp_input = input_str("\nPlease enter file name:", sound_lib["add_ring"][0])	
			if len(tmp_input) < 2:
				print "invalid string, take default"
			else: 
				sound_lib["add_ring"][0] = tmp_input
			tmp_input = input_str("\nPlease enter display info:", sound_lib["add_ring"][1])	
			if len(tmp_input) < 1:
				print "invalid string, take default"
			else:
				sound_lib["add_ring"][1] = tmp_input
			add_ring = input_float("\nSet ring frequency [min]: (set 0 to switch OFF)", 0)	
			if add_ring < 0:
				print "invalid value, take default"
				add_ring = 0
			else: 
				sound_lib["add_ring"][2] = add_ring
			
			pg_line()
			if add_ring:
				print "\nAdditional ring switched ON!\n"
			else:
				print "\nAdditional ring switched OFF!\n"
			pg_line()
		except:
			print "\nError occurs during setting\n"
			sound_lib["add_ring"][2] = 0
		
		raw_input("\n\nPress ENTER to continue\n")
		
	return (sound_lib["sys_period"][2],sound_lib["sys_step"][2],sound_lib["cheer"][2],sound_lib["water"][2],sound_lib["add_ring"][2])
	
#sound system
def play_sound(sound = "\a"):
	try:
		winsound.PlaySound(sound, winsound.SND_FILENAME)
		return
	except:
		print "\a"

def play_queue(queue=[]):
	"""play all sound in a queue
		
		first-in, first-out
	"""
	#play sound_queue from left till depletion
	while queue:
		elm = queue.popleft() #elm --> ("file name","message",frequency)
		pg_line()
		print "\n{:^35}\n".format(elm[1]) # show prompt
		pg_line()
		play_sound(elm[0])		
	return

#udpate new sound to library by admin	
def update_sound_lib(key = "usr_key", sound = None,
			prompt = "usr-defined sound", frequency = 15):
	sound_lib.update({key:(sound, prompt, frequency)})
	return

#load sound from library
def load_lib_sound_queue(key = ""):
	if key in sound_lib:
		sound_queue.append(sound_lib[key])
	else: 
		print "invalid key!"
lsq = load_lib_sound_queue

	
# time display	
def dsp_time(*arg):
	#unpack data
	period,time_remain = arg

	#convert period , time_remain to seconds
	tot = period * 60
	secs = time_remain.total_seconds()
	
	#generate percentage
	p = round((secs/tot)*100, 1) #1-digit float * 100%
	
	#generate (h,m,s)
	i = int(secs)
	h = i // 3600
	i %= 3600
	m = i // 60
	s = i % 60
	
	print "[hh:mm:ss] {:0>2}:{:0>2}:{:0>2}  {:<5}% remain".format(h,m,s,p)
	return 


	
# time core
def timer(period, step, cheer, water, add_ring=None):
	pg_clear()
	pg_line("=")
	print "Ready!"
	pg_line()
	print "Total time : {} min\nClock step : {} sec".format(period, step)
	print "\nCheer every {} min\nWater every {} min".format(cheer, water)
	if add_ring:
		print "\nAdditional ring every {} min".format(add_ring)
	pg_line()
	raw_input("\nPress ENTER to start!\n")
	
	now = datetime.now()
	alarm_time = now + timedelta(minutes = period)
	pg_line("-")
	print "\n{:12} : {} [hh:mm:ss]\n{:12} : {} [hh:mm:ss]\n".format("current time", now.strftime("%H:%M:%S"),"alarm time", alarm_time.strftime("%H:%M:%S")) 	
	pg_line("-")
	#actuator
	theta = timedelta(seconds = step)
	water_sec = water * 60
	cheer_sec = cheer * 60
	if add_ring:
		add_sec = add_ring * 60
	
	while 1:
		time_remain = alarm_time - datetime.now()
		if time_remain > 2 * theta: #not yet end till almost end
			dsp_time(period, time_remain)
			time_remain_sec = time_remain.total_seconds()
			if time_remain_sec % water_sec < step:
				lsq("water")
			if time_remain_sec % cheer_sec < step:
				lsq("cheer")
			if add_ring:
				if time_remain_sec % add_sec < step:
					lsq("add_ring")
			play_queue(sound_queue)
		else: # ready to end
			lsq("end")
			play_queue(sound_queue)
			break
		time.sleep(step) # set calculation interval to save CPU rate

def pg_clear(empty=30):
	print "\n"*empty
	
def pg_line(spacer = "-", length=35):
	print spacer * length

def pg_exit():
	if raw_input("\n\ntype 'exit' to quit, or press ENTER to restart\n") == "exit":
		return True
		
def main():
	while 1:
		pg_clear()
		pg_line("=")
		print prgm_info
		pg_line()
		timer(*setting())
		
		if pg_exit(): break
		
	pg_clear()
	pg_line()
	print "{:^35}\n\n{:^35}".format("End of Program","by Rabbit 2017 (c)") 
	pg_line()

#main	
main()


