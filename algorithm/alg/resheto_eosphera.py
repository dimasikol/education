def resheto_eosphera(size: int) -> list[int]:
    seed = [True for _ in range(size)]
    data = []
    for i in range(2, int(size**0.5)+1):
        if seed[i]:
            data.append(i)
        for j in range(i*i, size, i):
            seed[j] = False
    return data
if __name__ == '__main__':
    print(resheto_eosphera(20_000_000))