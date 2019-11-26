#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

def movement(pos1, pos2):
	m = ""
	dy = pos1[0] - pos2[0]
	dx = pos1[1] - pos2[1]

	if dx>0:
		m += dx * "<"
	elif dx<0:
		m += (-dx) * ">"

	if dy>0:
		m += dy * "^"
	elif dy<0:
		m += (-dy) * "v"

	return m

N = int(lines[0])

pos_coins = []
pos_multi = []

for i in range(N):
	l = lines[i+1]
	for j in range(N):
		if l[j] == "o":
			pos_coins.append((i,j))
		elif l[j] == "*":
			pos_multi.append((i,j))

m = movement((0,0),pos_coins[0]) + "x"

for k in range(len(pos_coins)-1):
	m += movement(pos_coins[k], pos_coins[k+1])
	m += "x"

m += movement(pos_coins[-1],pos_multi[0]) + "x"

for k in range(len(pos_multi)-1):
	m += movement(pos_multi[k], pos_multi[k+1])
	m += "x"

sys.stdout.write( m + '\n')