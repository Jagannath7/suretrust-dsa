n = int(input())

def generateBrackets(s, n , i , open, close):
    #Base Case:
    if i == 2*n:
        print(s[:])
        return

    # add open brackets
    if open<n:
        generateBrackets(s+'(', n, i+1, open+1, close)

    if close<open:
        generateBrackets(s+')', n, i+1, open, close+1)

    return

s = ""
generateBrackets(s, n, 0, 0, 0)