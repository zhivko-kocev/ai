pairs = [('a', 1), ('b', 2), ('c', 3)]

# pairs = map(lambda pair: (pair[1], pair[0]), pairs)

pairs = [(pair[1], pair[0]) for pair in pairs]

print(pairs)
