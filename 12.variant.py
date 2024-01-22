
#12 Варинат Черанёва Наталья
from datetime import datetime


def read_transactions(): #Функция чтения строк, разделения на части по необходимой информации
    transactions = [] #Создание списка для хранения информации
    with open('transactions.txt', 'r', encoding='utf-8') as file: #Открытие и интерпретация файла в кодировке UTF-8 для русского языка
        lines = file.readlines() #Чтение каждой строчки файла
    for i, line in enumerate(lines): # переменная i для отслеживания позиции текущей строки в списке lines.
        #генерирация индексов и значений для каждой строки в lines списке
        parts = line.strip().split(', ') # Разделение на части по запятой и пробелу
        transaction = parts
        transactions.append(transaction)#Добавление всех частей, строк в отдельный список
    return transactions #Возвращает прочитанный, разделенный по частям список


def write_transactions(transactions): #Функция чтения и записи транзакций в файл
    with open('transactions.txt', 'w', encoding='utf-8') as file:
        for transaction in transactions:
            file.write(", ".join([transaction[0], transaction[1], transaction[2], transaction[3], str(transaction[4]), transaction[5]]) + '\n')


def add_transaction():
    transactions = read_transactions()
    while True:

        date = input("Введите новую дату транзакции (дд.мм.гггг): ") #Проверка на дурака
        if len(date) != 10 or date[2] != '.' or date[5] != '.' or not date.replace('.','').isdigit(): 
            print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")
            break

        day = int(date[:2]) #Срез и запоминание информации с помощью переменной
        month = int(date[3:5])
        year = int(date[6:])

        if len(date) != 10 or date[2] != '.' or date[5] != '.': #Проверка на дурака
            print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")
            break

        elif day < 1 or day > 31 or month < 1 or month > 12 or (year <1000 or year>2024):
            print("Неверный день, месяц или год. Пожалуйста, введите дату снова.")
            break

        time = input("Введите время транзакции (чч:мм): ")
        if len(time) != 5 or time[2] != ':':
            print("Неверный формат времени. Пожалуйста, введите время в формате hh:mm.")
            break

        else:
            hour = int(time[:2])
            minute = int(time[3:])
            if hour > 23 or minute > 59:
                print("Неверный час или минуты. Пожалуйста, введите время снова.")
                break

        direction = input("Введите направление с большой буквы (Приход / Расход): ")
        if direction not in ['Приход', 'Расход']:
            print("Неверное направление. Пожалуйста, введите Приход или Расход.")
            break

        category = input("Введите категорию: ") 
        if not category:
            print("Категория не может быть пустой. Пожалуйста, введите категорию заново")
            break

        amount = input("Введите сумму: ")
        if not amount.replace('.', '', 1).isdecimal():#Замена знаков чтоб осталась строка, которую мы могли бы проверить на то, что введены числа
            print("Неверный формат суммы. Пожалуйста, введите сумму как число.")
            break

        counterparty = input("Введите контрагента: ")
        if not counterparty:
            print("Контрагент не может быть пустым. Пожалуйста, введите Контрагента заново")
            break

        transaction = [date, time,  direction, category,  float(amount), counterparty]
        transactions.append(transaction)
        write_transactions(transactions)
        print("Транзакция добавлена успешно.")
        break


def delete_transaction():
    transactions = read_transactions()

    if not transactions:
        print("База транзакций пуста.")
        return
    
    index = input("Введите индекс транзакции для удаления: ")
    if not index.isdigit(): #Проверка, что строка содержит только число
        print('Пожалуйста, введите корректный индекс числом')
        return
    
    index = int(index)

    if index <= 0 or index >= len(transactions)+1: #Смотрим входит ли индекс в номер списка
        print("Неверный индекс транзакции.")
        return
    
    else:
        transactions.pop(index-1)#Удаление транзакции 
        print("Транзакция удалена успешно.")
        write_transactions(transactions)


def update_transaction():
    transactions = read_transactions()
    if not transactions:
        print("База транзакций пуста.")
        return
    
    index = input("Введите индекс транзакции для обновления: ")
    if not index.isdigit(): #Проверка на ввод чисел
        print('Пожалуйста, введите корректный индекс')
        return
    
    index = int(index) #Преобразование введеннного пользователем значение в целое число и сохранение его в переменной index.
    transaction = transactions[index-1]

    while True:
        date = input("Введите новую дату транзакции (дд.мм.гггг): ")#Проверка на дурака
        if len(date) != 10 or date[2] != '.' or date[5] != '.' or not date.replace('.','').isdigit(): #Проверка на дурака
            print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")
            break

        day = int(date[:2]) #Срез и запоминание информации с помощью переменной
        month = int(date[3:5])
        year = int(date[6:])

        if len(date) != 10 or date[2] != '.' or date[5] != '.': #Проверка на дурака
            print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")
            break

        elif day < 1 or day > 31 or month < 1 or month > 12 or (year <1000 or year>2024):
            print("Неверный день, месяц или год. Пожалуйста, введите дату снова.")
            break

        time = input("Введите время транзакции (чч:мм): ")
        if len(time) != 5 or time[2] != ':':
            print("Неверный формат времени. Пожалуйста, введите время в формате hh:mm.")
            break

        else:
            hour = int(time[:2])
            minute = int(time[3:])
            if hour > 23 or minute > 59:
                print("Неверный час или минуты. Пожалуйста, введите время снова.")
                break

        direction = input("Введите направление с большой буквы (Приход / Расход): ")
        if direction not in ['Приход', 'Расход']:
            print("Неверное направление. Пожалуйста, введите Приход или Расход.")
            break

        category = input("Введите категорию: ") 
        if not category:
            print("Категория не может быть пустой. Пожалуйста, введите категорию заново")
            break

        amount = input("Введите сумму: ")
        if not amount.replace('.', '', 1).isdecimal(): #Проверка, что вводят числа
            print("Неверный формат суммы. Пожалуйста, введите сумму как число.")
            break

        counterparty = input("Введите контрагента: ")
        if not counterparty:
            print("Контрагент не может быть пустым. Пожалуйста, введите Контрагента заново")
            break
        
        transaction[0] = date #Обновление и замена транкзации новой информацией
        transaction[1] = time
        transaction[2] = direction
        transaction[3] = category
        transaction[4] = amount
        transaction[5] = counterparty

        with open("transactions.txt", "w", encoding='utf-8') as file:
            write_transactions(transactions)
        print("Транзакция обновлена успешно.")
        break


def display_all_transactions():
    transactions = read_transactions()
    if not transactions: #Проверка является ли список пустым
        print("База транзакций пуста.")
        return
    
    print("Список всех транзакций:")
    for transaction in transactions:
        print(f"Дата: {transaction[0]}, Время: {transaction[1]}, Направление: {transaction[2]}, Категория: {transaction[3]}, Сумма: {transaction[4]}, Контрагент: {transaction[5]}")


def compare_dates_5(date1, date2, amount1, amount2):
    date1_obj = datetime.strptime(date1, "%d.%m.%Y") #Разделение даты на день, месяц и год
    date2_obj = datetime.strptime(date2, "%d.%m.%Y")
    if date1_obj > date2_obj: #Сравнение дат для сортировки данных
        return 1
    elif date1_obj < date2_obj:
        return -1
    elif amount1 > amount2: 
        return 1
    elif amount1 < amount2:
        return -1
    else:
        return 0


def heapify_5(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n: #Проверка существования левого дочернего элемента 
        date_comp = compare_dates_5(arr[i][0], arr[left][0], arr[i][4], arr[left][4])
        if date_comp == 1: #Если текущий узел меньше его левого потомка, обновляет largest индексом левого потомка.
            largest = left

    if right < n: #Проверка существования правого дочернего элемента 
        date_comp = compare_dates_5(arr[largest][0], arr[right][0], arr[largest][4], arr[right][4])
        if date_comp == 1:#Если текущий узел меньше его правого потомка, обновляет largest индексом правого потомка.
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_5(arr, n, largest)
        

def heap_sort_5(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1): #начинаем с элемента, который находится на позиции n//2 - 1 и заканчивая элементом на позиции 0
        heapify_5(arr, n, i)

    for i in range(n-1, 0, -1): #Проходимся сортировкой в обратном порядке
        arr[i], arr[0] = arr[0], arr[i]
        heapify_5(arr, i, 0)


def sorted_5_0():
    transactions = read_transactions() 
    heap_sort_5(transactions)
    transaction_0 = []

    for transaction in transactions:
        if transaction[2] == 'Приход':
            transaction_0.append(transaction)
    return transaction_0
           

def sorted_5():
    transactions_sorted = sorted_5_0() #Сохранение отсортированной информации как переменной
    #выводим список задач за последние n дней
    n = input("Введите за какое последнее количество дней показать поступления: ")

    if not n.isdigit():
        print('Пожалуйста, введите корректное количество дней')
        return
    
    n = int(n)
    print("Поступления за", n, "дней:")

    current_date = datetime.now().date() #использование datetime модуля для получения текущей даты и сохранения ее в переменной current_date.
    for transactions_0 in transactions_sorted:#запуск цикла, который повторяет каждый элемент в tasks_sorted списке. Каждый элемент временно сохраняется в переменной transactions_0.
        transaction_date = datetime.strptime(transactions_0[0], '%d.%m.%Y') #преобразует часть даты транзакции (которая является строкой) в datetime.datetime объект и присваивает ее transaction_date переменной.
        current_date = datetime.combine(current_date, datetime.min.time()) #преобразование current_date в datetime.datetime для последующего вычитания
    
    #проверка, является ли разница в днях между текущей датой и датой транзакции меньше или равна n.
        if (current_date - transaction_date).days <= n:
            print(f'Дата: {transactions_0[0]}, Время: {transactions_0[1]}, Направление: {transactions_0[2]}, Категория: {transactions_0[3]}, Сумма: {transactions_0[4]}, Контрагент: {transactions_0[5]}')


def compare_dates_6(date1, date2, counterparty1, counterparty2, amount1, amount2):
    date1_obj = datetime.strptime(date1, "%d.%m.%Y")
    date2_obj = datetime.strptime(date2, "%d.%m.%Y")

    if date1_obj > date2_obj:
        return 1
    elif date1_obj < date2_obj:
        return -1
    elif counterparty1 > counterparty2:
        return 1
    elif counterparty1 < counterparty2:
        return -1
    elif amount1 > amount2: 
        return 1
    elif amount1 < amount2:
        return -1
    else:
        return 0


def heapify_6(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        date_comp = compare_dates_6(arr[i][0], arr[left][0], arr[i][5], arr[left][5], arr[i][4], arr[left][4])
        if date_comp == 1:#Если текущий узел меньше его левого потомка, обновляет largest индексом левого потомка.
            largest = left

    if right < n:
        date_comp = compare_dates_6(arr[largest][0], arr[right][0], arr[largest][5], arr[right][5], arr[largest][4], arr[right][4])
        if date_comp == 1:#Если текущий узел меньше его правого потомка, обновляет largest индексом правого потомка.
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_6(arr, n, largest)


def heap_sort_6(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1):#начинаем с элемента, который находится на позиции n//2 - 1 и заканчивая элементом на позиции 0
        heapify_6(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify_6(arr, i, 0)


def sorted_6():
    n = input('Введите название категории, за которую хотите получить список расходов: ').strip().lower()
    transactions = read_transactions() 
    heap_sort_6(transactions)
    found = False

    for transaction in transactions:
        if transaction[2] == 'Расход' and n == transaction[3].strip().lower(): #удалить начальные и конечные пробелы и преобразовать все в нижний регистр, чтоб чтение проимходило с любым регистром
            print (f'Дата: {transaction[0]}, Время: {transaction[1]}, Направление: {transaction[2]}, Категория: {transaction[3]}, Сумма: {transaction[4]}, Контрагент: {transaction[5]}')
            found = True

    if not found:
        print('Транзация с направлением "Расход" или с выбранной вами категорией не существует. Пожалуйста, попробуйте ещё раз.')


def sorted_7_proverka():
    transactions =read_transactions()

    while True:
        #Преобразование строки начальной даты, введенную пользователем, в объект datetime с помощью функции
        start_time = input('Введите начальную дату в формате дд.мм.гггг: ')
        if len(start_time) != 10 or start_time[2] != '.' or start_time[5] != '.' or not start_time.replace('.','').isdigit(): #Проверка на дурака
            print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")
            return
        
        day = int(start_time[:2]) #Срез и запоминание информации с помощью переменной
        month = int(start_time[3:5])
        year = int(start_time[6:])

        if day < 1 or day > 31 or month < 1 or month > 12 or (year <1000 or year>2024):
            print("Неверный день, месяц или год. Пожалуйста, введите дату снова.")
            break

        end_time = input('Введите конечную дату в формате дд.мм.гггг: ')
        if len(end_time) != 10 or end_time[2] != '.' or end_time[5] != '.' or not end_time.replace('.','').isdigit(): #Проверка на дурака
            print("Неверный формат даты. Пожалуйста, введите дату в формате dd.mm.yyyy.")
            return
        
        day = int(end_time[:2]) #Срез и запоминание информации с помощью переменной
        month = int(end_time[3:5])
        year = int(end_time[6:])

        if len(end_time) != 10 or end_time[2] != '.' or end_time[5] != '.': #Проверка на дурака
            print("Неверный формат даты. Пожалуйста, введите дату в формате дд.мм.гггг.")
            break

        elif day < 1 or day > 31 or month < 1 or month > 12 or (year < 1000 or year>2024):
            print("Неверный день, месяц или год. Пожалуйста, введите дату снова.")
            break

        start_time = datetime.strptime(start_time, '%d.%m.%Y')
        end_time = datetime.strptime(end_time, '%d.%m.%Y')
        break

    filtered_transactions = []

    for transaction in transactions:
        if start_time <= datetime.strptime(transaction[0], '%d.%m.%Y') <= end_time and transaction[2] == 'Расход':
            filtered_transactions.append(transaction)#Если дата подходит, то записываем её

    if not filtered_transactions:#Если в списке нет ни одной транзакции - пишем не найдено
        print("Транзакций с данным промежутком времени не найдено")

    else:
        sorted_7()


def compare_7(amount1, amount2, counterparty1, counterparty2):
    amount1 = float(amount1) #Присваивание элементу тип данных с плавающей запятой
    amount2 = float(amount2)
    if amount1 > amount2: 
        return 1
    elif amount1 < amount2:
        return -1
    elif counterparty1 > counterparty2: 
        return 1
    elif counterparty1 < counterparty2:
        return -1
    else:
        return 0


def heapify_7(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n:
        date_comp = compare_7( arr[i][4], arr[left][4], arr[i][5], arr[left][5])
        if date_comp == 1:#Если текущий узел меньше его левого потомка, обновляет largest индексом левого потомка.
            largest = left

    if right < n:
        date_comp = compare_7( arr[largest][4], arr[right][4], arr[largest][5], arr[right][5])
        if date_comp == 1:#Если текущий узел меньше его правого потомка, обновляет largest индексом правого потомка.
            largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify_7(arr, n, largest)


def heap_sort_7(arr):
    n = len(arr)

    for i in range(n//2 - 1, -1, -1): #начинаем с элемента, который находится на позиции n//2 - 1 и заканчивая элементом на позиции 0
        heapify_7(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]#Запуск цикла от последнего элемента массива до второго. 
        heapify_7(arr, i, 0)


def sorted_7():
    transactions = read_transactions()
    transaction_0 = []
    heap_sort_7(transactions)

    for transaction in transactions:
        if transaction[2] == 'Расход':#Добавление транзакций направления "Расход"
            transaction_0.append(transaction)
    for transaction in transaction_0:
        print (f'Дата: {transaction[0]}, Время: {transaction[1]}, Направление: {transaction[2]}, Категория: {transaction[3]}, Сумма: {transaction[4]}, Контрагент: {transaction[5]}')


def menu():
    while True:
        print("Меню программы:")
        print("1. Добавить транзакцию")
        print("2. Удалить транзакцию")
        print("3. Обновить транзакцию")
        print("4. Вывести все транзакции")
        print("5. Вывести список поступлений за последние N дней")
        print("6. Вывести список затрат заданной категории")
        print("7. Вывести список затрат в определенном временном промежутке")
        print("8. Выход")
        choice = input("Введите номер действия: ")
        if choice == "1":
            add_transaction() #После получения выбора запускаем функцию
        elif choice == "2":
            delete_transaction()
        elif choice == "3":
            update_transaction()
        elif choice == "4":
            display_all_transactions()
        elif choice == "5":
            sorted_5()
        elif choice == "6":
            sorted_6()
        elif choice == "7":
            sorted_7_proverka()
        elif choice == "8":
            break
        else:
            print("Неверный выбор. Попробуйте еще раз.")
menu()
