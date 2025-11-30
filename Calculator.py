# Project 10 - Calculator
#I was originally going to do this instead of the StudyBuddy project, but I didn't since I knew this was coming up on the Udemy course I am taking.

logo = r"""
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""

print(logo)

def add(n1, n2):
    return n1 + n2
def sub(n1, n2):
    return n1 - n2
def mul(n1 , n2):
    return n1 * n2
def div(n1, n2):
    return n1 / n2
n1 = int(input("What's the first number?"))
while True:
    operation = input("+\n-\n*\n/\nPick an operation:")
    n2 = int(input("What's the second number?"))
    end = 0
    if operation == "+":
        end = add(n1,n2)
        print(f"{n1}+{n2}={end}")
    elif operation == "-":
        end = sub(n1,n2)
        print(f"{n1}-{n2}={end}")
    elif operation == "*":
        end = mul(n1,n2)
        print(f"{n1}*{n2}={end}")
    elif operation == "/":
        end = div(n1,n2)
        print(f"{n1}/{n2}={end}")
    else:
        print("Invalid operation.")
    restart = input(f"Type 'y' to continue calculating with {end}, or type 'n' to start a new calculation:")
    if restart == "y":
        n1 = end
    elif restart == "n":
        n1 = input("What's the first number?")
    else:
        print("Invalid answer. Automatically choosing 'n'.")
        n1 = int(input("What's the first number?"))
