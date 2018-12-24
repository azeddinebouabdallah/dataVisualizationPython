# Minion game 
string = input()

kevin = 0
stuart = 0

vowels= 'AEIOU'

for i in range(len(string)):
	if string[i] in vowels:
		kevin += len(string[i]-i)
	else :
		stuart += len(string[i] - i)

if kevin > stuart :
	print('Kevin', kevin)
elif stuart > kevin: 
	print('Stuart', stuart)
else :
	print('Draw')