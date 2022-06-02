tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]

def gen_tuples():
    i_t = 0                          # Счетчик индексов tutors
    i_k = 0                          # Счетчик индексов klasses
    while i_k <= len(klasses):
        if i_k >= len(tutors):
            yield (None, tutors[i_t])
            i_t += 1
            i_k += 1
            break
        else:
            yield(tutors[i_t], klasses[i_k])
            i_t += 1
            i_k += 1

for gen in gen_tuples():
    print(gen)

# Не понял как вывести None