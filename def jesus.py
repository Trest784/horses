a = ['dest', 'fati', 'pedri', 'nico']


def position(player, a):
    x = a.pop(a.index(player))
    print(a)
    return 'popped ' + x


# print(position('dest', a))
# print(position('fati', a))

a = ['23', '34', '99', '9', '77']
b = "hello 23"


def check_9(data, substr='34'):
    if substr in data:
        return True
    else:
        return False


# print(check_9(a, '24'))
# print(check_9(b, 'hello'))

def study_args(*args):
    print(args)
    return sum(args)


# print(study_args(1, 2, 6, 9))
# print(study_args(1))
# print(study_args(-1, -2, -6, 20, 1000, 20))
#

# a = int(input('enter the number'))


def check_even(input_int, second_num):
    if input_int % second_num == 0:
        return True
    else:
        return False


# print(check_even(a, 5))
# print(check_even(a, 7))
# print(check_even(a, 5))
# print(check_even(a, 7))
# print(check_even(a, 5))
# print(check_even(a, 7))

a = [32,44,89,34]
b = [ 'gf','mtz_ripo','trojan','dm', 25]


def list_sum(a, b, first_index_a=0, second_index_a=-1, first_index_b=0, second_index_b=-1):
    return [a[first_index_a:second_index_a]] + [b[first_index_b:second_index_b]]


# print(list_sum(a, b, second_index_b=2))










