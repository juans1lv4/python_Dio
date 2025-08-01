def cal_t(num):
    return sum(num)

def retorno_sucessor_antecessor(numo):
    antecessor = numo - 1
    sucessor = numo + 1

    return antecessor, sucessor

print(cal_t([10, 30, 5]))
print(retorno_sucessor_antecessor(10))