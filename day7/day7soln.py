#part 1
#
import re

day7input=open("input.txt")
input = day7input.readlines()
#101 lines, one format

rules = [[line.strip().split()[x] for x in (1,7)] for line in input]

#build up dictionary of steps, what they come before
steps = {}

#also keep track of all steps that come after another, to find potential start steps and delay steps until all earlier ones are done
laters = {}

for rule in rules:
    earlier, later = rule[0], rule[1]
    if later in laters:
        laters[later].add(earlier)
    else:   
        laters[later] = set(earlier)
    if earlier in steps:
        steps[earlier].add(later)
    else:
        steps[earlier] = set(later)

#steps with no rule for preceding
current_options = set(steps.keys()) - set(laters.keys())
#Q, M, W, N
#
#steps with no rule for following      
set(laters.keys()) - set(steps.keys()) 
#D   



#build up list of steps in order, alphabetical breaking ties
ordered_steps = [] 

while len(current_options) > 0:
    #choose alphabetically next option as next step
    next_step = min(current_options)
    ordered_steps.append(next_step)
    current_options.remove(next_step)
    #add steps following current to options, if they don't need to come later than something else
    if next_step in steps:
        for later in steps[next_step]:
            if later in laters:
                #check if all steps that need to come before this have already been taken
                if len(laters[later] - set(ordered_steps)) == 0:
                    current_options.add(later)
            else:
                current_options.add(later)
            


''.join(ordered_steps)    
#'MNQKRSFWGXPZJCOTVYEBLAHIUD'
        
#
        
#part 2	
#each step takes 60s + position in alphabet of the letter
#5 workers available to work in parallel

#check second by second: current options, workers available, finished steps
timed_steps = [] 
workers = {}
for worker in ['a','b','c','d','e']:
    workers[worker] = {'step':'','finish_time':0}

current_options = set(steps.keys()) - set(laters.keys())

time = 0

while len(timed_steps) < 26:
    #keep track of what happens in this second
    
    #if a step finished, update list and current_options, free up worker
    just_finished = set()
    for worker in workers:
        if (workers[worker]['step'] != '') and (workers[worker]['finish_time'] == time):
            just_finished.add(workers[worker]['step'])
            workers[worker] = {'step':'','finish_time':0}
    
    while len(just_finished) > 0:
        #choose alphabetically next option as next step
        next_step = min(just_finished)
        timed_steps.append(next_step)
        just_finished.remove(next_step)
        #add steps following current to options, if they don't need to come later than something else
        if next_step in steps:
            for later in steps[next_step]:
                if later in laters:
                    #check if all steps that need to come before this have already been taken
                    if len(laters[later] - set(timed_steps)) == 0:
                        current_options.add(later)
                else:
                    current_options.add(later)
                
    
    
    #check if options available and assign if possible
    for option in range(len(current_options)):
        #choose alphabetically next option as next step to start work on
        next_step = min(current_options)
        #see if a worker is available to start work on it
        for worker in workers:
            if workers[worker]['step'] == '':
                #choose this one
                workers[worker]['step'] = next_step
                workers[worker]['finish_time'] = time + 60 + (ord(next_step) - 64)
                current_options.remove(next_step)
                break
    
    time += 1

''.join(timed_steps)    
#'MNQWKGRSFXZJPOCVTYEBLAHIUD'
print time - 1
 
   

