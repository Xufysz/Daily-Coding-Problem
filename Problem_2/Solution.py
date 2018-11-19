#Original
def getProductOriginal(num, arr):
    product = 1
    for x in arr:
        if x != num:
            product = product * x

    return product

#Bonus method
def getProductBonus(num, arr):
    product = 1
    for x in arr:
        if x != num:
            product = multiplyWithoutOperator(product, x)
    return product

def multiplyWithoutOperator(x, y):
    if y == 0:
        return 0
    
    if y > 0:
        return (x + multiplyWithoutOperator(x, y-1))
    
    if y<0:
        return -multiplyWithoutOperator(x,-y)
#End bonus methods

arr = [1,2,3,4,5]
newArr = []
for x in arr:
    newArr.append(getProductOriginal(x, arr))

for x in newArr:
    print(str(x))

newArr.clear()

print("Finished original algo")

for x in arr:
    newArr.append(getProductBonus(x, arr))

for x in newArr:
    print(str(x))

print("Finished bonus algo")