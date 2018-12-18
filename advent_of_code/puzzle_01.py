def add_freq_shift(in_data, freq=0):
    for shift in in_data:
        shift = shift.strip()
        if shift is not None and shift != "":
            freq += int(shift)
    return freq


def find_first_duplicate_freq2(shifts, freq=0, frequencies=None):
    if frequencies is None:
        frequencies = set()

    for shift in shifts:
        shift = shift.strip()
        if shift is None or shift == "":
            continue
        freq += int(shift)
        if freq in frequencies:
            return freq
        else:
            frequencies.add(freq)
    return find_first_duplicate_freq2(shifts, freq, frequencies)
