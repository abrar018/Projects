# calculator.py
# ABRAR REHAN, ENDG 233 F21
#
# A terminal-based calculator application for determining the result of a mathematical expression containing three values and two operators.
# Detailed specifications are provided via the Assignment 1 handout.
#
first_integer=int(input('Enter the first value: '))                            # Prompting the user to input 3 integers and 2 operators
first_operator=input('Enter the first operator: ')
second_integer=int(input('Enter the second value: '))
second_operator=input('Enter the second operator: ')
third_integer=int(input('Enter the third value: '))

if first_operator=='+':                                                        # Checking to see if the first operator is +
    if second_operator=='+':                                                   # Checking to see what the second operator is, if the first operator is +, and then calculating the final answer
        answer=((first_integer+second_integer)+third_integer)
    elif second_operator=='-':
        answer=((first_integer+second_integer)-third_integer)
    elif second_operator=='*':
        answer=(first_integer+(second_integer*third_integer))
    elif second_operator=='/':
        answer=(first_integer+(second_integer//third_integer))
elif first_operator=='-':                                                      # Checking to see if the first operator is -
    if second_operator=='+':                                                    # Checking to see what the second operator is, if the first operator is -, and then calculating the final answer
        answer=(first_integer-(second_integer+third_integer))
    elif second_operator=='-':
        answer=((first_integer-second_integer)-third_integer)
    elif second_operator=='*':
        answer=(first_integer-(second_integer*third_integer))
    elif second_operator=='/':
        answer=(first_integer-(second_integer//third_integer))
elif first_operator=='*':                                                      # Checking to see if the first operator is *
    if second_operator=='+':                                                   # Checking to see what the second operator is, if the first operator is *, and then calculating the final answer
        answer=((first_integer*second_integer)+third_integer)
    elif second_operator=='-':
        answer=((first_integer*second_integer)-third_integer)
    elif second_operator=='*':
        answer=((first_integer*second_integer)*third_integer)
    elif second_operator=='/':
        answer=((first_integer*second_integer)//third_integer)
elif first_operator=='/':                                                       # Checking to see if the first operator is /
    if second_operator=='+':                                                    # Checking to see what the second operator is, if the first operator is /, and then calculating the final answer
        answer=((first_integer//second_integer)+third_integer)
    elif second_operator=='-':
        answer=((first_integer//second_integer)-third_integer)
    elif second_operator=='*':
        answer=(first_integer//(second_integer*third_integer))
    elif second_operator=='/':
        answer=((first_integer//second_integer)//third_integer)
print(f'Entered expression: {first_integer} {first_operator} {second_integer} {second_operator} {third_integer}')             #Printing the expression formed from the input of the user
print(f'Your final answer = {answer}')                                                                                        #Printing the final answer
        

