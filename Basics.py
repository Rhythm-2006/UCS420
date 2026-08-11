#   QUESTION 1
print("hello world")

#QUESTION 2
print(3*"Rhythmpreet singh")

#QUESTION 3
a = "Rhythmpreet"
b = " Singh"
c = a+b
print(a ,"+", b , "->" ,c)

#QUESTION 4
a = "Rhythm"
b = 100
c = a + str(b)
print(c)

#QUESTION 5 
a = (input("Enter 1st number:"))
b = input("Enter 2nd number:")
c = input("Enter 3rd number:")
print(int(a)+int(b)+int(c))

#QUESTION 6
for i in range(1,11):
    print(5*i)

#QUESTION 7
i=1
while i <= 10:
    print(5*i);
    i=i+1;

#QUESTION 8
print("range(10) ->", list(range(10)))
print("range(10,20) ->", list(range(10,20)))
print("range(10,20,2) ->", list(range(10,20,2)))
print("range(-10,-20,2) ->", list(range(-10,-20,2)))
print("range(-10,-20,-2) ->", list(range(-10,-20,-2)))

#QUESTION 9
for i in range(1,11):
    print(7*i)
for j in range(1,11):
    print(9*j) 

#QUESTION 10
a = int(input("Enter number:")) 
for i in range(1,11):
    print(a*i)

#QUESTION 11
a = int(input("Enter number:"))
b = 0
for i  in range(1,a+1):
    b = b+i;
print(b)
