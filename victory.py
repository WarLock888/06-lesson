import random

AUTHORS = {
    'Пушкина': '06.06.1799',
    'Толстого': '09.09.1828',
    'Лермонтова': '15.10.1814',
    'Гоголя': '20.03.1807',
    'Достоевского': '11.11.1821',
    'Дюма': '24.07.1802',
    'Шекспира': '23.04.1564',
    'Бунина': '22.10.1870',
    'Некрасова': '10.12.1821',
    'Тютчева': '23.11.1803',
}

WORDS_DAYS = ['-', 'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое', 'девятое',
              'десятое',
              'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое', 'пятнадцатое', 'шестандцатое',
              'семнадцатое', 'восемнадцатое', 'девятнадцатое',
              'двадцатое', 'двадцатьпервое', 'двадцатьвторое', 'двадцатьтретье', 'двадцатьчетвертое', 'двадцатьпятое',
              'двадцатьшестое', 'двадцатьседьмое', 'двадцатьвосьмое', 'двадцатьдевятое',
              'тридцатое', 'тридцатьпервое', ]

WORDS_MONTHS = ['-', 'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября',
                'ноября', 'декабря', ]


# Функция возврата текстового описания даты прописью из строки даты в формате dd.mm.yyyy
def date_spelling(date: str):
    dd, mm, yyyy = [int(i) for i in date.split('.')]  # получим кортеж дат из спискового генератора после сплита даты
    return f'{WORDS_DAYS[dd]} {WORDS_MONTHS[mm]} {yyyy} года'  # возвращаем дату строкой


def start_victory():
    # print( date_spelling(AUTHORS['Пушкина']) )
    # exit()

    again = True  # заранее включим флаг продолжения игры по умолчанию для старта цикла

    while again:  # пока на входе цикла True то играем
        answers = {}  # здесь будут ответы пользователя и авторы
        selected_authors = random.sample(list(AUTHORS), 5)  # выберем случайно 5 писателей для игры

        for author in selected_authors:  # пройдем по выбраным писателям
            answer = input(f'Введите дату рождения {author} в формате dd.mm.yyyy: ')
            if answer != AUTHORS[author]:
                print('Неверно! Правильный ответ:\n', date_spelling(AUTHORS[author]))
            # else:
            #     print('Верно!')

            answers[author] = answer

        score = sum(answers[author] == AUTHORS[author] for author in
                    selected_authors)  # берем сумму от генератора списка булевых ответов для всех авторов

        print(f'Количество правильных: {score}')
        print(f'Количество ошибок: {len(selected_authors) - score}')
        print(f'Процент правильных: {score * 100 / len(selected_authors)}%')
        print(f'Процент НЕправильных: {100 - (score * 100 / len(selected_authors))}%')

        again = input(
            'Хотите сыграть еще раз?\n').lower() == 'да'  # спросим у пользователя о продолжении и положим ответ в  переменную again


if __name__ == '__main__':
    start_victory()
