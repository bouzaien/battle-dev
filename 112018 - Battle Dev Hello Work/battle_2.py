#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def magic(word):
	c1 = len(word) in range(5,7+1)
	c2 = ord(word[0]) - ord(word[1]) == -1
	c3 = word[-1] in ['a', 'e', 'i', 'o', 'u', 'y']
	return (c1 and c2 and c3)

words = []

for word in lines[1:]:
	if magic(word):
		if word not in words:
			words.append(word)

sys.stdout.write(str(len(words)) + '\n')