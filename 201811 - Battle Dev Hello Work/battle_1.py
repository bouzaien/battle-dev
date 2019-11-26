#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/


import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

max = -1
winner = 'KO'

for line in lines[2:]:
	cost = int(line.split(' ')[0])
	if cost > max and cost > int(lines[1]):
		max = cost
		winner = line.split(' ')[1]

sys.stdout.write(winner + '\n')