
import logger as l
import view
def calc(num1, num2, znak):
    if znak == '+':
        l.logger(f'{num1} + {num2} = {num1 +num2}')
        print(num1 + num2)
        return num1 + num2      
    elif znak == '-':
        l.logger(f'{num1} - {num2} = {num1 - num2}')
        print(num1 - num2)
        return num1 - num2
    elif znak == '*':
        l.logger(f'{num1} * {num2} = {num1 * num2}')
        print(num1 * num2)
        return num1 * num2
    elif znak == '/':
        l.logger(f'{num1} / {num2} = {num1 / num2}')
        print(num1 / num2)
        return num1 / num2



