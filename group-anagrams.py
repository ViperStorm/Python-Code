from collections import defaultdict

words = ["eat","tea","tan","ate","nat","bat"]

anagram_map = defaultdict(list)
result = []

for s in words:
    sorted_s = tuple(sorted(s))
    anagram_map[sorted_s].append(s) 

for value in anagram_map.values():
    result.append(value)
print(result)