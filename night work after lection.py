asd = [1,2,3,4,5,6,7,8,9,10]
bas = ['verder','psv','arsenal','sevilla']
pi = 3.14
# def control(var,arm):
#     var = united()
#     arm = quantity()
#
# def united(cls):
#    cls = asd + bas
#    return cls
#
#
# def quantity(btb):
#     btb = cls[0:-1]
#     return btb



def control(var, arm):
    res_united = united(var, arm)
    len_cls = quantity(res_united)
    return res_united, len_cls

def united(cls, cls2):
    all_cls = cls + cls2
    return all_cls

def quantity(btb):
    len_cls = len(btb)
    return len_cls

res = control(('feyenord', 'genk', 'celtic'), tuple(['123', '1233333']))
print(res)