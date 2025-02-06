def get_arg_dict(clothes):
    arg_dict = dict()
    for arg, arg_type in clothes:
        if arg_type in arg_dict:
            arg_dict[arg_type] += 1
        else:
            arg_dict[arg_type] = 2
    return arg_dict


def solution(clothes):
    arg_dict = get_arg_dict(clothes)
    answer = 1
    for cnt in arg_dict.values():
        answer *= cnt
    return answer - 1
