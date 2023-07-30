#row=int(input("Enter the row:"))
#a=" * "
#count=1
#while row>0:
   #print(" "*row+a *count)
   #row=row-1
   #count=count+1
#else:
    #print("Pyramid is NOT print.... ")


num = int(input("enter no of rows : "))
for i in range(1, num + 1):
    print("  " * (num - i) + "* " * i)