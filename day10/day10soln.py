#part 1
#move lights in sky until they align
import re

day10input=open("input.txt")
input = day10input.readlines()

class Star(object):
    def __init__(self,id,x,y,xvel,yvel):
        self.id = id
        self.x = x
        self.y = y
        self.xvel = xvel
        self.yvel = yvel
    #
    def move(self):
        self.x = self.x + self.xvel
        self.y = self.y + self.yvel
        #
    def dist(self,x,y):
        #manhattan distance from a point
        return(abs(self.x - x) + abs(self.y - y))
    #

            
def input2star(line,id):
    params = re.split("[ ,<>]+",line.strip())
    #numpy array indices are opposite to definition in input so invert
    return(Star(id,int(params[1]),int(params[2]),int(params[4]),int(params[5])))


stars = {str(index):input2star(line,str(index)) for index, line in enumerate(input)}

#find if a star has a neighbour
def check_neighbours(stars,index):
    current = stars[index]
    for star in stars:
        if (star != index) and (current.dist(stars[star].x,stars[star].y) < 2):
            return(True)
    return(False)

#calculate fraction of stars with a neighbour, look if it's > 50%
def potential_match(stars):
    neighbours = 0
    total_stars = len(stars)
    for star in stars:
        if check_neighbours(stars,star):
            neighbours += 1
        if neighbours > total_stars/2:
            return(True)
    print neighbours
    return(False)


#move stars until a potential match is found
def pass_time(stars):
    for star in stars:
        stars[star].move()
    return(0)

def find_pattern(stars):
    match = False
    moves = 0
    while not match:
        pass_time(stars)
        match = potential_match(stars)
        moves +=1
        print moves
    return(0)

#stars start out very far apart, let's get them close before searching thoroughly
#380 stars
#star 0 starts at -41725, 10659 with velocity 4,-1
#star 1 starts at 10669, -31205 with velocity -1,3
#10,000 moves will bring them to -1725, 659 and 669,-1205

for x in range(10000):
    pass_time(stars)

find_pattern(stars)

#print to check message
xmin = min(stars[star].x for star in stars)
ymin = min(stars[star].y for star in stars)
xmax = max(stars[star].x for star in stars)
ymax = max(stars[star].y for star in stars)

import numpy as np 

space = np.zeros((ymax - ymin + 1, xmax - xmin + 1), dtype=int)
#update with star positions
for star in stars.values():
    space[star.y - ymin, star.x - xmin] = 1

for line in space:
    print ''.join([str(x) for x in line])
#PLBPGFRR

#part 2
#how many seconds did that take?

#10,000 + 465 + 2
#check with dist from input of star 1
star1check = input2star(input[1],'star1check')
moves = (stars['1'].x - star1check.x)/star1check.xvel
#10519, not sure where I lost some moves!


