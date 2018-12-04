#part 1
#find most popular sleep minute for guard with longest total sleep time
#ignore any bias due to some guards having more and/or longer shifts than others
import re
from datetime import datetime

day4input=open("input.txt")
input = day4input.readlines()
			
def process_input(line):
	params = re.split("\[|\] ",line.strip())
	timestamp = datetime.strptime(params[1],"%Y-%m-%d %H:%M")
	if params[2][:5] == "Guard":
		action = params[2].split()[1]
	else:
		action = params[2].split()[0]
	return(timestamp,action)

actions = [process_input(line) for line in input]

# take first element for sort
def take_first(elem):
    return elem[0]

# sort list with key
actions.sort(key=take_first)

#store total time sleeping by minute for each guard in a dictionary
guards = {}

#initialise guard id and sleep start and end times
guard=''
sleeptime=0
waketime=0

#assume we have all guard start times included in input and all sleeptimes have an endtime before the next guard comes on duty
for row in actions:
	#discard timestamp
	action=row[1]
	#check if new guard beginning shift
	if action[0] == '#':
		#make this guard current
		guard = action
		if guard not in guards:
			#initialise sleep times by minute
			guards[guard] = [0 for x in range(60)]
	elif action[0] == 'f':
		#falls asleep
		sleeptime = row[0].minute
	elif action[0] == 'w':
		#wakes
		waketime = row[0].minute
		#update minutes slept for current guard
		guards[guard][sleeptime:waketime] = [x+1 for x in guards[guard][sleeptime:waketime]]
	else:
		print row, "invalid input row"
		break

#find guard who sleeps the most total minutes
sleepiest = ('',0)
for guard in guards:
	sleeptime = sum(guards[guard])
	if sleeptime > sleepiest[1]:
		sleepiest = (guard,sleeptime)
#2351 with 451 minutes

#most popular minute for #2351 to sleep
max([(v,i) for i,v in enumerate(guards['#2351'])])
#40

#part 2	
#find minute for which a guard is most frequently asleep
#find guard who sleeps the most at one particular minute
sleepiest = ('',0,0) #id, times, minute
for guard in guards:
	sleepiesttime = max([(v,i) for i,v in enumerate(guards[guard])])
	if sleepiesttime[0] > sleepiest[1]:
		sleepiest = (guard,sleepiesttime[0],sleepiesttime[1])
#1997 at 20 past midnight, 15 times




