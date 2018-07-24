def merge(list1, list2):
    # implement your solution here
    
    i=0
    j=0
    while i < len(list1):
        if list2[j]>=list1[i]:
            list2.insert(j,list1[i])
            i+=1
            j+=1
        else:
            j+=1
      
    return list2

list1 = [1,3,8,19]
list2 = [5,6,11,12,21]
print str(merge(list2, list1))


# keep testing
# another comment, yes, keep testing
