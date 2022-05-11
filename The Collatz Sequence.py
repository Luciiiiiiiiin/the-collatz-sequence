def collatz(number):
    remains = number % 2
    if remains == 0:
        return number // 2
    else:
        return 3 * number + 1


print('Type in an integer')
user = int(input())
while True:
    print(collatz(user))
    user = collatz(user)
    if user == 1:
        break



