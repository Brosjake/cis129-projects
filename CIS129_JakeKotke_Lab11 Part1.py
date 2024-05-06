#9.1
def write():
    with open('grades.txt', 'w') as f:
        i = (int(input('how many grades would you like to enter? ')))
        
        
        for _ in range(i):
            grades = (input("enter grade "))
            f.write(grades + '\n')
    return i
    
def calculate(grades):
    with open('grades.txt', 'r') as f:
        total = 0
        for _ in range(grades):
            g = float(f.readline())
            total = total + g
    average = (total/grades)
    print(f'{average:.2f}')  

def main():
    i = write()
    calculate(i)
    
main()