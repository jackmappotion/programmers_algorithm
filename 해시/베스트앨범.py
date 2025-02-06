from collections import defaultdict

def get_info_dict(genres, plays):
    info_dict = defaultdict(
        lambda: {
            'play': 0,
            'songs': {}
        }
    )
    for idx, (genre, play) in enumerate(zip(genres, plays)):
        info_dict[genre]['play'] += play
        info_dict[genre]['songs'][idx] = play
    return info_dict


def solution(genres, plays):
    info_dict = get_info_dict(genres, plays)
    genres = sorted(info_dict, key=lambda genre: -info_dict[genre]['play'])
    answer = []
    for genre in genres:
        genre_song_dict = info_dict[genre]['songs']
        answer += sorted(genre_song_dict, key=lambda song: -genre_song_dict[song])[:2]
    return answer