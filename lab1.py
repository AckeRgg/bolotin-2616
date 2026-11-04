import sys
import math

MAX_VALUE = 10000

# проверяем параметры
if len(sys.argv) == 1:
    help = True
elif sys.argv[1] == "--help":
    help = True
else:
    help = False

if help == True:
    print("mathtool - решение уравнений вида A*x^2 + B*x + C = 0")
    print("")
    print("Использование:")
    print("    python mathtool.py                         вывод справки")
    print("    python mathtool.py --help                  вывод справки")
    print("    python mathtool.py solve                   ввод коэффициентов с клавиатуры")
    print("    python mathtool.py solve -a 1 -b -3 -c 2   решение с заданными коэффициентами")
    print("")
    print("Коэффициенты A, B, C - целые числа, по модулю не превышающие 10000.")
    sys.exit(0)

if sys.argv[1] != "solve":
    print("ОШИБКА: неизвестная команда", file=sys.stderr)
    sys.exit(1)

# вводим числа
if len(sys.argv) == 2:
    a = input("Введите A: ")
    b = input("Введите B: ")
    c = input("Введите C: ")
elif len(sys.argv) == 8:
    if sys.argv[2] != "-a":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    if sys.argv[4] != "-b":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    if sys.argv[6] != "-c":
        print("ОШИБКА: неизвестный параметр", file=sys.stderr)
        sys.exit(1)
    a = sys.argv[3]
    b = sys.argv[5]
    c = sys.argv[7]
else:
    print("ОШИБКА: неверный набор параметров", file=sys.stderr)
    sys.exit(1)

# переводим в int
try:
    a = int(a)
    b = int(b)
    c = int(c)
except ValueError:
    print("ОШИБКА: коэффициент не является целым числом", file=sys.stderr)
    sys.exit(1)

# проверяем что числа не больше 10000
if abs(a) > MAX_VALUE or abs(b) > MAX_VALUE or abs(c) > MAX_VALUE:
    print("ОШИБКА: значение вне допустимого диапазона", file=sys.stderr)
    sys.exit(1)

# решаем уравнение
if a == 0:
    if b == 0:
        print("ОШИБКА: это не уравнение, неизвестное отсутствует", file=sys.stderr)
        sys.exit(1)
    else:
        print("Уравнение линейное")
        x = -c / b
        print(f"x = {x:.3f}")
else:
    print("Уравнение квадратное")
    d = b * b - 4 * a * c
    print("D =", d)
    if d > 0:
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        print(f"x1 = {x1:.3f}")
        print(f"x2 = {x2:.3f}")
    if d == 0:
        x = -b / (2 * a)
        print(f"x = {x:.3f}")
    if d < 0:
        print("Действительных корней нет")

