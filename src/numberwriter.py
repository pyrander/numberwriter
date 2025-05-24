import re
import random
import time


class NumberToWords:
    def __init__(self):
        self.thousandsInfix = " MIL "
        self.millionInfix = " MILLON "
        self.millionsInfix = " MILLONES "
        self.moneda = "SOLES"
        self.quincenas = [
            "",
            "UN",
            "DOS",
            "TRES",
            "CUATRO",
            "CINCO",
            "SEIS",
            "SIETE",
            "OCHO",
            "NUEVE",
            "DIEZ",
            "ONCE",
            "DOCE",
            "TRECE",
            "CATORCE",
            "QUINCE",
        ]
        self.decenas = [
            "",
            "DIEZ",
            "VEINTE",
            "TREINTA",
            "CUARENTA",
            "CINCUENTA",
            "SESENTA",
            "SETENTA",
            "OCHENTA",
            "NOVENTA",
            "CIEN",
        ]
        self.decenarios = [
            "",
            "DIECI",
            "VEINTI",
            "TREINTI",
            "CUARENTI",
            "CINCUENTI",
            "SESENTI",
            "SETENTI",
            "OCHENTI",
            "NOVENTI",
        ]
        self.centenas = [
            "",
            "CIENTO ",
            "DOSCIENTOS ",
            "TRESCIENTOS ",
            "CUATROCIENTOS ",
            "QUINIENTOS ",
            "SEISCIENTOS ",
            "SETECIENTOS ",
            "OCHOCIENTOS ",
            "NOVECIENTOS ",
            "MIL ",
        ]

    def validate_number(self, number):
        if isinstance(number, str):
            number = number.replace(",", ".")
            try:
                number = float(number)
            except ValueError:
                return False
        return isinstance(number, (int, float))

    def get_prefix(self, number):
        if number < 0:
            return "MENOS "
        elif number < 1:
            return "CERO "
        return ""

    def clean_spaces(self, text):
        text = re.sub(r"\s+", " ", text)  # Replace multiple spaces with a single space
        return text.strip()  # Remove leading and trailing spaces

    def convert(self, number):
        if not self.validate_number(number):
            raise ValueError("El número no es válido")

        prefix = self.get_prefix(number)
        result = prefix + self.convertir(abs(number), True)
        return self.clean_spaces(result)

    def get_suffix_and_currency(self, number):
        number = round(number, 2)
        number = int(number * 100)
        return f" Y {number:02}/100 {self.moneda}"

    def convertir(self, number, top=False):
        if number < 1:
            return self.get_suffix_and_currency(number)
        elif 0 < number < 16:
            return self.unidades(number)
        elif number < 101:
            return self.diesmos(number)
        elif number < 1001:
            return self.cientos(number)
        elif number < 16000:
            return self.miles(number, top)
        elif number < 101000:
            return self.diezmiles(number)
        elif number < 1000000:
            return self.cienmiles(number)
        elif number < 16000000:
            return self.millones(number, top)
        elif number < 101000000:
            return self.diezmillones(number)

        return ""

    def unidades(self, number):
        if int(number) == 1:
            prefix = "UNO"
        else:
            prefix = self.quincenas[int(number)]
        return prefix + self.convertir(number - int(number))

    def diesmos(self, number):
        index = int(number / 10)
        remainder = number % 10
        if int(remainder) == 0:
            prefix = self.decenas[index]
        else:
            prefix = self.decenarios[index]
        return prefix + self.convertir(remainder)

    def cientos(self, number):
        index = int(number / 100)
        remainder = number % 100
        prefix = self.centenas[index]
        return prefix + self.convertir(remainder)

    def miles(self, number, top):
        index = int(number / 1000)
        remainder = number % 1000
        if index == 1 and top:
            index = 0
        prefix = self.quincenas[index] + self.thousandsInfix
        return prefix + self.convertir(remainder)

    def diezmiles(self, number):
        index = int(number / 10000)
        remainder = number % 10000
        if int(remainder / 1000) == 0:
            prefix = self.decenas[index] + self.thousandsInfix
        else:
            prefix = self.decenarios[index]
        return prefix + self.convertir(remainder)

    def cienmiles(self, number):
        index = int(number / 100000)
        remainder = number % 100000
        prefix = self.centenas[index]
        if int(remainder / 1000) == 0:
            prefix += self.thousandsInfix
        return prefix + self.convertir(remainder)

    def millones(self, number, top):
        index = int(number / 1000000)
        remainder = number % 1000000
        if index == 1 and top:
            infix = self.millionInfix
        else:
            infix = self.millionsInfix

        prefix = self.quincenas[index] + infix
        return prefix + self.convertir(remainder)

    def diezmillones(self, number):
        index = int(number / 10000000)
        remainder = number % 10000000
        if int(remainder / 1000000) == 0:
            prefix = self.decenas[index] + self.millionsInfix
        else:
            prefix = self.decenarios[index]
        return prefix + self.convertir(remainder)


if __name__ == "__main__":
    start_time = time.time()
    number_to_words = NumberToWords()
    number = round(random.uniform(0, 100), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(101, 1001), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(1001, 10000), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(10001, 100000), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(100001, 1000000), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(1000001, 10000000), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(10000001, 15999999), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    number = round(random.uniform(16000000, 100999999), 2)
    print(f"Random number: {number}")
    print(f"Number in words: {number_to_words.convert(number)}")
    print(f"Execution time: {time.time() - start_time}")
