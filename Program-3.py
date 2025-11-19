a = int(input("Enter a number: "))

# If even, reduce by 1 (so we print only odd numbers)
if a % 2 == 0:
    a = a - 1

series = []
for i in range(1, a + 1, 2):
    series.append(i)

print(*series, sep=", ")
