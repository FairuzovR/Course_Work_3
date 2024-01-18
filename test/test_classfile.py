from src.classfile import Transactiondata


def test_data_operation():
    assert check_instance.data_operation() == '05.01.2019'


def test_status_description():
    assert check_instance.status_description() == 'Перевод со счета на счет'


def test_sent_from():
    assert check_instance.sent_from() == 'Счет **8266 -> '
    assert check_instance_2.sent_from() == 'Visa Gold 8326 53** **** 6459 -> '
    assert check_instance_3.sent_from() == 'Visa Gold 8326 53** **** **** 1010 -> '


def test_sent_to():
    assert check_instance.sent_to() == 'Счет **8409'
    assert check_instance_2.sent_to() == 'MasterCard 6783 91** **** 1847'
    assert check_instance_3.sent_to() == 'MasterCard 6783 91** **** **** 1010'


def test_displays_amount():
    assert check_instance.displays_amount() == '87941.37'


def test_displays_currency():
    assert check_instance.displays_currency() == 'руб.'


check_instance = Transactiondata(957763565, '2019-01-05T00:52:30.108534', 'EXECUTED',
                                 {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                 'Перевод со счета на счет', 'Счет 46363668439560358409',
                                 'Счет 18889008294666828266')

check_instance_2 = Transactiondata(957763565, '2019-01-05T00:52:30.108534', 'EXECUTED',
                                   {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                   'Перевод со счета на счет', 'MasterCard 6783917276771847',
                                   'Visa Gold 8326537236216459')

check_instance_3 = Transactiondata(957763565, '2019-01-05T00:52:30.108534', 'EXECUTED',
                                   {'amount': '87941.37', 'currency': {'name': 'руб.', 'code': 'RUB'}},
                                   'Перевод со счета на счет', 'MasterCard 67839172767718471010',
                                   'Visa Gold 83265372362164591010')