...
Longest Substring Without Repeating Characters

Find the length of the longest substring without repeating chars.

Example:
Input: "abcabcbb"
Output: 3 ("abc")
...
def longSub(inp):
    left=0
    max_len=0
    uniq=set()
    for right in range(len(inp)):
        while inp[right] in uniq:
            uniq.remove(inp[left])
            left+=1
        uniq.add(inp[right])
        if right-left+1>max_len:
            max_len=right-left+1
            start_index=left
    return inp[start_index:start_index + max_len]

inp=input()
result=longSub(inp)
print(result)