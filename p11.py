

def search_naive(query, lst):  # O(|word_len| * |lst_len|)
    ans = []
    for string in lst:
        if string[: len(query)] == query:  # pythonic string.startswith(query)
            ans.append(string)
    return ans


lst = ['dog', 'deer', 'deal']
print(search_naive("de", lst))


# not tested thoroughly
def bin_search(query, lst):  # O(|word_len| * log|lst_len|)
    def hop(index, l):
        if l // 2 == 0:
            return
        if lst[index][: len(query)] > query:
            hop(index - l // 2, l // 2)
        elif lst[index][: len(query)] < query:
            hop(index + l // 2, l // 2)
        else:
            return index

    index = hop(len(lst) // 2, len(lst) // 2)
    upper, lower = index, index

    # could just find the leftmost on binary search then this won't be needed
    while lst[lower][: len(query)] == query:
        lower -= 1
    while lst[upper][: len(query)] == query:
        upper += 1

    return lst[lower + 1: upper]


# lst = ['deal', 'deer', 'dog']
# print(bin_search("de", lst))

class Trie:
    def __init__(self, char, lst):
        self.char = char
        self.lst = lst

    def add_word(self, word):
        if word == '':
            return

        if self.lst is not None:
            for trie in self.lst:
                if trie.char == word[0]:
                    return trie.add_word(word[1:])

        new = Trie(word[0], None)
        new.add_word(word[1:])
        if self.lst is None:
            self.lst = [new]
        else:
            self.lst.append(new)

    def _query(self, string):
        if string == '' and self.char != '0':
            return self.words()

        if self.lst is not None:
            for trie in self.lst:
                if trie.char == string[0]:
                    return trie.query(string[1:])

        return None

    def query(self, string):
        return [string[:-1] + word for word in self._query(string)]

    def words(self):
        if self.lst is None:
            return [self.char]

        return [self.char + word for trie in self.lst for word in trie.words()]

    def __str__(self):
        if self.lst is None:
            return self.char
        else:
            return self.char + ' ' + str([str(trie) for trie in self.lst])


print(Trie('0', [Trie('a', [Trie('c', None)]), Trie('b', None)]))


def preprocessing(lst):
    root = Trie('0', None)
    for word in lst:
        root.add_word(word)

    return root


lst = ['dog', 'deer', 'deal', 'diamond', 'data', 'daily']
root = preprocessing(lst)
print(root, '\n')
print(root.query("de"))