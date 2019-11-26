#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

l1 = lines[0].split()
N = int(l1[0])
M = int(l1[1])


reqs = [list(map(int,line.split()))+[i] for (i,line) in enumerate(lines[1:])]
reqs.sort(key=lambda x: x[0])
#sys.stderr.write(str(lines)+"\n")
#sys.stderr.write(str(reqs)+"\n")
#finals = [int(line.split()[1]) for line in lines[1:]]
#maxt = max(finals)
available = list(range(1,N+1))
satisfied = 0
running = []
t = 0
ch = [0] * M
while t<=2500 and satisfied < M and ch != "pas possible":
	if len(available) == 0:
		ch = "pas possible"
	else:
		#sys.stderr.write(str(t)+"\n")
		#sys.stderr.write(str(running)+"\n")
		temp = running.copy()
		for r in range(len(running)):
			#sys.stderr.write(str(t)+"\n")
			#sys.stderr.write(str(running)+"\n")
			
			try:
				if t == running[r][1]:
					available.append(running[r][2])
					del temp[r]
					# running = running[:r] + running[r+1:]
			
			except:
				sys.stderr.write(str(t)+"\n")
				sys.stderr.write(str(r)+"\n")
				sys.stderr.write(str(running)+"\n")
		running = temp
		if reqs[0][0] == t:
			running.append((reqs[0][0], reqs[0][1], available[0]))
			ch[reqs[0][2]] = available[0]
			reqs = reqs[1:]
			available = available[1:]
			satisfied += 1
	t += 1

if ch != "pas possible":
	#sys.stderr.write(str(ch)+"\n")
	ch = list(map(str,ch))
	ch = [x for x in ch if x!='0']
	ch = " ".join(ch)


sys.stdout.write( ch + '\n')
