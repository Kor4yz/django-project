from django.shortcuts import render

# Данные хранятся в словарях
STUDENT_DATA = {
    'full_name': 'Морозов Денис Сергеевич',
    'email': 'desemorozov@edu.hse.ru',
    'phone': '+7 (999) 123-45-67',
    'photo': None,
}

PROGRAM_DATA = {
    'name': 'Разработка веб-приложений',
    'description': 'Программа направлена на подготовку специалистов в области '
                   'разработки веб-приложений с использованием современных технологий '
                   'и фреймворков, включая Python, Django, JavaScript и CSS.'
}

CLASSMATES_DATA = [
    {'name': 'Алексеев Алексей Алексеевич', 'email': 'alekseev@example.com', 'phone': '+7 (999) 111-11-11', 'photo': None},
    {'name': 'Борисова Борислава Борисовна', 'email': 'borisova@example.com', 'phone': '+7 (999) 222-22-22', 'photo': None},
    {'name': 'Васильев Василий Васильевич', 'email': 'vasiliev@example.com', 'phone': '+7 (999) 333-33-33', 'photo': None},
]

PAINTINGS = [
    {'name': 'Чёрный квадрат', 'price': 23000},
    {'name': 'Версаль', 'price': 14550},
    {'name': 'Осень', 'price': 12990},
    {'name': 'Ночь', 'price': 17000},
    {'name': 'Девятый вал', 'price': 25000},
    {'name': 'Мона Лиза', 'price': 23500},
    {'name': 'Рассвет', 'price': 15500},
    {'name': 'Буря', 'price': 18000},
]


def solve_paintings(paintings, bill=500):
    result = sorted(
        [p['name'] for p in paintings if p['price'] % bill == 0],
        key=lambda x: x.lower()
    )
    return result


def home(request):
    return render(request, 'main/home.html', {'student': STUDENT_DATA})


def about(request):
    return render(request, 'main/about.html', {
        'student': STUDENT_DATA,
        'classmates': CLASSMATES_DATA,
    })


def education(request):
    return render(request, 'main/education.html', {
        'student': STUDENT_DATA,
        'program': PROGRAM_DATA,
    })


def algorithm(request):
    result = solve_paintings(PAINTINGS)
    return render(request, 'main/algorithm.html', {
        'paintings': PAINTINGS,
        'result': result,
        'result_str': ', '.join(result),
    })


def gallery(request):
    return render(request, 'main/gallery.html', {
        'student': STUDENT_DATA,
    })
