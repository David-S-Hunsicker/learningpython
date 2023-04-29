def find_is_paldindrome(arr:list[[]], n: int, s:str):
    for i in range(1, n):
        for start in range(n):
            stop = start + i -1
            if stop >= n:
                break
            arr[start][stop] = False
            if i <= 2: # if neighbor letters are equal they're palindrome
                arr[start][stop] = s[start] == s[stop]
            elif s[start] == s[stop]:
                arr[start][stop] = arr[start+1][stop-1]

def generate_palindromic_decompositions(s: str):
    is_palindrome = [[False] * len(s)] * len(s)
    find_is_paldindrome(is_palindrome, len(s), s)
    decompositions = [[] * len(s)]
    for i in range(len(s)):
        if is_palindrome[0][i]:
            decompositions[i].append(s[0:i+1])

        for j in range(i):
            if is_palindrome[j + 1][i]:
                cur_sub_string = "|" + s[j+1:i+1]
                l = len(decompositions[j])
                for k in range(l):
                    decompositions[i].append(decompositions[j][k] + cur_sub_string)
    return decompositions[-1]

print(generate_palindromic_decompositions("abracadabra"))