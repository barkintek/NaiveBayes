# Naive bayes algorithm implementation in python
import csv
import copy
from sys import argv

def main():

	script, filein, fileout = argv

	matrix = readcsv(filein)
	#pmatrix(matrix)
	
	fout = open(fileout, 'w')
	wr = csv.writer(fout, quoting=csv.QUOTE_ALL)

	for i in range(0, len(matrix[0]) -1):
		ptable = classprobtable(matrix, i, 6)
		#pmatrix(ptable)
		for row in ptable:
			wr.writerow(row)
		wr.writerow([]) # newline

# Construct P(class | condition) table
def classprobtable(matrix, ccol, tcol):
	# matrix headerless
	matrixhl = matrix[1:]
	# frequency, condition tables
	ftable = freqtable(matrix, ccol, tcol)
	ctable = condprobtable(ftable)
	# class probability - P(class|condition) table
	ptable = copy.deepcopy(ctable)
	# rename table name as P(class|condition)
	tnames = ptable[0][0].split("|")
	ptable[0][0] = "P(" + tnames[1][:-1] + "|" + tnames[0][2:] + ")"
	# column length
	clength =  len(ptable)
	# for each column starting from 1
	for c in range(1, len(ptable[0])):
		# for each row starting from 1
		for r in range(1, clength):
			# P(class) * length of total size
			classprob = len([row for row in matrixhl if row[tcol] == ptable[0][c]])
			# P(condition) * length of total size
			condprob = len([row for row in matrixhl if row[ccol] == ptable[r][0]])
			# note that both probabilities have *length of total size
			# so it is unneccessary to divide them with it, since dividing those altogether will omit those
			ptable[r][c] = (ptable[r][c] * classprob) / condprob

	return ptable

# Construct P(condition | class) table 
def condprobtable(ftable):
	ctable = copy.deepcopy(ftable)
	# rename table name as P(condition|class)
	ctable[0][0] = "P" + ctable[0][0][1:]
	# for each column starting from 1
	for c in range(1, len(ctable[0])):
		# column sum - sum of frequences of the current column 
		csum = sum(column(ftable[1:], c))
		# for each row starting from 1
		for r in range(1, len(ctable)):
			ctable[r][c] = ctable[r][c] / csum
	return ctable

# Construct frequency table
def freqtable(matrix, ccol, tcol):
	# matrix headerless
	matrixhl = matrix[1:]
	# table name
	tn = "f(" + matrix[0][ccol] + "|" + matrix[0][tcol] + ")" 
	# header
	ftable = [[tn] + list(set(column(matrixhl, tcol)))]
	# for each unique condition
	for ucond in set(column(matrixhl, ccol)):
		row = [ucond]
		# for each header(class) value
		for cval in ftable[0][1:]:
			# construct row with their corresponding frequency values
			row += [len([r for r in matrixhl if r[ccol] == ucond and r[tcol] == cval])]
		ftable.append(row)

	return ftable

# Slice column from matrix
def column(matrix, c):
	return [row[c] for row in matrix]

# Read matrix from csv file
def readcsv(filename):
	matrix = []
	with open(filename, "r") as csvfile:
		for line in csvfile:
			matrix.append(line.strip().split(","))

	return matrix

# Pretty print matrix
# For debug purposes
def pmatrix(matrix):
	for row in matrix:
		print(row)
	print()	# newline

if __name__ == '__main__':
	main()
