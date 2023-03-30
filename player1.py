# player 1 code

def __init__(self, overall, per_step):
    rocks = int(input())
    if rocks <= per_step and rocks <= overall:
        return rocks
    else:
        print('Некорректное количество камней!')
        # короче тут надо чтобы оно просило нормальное количество камней пока не получит
        # и еще надо сделать в testsystem саму проверку не проиграл ли ты уже случайно