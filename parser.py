#
# Get coordination count from ____ output for each timestep
#
# Gonzalo Aguirre <graguirre@gmail.com>
#
import sys, getopt

def usage():
	print >> sys.stderr, "Options:"
	print >> sys.stderr, "	-h		Show help"
	print >> sys.stderr, "	-i <inputfile>	Input file"
	print >> sys.stderr, "Syntax: python2 parser.py -i data.txt"
	sys.exit(1)

def main(argv):

	# variables
	tf = 0	# timestep flag
	nf = 0	# number flag
	af = 0	# atoms falg
	t = 0	# time
	n = 0	# number of atoms
	
	d = {}	# init dictionary
	inputfile = ''

	try:
		opts, args = getopt.getopt(argv,"hi:")
	except getopt.GetoptError:
		usage()

	for opt, arg in opts:
		if opt == '-h':
			usage()
		elif opt == '-i':
			inputfile = arg

	if inputfile == '':
		usage()

	try:
		fid = open(inputfile,'r')
	except IOError:
		print >> sys.stderr, "ERROR: File "+inputfile+" not found."
		sys.exit(2)
	
	for i in fid:
		# don't alter the if statement order
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

if __name__ == "__main__":
	main(sys.argv[1:])
