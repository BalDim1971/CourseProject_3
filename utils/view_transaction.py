#########################################################################################
# Функции просмотра операций клиента
#########################################################################################

import json
from datetime import datetime


def load_operation(name_file):
	'''
	Функция чтения данных по операциям из json-файла
	и преобразования в формат Python
	:param name_file: имя файла с данными в формате json
	:return: список данных
	'''
	
	# Инициируем переменные
	list_operation = []
	
	# Открываем файл с проверкой по исключению
	try:
		with open(name_file, "r", encoding="utf-8") as f:
			raw_json = f.read()
	
	# Нет файла, выкидываем пустой список
	except FileNotFoundError:
		return list_operation
	
	# Преобразуем json в стандартный список Python
	list_operation = json.loads(raw_json)
	
	while {} in list_operation:
		list_operation.remove({})

	return list_operation


def string_check(str_check):
	'''
	Формируем строку для засекречивания номера счета (карты)
	:param str_check: счет (карта) и номер
	:return: строка с частично скрытым номером
	'''
	
	if str_check.find("Счет") != -1:
		temp_str = "Счет **" + str_check[-4:]
	else:
		temp_str = str_check[-16:]
		array_4 = []
		for i in range(4):
			array_4.append(temp_str[i*4:i*4+4])
			if i == 1:
				array_4[i] = array_4[i][0:2] + "**"
			if i == 2:
				array_4[i] = "****"
		
		temp_str = " ".join(array_4)
		temp_str = str_check[0:-16] + temp_str
	
	return temp_str


def string_from_to(operation):
	'''
	Функция формирует строку с данными с какого счета (при наличии)
	на какой счет переводили
	:param operation: данные по оперции
	:return: строка номер счета (карточки) -> номер счета или просто номер счета
	'''
	
	# Инициируем переменные
	str_from = ''
	
	# Откуда переводим есть данные?
	if "from" in operation.keys():
		temp_str = operation["from"]
		temp_str = string_check(temp_str)
		str_from = f'{temp_str} -> '
	
	temp_str = operation["to"]
	temp_str = string_check(temp_str)
	str_to = temp_str
	
	return str_from + str_to

def view_last_five_operations(list_operation):
	'''
	Выводит на экран список из 5 последних операций,
	Формат списка:
	дата название
	карта -> счет
	сумма валюта
	:param list_operation:
	:return:
	'''
	
	# Проверяем на пустоту список
	if len(list_operation) == 0:
		return ''
	
	# Инициируем переменную для остановки вывода
	count = 0
	
	# Строка для вывода на экран
	my_view_operation = ''
	
	# Основной цикл вывода данных
	for i in range(len(list_operation)):
		
		# Вывели 5 строк?
		if count == 5 :
			break
		
		# Операция выполнена?
		if list_operation[i]['state'] == 'EXECUTED':
			count += 1
			
			date_object = datetime.strptime(list_operation[i].get('date'), "%Y-%m-%dT%H:%M:%S.%f")
			my_view_operation += f'{date_object.strftime("%d.%m.%Y")} {list_operation[i]["description"]}\n'
			
			my_view_operation += string_from_to(list_operation[i]) + '\n'
			
			# Формируем  строку с суммой
			my_view_operation += f'{list_operation[i]["operationAmount"]["amount"]} {list_operation[i]["operationAmount"]["currency"]["name"]}\n'
			if count < 5:
				my_view_operation += '\n'
		
	return my_view_operation

#########################################################################################
