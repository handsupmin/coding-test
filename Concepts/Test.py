# Test.py
# 실험용 파일입니다.

from collections import defaultdict
list_dict = defaultdict(list)
lists = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
for l in lists:
    list_dict[l[0]].append(l[1])

print(list_dict)