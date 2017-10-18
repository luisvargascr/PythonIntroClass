def addNumbers():
    num = int(input ("Please enter a positive number: "))
    while (num >=0 ):
        range_num = list(range(0,num + 1))
        sum_range = 0;
        for i in range_num:
            sum_range += i
        print("Sum is " + str(sum_range))
        num = int(input ("Please enter a positive number: "))


def countPages():
    num_pages = int(input ("Please enter the total pages: "))
    while (num_pages >= 0):
        page_range_sum = str(list(range(0,num_pages+1))).count('1')
        print (str(page_range_sum))
        num_pages = int(input ("Please enter the total pages: "))

def addEvenNumbers(x,y):
    range_num = list(range(x,y+1))

    sum_of_num = 0

    #for i in range_num:
     #   if i % 2 != 0:
      #      continue
       # sum_of_num += i

    sum_of_num = sum([i for i in list(range(x,y+1)) if i%2 == 0])
    print(str(sum_of_num))

num_x = int(input("Enter first number: "))
num_y = int(input("Enter second number: "))
addEvenNumbers(num_x,num_y)



