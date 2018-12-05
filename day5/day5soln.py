#part 1
#remove adjacent instances of same letter from a word, where the instances have different capitalisation
#assume problem is well-posed ie order of removing instances is irrelevant 
import re

day5input=open("input.txt")
input = day5input.readlines()[0].strip()
#50,000 character string	

word = input
last_char = ''
new_word = ''
change_count = 0
clean_pass = 0

while clean_pass == 0:
	for letter in word:
		if (letter.lower() == last_char.lower()) & (letter.islower() != last_char.islower()):
			#remove from string
			new_word = new_word[:-1]
			change_count += 1
		else:
			#copy into temporary string
			new_word = new_word + letter
		#update last character
		if len(new_word) > 0:
			last_char = new_word[-1]
		else:
			last_char = ''
	if change_count == 0:
		#all changes found so exit
		clean_pass = 1
	else:
		#loop over current string to check for more changes
		#could optimise to start where first change from last loop was found
		print change_count
		word = new_word
		new_word = ''
		last_char = ''
		change_count = 0

len(word)
#12032

#part 2	
#find length of shortest word obtained by removing all of one letter then applying above contraction rule

#realised no loop needed since can update last_char to handle new matches as we go
def react(word,ignore=''):
	#print ignore
	last_char = ''
	new_word = ''
	for letter in word:
		if letter.lower() == ignore:
			pass
		elif (letter.lower() == last_char.lower()) & (letter.islower() != last_char.islower()):
			#remove from string
			new_word = new_word[:-1]
		else:
			#copy into temporary string
			new_word = new_word + letter
		#update last character
		if len(new_word) > 0:
			last_char = new_word[-1]
		else:
			last_char = ''
	return(len(new_word))

chars = [chr(x) for x in range(97, 123)]

word = input
min_length = -1
min_length_char = ''
for letter in chars:
	curr_length = react(word,letter)
	if (curr_length < min_length) or (min_length == -1):
		min_length = curr_length
		min_length_char = letter

print min_length, min_length_char
#11170




