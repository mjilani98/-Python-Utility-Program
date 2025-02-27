def print_menu():  # menu
    print("\n")
    print("1-compute pi: ")
    print("2-compute square root: ")
    print("3-display prime: ")
    print("4-process scores: ")
    print("5-compute tax: ")
    print("6-solve quadratic: ")
    print("7-sort list: ")
    print("8-id password: ")
    print("9-file sort: ")
    print("10-quit: ")
    print("\n")


def compute_pi(num):  # selection 1
    counter = 0
    sum = 0
    denominator = 1.0
    index = 1

    while counter < num:

        if index % 2 == 0:
            sum = sum - 1.0 / denominator

        else:
            sum = sum + 1.0 / denominator

        denominator = denominator + 2
        counter = counter + 1
        index = index + 1

    return 4 * sum


def compute_sqrt(x):  # selection 2
    firstGuess = 1
    last = firstGuess

    # calculating square root
    for i in range(0, 10, 1):
        next = 0.5 * (last + x / last)
        last = next

    # assigning the square root to the last next
    squareRoot = next

    return squareRoot


def display_prime(n):  # selection 3

    if is_prime(n):
        print("\nAll prime numbers less than or equal to: ", n)
        x = 0
        # printing all the prime numbers from 0 to n
        while x <= n:
            if (is_prime(x)):
                print(x, " ", end='')
            x += 1
    else:
        print("The number is not prime")


def is_prime(n):  # helper method to decide if a number is prime

    if n == 1:
        return False

    if n == 2 or n == 3:
        return True

    if n % 2 != 0 and n % 3 != 0:
        return True

    return False


def process_scores():  # selection 4

    studentCounts = 0  # keep track of number of students
    totalScores = 0  # sum of scores of all students

    highStudent = ''  # name of the highest student
    minStudent = ''  # name of the minimum student

    highestScore = 1  # highest score variable
    minimumScore = 1000  # minimum score variable

    while True:
        studentName = input("\nEnter a student name: ")

        if studentName == 'q' or studentName == 'Q':
            break
        else:
            studentScore = int(input("Enter a student score: "))
            totalScores += studentScore
            studentCounts += 1  # variable keeps track of number of students entered

            # checking for minimum score and student
            if studentScore < minimumScore:
                minStudent = studentName
                minimumScore = studentScore

            # checking for highest score and student
            if studentScore > highestScore:
                highStudent = studentName
                highestScore = studentScore

    # calculate the average
    average = totalScores / studentCounts

    # printing data : highest and minimum score and student
    print("\nThe student with the highest score: ", highStudent)
    print("Score: ", highestScore)

    print("\nThe student with the minimum score: ", minStudent)
    print("Score: ", minimumScore)

    print("\nAverage score: ", average)


def compute_tax(income, status, state):  # selection 5

    taxRate = 0

    # if the status is single
    if (status == 'single' or status == 'SINGLE') and income < 30000:
        taxRate = 20
    if (status == 'single' or status == 'SINGLE') and income >= 30000:
        taxRate = 25

    # if the status is married
    if (status == 'married' or status == 'MARRIED') and income < 50000:
        taxRate = 10
    if (status == 'married' or status == 'MARRIED') and income >= 50000:
        taxRate = 15

    # if the state is 'o' out of state
    if state == 'o' or state == 'O':
        taxRate -= 3

    # calculating the tax amount
    taxRate = income * (taxRate / 100)

    return taxRate


def solve_quadratic(a, b, c):  # selection 6

    if a == 0:
        return 0, 0

    has_solution = b * b - (4 * a * c)

    if has_solution >= 0:
        solution1 = (-b + compute_sqrt(has_solution) / (2*a))
        solution2 = (-b - compute_sqrt(has_solution) / (2*a))

        return solution1, solution2

    else:
        return 0, 0


def sortList(list):

    # making a copy of a list to keep the original list as is
    sortedList = list.copy()

    # sorting the list
    for x in range(0, len(sortedList)):
        for y in range(x+1, len(sortedList)):
            if sortedList[x] >= sortedList[y]:

                tempVariable = sortedList[x]
                sortedList[x] = sortedList[y]
                sortedList[y] = tempVariable

    return sortedList


def id_password(firstName, lastName):  # selection 8

    user = firstName[0] + lastName
    userId = user.upper()

    passw = firstName[0] + firstName[len(firstName)-1] + \
        lastName[:3] + str(len(firstName)) + str(len(lastName))

    password = passw.upper()

    return userId, password


def file_sort(infile, outfile):  # selection 9

    # opening and reading from afile
    inputfile = open(infile, 'r')

    # reading the number of the students
    numStudents = int(inputfile.readline())

    # creating a list for students ids with the size of number of students
    studentsId = [0] * numStudents

    # creating a list for students names with the size of number of students
    studentsNames = [0] * numStudents

    # creating a list for students gpa with the size of number of students
    studentsGpa = [0] * numStudents

    # a variable will hold one student (one student)
    student = []

    # getting and assigning information from the file
    for x in range(0, numStudents, 1):
        line = inputfile.readline()
        student = line.split()

        # filling the student id list with id
        studentsId[x] = int(student[0])

        # filling student names list with names
        studentsNames[x] = student[1]

        # filling student gpa list with gpa
        studentsGpa[x] = float(student[2])

    # sorting students based on id

    for x in range(0, len(studentsId)):
        for y in range(x+1, len(studentsId)):
            if studentsId[x] >= studentsId[y]:

                # sorting student id
                tempId = studentsId[x]
                studentsId[x] = studentsId[y]
                studentsId[y] = tempId

                # sorting student names
                tempName = studentsNames[x]
                studentsNames[x] = studentsNames[y]
                studentsNames[y] = tempName

                # sorting student gpa
                temGpa = studentsGpa[x]
                studentsGpa[x] = studentsGpa[y]
                studentsGpa[y] = temGpa

    # closing input file
    inputfile.close()

    # creating a new file with sorted students

    # opening an file
    outputfile = open(outfile, 'w')

    # writing the number of the students in the first line of the file
    outputfile.write(str(numStudents) + "\n")

    # writing the students to the file
    for x in range(0, len(studentsId)):
        outputfile.write(
            str(studentsId[x]) + "\t" + studentsNames[x] + "\t" + str(studentsGpa[x]) + "\n")

    # closing the file
    outputfile.close()


# ---------------------- rectangle class ----------------------


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width

    # default constructor
    # def __init__(self):
    #     self.length = 0
    #     self.width = 0

    # setters

    def setLength(self, length):
        self.length = length

    def setWidth(self, width):
        self.width = width

    # getters

    def getLength(self):
        return self.length

    def getWidth(self):
        return self.width

    # area
    def calculateArea(self):
        # area of rectangle = width * length
        return self.width * self.length
    # to string method

    def __str__(self):
        return "\nWidth: " + str(self.width) + "\nLength: " + str(self.length) + "\nArea " + str(self.calculateArea())
# --------------------------------------------


# Main program
userSelection = 0

while userSelection != 10:

    print_menu()
    userSelection = int(input("Enter a selection: "))

    if userSelection == 1:  # compute pi

        piInput = int(input("Enter a number to compute for pi: "))
        print("The result is: ", compute_pi(piInput))

    if userSelection == 2:  # compute square root

        sqrInput = int(input("Enter a number to calculate it's square root: "))
        print("The square root is: ", compute_sqrt(sqrInput))

    if userSelection == 3:  # display prime
        n = int(input("Enter a number: "))
        display_prime(n)

    if userSelection == 4:  # process scores
        process_scores()

    if userSelection == 5:  # compute tax
        income = int(input("\nEnter income: "))
        status = input("Enter status: 'single' or 'married': ")
        state = input("'i' in state 'o' out state: ")

        print("\nTax amount: ", compute_tax(income, status, state))

    if userSelection == 6:  # solve quadratic
        a = int(input("Enter a: "))
        b = int(input("Enter b: "))
        c = int(input("Enter c: "))

        solution1, solution2 = solve_quadratic(a, b, c)
        print("\nSolution 1: ", solution1)
        print("Solution 2: ", solution2)

    if userSelection == 7:  # sort list

        list = [17, 13, 23, 11, 2, 23, 8, 19, 9]

        sortedList = sortList(list)

        print("original list: ", list)
        print("Sorted list: ", sortedList)

    if userSelection == 8:  # id password
        fName = input("Enter first name: ")
        lName = input("Enter last name: ")

        userId, password = id_password(fName, lName)

        print("User id: ", userId)
        print("Password: ", password)

    if userSelection == 9:  # file sort

        infile = input("Enter an input file name: ")
        outfile = input("Enter an output file name: ")

        file_sort(infile, outfile)


# testing rectangle class

# creating a rectangle object using constructor

rectangle1 = Rectangle(0, 0)

# printing values of rectangle 1
print("\nValues of rectangle using to string method: ", end='')
print(rectangle1)

# setting values to the object using setters
rectangle1.setLength(2)
rectangle1.setWidth(3)

# getting values using getters
print("\nValues of rectangle using getters: ")
print("Width: ", rectangle1.getWidth())
print("Length: ", rectangle1.getLength())
print("Area: ", rectangle1.calculateArea())
