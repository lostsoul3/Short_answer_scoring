import sys
import re
from subprocess import Popen, PIPE

def grammar(state):
	p = Popen('hunshell -a'.split(), stdin=PIPE, stdout=PIPE)
	stdout, stderr = p.communicate('\n'.join(state))
	stdout = re.sub('@\(#\).*', '', stdout)
	stdout = re.split('\n\n', stdout.strip())
	final = []

	assert len(stdout) == len(state)
	for out, s in zip(stdout, state):
		out = out.strip().splitlines()
		ws = s.split()

		assert len(ws) == len(out)
		line=[]
		for w, o in zip(ws, out):
			m = re.match('& \w+ \d+ \d+: (.*)', o)
			if m:
				suggestions = m.group(1).split(',')
				if suggestions:
					line.append(suggestions[0].lower())
				else:
					line.append(w)
			else:
				line.append(w)
		final.append(' '.join(line))
	return final


if __name__ == '__main__':
	print grammar(sys.stdin.readlines())
