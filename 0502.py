largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try :
        n = int(num)
        if largest is None :
            largest = n
        else :
            if largest < n :
                largest = n

        if smallest is None :
            smallest = n
        else :
            if smallest > n :
                smallest = n
    except:
        print("Invalid input")
        continue

print("Maximum is ", largest)
print("Minimum is ", smallest)
