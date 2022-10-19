#файл объединяет отдельные методы
import view as v
import rational as r
import logger as l


def button_click():# Опишим метод кнопки
    print(r.calc(v.input_data()))
    
#print(v.input_data())