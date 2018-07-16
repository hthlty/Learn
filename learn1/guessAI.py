#coding=utf-8

while True:
    try:
        num=int(input('Enter a num:'))
    except ValueError:
        print('The input must be integer!')
        continue
    break

guess = num / 2
middle = num / 4
step = 0

while guess !=num:
    if num > guess:
        guess +=middle
        print("I guess:" ,guess)
    elif num < guess:
        guess -=middle
        print("I guess:" ,guess)
    middle /=2
    if middle==0:
        middle=1
    step +=1

print ("Aha! The answer is: ", guess)
print ("I totally use %d steps." % step)