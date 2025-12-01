def calculadora(op = str):

    def soma(num1, num2):
        return num1 + num2
    def mult(num1, num2):
        return num1 * num2
    def sub(num1, num2):
        return num1 - num2
    def div(num1, num2):
        return num1 / num2
    def pot(num1, num2):
        return num1 ** num2
    
    match op:
        case "+":
            return soma
        case "-":
            return sub
        case "*":
            return mult
        case "**":
            return pot
        case "/":
            return div
        case _:
            return "Digite operadores válidos"
        
print(calculadora("+")(5, 9))