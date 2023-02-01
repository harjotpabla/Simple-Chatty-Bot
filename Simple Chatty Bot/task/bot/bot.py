def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age) + "; that's a good time to start programming!")


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    counter = 0
    while counter <= num:
        print(counter, '!')
        counter += 1


def test():
    print("Let's test your programming knowledge.")
    print('Which one IS an example of a programming language?')
    print('1. Ruby')
    print('2. GuavaScript')
    print('3. Cobra')
    print('4. A++')

    user_answer = int(input())
    if user_answer != 1:
        print('Please, try again.')
        test()
    else:
        print('Good job, you have successfully completed the test!')
        print('Congratulations, have a nice day!')


greet('Goofy', '2023')
remind_name()
guess_age()
count()
test()
