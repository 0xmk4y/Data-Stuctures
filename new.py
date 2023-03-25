#Checking in two numbers are the same
#Complexity O(1)
def equal(a, b):
    if a^b == 0:
        return True
    else:
        return False
print(equal(3,3))
#returns True
print(equal(3,5))
#returns False




