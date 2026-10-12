#String & Numeric values can operate together with *
A,B = 2,3
Txt = "@"
print(2*Txt*3)

#String & String can operate with *
A,B = "2" ,3
Txt = "@"
print((A+Txt)*B)

#Numeric values can operate with all arithmetic operators
A,B = 2,3
C = 4
print(A+B*C)

#Arithmetic expression with Integer and float will result in float
A,B = 10,5.0
C = A * B
print(C)

#Result of division operator with two integers will be float
A,B = 1,2
C = A/B #float division
print(C)

#Integer division with float and int will give int displayed as float
A,B = 1.5,3
C = A//B #integer division = floor
print(C, A/B)

#Floor concept in maths gives a closest number after the division of 2 numbers and it is equal to integer division of 2 numbers

#Remainder is negative when denominator is negative
A,B = -5,2
C = A % B
print(C)

A,B = 5,2
C = A % B
print(C)

A,B = 5,-2
C = A % B
print(C)