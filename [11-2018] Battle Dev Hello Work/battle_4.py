#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
from itertools import permutations, combinations

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

N = int(lines[0])

# d = {i:[(int(lines[i+1].split(' ')[0]), int(lines[i+1].split(' ')[0])+60), (int(lines[i+1].split(' ')[1]), int(lines[i+1].split(' ')[1])+60)] for i in range(1,N+1)}

# start_hours = [(i-1, int(lines[i].split(' ')[0]), int(lines[i+1].split(' ')[1])) for i in range(1,N+1)]

l = []
for i in range(1,N+1):
	l.append((int(lines[i].split(' ')[0]),i-1))
	l.append((int(lines[i].split(' ')[1]),i-1))

