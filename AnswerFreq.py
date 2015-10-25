import urllib.request

def print_12(answer_freq_12, letter_freq_12):
	'''
	Prints the AMC 12 data in a more easily readable format
	'''
	print('_________AMC 12_________')	
		
	for i in range(25):
		print('Problem {0}:'.format(i+1), end=" ")
		for j in range(5):
			print(answer_freq_12[i][j], end=" ")
		print()
			
	print('Total:', end=" ")	
	for i in range(5):
		print(letter_freq_12[i], end=" ")
	print()
		
def print_10(answer_freq_10, letter_freq_10):
	'''
	Prints the AMC 10 data in a more easily readable format
	'''
	print('_________AMC 10_________')	
		
	for i in range(25):
		print('Problem {0}:'.format(i+1), end=" ")
		for j in range(5):
			print(answer_freq_10[i][j], end=" ")
		print()
			
	print('Total:', end=" ")	
	for i in range(5):
		print(letter_freq_10[i], end=" ")
	print()
	
def map(i):
	'''
	Maps an answer choice (A, B, C, D, or E) to its numerical value. Returns 5 (signifying an error) if the input is not a possible answer choice.
	'''

	if i=='A':
		return 0
	if i=='B':
		return 1
	if i=='C':
		return 2
	if i=='D':
		return 3
	if i=='E':
		return 4
	return 5

def update(year, grade, test, prev_ans_freq, prev_let_freq):
	'''
	Updates answer frequencies, both by problem and overall. Takes in 5 values as input:
	Year: The year of the test
	Grade: Either 10 or 12, signifying the level of the test (AMC 10 or AMC 12)
	Test: Either 'A' or 'B', signifying the date of the test given (A-date or B-date)
	prev_ans_freq: Previous answer frequencies by problem
	prev_let_freq: Previous answer frequencies overall
	''' 

	url='http://artofproblemsolving.com/wiki/index.php/{0}_AMC_{1}{2}_Answer_Key'.format(year, grade, test)
	response=urllib.request.urlopen(url)
	html_str=str(response.read())
	
	idx=0
	
	'''
	Answer choices in the html are of the form <li>answer</li> or #. answer; account for both possibilities
	'''
	
	for i in range(len(html_str)-4):
		if(html_str[i:i+4] == '<li>'):
			if map(html_str[i+4]) > 4:
				continue
			if idx >= 25:
				continue
			prev_ans_freq[idx][map(html_str[i+4])] = prev_ans_freq[idx][map(html_str[i+4])] + 1
			prev_let_freq[map(html_str[i+4])] = prev_let_freq[map(html_str[i+4])] + 1
			idx = idx + 1
		size=len('{0}. '.format(idx+1))
		if(html_str[i:i+size] == '{0}. '.format(idx+1)):
			if map(html_str[i+size]) > 4:
				continue
			if idx >= 25:
				continue
			prev_ans_freq[idx][map(html_str[i+size])] = prev_ans_freq[idx][map(html_str[i+size])] + 1
			prev_let_freq[map(html_str[i+size])] = prev_let_freq[map(html_str[i+size])] + 1
			idx = idx + 1
	return (prev_ans_freq, prev_let_freq)

'''
Initializes answer_freq_10/12 to hold answer frequencies by problem, and letter_freq_10/12 to hold overall answer frequencies
'''
answer_freq_12=[[0]*5 for i in range(25)]
answer_freq_10=[[0]*5 for i in range(25)]
letter_freq_12=[0]*5
letter_freq_10=[0]*5
	
'''
Updates answer frequencies for tests after 2002
'''
for i in range(2002,2016):
	(answer_freq_12, letter_freq_12)=update(i, 12, 'A', answer_freq_12, letter_freq_12)
	(answer_freq_12, letter_freq_12)=update(i, 12, 'B', answer_freq_12, letter_freq_12)
	(answer_freq_10, letter_freq_10)=update(i, 10, 'A', answer_freq_10, letter_freq_10)
	(answer_freq_10, letter_freq_10)=update(i, 10, 'B', answer_freq_10, letter_freq_10)

print_12(answer_freq_12, letter_freq_12)
print_10(answer_freq_10, letter_freq_10)
