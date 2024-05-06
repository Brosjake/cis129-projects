#9.3

def exams():
    Continue = True
    
    with open('grades.csv', 'w') as grades:
        while Continue == True:
        
            fname = input("First Name: ")
            lname = input("Last Name: ")
            exam1 = int(input("Exam 1: "))
            exam2 = int(input("Exam 2: "))
            exam3 = int(input("Exam 3: "))
            
            grades.write(f'{fname},{lname},{exam1},{exam2},{exam3}\n')
            again = True
            while again == True:
                again = False
                question = input("Enter another student (y/n)")
                
                if(question == 'y'):
                    Continue = True
                elif(question == 'n'):
                    Continue = False
                else: 
                    print("input not recognized, try again. \n")
                    again = True
                    Continue = False

exams()