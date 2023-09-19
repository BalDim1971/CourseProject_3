#########################################################################################
# Тестирование функций просмотра транзакций
#########################################################################################

import pytest
from utils import view_transaction

def test_load_operations():
	assert view_transaction.load_operation('') == []
	assert view_transaction.load_operation('oper.json') == []


def test_create_last_five_operations():
	assert view_transaction.view_last_five_operations([]) == []
	
#########################################################################################
