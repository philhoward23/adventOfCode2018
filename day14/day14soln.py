#part 1
#iterate recipes 
#input
iterations = 260321

scores = [3,7]

elves = [0,1]

def add_new_recipes(elves, scores):
    new = scores[elves[0]]+scores[elves[1]]
    for digit in str(new):
        scores.append(int(digit))

def pick_new_recipes(elves,scores):
    for i, recipe in enumerate(elves):
        elves[i] = (recipe + 1 + scores[recipe]) % len(scores)

def step(elves, scores):
    add_new_recipes(elves, scores)
    pick_new_recipes(elves, scores)

def n_steps(n,elves,scores):
    for x in range(n):
        step(elves,scores)

def find_nth_recipe(n,elves,scores):
    found = False
    while not found:
        step(elves,scores)
        if len(scores) > n:
            found = True

find_nth_recipe(iterations+10, elves, scores)
''.join(str(i) for i in scores[iterations:iterations+10])
#9276422810

#part 2
#find sequence first appearance and index

def find_recipe_seq(seq,elves,scores):
    size = len(str(seq))
    found = False
    count = 0
    while not found:
        count += 1
        if count % 100000 == 0:
            print count, len(scores), elves
        step(elves,scores)
        if str(seq) in ''.join(str(i) for i in scores[-(size+1):]):
            found = True

scores = [3,7]
elves = [0,1]
find_recipe_seq(iterations,elves,scores)

