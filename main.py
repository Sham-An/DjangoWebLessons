#STR 44 52 57 61? 62
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
"""Что делать если вы забали пароль от админки к django? Есть как минимум 2 решения проблемы.

Первое решение просто поменять пароль на root или другого суперпользователя, которого вы создали при создании базы данных. Для этого входим в manage.py shell

python manager.py shell

и набираем

>>>from django.contrib.auth.models import User
>>>user = User.objects.get( username='root')
>>>user.set_password(«password»)
>>>user.save()
Второй способ еще проще, он также пригодится если вы вместе с паролем забыли и логин от админки,
в этом случае можно создать нового суперпользователя, для этого в терминале вводим

python manage.py createsuperuser
 И вводим новые данные."""

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
