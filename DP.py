while True:
 row=int(input("enter the no. of rows : "))
 if row %2==0:
  hDiamrow=int(row/2)
 else:
   hDiamrow=int(row/2)+1
 space=hDiamrow-1
 for i in range(1,hDiamrow+1):
   for j in range(1,space+1):
     print(end=" ")
   space=space-1
   num=1
   for j in range(2*i-1):
     print(end=str(num))
     num=num+1
   print()
 space=1
 for i in range(1,hDiamrow):
   for j in range(1,space+1):
     print(end=" ")
   space=space+1
   num=1
   for j in range(1,2*(hDiamrow-i)):
     print(end=str(num))
     num=num+1
   print()