#define integers 1 to 5 and illicit input from user
int1 = int(input("Enter the first Integer: "))
int2 = int(input("Enter the second Integer: "))
int3 = int(input("Enter the third Integer: "))
int4 = int(input("Enter the fourth Integer: "))
int5 = int(input("Enter the fifth Integer: "))

#set minimum and maximum integers
minimum = min(int1,int2,int3,int4,int5)
maximum = max(int1,int2,int3,int4,int5)

#print the minimum and maximum integers
print("The maximum integer is " + str(maximum))
print("The minimum integer is " + str(minimum))