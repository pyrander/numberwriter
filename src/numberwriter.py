import re
import math
import random
import time


class NumberToWords:
    def __init__(self):
        self.negativePrefix = "MENOS "
        self.zeroPrefix = "CERO "
        self.onePrefix = "UNO"
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
            prefix = self.negativePrefix
        elif number < 1:
            prefix = self.zeroPrefix
        else:
            prefix = ""
        return prefix

    def fix_threshold(self, number, threshold):
        #threshold can't be less than 1
        if threshold == 1:
            return threshold
        # there need to be fixes for numbers between 10 and 15
        # for numbers between 10001 and 15999 and 100001 and 101000
        # and 10000001 and 15999999 and 100000001 and 101000000
        specialcase = False
        if (
            number == threshold
            or 10 < number < 16
            or 10000 < number < 16000
            or 100000 < number < 101000
            or 10000000 < number < 16000000
            or 100000000 < number < 101000000
            
        ):
            specialcase = True

        if specialcase:
            return int(threshold / 10)
        return threshold

    def get_prefix_and_remainder(self, number, top=False):
        prefix = ""
        # Get the power of 10 for the number needed to determine index
        # and the threshold for the number
        power = int(math.log10(int(number)))
        # Get the threshold for the number, its the closest power of 10
        # that is less than the number
        threshold = int(math.pow(10, power))
        # Fix the threshold for special cases
        threshold = self.fix_threshold(number, threshold)
        # Get the index for the number, its the number divided by the threshold
        index = int(number / threshold)
        # Get the remainder for the number, its the number modulo the threshold
        remainder = number - int(number) if number < 16 else number % threshold
        if 1 <= number < 16:
            if index == 1:
                prefix = self.onePrefix
            else:
                prefix = self.quincenas[index]
        elif number < 101:
            if int(remainder) == 0:
                prefix = self.decenas[index]
            else:
                prefix = self.decenarios[index]
        elif number < 1001:
            prefix = self.centenas[index]
        elif number < 16000:
            if index == 1 and top:
                index = 0
            prefix = self.quincenas[index] + self.thousandsInfix
        elif number < 101000:
            if int(remainder / 1000) == 0:
                prefix = self.decenas[index] + self.thousandsInfix
            else:
                prefix = self.decenarios[index]
        elif number < 1000000:
            prefix = self.centenas[index]
            if int(remainder / 1000) == 0:
                prefix += self.thousandsInfix
        elif number < 16000000:
            if index == 1 and top:
                infix = self.millionInfix
            else:
                infix = self.millionsInfix
            prefix = self.quincenas[index] + infix
        elif number < 101000000:
            if int(remainder / 1000000) == 0:
                prefix = self.decenas[index] + self.millionsInfix
            else:
                prefix = self.decenarios[index]

        return {"prefix": prefix, "remainder": remainder}

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
        elif 1 <= number < 101000000:
            data = self.get_prefix_and_remainder(number, top)
            prefix = data.get("prefix")
            remainder = data.get("remainder")
            return prefix + self.convertir(remainder)
        elif number >= 101000000:
            raise ValueError("El número es demasiado grande")

        return ""


if __name__ == "__main__":
    """
    number_to_words = NumberToWords()
    print(f"Number in words: {number_to_words.convert(15999999)}")
    print(f"Number in words: {number_to_words.convert(15999)}")
    print(f"Number in words: {number_to_words.convert(15)}")
    print(f"Number in words: {number_to_words.convert(0)}")
    """

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
