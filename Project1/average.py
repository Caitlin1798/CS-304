
print ("Hello, how many grades will you be entering today?")

howManyGrades = int(input())

total= 0
totalGrade = 0
gradeList = []

for i in range(howManyGrades):
	print("please enter grade " + str(i+1))
	studentGrade = float(input())
	gradeList.append(studentGrade)
	total += studentGrade

average = total / howManyGrades

Max = gradeList[0]
for i in range (0, len(gradeList),1):
	if Max < gradeList[i]:
	Max = gradeList[i]
gradeList.sort()
print(gradeList[1])

print ("The average of those " +str(howManyGrades) + " grades is " +str(average))

