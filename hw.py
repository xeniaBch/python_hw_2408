# task1
x = int(input('Enter month number '))

if (x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12):
    print(31)
elif (x == 4 or x == 6 or x == 9 or x == 11):
    print(30)
elif (x == 2):
    print(28)
else:
    print(0)

# task2
a = int(input('Enter Antons age '))
b = int(input('Enter Boris age '))
c = int(input('Enter Viktors age '))

if a > b and a > c:
    print('A')
elif b > a and b > c:
    print('B')
elif c > a and c > b:
    print('C')
elif a > c and c < b == a:
    print('A B')
elif b > a and a < c == b:
    print('B C')
else:
    print(0)

# level2
# task Rook
x1 = int(input('Enter Rooks x coordinate '))
y1 = int(input('Enter Rooks y coordinate '))

x2 = int(input('Enter other figure x coordinate '))
y2 = int(input('Enter other figure y coordinate '))

if (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')

# task2 coordinates
x1 = int(input('Enter first point coordinate x '))
y1 = int(input('Enter first point coordinate y '))
x2 = int(input('Enter second point coordinate x '))
y2 = int(input('Enter second point coordinate y '))
if x1 * x2 > 0 and y1 * y2 > 0:
    print("YES")
else:
    print("NO")
