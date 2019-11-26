#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))
	
N = int(lines[0])
s = 0
i = 1
k = 0

while i<=N:
	if int(lines[i]) + s <= 100:
		s += int(lines[i])
		i += 1
	else:
		s = 0
		k +=1
k += 1

sys.stdout.write( str(k)+ '\n')