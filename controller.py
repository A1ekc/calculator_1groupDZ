#файл объединяет отдельные методы
import view 
import compl
import rational
import logger


def button_click():# Опишим метод кнопки
    value_a = view.get_value()
    value_b = view.get_value()
    value_oper = view.get_value()
    compl.init(value_a, value_b, value_oper)# ?
    rational.init(value_a, value_b,value_oper)# ?
    #result = ex046_lec.sum()
    #result = compl()
    #result = rational()
    #view.view_data(result)

