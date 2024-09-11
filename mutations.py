def mutate_string(string, pos, char):
    return string[:pos] + char + string[pos+1:]

if __name__ == '__main__':
    s = input()
    pos, char = input().split()
    s_new = mutate_string(s, int(pos), char)
    print(s_new)
