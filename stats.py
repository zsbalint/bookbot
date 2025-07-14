def count_words(text):
    return len(text.split())


def count_characters(text):
    result = {}
    for char in text:
        if char.lower() in result:
            result[char.lower()] += 1
        else:
            result[char.lower()] = 1
    return result


def sort_on(items):
    return items["num"]


def sort_dict(dict):
    list_of_dict = []
    for item in dict:
        if item.isalpha():
            to_add = {"char": item, "num": dict[item]}
            list_of_dict.append(to_add)
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict
