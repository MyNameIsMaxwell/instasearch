import re
import os

from get_profile_info import google_sheet_parse

path = os.path.abspath(os.path.join("./get_followers/pars_res.txt"))


def reformat_result(string: str) -> set:
	"""
	Функция через регулярные выражения получает id профилей из полного списка информации о подписчиках.
	:param string: строка с информацией об аккаунтах подписчиков.
	:return: user_id: множестово с id пользователей. Множество убирает повторяющиеся id.
	"""
	user_id = re.findall(r".'(\d+)'", string)
	return set(user_id)


def write_info_to_file(info: list) -> None:
	"""
	Функция, которая записывает id пользователей в файл pars_res.txt.
	Если надо можно записывать сразу в таблицу google sheets. (Закомментировано)  
	:param info: список с информацией о подписчиках.
	"""
	info = str(reformat_result(str(info)))
	# print(info)
	with open(path, 'a+', encoding="utf-8") as file:
		file.write(info)
		file.write("\n")
	# google_sheet_parse.post_table_values_info(read_info_from_file())


def read_info_from_file():
	with open(path, encoding="utf-8") as f:
		text = re.findall(r"'(\d+)'", f.read())
		text = str(text)
		return text

