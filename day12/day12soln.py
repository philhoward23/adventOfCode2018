#part 1
#cellular automaton

day12input=open("input.txt")
input = day12input.readlines()

right = input[0].strip().split()[2]

left = '....'

rules = {line.strip().split()[0]:line.strip().split()[2] for line in input[2:]}

#apply rules to each element of the string, taking care around right left divide

def generation(rules, left, right):
    max_right = len(right)
    max_left = len(left)
    next_right = ''
    next_left = ''
    for element in range(max_right):
        if element == 0:
            pattern = left[-2:]+right[:3]
        elif element == 1:
            pattern = left[-1]+right[:4]
        elif element == max_right-1:
            pattern = right[-3:]+'..'
        elif element == max_right-2:
            pattern = right[-4:]+'.'
        else:
            pattern = right[element - 2:element + 3]
        next_right += rules[pattern]
    #see if string should be extended
    if rules[right[-1]+'....'] == '#':
        if rules[right[-2:]+'...'] == '#':
            next_right += '##'
        else:
            next_right += '.#'
    elif rules[right[-2:]+'...'] == '#':
        next_right += '#'
    #left
    for element in range(max_left):
        if element == 0:
            pattern = '..'+left[:3]
        elif element == 1:
            pattern = '.'+left[:4]
        elif element == max_left-1:
            pattern = left[-3:]+right[:2]
        elif element == max_left-2:
            pattern = left[-4:]+right[0]
        else:
            pattern = left[element - 2:element + 3]
        next_left += rules[pattern]
    #see if string should be extended
    if rules['....'+left[0]] == '#':
        if rules['...'+left[:2]] == '#':
            next_left = '##' + next_left
        else:
            next_left = '#.' + next_left
    elif rules['...'+left[:2]] == '#':
        next_left = '#' + next_left
    return(next_left,next_right)
    #

#iterate for n generations
def n_generations(n,rules, left, right):
    for x in range(n):
        left, right = generation(rules, left, right)
        print left, right
        if x % 100 == 0:
            print x
    return(left,right)

left_20, right_20 = n_generations(20,rules, left, right)

sum(i for i, char in enumerate(right_20) if char == '#') - sum(i+1 for i, char in enumerate(left_20) if char == '#')
#2995

#part 2
#do 50000000000 iterations
#rewrite as dictionary, perhaps?
plants = {i:char for i, char in enumerate(right)}
plants_min = 0
plants_max = len(plants)

def generation(rules, plants, plants_min, plants_max):
    last_two, last_one = '.','.'
    plants_min_new = plants_min
    plants_max_new = plants_max
    #see if should be extended left
    if rules['...'+plants[plants_min]+plants[plants_min+1]] == '#':
        last_one = '#'
        plants_min_new = plants_min - 1
    if rules['....'+plants[plants_min]] == '#':
        last_two = '#'
        plants_min_new = plants_min - 2
    #iterate over current generation
    for element in range(plants_min,plants_max):
        if element == plants_min:
            pattern = '..'+plants[plants_min]+plants[plants_min+1]+plants[plants_min+2]
        elif element == plants_min+1:
            pattern = '.'+plants[plants_min]+plants[plants_min+1]+plants[plants_min+2]+plants[plants_min+3]
        elif element == plants_max-1:
            pattern = plants[plants_max-3]+plants[plants_max-2]+plants[plants_max-1]+'..'
        elif element == plants_max-2:
            pattern = plants[plants_max-4]+plants[plants_max-3]+plants[plants_max-2]+plants[plants_max-1]+'.'
        else:
            pattern = plants[element-2]+plants[element-1]+plants[element]+plants[element+1]+plants[element+2]
        #update element that won't be used again this loop
        if (element == plants_min) and (last_two == '#'):
            plants[element-2]=last_two
            plants[element-1]='.' #placeholder so full range populated
        elif (element == plants_min+1) and (last_two == '#'):
            plants[element-2]=last_two
        elif element >= plants_min+2:
            plants[element-2]=last_two
        last_two, last_one = last_one, rules[pattern]
    #see if should be extended right
    if rules[plants[plants_max-1]+'....'] == '#':
        plants[plants_max] = '.' #placeholder so full range populated
        plants[plants_max+1] = '#'
        plants_max_new = plants_max+2
    if rules[plants[plants_max-2]+plants[plants_max-1]+'...'] == '#':
        plants[plants_max] = '#'
        plants_max_new = max(plants_max_new,plants_max+1)
    #update last two elements
    plants[plants_max-2]=last_two
    plants[plants_max-1]=last_one
    return(plants_min_new,plants_max_new)
    #

#iterate for n generations
def n_generations(n,rules,plants,plants_min,plants_max):
    for x in range(n):
        plants_min,plants_max = generation(rules, plants, plants_min, plants_max)
        print sum(i for i in plants if plants[i] == '#')
        if x % 100 == 0:
            print 'counter', x
    return(plants_min, plants_max)

plants = {i:char for i, char in enumerate(right)}
plants_min = 0
plants_max = len(plants)

plants_min_20, plants_max_20 = n_generations(20,rules, plants, plants_min, plants_max)

sum(i for i in plants if plants[i] == '#')
#2995

plants = {i:char for i, char in enumerate(right)}
plants_min = 0
plants_max = len(plants)

plants_min_50, plants_max_50 = n_generations(50,rules, plants, plants_min, plants_max)

sum(i for i in plants if plants[i] == '#')

#50k
plants = {i:char for i, char in enumerate(right)}
plants_min = 0
plants_max = len(plants)

plants_min_50000, plants_max_50000 = n_generations(50000,rules, plants, plants_min, plants_max)

sum(i for i in plants if plants[i] == '#')
#too slow

plants = {i:char for i, char in enumerate(right)}
plants_min = 0
plants_max = len(plants)

plants_min_1000, plants_max_1000 = n_generations(1000,rules, plants, plants_min, plants_max)
#pattern fixed but shifting one to right after some early dynamics
#1000 generations -> 55800, seems increments 54 each time since 54 values are '#'
55800 + (50000000000-1000)*54





