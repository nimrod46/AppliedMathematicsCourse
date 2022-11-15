import random
from typing import List


def get_random_word(length: int = 4, abc: List[str] = ['A', 'T', 'G', 'C']) -> str:
    return ''.join(random.choices(abc, k=length))


di = {}
max_word = get_random_word()
w = max_word
for i in range(4 ** 4 + 1):
    # if w in di:
    #     di.update({w: di.get(w) + 1})
    # else:
    #     di.update({w: 1})
    di[w] = di.get(w, 0) + 1
    if di.get(w) > di.get(max_word):
        max_word = w
    w = get_random_word()
print(di)
print(max_word + ": " + str(di.get(max_word)))
