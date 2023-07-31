#importing functions from func:
from art import logo
from func import add
from func import sub
from func import multi
from func import div
import os

def calculation():
    #Asking for inputs of num1 and num2 from the user:
    print(logo)
    num1=float(input("Give the first number? "))
    should_continue=True 
    while should_continue:
    #creating a dictionary accessing all the functions:
        operations={
            "+":add,
            "-":sub,
            "*":multi, 
            "/":div
        }
        print("Which among these operations would you like to perform: ")
        #looping through keys of operation dictionary:
        for i in operations:
            print(i)
        key=input("operation: ")
        num2=float(input("Give the next number? "))
        #printing the result:
        calc_function1=operations[key]
        answer1=calc_function1(num1, num2)
        print(f"{num1} {key} {num2} = {answer1}")
        #Asking the user to give another operation to be performed using the 1st answer as num1 and asking for num2 again:
        k=input("Would you like to use another Operation on your answer: (Y) \nor would you like to start new calculations (N) \n type (E) if you want to exit the program:  : ").lower()
        if k=="y":
            num1=answer1 
        elif k =="n":
            os.system("clear")
            calculation()        
        else:
            should_continue=False
            print("Thank You for using calculator")
         

#calling the main calculations function:
calculation()