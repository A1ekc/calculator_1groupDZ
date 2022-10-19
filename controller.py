#файл объединяет отдельные методы
import view as v
import rational_calc as r

def button_click():# Опишем метод кнопки
    a, b, c = v.input_data()
    print(r.calc(a, b, c))