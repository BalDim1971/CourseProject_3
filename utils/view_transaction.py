#########################################################################################
# Функции просмотра операций клиента
#########################################################################################

import json
from datetime import datetime


def sort_list_operation(list_operation):
	'''
	Сортируем список операций
	:param list_operation: список операций из файла
	:return: отсортированный по времени список
	'''
	
	for i in range(len(list_operation)-1):
		for j in range(len(list_operation)-1):
			if len(list_operation[j]) == 0:
				my_date_object = None
			else:
				my_date_object = datetime.strptime(list_operation[j].get('date'), "%Y-%m-%dT%H:%M:%S.%f")
			
			if len(list_operation[j+1]) == 0:
				date_operation = None
			else:
				date_operation = datetime.strptime(list_operation[j+1].get('date'), "%Y-%m-%dT%H:%M:%S.%f")
			
			if date_operation == None or my_date_object == None or my_date_object < date_operation:
				temp = list_operation[j]
				list_operation[j] = list_operation[j+1]
				list_operation[j+1] = temp
	
	return list_operation


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
	
	list_operation = sort_list_operation(list_operation)
	
	return list_operation


def create_last_five_operations(list_operation):
	'''
	Возвращает список из 5 последних операций,
	Формат списка: дата название карта счет сумма валюта
	:param list_operation:
	:return:
	'''
	
	last_five_operation = []
	
	if len(list_operation) == 0:
		return last_five_operation
	
	return last_five_operation

#########################################################################################
