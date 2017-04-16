from sys import exit

class scene(object):
	def __init__(self):
		self.description = []
		self.name =[] 
	def load_story(self,scene_name):
		self.name=map_0.scene_change_name(scene_name)
		self.description=map_0.scene_story(scene_name)
	def	arrive(self):
		print "\n","-"*15,self.name,"-"*15,"\n"
		print self.description
	def leave(self):
		print "I am about to leave now"
		target=raw_input("Where shall I go? > ") 
		target = map_0.scene_check(target)
		print "I am leaving %s" % self.name
		return target
class room_0(scene):
	def __init__(self):
		pass
	def enter(self,scene_name):
		self.load_story(scene_name)
		self.arrive()
		print "I find myself in %s, I have seen something" % self.name
		raw_input()
		print "I have done this and that"
		target=self.leave()
		return target

class room_1(scene):
	def __init__(self):
		pass
	def enter(self,scene_name):
		self.load_story(scene_name)
		self.arrive()
		print "I am now in %s, I have seen something" % self.name
		raw_input()
		print "I have done this and that"
		target=self.leave()
		return target
		
		
class end_good(scene):
	def __init__(self):
		pass
	def enter(self,scene_name):
		self.load_story(scene_name)
		print "\n","="*15,"Congratulations! You Win!!","="*15,"\n"
		exit(1)		

class end_bad(scene):
	def __init__(self):
		pass
	def enter(self,scene_name):
		self.load_story(scene_name)
		print "\n","="*15,"You lose! Good luck next time!","="*15,"\n"
		exit(1)
		
class scene_map(object):
	init_scene = "room_0"
	# story for each scene
	story ={
		"room_0":"central_corridor story",
        "room_1":"laser_weapon_armory story, very long",
        "room_2":"the_bridge, kind of long ",
        "exit":"escape! finally!!",
        "end_bad":"Very sorry to see you here"
        }
	
	fancy_scenes ={
		"room_0":"central_corridor",
        "room_1":"laser_weapon_armory",
        "room_2":"the_bridge",
        "exit":"escape_pod",
        "end_bad":"END..."
        }
	#exchange string to syntax in code
	synt_scenes = {
	"room_0": room_0(),
	"room_1": room_1(),
	"exit": end_good(), #win
	"end_bad": end_bad() #lose
	}
	def __init__(self):
		pass
	def scene_open(self,scene_name):
		print "running scene_open, scene_name = ", scene_name,"\n..."
		return self.synt_scenes.get(scene_name)
	def scene_change_name(self,scene_name):
		print "running scene_change_name, scene_name = ", scene_name,"\n..."
		return self.fancy_scenes.get(scene_name)
	def scene_story(self,scene_name):
		print "running scene_story, scene_name = ", scene_name,"\n..."
		return self.story.get(scene_name)
	def scene_check(self,scene_name):
		j=3 #3 time trial error input
		for i in range (0,100):
			print "running scene_check, recieve scene_name = ", scene_name, "\n..."
			if scene_name in self.synt_scenes:
				print "scene_name found, proceesing\n..."
				return scene_name
			else:
				if i > j-2: break
				print "location not found, proceesing\n..."
				print "please try it again! (%d times left)" % (j-i-1)
				scene_name = raw_input("> ") 
			i+=1
		print "too much error! I quit!"
		exit()

class engine(object):
	def __init__(self,scene_map):
		self.scene_map=scene_map
	def play(self):
		print "\n","="*15,"engine running! Ready to start!","="*15,"\n"
		scene_name=scene_map.init_scene #set scene_name to init_scene
		print "initial scene_name =", scene_name
		for i in range(0,100): #maxium 99 run of system
			i+=1
			cur_scene=self.scene_map.scene_open(scene_name) #set cur_scene to an instance of class specified by scene_name
			scene_name = cur_scene.enter(scene_name) #from cur_scene call function enter, get the next valid target and set to scene_name
			
		print "I am tired, let's do it later, engine stop!"
		
	
map_0 = scene_map()
game = engine(map_0)
game.play()
