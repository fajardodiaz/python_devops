squares = []
for i in range(10):
    squared = i*i
    squares.append(squared)

print(squares)

squares = [j*j for j in range(10)]
print(squares)

doble = [k for k in range(21) if k%2==0]
print(doble)