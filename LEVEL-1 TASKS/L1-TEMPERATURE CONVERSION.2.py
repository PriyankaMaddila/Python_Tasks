#level1-T2
# Prompt the user for input
value = float(input('Enter the temperature value: '))
scale = input('Enter the temperature scale (C or F): ').upper()

# Convert the temperature and print the result
if scale == 'C':
    result = value * 1.8 + 32
    print(f'{value} C = {result} F')
elif scale == 'F':
    result = (value - 32) / 1.8
    print(f'{value} F = {result} C')
else:
    print('Invalid temperature scale')
