''' Write a console application in the choice of your programming language that takes in a currency value (Min Value 00, Max Value 9,99,999.99) and prints out a text.
For e.g. -  If provided "123456.78", it should print out "Rs. One Lakh Twenty Three Thousand Four Hundred And Fifty-Six 78/100 ONLY".
And provide unit tests that do a code coverage of 90%. Share the output via Github with clear instructions on how to run it locally with the right prerequisites. '''

# If zeroes are prepended to the input, this solution will ignore them and start counting the number from the first non-zero number.
# Example: 00035 will be read as 35.

def num_to_words(value):
    if (isinstance(value, str)):
        raise ValueError('Enter a number!')
    if value == 0:
        return 'Rs. Zero ONLY'
    elif value < 0:
        raise ValueError('Currency cannot be negative!')
    elif value >= 1000000:
        raise ValueError('Currency value too high! Maximum is 999999.')

    ones_place = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    eleven_to_nineteen = ['Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
    tens_place = ['', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']

    words = ''
    current_place = 1 # Initially at ones place. Then tens place, hundredth's place, etc.

    # Dealing with the decimal at the beginning since we're scanning the number from right to left.
    # After this point, the number is considered a whole number.
    is_decimal = False
    if(isinstance(value, float)):
        # This part of the code assumes that only a maximum of 2 decimal places are given in the input.
        decimal = int(round(value - int(value), 2) * 100) # Gets the two numbers after the decimal point (i.e. the fractional part)
        if decimal != 0: # If input had two zeroes in decimal places, ignore.
            is_decimal = True


    value = int(value) # If float, change to int. At this point, decimal places have already been dealt with and if left in, will mess up modulo divison.

    while value:

        current_digit = value % 10 # Scanning from right to left, one (and sometimes two) digits at a time.

        if current_place == 1:
            if value % 100 > 10 and value % 100 < 20: # If last two numbers as a whole are between 11-19, use different words to represent.
                words = eleven_to_nineteen[current_digit - 10]
                # The following two lines are because we're dealing with two numbers and the next one to process should be the digit at hundreth's place.
                current_place += 1
                value //= 10
            else: # If the numbers are from 0 - 10.
                words = ones_place[current_digit]

        elif current_place == 2:
            connector = '-' if (current_digit > 1 and words != '') else '' # Add hyphen only if the last number (upto tens place) is between 21 and 99 and not divisible by 10.
            words = tens_place[current_digit] + connector + words

        elif current_place == 3 and current_digit != 0: # If 0 encountered at hundreth place, skip. Eg. If the number is 100000, we need to move left.
            connector = ' Hundred' if words == '' else ' Hundred And ' # Use 'And' only if the number at hundred's place isn't a 0.
            words = ones_place[current_digit] + connector + words

        elif current_place == 4: # Three different possibilites that need to be dealt with seperately. Examples of each: two thousand (...02000), thirteen thousand, sixty seven thousand
            temp = value % 100 # Here we deal with two numbers at a time. This is because depending on the number at thousandth's place and ten thousandth's place, the word representation changes.
            if temp != 0: # If both numbers are 0, skip and wait for a number at 100 thousandth's place.
                thousand_connector = ' Thousand' if words == '' else ' Thousand ' # If numbers up until now have been zeroes, extra space at end of 'Thousand' isn't needed.
                if temp <= 10:
                    words = ones_place[temp] + thousand_connector + words
                elif temp > 10 and temp < 20:
                    words = eleven_to_nineteen[temp - 11] + thousand_connector + words
                else: # If the number is above 20 and below 99.
                    temp_ones = temp % 10 # Number at thousandth's place
                    temp_tens = temp // 10 # Number at ten thousandth's place
                    connector = ' ' if temp_ones != 0 else ''
                    words = tens_place[temp_tens] + connector + ones_place[temp_ones] + thousand_connector + words
            # Since we're dealing with two numbers, the following two lines are necessary.
            current_place += 1
            value //= 10

        elif current_place == 6:
            lakh_connector = ' Lakh' if words == '' else ' Lakh ' # If numbers up until now have been zeroes, extra space at end of 'Lakh' isn't needed.
            words = ones_place[current_digit] + lakh_connector + words

        # After processing each digit, increase current_place and remove the last digit of input.
        current_place += 1
        value //= 10

    if is_decimal:
        words += ' {}/100'.format(decimal)

    return 'Rs. ' + words + ' ONLY'
