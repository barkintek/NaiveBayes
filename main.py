import csv
import copy

# param1 - data matrix
# param2 - column
# returns specified column values of the matrix
def column(matrix, i):
	return [row[i] for row in matrix]

# param1 - data matrix
# param2 - condition column
# param3 - target column
# returns frequency table of conditions
def frequencyTable(matrix, ccol, tcol):
	# set headers
	table = [[matrix[0][ccol] + "|" + matrix[0][tcol]] + list(set(column(matrix[1:], tcol)))]
	for item in set(column(matrix[1:], ccol)):
		table.append([item])
	
	# fill frequencies
	# for each target value
	for i in range(1, len(table[0])):
		# for each condition value
		for j in range(1, len(column(table, 0))):
			table[j].append(len([d for d in matrix[1:] if d[ccol] == table[j][0] and d[tcol] == table[0][i]]))

	return table

# param1 - frequency table
# returns P(condition | class) table, or in other words, condition under class probability table
def conditionUnderClassProbTable(frequencyTable):
	table = copy.deepcopy(frequencyTable)
	table[0][0] = "P(" + table[0][0] + ")"
	# for each class
	for i in range(1, len(table[0])):
		# for each condition
		for j in range(1, len(column(table, 0))):
			# condition occurrences under class / total occurrences of class
			table[j][i] = table[j][i]/sum(column(frequencyTable[1:], i))

	return table

# param1 - data matrix
# param2 - condition column
# param3 - target column
# returns P(class | condition) table, or in other wods, class under condition probability table
def classUnderConditionProbTable(matrix, ccol, tcol):
	ftable = frequencyTable(matrix, ccol, tcol)
	ctable = conditionUnderClassProbTable(ftable)
	table = copy.deepcopy(ctable)
	table[0][0] = "P(" + matrix[0][tcol] + "|" + matrix[0][ccol] + ")"
	# for each class
	for i in range(1, len(table[0])):
		# for each condition
		for j in range(1, len(column(table, 0))):
			# P(class | condition) = (P(condition | class) * P(class)) / P(condition)
			table[j][i] *= sum(column(ftable[1:], i))/len(column(matrix[1:], 0))
			table[j][i] /= sum(ftable[j][1:])/len(column(matrix[1:], 0))

			pass

	return table

# param1 - input file to train
# param2 - output file to output trained data
def trainNaiveBayes(inFile, outFile):
	data = []
	with open(inFile, "r") as csvfile:
		for line in csvfile:
			data.append(line.strip().split(","))

	fout = open(outFile, 'w')
	wr = csv.writer(fout, quoting=csv.QUOTE_ALL)

	for i in range(0, len(data[0]) -1):
		ptable = classUnderConditionProbTable(data, i, len(data[0]) -1)
		for item in ptable:
			wr.writerow(item)
		wr.writerow([])

# main
trainNaiveBayes("data.csv", "trained_data.csv")
