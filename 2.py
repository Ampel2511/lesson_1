# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и
# выведите в формате чч:мм:сс. Используйте форматирование строк.
print("Задание 2.")
seconds = int(input("Введите время в секундах: "))
hours = seconds // 3600
seconds = seconds - hours * 3600
minutes = seconds // 60
seconds = seconds - minutes * 60
print("{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds))
