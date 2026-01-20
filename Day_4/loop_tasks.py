## 🔹 TASK 4: Loops & Iterations

def print_range_numbers(step):
    """Print numbers from 1 to n using a loop."""
    for i in range(1, 101,step):
        print(i)


def countTimer(n):
    while(n>=0):
        print(n, end='\t')
        n-=1


def vowelRemoval(str):
    vowels = "aeiouAEIOU"
    result = ""
    for char in str:
        if char not in vowels and char != 't':
            result += char
        else:
            continue    
    return result


## Generate multiplication table.

def multiplication_table(n,w):
    for i in range(1, w+1):
        print(f"{n} x {i} = {n*i}")


num=int(input("Enter a number to generate its multiplication table: "))
w=int(input("Enter the limit of the table: "))

multiplication_table(num,w)

str=input("Enter a string: ")
print("String after removing vowels:", vowelRemoval(str))


time=int(input("Enter the time in seconds for countdown: "))
countTimer(time)

step=int(input("Enter the step value: "))
print_range_numbers(step)
