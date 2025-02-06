def get_candidate_dict(phone_book):
    candidate_dict = {}
    for length in set(map(lambda x: len(x), phone_book)):
        candidate_dict[length] = set()

    for phone in phone_book:
        phone_length = len(phone)
        for length in candidate_dict.keys():
            if length < phone_length:
                candidate_dict[length].add(phone[:length])
                
    return candidate_dict


def solution(phone_book):
    phone_book.sort(key=lambda x: len(x))
    candidate_dict = get_candidate_dict(phone_book)
    for phone in phone_book:
        phone_length = len(phone)
        candidates = candidate_dict[phone_length]
        if phone in candidates:
            return False
    return True
