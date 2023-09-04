from Json_data import sched_w_st
from datetime import date

list_of_kabs_first_flour = ['Центральная столовая', 'Боковая столовая', 'П1', 'П2']

list_of_kabs_second_flour = []
for i in range(201, 268):
    list_of_kabs_second_flour.append(i)

list_of_kabs_second_flour.append('Сачок')

list_of_kabs_third_flour = ['Сачок']

list_of_kabs_fourth_flour = []

for i in range(201, 268):
    list_of_kabs_fourth_flour.append(i)


for i in range(1, 13):
    list_of_kabs_fourth_flour.append(f'Диванчик {i}')

list_of_kabs_fourth_flour.append('Сачок')

list_of_kabs_fith_flour = []

list_of_kabs_fith_flour.append('Сачок')
list_of_kabs_fith_flour.append('Столовка')

print(list_of_kabs_second_flour)

def foo():
    right_now = str(date.today())
    current_time = '09:00-10:30'
    for i in range(len(sched_w_st)):
        if sched_w_st[i]['date'] == right_now and sched_w_st[i]['time'] == current_time:
            if sched_w_st[i]['place'].startswith('2'):
                list_of_kabs_second_flour.remove(int(sched_w_st[i]['place']))
    print(list_of_kabs_second_flour)


def foo2():
    time = '18:55-20:25'
    for i in range(len(sched_w_st)):
        if sched_w_st[i]['time'] == time:
            print(sched_w_st[i]['place'])

foo2()