def sum_metadata(meta_data_inp):
    meta_data = meta_data_inp.strip().split(" ")
    sum = 0
    for m in meta_data:
        sum += int(m)
    return sum

