#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

l = list(map(int,lines))
m = min(l)

s=0

for i in l:
	s += (i-m)

sys.stdout.write( str(s) + '\n')