#part 1
#calculate total size of overlapping areas from list of rectangles
import re
import numpy as np

day3input=open("input.txt")
input = day3input.readlines()

class Rectangle(object):
	def __init__(self,id,index1,index2,index1length,index2length):
		self.id = id
		self.index1 = index1
		self.index2 = index2
		self.index1length = index1length
		self.index2length = index2length
    #
	def place(self,fabric):
		ymin = self.index1
		ymax = self.index1 + self.index1length
		xmin = self.index2
		xmax = self.index2 + self.index2length
		#
		fabric[ymin:ymax, xmin:xmax] = fabric[ymin:ymax, xmin:xmax] + np.ones((self.index1length,self.index2length), dtype=int)
	#

			
def input2rect(line):
	params = re.split("[ @,:x]+",line.strip())
	#numpy array indices are opposite to definition in input so invert
	return(params[0],int(params[2]),int(params[1]),int(params[4]),int(params[3]))


rectangles = [Rectangle(*input2rect(line)) for line in input]

#check maximum dimensions required
max([x.index1 + x.index1length for x in rectangles])
max([x.index2 + x.index2length for x in rectangles])
#10,000 is adequate

fabric = np.zeros((10000,10000), dtype=int)


for rectangle in rectangles:
	#print rectangle.id
	rectangle.place(fabric)

#count indices > 1
len(fabric[fabric>1])
#109785


#part 2	
#find the id of the rectangle that doesn't overlap any others
def check_place(rectangle,fabric):
	#only valid once all rectangles already placed
	ymin = rectangle.index1
	ymax = rectangle.index1 + rectangle.index1length
	xmin = rectangle.index2
	xmax = rectangle.index2 + rectangle.index2length
	#
	target = fabric[ymin:ymax, xmin:xmax]
	#return the number of overlapping indices
	return(len(target[target>1]))

for rectangle in rectangles:
	#print rectangle.id
	if check_place(rectangle,fabric) == 0:
		print rectangle.id
		break
#504





