from helper import sort   #importing sor function defined in helper.py
array1=[]  # initializing array
print("initial array :", array1)
#pushing elements to the array
for i in range(0,5):
    s=int(input("Enter a number to be pushed  at index "+str(i)+" :"))
    array1.append(s)
print("final array after pushing five elements to the array :")    

print(sort(array1))
