from Json_data import sched_w_st
from datetime import date

list_of_kabs_first_flour = ['Центральная столовая', 'Боковая столовая', 'П1', 'П2']

list_of_kabs_second_flour = ['П3', 'П4']
for i in range(201, 268):
    list_of_kabs_second_flour.append(str(i))

list_of_kabs_second_flour.append('Сачок')

list_of_kabs_third_flour = ['Сачок', 'П5', 'П6']

list_of_kabs_fourth_flour = ["П7", "П8"]

for i in range(401, 468):
    list_of_kabs_fourth_flour.append(str(i))


for i in range(1, 13):
    list_of_kabs_fourth_flour.append(f'Диванчик {str(i)}')

list_of_kabs_fourth_flour.append('Сачок')

list_of_kabs_fith_flour = ["П9"]

list_of_kabs_fith_flour.append('Сачок')
list_of_kabs_fith_flour.append('Столовка')
for i in range(502, 571):
    list_of_kabs_fith_flour.append(str(i))

# print(list_of_kabs_second_flour)


def foo():
    right_now = str(date.today())
    current_time = '15:40-17:10'
    for i in range(len(sched_w_st)):
        if sched_w_st[i]['date'] == right_now and sched_w_st[i]['time'] == current_time:
            for i in range(len(sched_w_st)):
                if sched_w_st[i]['date'] == right_now and sched_w_st[i]['time'] == current_time:
                    if sched_w_st[i]['place'].startswith('1') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_first_flour:
                        list_of_kabs_first_flour.remove(str(sched_w_st[i]['place']))
                        print(list_of_kabs_first_flour)
                    elif sched_w_st[i]['place'].startswith('2') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_second_flour:
                        list_of_kabs_second_flour.remove(str(sched_w_st[i]['place']))
                        print(list_of_kabs_second_flour)
                    elif sched_w_st[i]['place'].startswith('3') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_third_flour:
                        list_of_kabs_third_flour.remove(str(sched_w_st[i]['place']))
                        print(list_of_kabs_third_flour)
                    elif sched_w_st[i]['place'].startswith('4') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_fourth_flour:
                        list_of_kabs_fourth_flour.remove(str(sched_w_st[i]['place']))
                        print(list_of_kabs_fourth_flour)
                    elif sched_w_st[i]['place'].startswith('5') and str(sched_w_st[i]['place']) in \
                            list_of_kabs_fith_flour:
                        print(list_of_kabs_fith_flour)
    print(list_of_kabs_first_flour)



# foo()

