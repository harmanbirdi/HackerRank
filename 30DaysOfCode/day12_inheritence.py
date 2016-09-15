#!/usr/bin/env python

#
# Problem: https://www.hackerrank.com/challenges/30-inheritance
# __author__ : Harman Birdi
#


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print "Name:", self.lastName + ",", self.firstName
        print "ID:", self.idNumber


# Add your code to class Student
class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.grade = ''
        self.scores = scores
        Person.__init__(self, firstName, lastName, idNumber)

    def calculate(self):
        grades = {'O': [90, 100], 'E': [80, 89], 'A': [0, 79], 'P': [55, 69], 'D': [40, 54], 'T': [0, 39]}
        avg = int(reduce(lambda x, y: x + y, self.scores) / (len(self.scores) * 1.0))

        for grade in grades.keys():
            if grades[grade][0] <= avg <= grades[grade][1]:
                self.grade = grade

        return self.grade

# Code below provided by HackerRank template
line = raw_input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(raw_input())  # not needed for Python
scores = map(int, raw_input().split())
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print "Grade:", s.calculate()
