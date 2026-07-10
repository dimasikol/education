

def levenstein_distance(string1:str, string2:str):
    left_len = len(string1)
    right_len = len(string2)
    data:list[list[int]] = [[0 for _ in range(left_len+1)] for i in range(right_len+1)]
    for i in range(right_len+1):
        data[i][0] = i
    for i in range(left_len+1):
        data[0][i] = i
    for i in range(1, right_len+1):
        for j in range(1, left_len+1):
            edit = 0
            if string1[j-1] != string2[i-1]:
                edit = 1
            data[i][j] = min(
                             data[i-1][j-1]+edit,
                             data[i-1][j]+1,
                             data[i][j-1]+1)

    print(*data,sep="\n")
    print(data[-1][-1])
    return data[-1][-1]

if __name__ == "__main__":
    levenstein_distance("looae","google")
