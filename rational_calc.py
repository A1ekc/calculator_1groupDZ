from logger import  logger
def calc (num1, num2, znak):
    if znak == '+':
        logger(f'{num1} + {num2} = {num1 +num2}')
        return num1 + num2
    elif znak == '-':
        logger(f'{num1} - {num2} = {num1 - num2}')
        return num1 - num2
    elif znak == '*':
        logger(f'{num1} * {num2} = {num1 * num2}')
        return num1 * num2
    elif znak == '/':
        logger(f'{num1} / {num2} = {num1 / num2}')
        return num1 / num2
