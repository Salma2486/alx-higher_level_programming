#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    max_value = max(a_dictionary.values())
    best_key = None

    for key, value in a_dictionary.items():
        if value == max_value:
            if best_key is None:
                best_key = key

    return best_key
