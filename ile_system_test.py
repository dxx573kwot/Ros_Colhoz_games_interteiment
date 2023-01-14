f = open('text.txt', 'w')
l = [1, 2, 3, 4, 5]
for index in l:
    f.write("Витя кислый" + "///" + str(index) + '\n')
f.close()
f2 = open('text.txt', 'r')
print(f2.read().split("\n"))
