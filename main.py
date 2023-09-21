################################################################################
'''
Программа выводит на экран список из 5 последних выполненных клиентом операций
по переводу денежных средств
'''
################################################################################

# Подключаем конфигурационный файл с именем файла, cодержащим список операций клиента
from data.config import name_file_operations
from utils.view_transaction import *
from datetime import datetime

def main():
	'''
	Основная функция, вызывает функции по работе со списком операций
	'''
	
	# Читаем список операций из файла name_file_operations
	list_operation = load_operation(name_file_operations)

	# Пустой список выходим
	if len(list_operation) == 0:
		return
	
	# Сортируем список по убыванию
	list_operation.sort(key=lambda k: k['date'], reverse = True)

	# Выводим последние 5 операций
	my_view_operation = view_last_five_operations(list_operation)
	print(my_view_operation)

if __name__== '__main__':
	main()

################################################################################