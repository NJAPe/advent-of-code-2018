def parse_entry(entry):
    at_idx = entry.find('@')
    colon_idx = entry.find(':')
    id = entry[entry.find('#')+1:at_idx]
    start = entry[at_idx+1:colon_idx].split(',')
    size = entry[colon_idx+1:].split('x')
    if len(start) != 2 and len(size) != 2:
        return None

    patch=dict()
    patch['id'] = int(id.strip())
    patch['start_x'] = int(start[0].strip())
    patch['start_y'] = int(start[1].strip())
    patch['size_x'] = int(size[0].strip())
    patch['size_y'] = int(size[1].strip())
    return patch


def build_patches(patches_raw):
    patches = dict()
    for p in patches_raw:
        patches[p['id']] = set()
        for x in range(p['size_x']):
            for y in range(p['size_y']):
                patches[p['id']].add((p['start_x']+x, p['start_y']+y))
    return patches


def get_intersection_patches(input):
    patches_raw = list()
    for entry in input:
        parsed = parse_entry(entry)
        if parsed is None:
            continue
        patches_raw.append(parsed)

    patches = build_patches(patches_raw)
    iterated = list()
    overlapping = set()
    for k, v in patches.items():
        for i in iterated:
            intersections = v.intersection(i)
            for inter in intersections:
                overlapping.add(inter)
        iterated.append(v)

    return overlapping
    
def get_non_intersecting_patch(input):
    patches_raw = list()
    for entry in input:
        parsed = parse_entry(entry)
        if parsed is None:
            continue
        patches_raw.append(parsed)

    patches = build_patches(patches_raw)
    rejected = set()
    still_ok = patches.keys()
    for k,v in patches.items():
        if k in rejected:
            continue
        for k_other, v_other in patches.items():
            if k == k_other:
                continue
            inter = v.intersection(v_other)
            if len(inter) != 0:
                rejected.add(k)
                if k in still_ok:
                    still_ok.remove(k)
                rejected.add(k_other)
                if k_other in still_ok:
                    still_ok.remove(k_other)
                continue
    if len(still_ok) != 1:
        print("error")
        print(still_ok)
    print(still_ok)
        


#input = ["#1 @ 1,3: 4x4", "#2 @ 3,1: 4x4", "#3 @ 5,5: 2x2", ""]
with open("03_input.txt") as f:
    input = f.read().split("\n")
#print(len(get_intersection_patches(input)))
get_non_intersecting_patch(input)

