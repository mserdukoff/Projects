import math

#ask user to input a file name
print("Benford's Law.\n")

file = open("data.txt", 'r')

content = file.readlines()

# list for expected data distribution
pairs = [
        ['Ones', 0, 30.1],
        ['Twos', 0, 17.6],
        ['Threes', 0, 12.5],
        ['Fours', 0, 9.7],
        ['Fives', 0, 7.9],
        ['Sixes', 0, 6.7],
        ['Sevens', 0, 5.8],
        ['Eights', 0, 5.1],
        ['Nines', 0, 4.6]
                            ]

arr = list(pairs)

total = 0
for line in content:
    tempstr = str(line)
    first = tempstr[:1]
    first = int(first)
    arr[first - 1][1] += 1
    total += 1

#print distribution
f = open('output.txt', 'w')
f.write("Total amount of each digit observed:\n")
for digit in arr:
    f.write(str(digit))
    f.write('\n')
f.write('\n\n')

#calculate adherences
for digit in arr:
    digit[1] = round((digit[1] / total) * 100, 2)

f.write("Calculated percentages compared to Benford's Law expected distribution:\n")
for digit in arr:
    f.write(digit[0])
    f.write(': ')
    f.write(str(digit[1]))
    f.write(' %     COMPARED TO EXPECTED     ')
    f.write(str(digit[2]))
    f.write(' %')
    f.write('\n')
