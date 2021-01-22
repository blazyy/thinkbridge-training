''' Write a console application in the choice of your programming language that takes in a currency value (Min Value 00, Max Value 9,99,999.99) and prints out a text.
For e.g. -  If provided "123456.78", it should print out "Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty-Six 78/100 ONLY".
And provide unit tests that do a code coverage of 90%. Share the output via Github with clear instructions on how to run it locally with the right prerequisites. '''

import n2w

print('\nType any character other than a number to quit.')
while True:
    num = input('-> ')
    if num.isdigit() or '-' in num and not num.isalpha():
        print(n2w.num_to_words(int(num)))
    elif '.' in num and num.replace('.', '').isnumeric():
        print(n2w.num_to_words(float(num)))
    else:
        print('Quitting.')
        break
