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

m = int(lines[1].split()[1])
pos = 1

for i in range(2,N+1):
	l = lines[i].split()
	if int(l[1]) < m:
		m = int(l[1])
		pos = i

sys.stdout.write( lines[pos].split()[0] + '\n')