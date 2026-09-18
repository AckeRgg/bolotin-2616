import sys
import math


maxvalue = 10000
help_text = 
    "mathtool -- решение уровнений вида A*x^2 + B*x + C = 0"
    "python mathtool.py                         вывод справки"
    "python mathtool.py --help                  вывод справки"
    "python mathtool.py solve                   ввод коэффициентов с клавиатуры"
    "python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами" 
    "Коэффициенты A, B, C -- целые числа, по модулю не превышающие 10000"
    

def parse_args(argv):
        """
            Разбирает параметры командной строки (без имени файла программы).
        
            Возвращает кортеж строковых значений (a_str, b_str, c_str) или None,
            если коэффициенты нужно запросить у пользователя c клавиатуры.
            В случае ошибки выводит сообщение в stderr и завершает работу.
            """
        args = argv[1:]
    if len(args) == 0 or args[0] == "--help":
        print(help_text)
        sys.exit(0)
    if args[0] != "solve":
    print("Ошибка: неизвестная команда", file=sys.stderr)
    sys.exit(1)



if len(args) == 7:
    if args[1] != "-a" or args[3] != "-b" or args[5] != "-c":
        print("Ошибка: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    return args[2], args[4], args[6]

print("Ошибка: неверный набор параметров", file=sys.stderr)
sys.exit(1)



def read_from_keyboard():
    """Запрашивает коэффициенты у пользователя."""
    a_str = input("Введите A: ")
    b_str = input("Введите B: ")
    c_str = input("Введите C: ")
    return a_str, b_str, c_str


def to_int_coefficients(a_str, b_str, c_str):
    """
    Преобразует строковые коэффициенты в целые числа.
    При ошибке преобразования сообщает об этом и завершает работу с кодом 1
    """

    try:
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
    except ValueError:
         print("Ошибка: коэффициент не вявляется целым числом", file=sys.stderr)
         sys.exit(1)
    return a, b, c


def validate_range(a, b, c):
     if abs(a) > max_value or mabs(b) > max_value or abs(c) > max_value:
          print("Ошибка: значение вне допустимого диапазона", file-sys.stderr)
          sys.exit(1)




def solve_linear(b, c):
     """Решает уравнение B*x + C = 0 при B != 0 """