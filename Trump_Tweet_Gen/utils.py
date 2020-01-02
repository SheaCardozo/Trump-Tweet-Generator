from random import randint, uniform
from datetime import datetime


def generate_likes_rts():
    base = randint(10, 600)
    mult = uniform(2, 5)
    vs = [str(base), str(int(base * mult))]

    for i, v in enumerate(vs):
        if v[-1] == '0':
            vs[i] = v[:-1] + 'K'
        else:
            vs[i] = v[:-1] + '.' + v[-1] + 'K'

    return vs[1], vs[0]


def get_time_date():
    today = datetime.now()
    dt = today.strftime("%b %d, %Y")
    tm = today.strftime('%I:%M %p')

    if tm[0] == '0':
        tm = tm[1:]

    if dt[4] == '0':
        dt = dt[:4] + dt[5:]

    return tm, dt
