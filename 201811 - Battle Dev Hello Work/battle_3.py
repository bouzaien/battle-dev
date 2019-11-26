#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/

import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

s = 0

N = int(lines[0])
f = [int(x) for x in lines[1].split(' ')]

for i in range(0,len(f)-1):
	if f[i]==N/2 and f[i+1]==N/2:
		s = 'INF'
		break
	elif f[i]==N/2:
		s += 1
	elif (f[i]>N/2 and f[i+1]<N/2) or (f[i]<N/2 and f[i+1]>N/2):
		s += 1

sys.stdout.write(str(s) + '\n')