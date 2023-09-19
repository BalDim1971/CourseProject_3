#########################################################################################
# Тестирование функций просмотра транзакций
#########################################################################################

from utils.view_transaction import *


def test_sort_list_operation():
	assert sort_list_operation([]) == []
	assert sort_list_operation([{'date': '2019-12-08T22:46:21.935582'}, {'date': '2018-04-04T17:33:34.701093'}, {}]) == [{'date': '2019-12-08T22:46:21.935582'}, {'date': '2018-04-04T17:33:34.701093'}]
	assert sort_list_operation([{'date': '2018-04-04T17:33:34.701093'}, {'date': '2019-12-08T22:46:21.935582'}, {}]) == [{'date': '2019-12-08T22:46:21.935582'}, {'date': '2018-04-04T17:33:34.701093'}]


def test_load_operations():
	assert load_operation('') == []
	assert load_operation('oper.json') == []
#	assert load_operation('oper_test.json') == [{'id': 441945886}]


def test_view_last_five_operations():
	assert view_last_five_operations([]) == ''
	test_oper =	[{'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'},
	{'id': 114832369, 'state': 'EXECUTED', 'date': '2019-12-07T06:17:14.634890', 'operationAmount': {'amount': '48150.39', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Classic 2842878893689012', 'to': 'Счет 35158586384610753655'},
	{'id': 560813069, 'state': 'CANCELED', 'date': '2019-12-03T04:27:03.427014', 'operationAmount': {'amount': '17628.50', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 1796816785869527', 'to': 'Visa Classic 7699855375169288'},
	{'id': 154927927, 'state': 'EXECUTED', 'date': '2019-11-19T09:22:25.899614', 'operationAmount': {'amount': '30153.72', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Maestro 7810846596785568', 'to': 'Счет 43241152692663622869'},
	{'id': 482520625, 'state': 'EXECUTED', 'date': '2019-11-13T17:38:04.800051', 'operationAmount': {'amount': '62814.53', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 38611439522855669794', 'to': 'Счет 46765464282437878125'},
	{'id': 801684332, 'state': 'EXECUTED', 'date': '2019-11-05T12:04:13.781725', 'operationAmount': {'amount': '21344.35', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 77613226829885488381'},
	{'id': 509645757, 'state': 'EXECUTED', 'date': '2019-10-30T01:49:52.939296', 'operationAmount': {'amount': '23036.03', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Visa Gold 7756673469642839', 'to': 'Счет 48943806953649539453'}
	]
	assert view_last_five_operations(test_oper) == '''08.12.2019 Открытие вклада
Счет **5907
41096.24 USD

07.12.2019 Перевод организации
Visa Classic 2842 87** **** 9012 -> Счет **3655
48150.39 USD

19.11.2019 Перевод организации
Maestro 7810 84** **** 5568 -> Счет **2869
30153.72 руб.

13.11.2019 Перевод со счета на счет
Счет **9794 -> Счет **8125
62814.53 руб.

05.11.2019 Открытие вклада
Счет **8381
21344.35 руб.
'''


def test_string_check():
	assert string_check('Visa Classic 8906171742833215') == 'Visa Classic 8906 17** **** 3215'
	assert string_check('Счет 79619011266276091215') == 'Счет **1215'


def test_string_from_to():
	assert string_from_to({'from': 'Visa Classic 8906171742833215', 'to': 'Visa Platinum 6086997013848217'}) == 'Visa Classic 8906 17** **** 3215 -> Visa Platinum 6086 99** **** 8217'
	assert string_from_to({'to': 'Visa Platinum 6086997013848217'}) == 'Visa Platinum 6086 99** **** 8217'

#########################################################################################