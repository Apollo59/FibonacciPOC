x = 0
z = 1

answer = x + z

x1 = z

n = input('How many permuations do you want?\n')
n = int(n)
z1 = 0
for i in range(0, n):

    again = answer + z1
    print(again)
    answer = z1
    z1 = again
