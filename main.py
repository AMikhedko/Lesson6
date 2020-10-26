import re

def readMass(fileName):
    with open(fileName) as file:

        mass = []
        N = 0
        for row in file:
            z = []
            rowStr = row.strip('\n')
            rowStr = re.split(' +', rowStr)

            for i in rowStr:
                z.append(int(i))

            mass.append(z)
            N+=1
    return mass, N

def PrintMass(mass, N):

    for i in range(N):
        for j in range(N):
            print("%-4d" % mass[i][j], end='')
        print()

def ColumnMass(mass, N):
    sum_a = []

    for i in range(N):
        sum = 0
        for j in range(N):
            sum+=mass[j][i]
        sum_a.append(sum)
    for k in range(len(sum_a)):
        print(sum_a[k], end=' ')
    return sum_a

def CalcMax(sum_a):
    ind = 0
    print()
    print("The column with max sum of elements is: ", end=' ')
    for k in range(len(sum_a)):
        if sum_a[k] > sum_a[ind]:
            ind = k
    return ind+1

if __name__ == '__main__':
    mass, N = readMass(r'input.txt')
    PrintMass(mass, N)
    print("_   "*10)
    print(CalcMax(ColumnMass(mass, N)))
