NPV = [3, 5, 5, 4]
ROI = [2, 5, 4, 3]
risk = [1, 3, 3, 5]
SPA = [5, 5, 3, 3]
comp = [2, 2, 4, 5]
resource = [4, 4, 1, 1]
total = 0

for i in range(1,5):
	total = 0
	print("project " + str(i) + ":")
	x = i - 1
	total += .25 * NPV[x]
	total += .15 * ROI[x]
	total += .15 * risk[x]
	total += .20 * SPA[x]
	total += .15 * comp[x]
	total += .10 * resource[x]
	print(total)
