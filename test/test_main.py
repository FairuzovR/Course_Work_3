# from src.main import *
# from src.utils import * -добавил эксперементально
# from src.classfile import *  добавил эксперементально
#
#
# fail_list = [
#     {
#     'id': 207126257, 'state': 'EXECUTED', 'date': '2019-07-15T11:47:40.496961',
#     'operationAmount': {'amount': '92688.46', 'currency': {'name': 'USD', 'code': 'USD'}},
#     'description': 'Открытие вклада', 'to': 'Счет 35737585785074382265'
#     },
#     {
#         'id': 667307132, 'state': 'EXECUTED', 'date': '2019-07-13T18:51:29.313309',
#         'operationAmount': {'amount': '97853.86', 'currency': {'name': 'руб.', 'code': 'RUB'}},
#         'description': 'Перевод с карты на счет', 'from': 'Maestro 1308795367077170', 'to':
#         'Счет 96527012349577388612'
#     }]
#
# def test_start_code():
#     assert start_code(fail_list) == ('15.07.2019 Открытие вклада\n'
#                                      'Счет **2265\n'
#                                      '92688.46 USD\n\n'
#                                      '13.07.2019 Перевод с карты на счет\n'
#                                      'Maestro 1308 79 ** ** ** 7170 -> Счет ** 8612\n'
#                                      '97853.86 руб.')
