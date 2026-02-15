import argparse
import sys

parser=argparse.ArgumentParser()
parser.add_argument("num1",type=int)
parser.add_argument("num2",type=int)
args=parser.parse_args(sys.argv[1:])
num1=args.num1
num2=args.num2
operator=input("enter operation:\n + for addition \n - for subtraction\n * for multiplication\n / for division: \n")

match operator:
    case "+":
        print(num1, "+", num2, "=", num1+num2)
    case "-":                   
        print(num1, "-", num2, "=", num1-num2)
    case "*":
        print(num1, "*", num2, "=", num1*num2)  
    case "/":
        if num2 != 0:
            print(num1, "/", num2, "=", num1/num2)
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print(" operator yet to be defined `_` . Please use +, -, *, or /.")