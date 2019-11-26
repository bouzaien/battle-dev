#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

initial = int(lines[0])

for line in lines[1:]:
	tup = line.split()
	initial += int(tup[0])
	initial -= int(tup[1])

if initial<=100:
	cash = 1000
elif initial<=10000:
	cash = 100
else:
	cash = 'KO'

sys.stdout.write( str(cash)+ '\n')