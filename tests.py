from Json_data import sched_w_st
import datetime
from datetime import date, datetime
current_daatetime = str(date.today())


def f(teachers_name):
    i = 0
    while i < len(sched_w_st):
        if current_daatetime == sched_w_st[i]['date'] and teachers_name == sched_w_st[i]['teachers']:
            print(f"{sched_w_st[i]['place']}\n{sched_w_st[i]['time']}")
        i += 1

f('Кудряшова Елена Николаевна')