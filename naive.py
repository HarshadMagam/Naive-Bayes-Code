import xlrd

def calculate(k,total_rows,m):
	co2=0
	for i in range(0,total_rows):
		if table[i][k] == m :
			if table[i][5] == str("yes"):
				co2=co2+1
	px1=co2/int(count)
			
	return px1


def cal1(k,total_rows,m):
	co3=0
	for i in range(0,total_rows):
		if table[i][k] == m :
			if table[i][5] == str("no"):
				co3=co3+1
	py1=co3/int(count1)
			
	return py1
	




workbook =xlrd.open_workbook("userbook.xlsx")

worksheet = workbook.sheet_by_name("user")


total_rows=worksheet.nrows
total_cols=worksheet.ncols



table=list()
record=list()

for x in range(total_rows):
	for y in range(total_cols):
		record.append(worksheet.cell(x,y).value)
		
		
	table.append(record)
	record = []
	x+=1

for i in table:	
	print(i)	

print()
print("\nEnter the input to check whether customer by the computer or not")


a,b,c,d=input("Enter the age,income,student,credit rating").split()
print("\n age:",a,"   income:" ,b,"  student:",c,"  credit rating:",d)

	

count=0
count1=0


for i in range(0,total_rows):
	if table[i][total_cols-1] ==str("yes"):
		count=count+1
		
for i in range(0,total_rows):
	if table[i][total_cols-1] ==str("no"):
		count1=count1+1
	
px=count/int(total_rows-1)
print("\n probability of yes: ",round(px,3))

py=count1/int(total_rows-1)
print("\n probability of no: ",round(py,3))

print("probability of yes for age ",a)
px1=calculate(1,total_rows-1,a)
print(round(px1,3))
print("")

print("probability of no for age ",a)
py1=cal1(1,total_rows,a)
print(round(py1,3))

print("\nprobability of yes for income ",b)
px2=calculate(2,total_rows,b)
print(round(px2,3))
print("")

print("probability of no for income ",b)
py2=cal1(2,total_rows,b)
print(round(py2,3))


print("probability of yes for student ",c)
px3=calculate(3,total_rows-1,c)
print(round(px3,3))


print("\n probability of no for student",c)
py3=cal1(3,total_rows-1,c)
print(round(py3,3))


print("probability of yes for credit_rating ",d)
px4=calculate(4,total_rows-1,d)
print(round(px4,3))


print("probability of no for credit_rating",d)
py4=cal1(4,total_rows-1,d)
print(round(py4,3))

x=(px1*px2*px3*px4)
y=(py1*py2*py3*py4)

print("tuple of yes:",round(x,3))
print("tuple of no:",round(y,3))


count11=px*x
count22=py*y
print("final probability of yes",round(count11,3))
print("final probability of no",round(count22,3))


if count11 > count22:
	print("probability of yes is greater then no ")
	print("\n ----------------------Result--------------------------")
	print("customer bye the computer")
	
else:
	print("probability of no is greater then yes ")	
	print("\n ----------------------Result--------------------------")
	print("customer not  bye the computer")
	



