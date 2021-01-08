

def triInsertion(T):
    for i in range(1, len(T)):
        for j in range(i, 0, -1):
            if T[j-1] < T[j]:
                break
            T[j-1], T[j] = T[j], T[j-1]


if __name__ == '__main__':
    T = [4, 5, 2, 3]
    print(T)
    triInsertion(T)
    print(T)
