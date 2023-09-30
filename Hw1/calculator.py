# Задание 1. **
# В классе Calculator создайте метод calculateDiscount, который принимает сумму покупки и процент скидки и возвращает сумму с учетом скидки.
# Ваша задача - проверить этот метод с использованием библиотеки AssertJ.
# Если метод calculateDiscount получает недопустимые аргументы, он должен выбрасывать исключение ArithmeticException.
# Не забудьте написать тесты для проверки этого поведения.



def calculate(first_operand: int, second_operand: int, operator: str) -> int | float:
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("на 0 делить нельзя")
        case _:
            raise ValueError("не известный оператор, выберите другое значение: " + operator)
    return result



def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Скидка не может быть меньше нуля")
    elif discount_amount > 100:
        raise ArithmeticError("Скидка не может превышать 100")
    return purchase_amount - (purchase_amount * discount_amount) / 100



if __name__ == "__main__":
    print(calculate(4, 8, '-'))
    print(calculate(20, 10, '*'))
    print(calculate(20, 10, '/'))
    print(calculate_discount(1000, 100))
    print(calculate_discount(345, 15))
