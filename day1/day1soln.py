#part 1
#sum signed integers
day1input=open("input")
input = day1input.readlines()
sum(int(x.strip()) for x in input)

#part 2
#repeatedly sum a list of signed integers until the sum is equal to a previous value for the first time
freqs=set([0])
cumsum=0
dup=False
repeatCount=0

while not dup:
	print repeatCount
	for x in input:
		cumsum=cumsum+int(x.strip())
		if cumsum in freqs:
   		 	print(cumsum)
   		 	dup=True
   		 	break
  		else:
			freqs.add(cumsum)
	repeatCount+=1
