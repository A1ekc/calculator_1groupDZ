#файл объединяет отдельные методы

import compl
import rational
import view
import logger


def button_click():# Опишим метод кнопки
    value_a = view.get_value()
    value_b = view.get_value()
    compl.init(value_a, value_b)
    #result = ex046_lec.sum()
    result = compl()
    result = rational()
    view.view_data(result)

    # Кудато тут нужно вписать лог))
    write_log

