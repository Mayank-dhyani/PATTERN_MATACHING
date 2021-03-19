#pattern printingi
print("how Many Row you wnat to print:-")
num=int(input())
print("type 1 or 0:-")
num1=int(input())
new=bool(num1)
if new==True:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")
elif new==False:
    for i in range(num,0,-1):
        for j in range(1,i+1):
            print("*",end=" ")
        print("\n")