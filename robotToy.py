from numpy import array


"""The solution was developed using Python 3"""

class Robot(object):
	"""A Toy Robot. The class takes input and processes the command

	Attributes:
		isPlaced: Flag to indicate if the Robot has been placed on the table.
		location: 2 Dimensional co-ordinate of the robots position on the table.
		direction: String mentioning which way the robot is facing
		max_X: Size of the Table in X axis
		max_Y: Size of the Table in Y axis
	"""
	
	max_X=5
	max_Y=5
	
	"""Initializes Robot with location and direction"""
	def __init__(self, location=array([0,0]), direction = 'NORTH'):
		
		
		self.isPlaced=0
		self.location=location
		self.direction = direction
		
	"""This method shows the location of the robot"""
	def displayLocation(self):
		print (self.location[0],',',self.location[1],',',self.direction)
	
	"""Initalizes the robot placement"""
	def setPlaced(self):
		self.isPlaced = 1
	
	"""To check if the robot has been placed"""
	def getPlaced(self):
		return self.isPlaced
	
	"""To place the robot with co-ordinate and direction"""
	def placeRobot(self, locX, locY, direction):
		self.isPlaced=1
		self.location[0]=locX
		self.location[1]=locY
		self.direction = direction
	
	"""get input and process command"""
	def robotInput(self, command):
		command=command.replace(" ","")
		if command.find('PLACE')!=-1:
			self.placeCommand(command)
		else:
			if self.isPlaced==0:
				print("Sorry! Robot not intialized! Please place in an initial position")
			else:
				self.processCommand(command)
	
	"""TO process comman relating to placement"""
	def placeCommand(self, command):
		
		command=command.replace("PLACE","")
		locArray = command.split(",")
		if len(locArray)>=3:
			isError = 0
			locX = 0
			locY = 0
			if len(locArray)>3:
				print("You provided way too many info! Only gonna take the first 3.")
			if locArray[0].isdigit():
				locX=int(locArray[0])
			else: 
				print ("Entered Incorrect Info!")
				isError = 1
			
			if locArray[1].isdigit():
				locY=int(locArray[1])
			else: 
				print ("Entered Incorrect Info!")
				isError = 1
			
			tempDirection=locArray[2]
			
			if isError==0:
				if int(locX)>=0 and int(locX)<=int(self.max_X) and int(locY)>=0 and int(locY)<=int(self.max_Y):
					if tempDirection == 'EAST' or  tempDirection == 'WEST' or  tempDirection == 'NORTH' or  tempDirection == 'SOUTH':
						self.setPlaced()
						self.placeRobot(locX, locY, tempDirection)
					else:
						print(tempDirection+"! What direction is that?")
				else:
					print("The table is not that big!")
		else:
			print("You didn't input all required information!")
	
	"""TO process all comman except for Placement"""
	def processCommand(self, command):
		command=command.replace(" ","")
		locX = self.location[0]
		locY = self.location[1]
		tempDirection = self.direction
		
		if command=='LEFT':
			if tempDirection == 'NORTH':
				tempDirection = 'WEST'
			elif tempDirection == 'WEST':
				tempDirection = 'SOUTH'
			elif tempDirection == 'SOUTH':
				tempDirection = 'EAST'
			else:
				tempDirection = 'NORTH'
			
		elif command=='RIGHT':
			if tempDirection == 'NORTH':
				tempDirection = 'EAST'
			elif tempDirection == 'EAST':
				tempDirection = 'SOUTH'
			elif tempDirection == 'SOUTH':
				tempDirection = 'WEST'
			else:
				tempDirection = 'NORTH'
			
		elif command=='MOVE':
			if tempDirection == 'NORTH':
				locY=int(locY)-1
			elif tempDirection == 'EAST':
				locX=int(locX)+1
			elif tempDirection == 'SOUTH':
				locY=int(locY)+1
			else:
				locX=int(locX)-1
		elif command=='REPORT':
			self.displayLocation()
		else:
			print ("Command not recognized!")
		
		if int(locX)>=0 and int(locX)<=int(self.max_X) and int(locY)>=0 and int(locY)<=int(self.max_Y):
			self.placeRobot(locX, locY, tempDirection)
		else:
			print("I'm not gonna jump bro!")

"""Function to receive input"""
def setInput():      
	n = input("Input your command: ")     
	return n  
	
def main():     
	"""Initialize Robot"""
	rbt1 = Robot(array([0,1]),'SOUTH')
	
	"""Loop user input until quit/exit command"""
	isExit=0
	while isExit==0:
		command = setInput().upper()
		if command == 'QUIT' or command == 'EXIT':
			break
		rbt1.robotInput(command)

if __name__== "__main__":
  main()