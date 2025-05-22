import re
import random


class NumberToWords:
    def __init__(self):
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
        self.millares = [
            "",
            "MIL ",
            "DOS MIL ",
            "TRES MIL ",
            "CUATRO MIL ",
            "CINCO MIL ",
            "SEIS MIL ",
            "SIETE MIL ",
            "OCHO MIL ",
            "NUEVE MIL ",
            "DIECISEIS MIL ",
        ]

    def validate_number(self, number):
        if isinstance(number, str):
            number = number.replace(",", ".")
            try:
                number = float(number)
            except ValueError:
                return False
        return isinstance(number, (int, float))

    def convert(self, number):
        if not self.validate_number(number):
            raise ValueError("El número no es válido")

        prefix = ""
        if number < 0:
            prefix = "MENOS "
            number = abs(number)
        elif number < 1:
            prefix = "CERO "
        result = prefix + self.convertir(number)
        result = re.sub(
            r"\s+", " ", result
        )  # Replace multiple spaces with a single space
        return result.strip()  # Remove leading and trailing spaces

    def convertir(self, number):
        if number < 1:
            number = round(number, 2)
            number = int(number * 100)
            return f" Y {number:02}/100 {self.moneda}"
        elif 0 < number < 16:
            return self.unidades(number)
        elif number < 101:
            return self.diesmos(1, number)
        elif number < 1001:
            return self.cientos(1, number)
        elif number < 16000:
            return self.miles(1, number)
        elif number < 101000:
            return self.diezmiles(1, number)
        elif number < 1000000:
            return self.cienmiles(1, number)
        elif number < 16000000:
            return self.millones(1, number)

        return ""

    def unidades(self, number):
        if number == 1:
            prefix = "UNO"
        else:
            prefix = self.quincenas[int(number)]
        return prefix + self.convertir(number - int(number))

    def diesmos(self, index, number):
        if index < 11:
            next_upper_threshold = (index + 1) * 10
            if next_upper_threshold > number:
                if index * 10 != int(number):
                    prefix = self.decenarios[index]
                else:
                    prefix = self.decenas[index]
                return prefix + self.convertir(10 - (next_upper_threshold - number))
            return self.diesmos(index + 1, number)
        return ""

    def cientos(self, index, number):
        if index < 11:
            next_upper_threshold = (index + 1) * 100
            if next_upper_threshold > number:
                return self.centenas[index] + self.convertir(
                    100 - (next_upper_threshold - number)
                )
            return self.cientos(index + 1, number)
        return ""

    def miles(self, index, number):
        if index < 16:
            next_upper_threshold = (index + 1) * 1000
            if next_upper_threshold > number:
                return (
                    self.quincenas[index]
                    + " MIL "
                    + self.convertir(1000 - (next_upper_threshold - number))
                )
            return self.miles(index + 1, number)
        return ""

    def diezmiles(self, index, number):
        if index < 11:
            next_upper_threshold = (index + 1) * 10000
            if next_upper_threshold > number:
                if number - (index * 10000) >= 1000:
                    prefix = self.decenarios[index]
                else:
                    prefix = self.decenas[index] + " MIL "
                return prefix + self.convertir(10000 - (next_upper_threshold - number))
            return self.diezmiles(index + 1, number)
        return ""

    def cienmiles(self, index, number):
        if index < 11:
            next_upper_threshold = (index + 1) * 100000
            if next_upper_threshold > number:
                if number - (index * 100000) < 1000:
                    prefix = self.centenas[index] + " MIL "
                else:
                    prefix = self.centenas[index]
                return prefix + self.convertir(100000 - (next_upper_threshold - number))
            return self.cienmiles(index + 1, number)
        return ""

    def millones(self, index, number):
        if index < 16:
            next_upper_threshold = (index + 1) * 1000000
            if next_upper_threshold > number:
                if index == 1:
                    infix = " MILLON "
                else:
                    infix = " MILLONES "
                return (
                    self.quincenas[index]
                    + infix
                    + self.convertir(1000000 - (next_upper_threshold - number))
                )

            return self.millones(index + 1, number)
        return ""


if __name__ == "__main__":
    number_to_words = NumberToWords()
    for index in range(1, 5):
        number = round(random.uniform(0, 1999999), 2)
        print(f"Random number: {number}")
        print(f"Number in words: {number_to_words.convert(number)}")
