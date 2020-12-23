from colorama import Fore, Back, Style

# Banner, menu, quick withdrawal
q_banner = Fore.RED + """

░█████╗░██╗░░██╗████████╗███████╗██╗██╗░░░░░
██╔══██╗██║░░██║╚══██╔══╝██╔════╝██║██║░░░░░
██║░░██║███████║░░░██║░░░█████╗░░██║██║░░░░░
██║░░██║██╔══██║░░░██║░░░██╔══╝░░██║██║░░░░░
╚█████╔╝██║░░██║░░░██║░░░██║░░░░░██║███████╗
░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚══════╝
    —·– Создатель : t.me/ohtllinest –·—"""

q_so = Fore.RED + """
— t.me/ohtllinest
— vk.com/camicaze
"""

q_inf = Fore.RED + """
————————————————————————————————————————————————
"""

q_sellics = Fore.GREEN + """
— Готовые ссылки:"""

q_menu = Fore.WHITE + """
[1] Начать
[2] Инструкция
[3] Создатель
"""
# Banner output
print(q_banner)
print(' ')

# Display menu
print(q_menu)
q_display = input('— Введите номер функции : ')

# Function output number one
if q_display == "1":
	q_ident = input('— Введите номер фильма : ')
	
	# Displaying links
	print(q_inf)
	print(q_sellics)
	
	print("https://sskinopoisk.ru/film/" + q_ident)
	print("https://ww1.flink.su/film/" + q_ident)
	
if q_display == "2":
	print(q_inf)
	print (' ')
	
	print("[1] Выберите фильм")
	print("[2] В адресной строке будет номер фильма")
	print("[3] Вставьте его в утилиту")
	
	print(' ')
	print("— Например https://www.kinopoisk.ru/film/435")
	print("— 435 это и есть номер фильма")
	
if q_display == "3":
	print(q_so)
