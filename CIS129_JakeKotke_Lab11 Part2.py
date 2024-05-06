#9.2

def calculate():
    with open('grades.txt', 'r') as f:
        total = 0
        loop = 0
        i = f.readlines()
        j = len(i)
        for grade in i:
            k = float(grade.strip())
            total = total + k 
            loop += 1
            print(f'Grade {loop}: {k:.2f}%')
            
    average = (total/j)
    print(f'Average Grade: {average:.2f}%')  
    print(f'Total Amount of Grades Entered are: {j}')
    print(f'The total Percentage: {total:.2f}%')
def main():
    calculate()
    
main()