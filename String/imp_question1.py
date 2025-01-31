words = ["eat","tea","tan","ate","nat","bat"]
output = [["bat"],["nat","tan"],["ate","eat","tea"]]
from collections import defaultdict

def groupAnagram(words):
    answers=defaultdict(list)
    for word in words:
        sorted_word = ''.join(sorted(word))
        
        answers[sorted_word].append(word)
    return answers.values()   

print(groupAnagram(words))