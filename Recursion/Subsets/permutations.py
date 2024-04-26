

def permute(s, i, j):
    #Base Case
    if i == j:
        print("".join(s))
        return

    for k in range(i, j+1):
        s[i], s[k] = s[k], s[i]
        permute(s, i+1, j)
        s[i], s[k] = s[k], s[i] # undo what you did before recursion

s = 'abc'

permute(list(s), 0, len(s)-1)