squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)

print(squares)

for i, v in enumerate(squares): #enumerate index 뽑아내는 함수 ##중요##
    print("{}는 {}".format(i, v))

