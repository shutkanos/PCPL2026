import sys
import math


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    coef = float(coef_str)
    return coef

def get_tipa_sqrt(coef):
    if coef < 0:
        return []
    elif coef == 0:
        return [0]
    root = coef ** 0.5
    return [root, -root]

class Main:
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C

    def get_result(self):
        result = []
        D = self.B * self.B - 4 * self.A * self.C
        if D == 0.0:
            root = -self.B / (2.0 * self.A)
            result.extend(get_tipa_sqrt(root))
        elif D > 0.0:
            sqD = math.sqrt(D)
            root1 = (-self.B + sqD) / (2.0 * self.A)
            root2 = (-self.B - sqD) / (2.0 * self.A)
            result.extend(get_tipa_sqrt(root1))
            result.extend(get_tipa_sqrt(root2))
        return D, result


def main():
    '''
    Основная функция
    '''
    a = get_coef(1, 'Введите коэффициент А:')
    b = get_coef(2, 'Введите коэффициент B:')
    c = get_coef(3, 'Введите коэффициент C:')
    # Вычисление корней
    main_obj = Main(a, b, c)
    D, roots = main_obj.get_result()
    # Вывод корней
    print(f"Дискриминант: {D}, Корни: {sorted(roots)}")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()

# Пример запуска
# qr.py 1 0 -4