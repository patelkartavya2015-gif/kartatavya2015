n = int(input("Enter the number of items: "))
dic = {}
no = 0
for i in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dic[key] = value
    print("The dictionary is:", dic)
    K = input("Enter th value to check for frequency: ")
    if K in dic.values():
            no += 1
            print("The frequency of the value is:", no)
