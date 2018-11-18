#Init
arr = [10,15,3,7,2]
k = 17

#Inital solution
for i in arr:
    for x in arr:
          print("{} + {}: {}".format(i, x, (i + x) == k))

print("first phase completed")

#Bonus
numHash = {}

#+++pair is a match, ---pair is not a match
for i in range(len(arr)):
        numHash[arr[i]] = i
        if (k - arr[i]) in numHash:
                print("+++pair: " + str(arr[i]) + " + " + str(k - arr[i]))
        else:
                print("---pair: " + str(arr[i]) + " + " + str(k - arr[i]))    

print("second phase completed")