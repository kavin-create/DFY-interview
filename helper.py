#array only for checking implementation of sort function
#array=[3,2,5,4,1] 
#sorting function
def sort(arr1):
    length = len(arr1)     #refering to  length of array arr1
    for i in range(len(arr1)):
        for j in range(0,length):
            t=0
            if (arr1[i]<arr1[j]):
                t=arr1[i]
                arr1[i]=arr1[j]
                arr1[j]=t
    return(arr1)
 
            
#displaying the sorted array for checking
#print(sort(array))

