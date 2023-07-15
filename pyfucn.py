
#Write a Python function called max_num()to find the maximum of three numbers.

def max_num(num1, num2, num3):
    max_number = num1  # Assume num1 is the maximum
    
    if num2 > max_number:
        max_number = num2
    
    if num3 > max_number:
        max_number = num3
    
    return max_number


#Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(numbers):
    result = 1  # Start with 1 as the initial value
    
    for num in numbers:
        result *= num
    
    return result

#Write a Python function called rev_string() to reverse a string.

def rev_string(string):
    reversed_string = ''
    
    for char in string:
        reversed_string = char + reversed_string
    
    return reversed_string

#Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False

#Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.

def pascal(n):
    triangle = []

    for i in range(n):
        row = []
        for j in range(i + 1):
            if j == 0 or j == i:
                row.append(1)
            else:
                prev_row = triangle[i - 1]
                num = prev_row[j - 1] + prev_row[j]
                row.append(num)
        triangle.append(row)

    for row in triangle:
        print(' '.join(str(num) for num in row))


