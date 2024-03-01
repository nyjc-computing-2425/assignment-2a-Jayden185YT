num = input('Enter a number (decimal or integer): ')
# type your code here
number = str(num)
number = number.strip()
number = number.replace('.', '')
number = number.lstrip('0')
sf = len(number)


# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
