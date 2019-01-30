def print_matrix(matrix):
	for i in range(len(matrix)):
		for j in range(len(matrix[0])):
			print(matrix[i][j])
		print("\n")
	for h in matrix:
		print (h)
		
#def main():
a=int(input("matrix 1 rows:"))
b=int(input("matrix 1 columns:"))
c=int(input("matrix 2 rows:"))
d=int(input("matrix 2 columns:"))
if(b!=c):
	print("matrix multiplication is not possible:")
	exit()
#declaration of arrays
array1=[[0 for j in range (0,b)] for i in range (0,a)]
array2=[[0 for j in range (0,d)] for i in range (0,c)]
result=[[0 for j in range (0,d)] for i in range (0,a)]
print ("enter 1st matrix elements:" )
for i in range(0 , a):
	for j in range(0 , b):
		array1[i][j]=int (input("enter element"))
print ("enter 2nd matrix elements:")
for i in range(0 , c):
	for j in range(0 , d):
		array2[i][j]=int(input("enter element"))
print ("1st matrix")
print_matrix(array1)
print ("2nd matrix")
print_matrix(array2)
for i in range(0 , a):
	for j in range(0 , d):
		for k in range(0 , b):
			result[i][j] += array1[i][k] * array2[k][j]
print ( "multiplication of two matrices:" )
print_matrix(result)
