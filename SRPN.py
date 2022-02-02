stack = [] #Create the stack and assign a global variable to it
arithmeticOperators = ["^", "%", "/", "*", "+", "-", "="] #Create a list of all arithmetic operators used in this calculator
randomIntCounter = 0 #Declare the variable that stores the number regarding which random integer within the randomIntegers list we are on at any given time.

def pushRandomInteger():
    #Create a list of all "random" integers used in this calculator
    randomIntegers = [1804289383, 846930886, 1681692777, 1714636915, 1957747793, 424238335, 719885386, 1649760492, 596516649, 1189641421, 1025202362, 1350490027, 783368690, 1102520059, 2044897763, 1967513926, 1365180540, 1540383426,
                      304089172, 1303455736, 35005211, 521595368]
    global randomIntCounter
    if not(randomIntCounter<len(randomIntegers)):
        randomIntCounter = 0 #Reset the counter once we reach the end of the list of the "random" integers.
    stack.append(randomIntegers[randomIntCounter])#Add the random integer to the stack
    randomIntCounter += 1 #Increment the counter by 1
    


def stackOverflow():
    #Check for stack overflow - if the size of the stack goes over 23, the input will not be added to the stack and the user is told that the stack is overflown.
    stackSize = len(stack)
    if (stackSize>22):
        print("Stack overflow.")
        return True    
        


def negativeNumber(negative, element):
    #Checks whether the boolean flag 'negative' is true or false, and if it is, take the number passed onto it and make it negative.
    if(negative):
        element = int(element)
        element = -element
    return element



def manipulateOperators(userInput):
    #Manipulate the operators based on their order of precedence.
    #Dictionary stating the precedence of each operator, with the lowest number corresponding to the operator with the highest priority.
    operatorPrecedenceDict = {
    '^' : 1,
    '%' : 2,
    '/' : 3,
    '*' : 4,
    '+' : 5,
    '-' : 6,
    }
    
    inputOperatorsList = []
    splitInput = userInput.split() #Create a list of the user input split into different sections, divided at each empty space " ".
    
    for element in splitInput: #Iterate through every element in the created list
        #Reset the values of these variables at every reiteration
        unorderedOperatorsList = []
        unorderedOperators = ""
        rearrengedOperatorsList = []
        rearrengedOperators = ""
        multipleOperators = False
        
        for char in element:
            #Iterate through every character within each element
            if(char in operatorPrecedenceDict): #Check whether it's an operator defined in the dictionary.
                unorderedOperators += char #Add the operator to the string which holds every operator in the element
                unorderedOperatorsList.append(char) #Add the operator to the list of these unordered operators.
                
            if(len(unorderedOperatorsList)>1): #Check whether there is more than one operator in this element, and if so, change the value of this boolean flag to true.
                multipleOperators = True
                
        if(multipleOperators):

            for index in range(1, len(unorderedOperatorsList)):
                #Sort algorithm - Iterate through each operator within the list and compare the values of them as defined in the dictionary to each other
                currentPosition = index
                currentElement = unorderedOperatorsList[index]

                while(operatorPrecedenceDict[currentElement]<operatorPrecedenceDict[unorderedOperatorsList[currentPosition-1]] and currentPosition>0):
                    #Compare each element with the ones before it and if it's lower than the one before it, move it back.
                    unorderedOperatorsList[currentPosition] = unorderedOperatorsList[currentPosition-1]
                    currentPosition-=1

                unorderedOperatorsList[currentPosition] = currentElement

            for element in unorderedOperatorsList:
                #Add the operators from the now-sorted list to the empty string variable "rearrengedOperators"
                rearrengedOperators += element
                
            inputOperatorsList.append([unorderedOperators, rearrengedOperators]) #After iterating through every element in the list, add the initial unordered operators and the new rearrenged operators to the 2D list "inputOperators".

    for element in inputOperatorsList:
        #After iterating through every element in splitInput list, manipulate the user input by replacing the old, unordered operators with the new, rearrenged operators.
        userInput = userInput.replace(element[0], element[1])

    
    return userInput #Return the new userInput string.




   
def handleInput(userInput):
    inputList = userInput.split() #Create a variable and assign to it the list of every element in the userInput, divided by each empty space " ".
    handledInput = [] #Declare the list which is going to store elements that have gone through the necessary checks.
    invalidOctal = False #Boolean flag to indicate whether the element is an octal or not.
    
    for element in inputList:
        invalidOctal = False #Reset the "invalidOctal" boolean flag to false upon every iteration through the list.
        negative = False #Reset the "negative" boolean flag to false upon every iteration through the list.
        groupedDigits = "" #Reset the groupedDigits string.
        
        if(len(element)>1):
            #Check whether the element is a negative number.
            if(element[0]=="-" and element[1].isdigit()):
                negative = True
                element = element.replace(element[0], '', 1)

        #Check whether the element is a number.
        if(element.isdigit()):
            #Check whether the first digit is 0, indicating it's an octal.
            if(element[0]=="0"):
                
                try:
                    #Try converting the octal integer to its corresponding decimal integer. 
                    element = int(element, 8)
                except ValueError:
                    #If an error occurs, it means the octal was invalid (in other words, had digits above and including 8. Set the "invalidOctal" flag to true. 
                    invalidOctal = True
                    
            if(not(invalidOctal)): #If the boolean flag "invalidOctal" is false, execute the following code. No "else" statement, therefore the program ignores any invalid octals.
                element = negativeNumber(negative, element) #If it's a negative octal, make it a negative integer.
                handledInput.append(element)
                
        else:
            for index in range(len(element)):
                #If the element is not a number, iterate through every character in the element and run checks.
                if(element[index]=="-" and element[index+1].isdigit()): #Check whether the upcoming number is negative, and if so, add the already grouped-up digits to the list and clear the string.
                    negative = True
                    if(len(groupedDigits)>0):
                        handledInput.append(groupedDigits)
                        groupedDigits = ""
                elif(element[index].isdigit()):
                    #If the character is a digit, add it to the groupedDigits string variable.
                    groupedDigits += element[index]
                    
                else:
                    #If the character is not a digit, check whether the groupedDigits string has more than one character in it.
                    if(len(groupedDigits)>0):
                        #If so, convert the groupedDigits string to integer, turn it into a negative number if it's negative, change it back to a string and append it to the list, also resetting the groupedDigits string. 
                        groupedDigits = int(groupedDigits)
                        groupedDigits = negativeNumber(negative, groupedDigits)
                        groupedDigits = str(groupedDigits)
                        handledInput.append(groupedDigits)
                        groupedDigits = ""
                    handledInput.append(element[index]) #Add the character to the list regardless of whether it's an integer or not.
                    negative = False #Reset the "negative" boolean flag.
                    
            if(len(groupedDigits)>0): #If the groupedDigits string still includes characters at the end of the element, append it to the list.
                groupedDigits = negativeNumber(negative, groupedDigits)
                handledInput.append(groupedDigits)

    processInput(handledInput) #Move on to the step of processing this new list formed, taken as the handled user input - "handledInput" list.








def processInput(userInput):
    
    for element in userInput:
        #Iterate through every element in the list.
        try:
            #Assume it's a number, so convert it to integer and hence presume it's an operand.
            element = int(element)
            handleOperands(element)
        except ValueError:
            #If an error occurs, it means the element is not a number, so run multiple checks.
            if(element.isalpha()):
                #If it's a letter, check whether it's one of the unique operators (r and d).
                handleSpecialOperators(element)
                
            elif(element in arithmeticOperators):
                #If it's an operator defined within the arithmeticOperators list at the start, process it accordingly.
                handleArithmeticOperators(element)
                
            else:
                #Otherwise, class it as an invalid input.
                handleInvalidInput(element)




def stackUnderflow(userInput):
    #Check whether the stack contains more than 1 element or not. If not, output "Stack underflow." and return true.
    if(len(stack)<=1):
        print("Stack underflow.")
        return True
    else:
        return False







def handleInvalidInput(userInput):
    #If a character is invalid, output a message stating it's an unrecognised operator or operand.
    print(f"Unrecognised operator or operand \"{userInput}\".")







def handleArithmeticOperators(userInput):
    #Check what operator it is, and run tasks accordingly.
    
    if(userInput=="="):
        #If the operator is the equals sign, make sure the stack isn't empty. If it is, output "Stack empty." and return -1.
        if(len(stack)<1):
            print("Stack empty.")
            return -1
        #Otherwise, print the last item in the stack as an integer. Note, an "else" statement here would be redundant as if the stack is empty, -1 is returned so the program doesn't process this part of the function.
        lastItem = stack[-1]
        print(int(lastItem))
    
    else:
        #Check whether stack is underflown or not.
        if(stackUnderflow(userInput)):
            return -1

        #Remove and return the last and second to last items in the stack and assign them to appropriate variables.
        secondOperand = stack.pop()
        firstOperand = stack.pop()

        #Based on the operator, perform arithmetic operations on the items just removed from the stack.
        if (userInput=="+"):
            result = int(firstOperand + secondOperand)
            
        elif(userInput=="-"):
            result = int(firstOperand - secondOperand)

        elif(userInput=="*"):
            result = int(firstOperand * secondOperand)

        elif(userInput=="/"):
            try:
                #Try dividing the first operand by the second operand.
                result = firstOperand / secondOperand
            except ZeroDivisionError:
                #If the second operand is 0, an error occurs, the program identifies it and outputs "Divide by 0.", adding the items back to the stack and returning -1.
                print("Divide by 0.")
                stack.append(firstOperand)
                stack.append(secondOperand)
                return -1
            
        elif(userInput=="^"):
            if(secondOperand<0):
                #Check whether the second operand is a negative number, and if so, output "Negative power.", add both items to the stack and return -1.
                print("Negative power.")
                stack.append(firstOperand)
                stack.append(secondOperand)
                return -1
            result = int(firstOperand ** secondOperand)

        elif(userInput=="%"):
            result = int(firstOperand % secondOperand)


        #Handle saturation
        if(int(result)>2147483647):
            result = 2147483647
        elif(int(result<-2147483648)):
            result = -2147483648

        stack.append(result) #Add the final result to the stack







def handleSpecialOperators(userInput):
    #If the character is "d", check whether the stack contains any elements. If so, output each element in the stack one by one. Otherwise, return the smallest integer number.
    if(userInput=="d"):
        if(len(stack)<1):
            print(-2147483648)
        else:
            for element in stack:
                print(element)
    #If the character is "r", check whether the stack is going to be overflown if a random integer is added, and if so, return -1. Otherwise, push a random integer to the stack.
    elif(userInput=="r"):
        if(stackOverflow()):
            return -1
        pushRandomInteger()

    #If the character is neither "d" nor "r", it's an invalid character and execute the appropriate function. 
    else:
        handleInvalidInput(userInput)
        






def handleOperands(userInput):
    #Check whether the stack is going to be overflown if this operand is added to the stack. If so, return -1. Otherwise, append it to the stack.
    if(stackOverflow()):
        return -1
    stack.append(userInput)








def commentConditionsMet(userInput, index):
    #Check whether the conditions for an element to be classed as a comment is met.
    
    #Declare the boolean flag "conditionsMet", and assign the value of false to it.
    conditionsMet = False
    #Check whether it's an individual character, and if so, change the conditionsMet flag to true.
    if(userInput==userInput[index]):
        conditionsMet = True
    else:
        #Check whether it is followed by an empty space, or if it is at the end of the element with an empty space right before it, or if it follows and is followed by an empty space.
        #If either of these conditions are correct, set conditionsMet to true.
        if(index==0):
            if(userInput[index+1]==" "):
                conditionsMet = True
        elif(index==(len(userInput)-1)):
            if(userInput[index-1]==" "):
                conditionsMet = True
        else:
            if(userInput[index+1]==" " and userInput[index-1]==" "):
                conditionsMet = True
                
    #Return conditionsMet regardless of whether it's true or false.
    return conditionsMet







def identifyComment(userInput):
    #Keep taking the user's input.
    while True:
        userInput = input()
        try:
            #Try finding "#" within the input, and if so, check whether it meets the conditions of being the start/end of a comment.
            #If true, remove everything up to the "#" in the userInput string and break out of the loop.
            endOfComment = userInput.index("#")
            if(commentConditionsMet(userInput, endOfComment)):
                userInput = userInput.replace(userInput[0:endOfComment+1], '')
                break
        except Exception:
            #If no "#" is found, pass. The loop starts again.
            pass
        
    #Return the processed userInput once the program is out of the loop (once the end of comment is identified).
    return userInput







def handleComments(userInput):
    
    for charIndex in range(len(userInput)):
    #Iterate through every character in the user input.    
        if(userInput[charIndex]=="#"):
            #If the character is "#", check whether it meets the conditions of being the start/end of a comment
            if(commentConditionsMet(userInput, charIndex)):
                try:
                    #If it does, assume the comment ends within the same input.
                    #Search through the user input starting from the character right after the "#" which was found already. 
                    endOfComment = userInput.index("#", charIndex+1)
                    #Once again, assuming "#" exists, check whether it meets the conditions of being the start/end of a comment.
                    if(commentConditionsMet(userInput, endOfComment)):
                        #If so, remove everything entered from the input between the two hashtags ("#") found.
                        userInput = userInput.replace(userInput[charIndex:endOfComment+1], '')
                        #Recursion - execute this function again with the new, manipulated user input to check for further comments within this single input.
                        handleComments(userInput)
                        
                    else:
                        #If it doesn't satisfy the conditions of being the start/end of a comment, execute identifyComment() with this userInput.
                        userInput = identifyComment(userInput)
                        
                except Exception:
                    #If no corresponding "#" is found within the input, execute identifyComment().
                    userInput = identifyComment(userInput)
            break

    #Return the new, manipulated userInput.
    return userInput


def takeInput():
    
    while True:
        #Take the input of the user indefinitely and run the necessary procedures.
        userInput = input()
        userInput = handleComments(userInput)
        userInput = manipulateOperators(userInput)
        handleInput(userInput)


#Main program
takeInput()
