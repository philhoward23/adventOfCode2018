day1input=open("input")
input = day1input.readlines()
sum(int(x.strip()) for x in input)


#part 2
freqs=set()
cumsum=0
dup=False

while not dup:
	for x in input:
		cumsum=cumsum+int(x.strip())
		if cumsum in freqs:
   		 	print(cumsum)
   		 	dup=True
   		 	break
  		else:
			freqs.add(cumsum)
		