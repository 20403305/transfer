from typing import Union
from decimal import Decimal


def float_format(num1: Union[int, str, float], operator: str, num2: Union[int, str, float], scale: int = 2, is_round: bool = True) -> str:
    """
    两个数的高精度计算
    :param num1:数字1
    :param operator: 操作符，目前仅仅支持 + - * /
    :param num2:数字2
    :param scale: 保留的小数个数
    :param is_round:是否四舍五入
    :return:
    """
    a, b = Decimal(str(num1)), Decimal(str(num2))

    if operator == '+':
        c = a + b
    elif operator == '-':
        c = a - b
    elif operator == '*':
        c = a * b
    elif operator == '/':
        c = a / b
    else:
        raise Exception('operator not support')

    if scale < 1:
        scale = 1

    if is_round:
        precision = '.{}'.format('0' * scale)
        # 等价于 f'{c:.{scale}f}'
        return str(c.quantize(Decimal(precision), rounding=ROUND_HALF_UP))

    integer, _, decimal = str(c).partition('.')

    zero = '0'

    if not decimal:
        decimal = zero[:scale]

    decimal_len = len(decimal)

    if decimal_len < scale:
        decimal = '{}{}'.format(decimal, zero * (scale - decimal_len))
    else:
        decimal = decimal[:scale]

    return f'{integer}.{decimal}'


def float_compare(num1: Union[int, str, float], compare_char: str, num2: Union[int, str, float]) -> bool:
    """
    浮点数比较
    :param num1:
    :param compare_char: 比较运算符
    :param num2:
    :return:
    """
    a, b = Decimal(str(num1)), Decimal(str(num2))
    if compare_char not in ['==', '!=', '>', '>=', '<', '<=']:
        raise Exception('compare_char not support')

    expression = f'{a}{compare_char}{b}'
    return eval(expression)