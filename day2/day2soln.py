#part 1
#calculate checksum as product of count of words that contain exactly two of any letter, with count of words that contain exactly three of any letter
day2input=open("input")
input = day2input.readlines()

def letter_counts(word):
	counts={}
	for letter in word:
		if letter in counts:
			counts[letter] += 1
		else:
			counts[letter] = 1
	return counts

def count_2_3(counts):
	if 2 in counts.values():
		if 3 in counts.values():
			return(1,1)
		else:
			return(1,0)
	else:
		if 3 in counts.values():
			return(0,1)
		else:
			return(0,0)

words_2_3 = [count_2_3(letter_counts(word.strip())) for word in input]
sum(x[0] for x in words_2_3) * sum(x[1] for x in words_2_3)


#part 2
#find words that are identical except for the letter in one position
#assume all input equal length and only one solution

def character_distance(word1,word2):
	#count of positions where the words have different characters
	return(sum(1 if x!=y else 0 for x,y in zip(word1,word2)))

found=False
for index, word in enumerate(input):
	for word2 in input[index+1:]:
		if character_distance(word,word2)==1:
			print word, word2
			found=True
			break
	if found:
		break

