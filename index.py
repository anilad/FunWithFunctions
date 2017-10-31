def odd_even():
    for i in range (1, 2001):
        if i%2==0:
            print "Number is {}. This is an even number".format(i)
        else:
            print "Number is {}. This is an odd number".format(i)

def multiply(arr, num):
    for i in range(0, len(arr)):
        arr[i]= arr[i]*num
    return arr

def layered_multiples(arr):
    new_array=[]
    for i in arr:
        arr=[]
        for j in range(0, i):
            arr.append(1)
        new_array.append(arr)
    return new_array

# odd_even()

# a = [2, 4, 10, 16]
# b = multiply(a, 5)
# print b

x = layered_multiples(multiply([2,4,5],3))
print x