
from fractions import Fraction
def input_data():
    type = input('С какими числами будем работать? 1 -комплексные числа, 2 - рациональные числа')
    num1 = None
    num2 = None
    znak = None
    if type == '1':
        num1 = complex(input('Введите первое число (используйте формат: "5+3j "):'))
        num2 = complex(input('Введите второе число (используйте формат: "5+3j "):'))
        znak = input('Выберите операцию:')
    elif type == '2':
        num1 = Fraction(input('Введите первое число (используйте формат: "5/11 "):'))
        num2 = Fraction(input('Введите второе число (используйте формат: "5/11 "):'))
        znak = input('Выберите операцию(+,-,*,/):')
    return num1, num2, znak
