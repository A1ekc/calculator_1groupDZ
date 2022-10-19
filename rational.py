# для проверки ввела тут данные на вход. Работает корректно, если снять комментирование с вводных
# a = 1/2
# b = 1/2
# operand = '+'
# logger as log
#log.logger(f'{a} + {b} = {result}')  вставлять после каждого result 
#def calc_rational(type, a, operand, b):  eсли type == 2 то делать расчёт если 1 то нет) для комплексных наоборот
def calc_rational(x, y, znak): 
    global a
    global b
    global operand
x = a
y = b
znak = operand
if znak == '+':
    result = x + y
    print(result)
elif znak == '-':
     result = a-b
     print (result)
elif znak == '*':
    result = a * b
    print(result)
elif znak == '/':
    result = a / b
    print(result)
else: print('Error operation point. Enter correct operation')
