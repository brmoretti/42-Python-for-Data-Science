def count_in_list(lst: list, item: object) -> int:
    return sum(1 for x in lst if x == item)
