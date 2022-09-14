#!/usr/bin/env python3
#Timothy McGowan
#Python version 3.5.2
#CS-265-005-SP 17-18

import sys

OPERATORS = ['+', '-', '*', '/', '%', '(', ')'] #Global list of operators

def infix2postfix(infix):

	rights = {'*':3, '/':3, '%':3, '+':2, '-':2, '(':1} #Dictionary for order of operation right levels
	
	stack = [] 
	
	postFix = ''

	usrInput = infix.split() #Splits user input by white space
	for x in usrInput:
	

		if x not in OPERATORS: #If current datum is not an operator place it in the postfix
		
			postFix += x  
			postFix += ' '
		elif x == '(': #If current datum is a left parenthesis
			
			stack.append(x)
			
		elif x == ')': # If current datum is a right parenthesis pop from the stack and add to postfix untill a left parenthesis is encountered
		
			curOp = stack.pop()
				
			while curOp != '(':
					
				postFix += curOp
				postFix += ' '
				curOp = stack.pop()
						
		else: #If the current datum is (+-*/%)
			while len(stack) > 0 and rights[x] <= rights[stack[-1]]:#While the stack is populated and curent datum has less than or 										equal rights to the top of the stack
			
				postFix += stack.pop() #Add top of stac to postFix
				postFix += ' '	
			stack.append(x)	#Append curent datum to the stack
		  
				
	while len(stack) > 0: #Clean up rest of stack adding to postFix
		postFix += stack.pop()
		postFix += ' '
	return postFix

def evalPostfix(PostFix) : #Solves equation in PostFix form

	postNums = []
	postSplit = PostFix.split()
	
	for x in postSplit:
		if x not in OPERATORS: #Append non operators to the list of numbers as an integer
			postNums.append(int(x))
		else:
			number2 = postNums.pop() #Get second number from number list
			number1 = postNums.pop() #Get first number form number list
			
			if x == '+': #Perform Addition
				postNums.append(int(number1 + number2))
			elif x == '-':#Perform Subtraction
				postNums.append(int(number1 - number2))
			elif x == '*':#Perform Multiplication
				postNums.append(int(number1 * number2))
			elif x == '%':#Perform Modular Division
				postNums.append(int(number1 % number2))
			else:#Perform Standard Division
				postNums.append(int(number1 / number2))
				
	return postNums.pop()#Returns solution

try: #Try to get data from a file input through the command line
	
	inFile = sys.argv[1]
	with open(inFile) as f:
		for line in f:
			postForm = infix2postfix(line)
			postAns = int(evalPostfix(postForm))
			print(postForm,'=',postAns)
except IndexError: #If there is no command line argument ask the user for input and solve on the fly
	infixExp = []
	userChoice = ""

	while True:
		print('Please Enter Infix Expression (Type "done" to finish)')
		userChoice = sys.stdin.readline()
		postForm = infix2postfix(userChoice)
		postAns = int(evalPostfix(postForm))
		print(postForm,'=',postAns)
		
		moreMath = input("Would you like to enter more infix equations? (y/n) :\n")
		moreMath.lower()
		
		if moreMath == 'n':
			print("Thank you for using the Infix to Postfix solver!")
			break
		else:
			continue
