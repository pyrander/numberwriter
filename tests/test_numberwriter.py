from src.numberwriter import NumberToWords


def test_convert():

    # Create an instance of the NumbertoWords class
    number_to_words = NumberToWords()
    assert number_to_words.convert(0) == "CERO Y 00/100 SOLES"
    assert number_to_words.convert(1) == "UNO Y 00/100 SOLES"
    assert number_to_words.convert(2) == "DOS Y 00/100 SOLES"
    assert number_to_words.convert(3) == "TRES Y 00/100 SOLES"
    assert number_to_words.convert(4.50) == "CUATRO Y 50/100 SOLES"
    assert number_to_words.convert(5.89) == "CINCO Y 89/100 SOLES"
    assert number_to_words.convert(6) == "SEIS Y 00/100 SOLES"
    assert number_to_words.convert(7) == "SIETE Y 00/100 SOLES"
    assert number_to_words.convert(8) == "OCHO Y 00/100 SOLES"
    assert number_to_words.convert(9) == "NUEVE Y 00/100 SOLES"
    assert number_to_words.convert(10) == "DIEZ Y 00/100 SOLES"
    assert number_to_words.convert(11) == "ONCE Y 00/100 SOLES"
    assert number_to_words.convert(12) == "DOCE Y 00/100 SOLES"
    assert number_to_words.convert(13) == "TRECE Y 00/100 SOLES"
    assert number_to_words.convert(14) == "CATORCE Y 00/100 SOLES"
    assert number_to_words.convert(15) == "QUINCE Y 00/100 SOLES"
    assert number_to_words.convert(16) == "DIECISEIS Y 00/100 SOLES"
    assert number_to_words.convert(20) == "VEINTE Y 00/100 SOLES"
    assert number_to_words.convert(21) == "VEINTIUNO Y 00/100 SOLES"
    assert number_to_words.convert(22) == "VEINTIDOS Y 00/100 SOLES"
    assert number_to_words.convert(30) == "TREINTA Y 00/100 SOLES"
    assert number_to_words.convert(31) == "TREINTIUNO Y 00/100 SOLES"
    assert number_to_words.convert(40) == "CUARENTA Y 00/100 SOLES"
    assert number_to_words.convert(41.7) == "CUARENTIUNO Y 70/100 SOLES"
    assert number_to_words.convert(90) == "NOVENTA Y 00/100 SOLES"
    assert number_to_words.convert(100) == "CIEN Y 00/100 SOLES"
    assert number_to_words.convert(101) == "CIENTO UNO Y 00/100 SOLES"
    assert number_to_words.convert(200) == "DOSCIENTOS Y 00/100 SOLES"
    assert number_to_words.convert(333) == "TRESCIENTOS TREINTITRES Y 00/100 SOLES"
    assert number_to_words.convert(1000) == "MIL Y 00/100 SOLES"
    assert number_to_words.convert(2000) == "DOS MIL Y 00/100 SOLES"
    assert (
        number_to_words.convert(3333)
        == "TRES MIL TRESCIENTOS TREINTITRES Y 00/100 SOLES"
    )
    assert number_to_words.convert(4000) == "CUATRO MIL Y 00/100 SOLES"
    assert number_to_words.convert(5000) == "CINCO MIL Y 00/100 SOLES"
    assert number_to_words.convert(6000) == "SEIS MIL Y 00/100 SOLES"
    assert number_to_words.convert(7000) == "SIETE MIL Y 00/100 SOLES"
    assert number_to_words.convert(8000) == "OCHO MIL Y 00/100 SOLES"
    assert number_to_words.convert(9000) == "NUEVE MIL Y 00/100 SOLES"
    assert number_to_words.convert(16000) == "DIECISEIS MIL Y 00/100 SOLES"
    assert number_to_words.convert(20000) == "VEINTE MIL Y 00/100 SOLES"
    assert (
        number_to_words.convert(21674.55)
        == "VEINTIUN MIL SEISCIENTOS SETENTICUATRO Y 55/100 SOLES"
    )
    assert number_to_words.convert(30000) == "TREINTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(40000) == "CUARENTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(50000) == "CINCUENTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(60000) == "SESENTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(70000) == "SETENTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(80000) == "OCHENTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(90000) == "NOVENTA MIL Y 00/100 SOLES"
    assert number_to_words.convert(100000) == "CIEN MIL Y 00/100 SOLES"
    assert number_to_words.convert(500000) == "QUINIENTOS MIL Y 00/100 SOLES"
    assert number_to_words.convert(900000) == "NOVECIENTOS MIL Y 00/100 SOLES"
    assert number_to_words.convert(1000001) == "UN MILLON UNO Y 00/100 SOLES"
    assert number_to_words.convert(1000100) == "UN MILLON CIEN Y 00/100 SOLES"
    assert number_to_words.convert(1001000) == "UN MILLON MIL Y 00/100 SOLES"
    assert number_to_words.convert(1010000) == "UN MILLON DIEZ MIL Y 00/100 SOLES"
    assert (
        number_to_words.convert(1600000) == "UN MILLON SEISCIENTOS MIL Y 00/100 SOLES"
    )
    assert number_to_words.convert(2000000) == "DOS MILLONES Y 00/100 SOLES"
    assert number_to_words.convert(2000000.50) == "DOS MILLONES Y 50/100 SOLES"
    assert (
        number_to_words.convert(9493516)
        == "NUEVE MILLONES CUATROCIENTOS NOVENTITRES MIL QUINIENTOS DIECISEIS Y 00/100 SOLES"
    )
    assert (
        number_to_words.convert(15999999)
        == "QUINCE MILLONES NOVECIENTOS NOVENTINUEVE MIL NOVECIENTOS NOVENTINUEVE Y 00/100 SOLES"
    )
    assert number_to_words.convert(20000000) == "VEINTE MILLONES Y 00/100 SOLES"
    assert (
        number_to_words.convert(32500000)
        == "TREINTIDOS MILLONES QUINIENTOS MIL Y 00/100 SOLES"
    )
    assert (
        number_to_words.convert(61232288.64)
        == "SESENTIUN MILLONES DOSCIENTOS TREINTIDOS MIL DOSCIENTOS OCHENTIOCHO Y 64/100 SOLES"
    )
    assert (
        number_to_words.convert(81307476.37)
        == "OCHENTIUN MILLONES TRESCIENTOS SIETE MIL CUATROCIENTOS SETENTISEIS Y 37/100 SOLES"
    )
    assert number_to_words.convert(100000000) == "CIEN MILLONES Y 00/100 SOLES"
    assert number_to_words.convert(100000001) == "CIEN MILLONES UNO Y 00/100 SOLES"
    assert number_to_words.convert(100000010) == "CIEN MILLONES DIEZ Y 00/100 SOLES"
    assert (
        number_to_words.convert(100000110) == "CIEN MILLONES CIENTO DIEZ Y 00/100 SOLES"
    )
    assert number_to_words.convert(100001000) == "CIEN MILLONES MIL Y 00/100 SOLES"
    assert number_to_words.convert(100010000) == "CIEN MILLONES DIEZ MIL Y 00/100 SOLES"
    assert number_to_words.convert(100100000) == "CIEN MILLONES CIEN MIL Y 00/100 SOLES"
    assert (
        number_to_words.convert(100999000)
        == "CIEN MILLONES NOVECIENTOS NOVENTINUEVE MIL Y 00/100 SOLES"
    )
    assert (
        number_to_words.convert(100999999)
        == "CIEN MILLONES NOVECIENTOS NOVENTINUEVE MIL NOVECIENTOS NOVENTINUEVE Y 00/100 SOLES"
    )
