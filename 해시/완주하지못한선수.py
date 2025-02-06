from collections import Counter


def solution(participant, completion):
    target = Counter(participant) - Counter(completion)
    # answer = list(target.keys())[0]
    answer = next(iter(target.keys()))
    return answer
