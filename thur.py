a = 10
b= 0 
# print(a/b) this generates an error hence we handle it by try and exception 
try:
    print(a/b)
except:
    print("invalid input")
print("bye ")

list2= [1,2,3,4,54]
#n = int(input("enter the  element you want to check in the list "))
for k in list2:
    if k==1:
        print("yes element is one ")
    elif k==4:
        print("yes element is four")
    else:
        print("the next element is: ", k)
