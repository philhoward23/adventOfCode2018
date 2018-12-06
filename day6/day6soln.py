#part 1
#find closest input point to each element of a grid, then identify which input point is closest to most elements, excluding elements which are closest to the boundary
import numpy as np

day6input=open("input.txt")
input = day6input.readlines()
#50 points

#identify bounding rectagle for all points
#assume no duplicates, valid input etc
points = [ [int(coord) for coord in line.strip().split(',') ] for line in input]

xmin = min(x[0] for x in points)
xmax = max(x[0] for x in points)
ymin = min(x[1] for x in points)
ymax = max(x[1] for x in points)
#41,357,40,358

#manhattan distance
def manhat(a,b):
	return(abs(a[0]-b[0]) + abs(a[1]-b[1]))

def closest_point(coord,comparisons):
	#return index of closest point to coord from list, list of indices for ties
	mindist = -1
	minindex = []
	tie = False
	for index, point in enumerate(comparisons):
		dist = manhat(coord,point)
		if (dist < mindist) or (mindist == -1):
			mindist = dist
			minindex = [index]
			tie = False
		elif dist == mindist:
			minindex.append(index)
			tie = True
	return(minindex)



#assign a closest point (1 to 50, 0 if a tie) for all points in the bounding rectangle and count area closest to each 
#any point outside bounding triangle have a unique closest point on the bound so all boundary points are in an infinite area
area = [0 for x in range(50)]
boundaries = [0 for x in range(50)]
for x in range(41,357):
	for y in range(40,358):
		closest = closest_point((x,y),points)
		#ignore ties
		if len(closest) == 1:
			area[closest[0]] += 1
		#assign boundaries
		if (x in (41,357)) or (y in (40,358)):
			for item in closest:
				boundaries[item] = 1

#check largest area not on boundary
max(zip(area,boundaries))
#4771

#part 2	
#find the size of the region containing all locations which have a total distance to all given coordinates of less than 10000

#50 points total so region cannot extend more than 10000/50 = 200 beyond boundary points defined above
def total_dist(coord,comparisons):
	#return sum of distances between coord and comparisons
	total = sum([manhat(coord,point) for point in comparisons])
	return(total)



area = 0
for x in range(-150,560):
	for y in range(-150,560):
		if total_dist((x,y),points) < 10000:
			area += 1
#39149





