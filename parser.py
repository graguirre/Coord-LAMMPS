#
# Get coordination count from ____ output for each timestep
#
# Gonzalo Aguirre <graguirre@gmail.com>
#

tf = 0	# timestep flag
nf = 0	# number flag
af = 0	# atoms falg
t = 0	# time
n = 0	# number of atoms

d = {}

for i in open('datos.txt'):
	if tf:
		t = int(i)	# get timestep
		tf = 0	# unset flag
		d[t]=[0 for j in range(4)]
	if i.find('ITEM: TIMESTEP') != -1:
		tf = 1	# set falg

	if nf:
		n = int(i)	# get number
		nf = 0		# unset flag
	if i.find('ITEM: NUMBER') != -1:
		nf = 1	# set flag

	if n == 0:
		af = 0	# unset flag
	if af:
		l = i.split()
		d[t][int(l[4])] += 1
		n -= 1
	if i.find('ITEM: ATOMS') != -1:
		af = 1

print d
