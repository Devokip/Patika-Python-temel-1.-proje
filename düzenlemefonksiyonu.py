def flatten(lst):
    flattened_lst = []
    for item in lst:
        if isinstance(item, list):  # eleman bir listeyse
            flattened_lst.extend(flatten(item))  # listeyi tekrar düzleştir
        else:
            flattened_lst.append(item)  # eleman doğrudan listeye ekle
    return flattened_lst
