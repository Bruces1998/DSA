from collections import defaultdict
def findLadders( beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if endWord not in wordList:
            return []
        
        wordset = set(wordList)
        queue = {}
        queue[beginWord] = [[beginWord]]

        while queue:
            nqueue = defaultdict(list)

            for word in queue:
                if word == endWord:
                    return queue[word]
                
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in wordset:
                            nqueue[new_word] += [j + [new_word] for j in queue[word]]

            wordset -= set(nqueue.keys())
            queue = nqueue

        return []