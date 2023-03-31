def reverse(lst):
    reversed_lst = lst[::-1]  # ana liste ters çevriliyor
    for i, item in enumerate(reversed_lst):
        if isinstance(item, list):  # eleman bir liste ise
            reversed_lst[i] = reverse(item)  # listenin içindeki elemanlar da ters çevriliyor
    return reversed_lst
