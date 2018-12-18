from datetime import datetime
import operator


def parse_entries(input):
    entries = dict()
    for entry in input:
        if entry is None or entry == "":
            continue
        time_str = entry[entry.find("[")+1:entry.find("]")]
        dt = datetime.strptime(time_str, "%Y-%m-%d %H:%M")
        event_str = entry[entry.find("]")+1:].strip()
        entries[dt] = event_str
    return entries
    

def get_new_guard(event_str):
    hashtag = event_str.find("#")
    return int(event_str[hashtag+1:event_str.find(" ", hashtag)])
    
    
def build_guard_dict(entries):
    guards = dict()
    curr_guard = None
    fell_asleep = None
    for ent in sorted(entries):
        if(entries[ent].find("Guard #") > -1):
            curr_guard = get_new_guard(entries[ent])
            if curr_guard not in guards:
                guards[curr_guard] = dict()
            continue
        elif(entries[ent] == "falls asleep"):
            fell_asleep = ent.minute
        elif(entries[ent] == "wakes up"):
            for i in range(fell_asleep, ent.minute):
                if i in guards[curr_guard]:
                    guards[curr_guard][i] += 1
                else:
                    guards[curr_guard][i] = 1
        else:
            print("error")
            print(ent)
            print(entries[ent])
    return guards
    
    
def calc_strategy1(my_input):
    guards = build_guard_dict(parse_entries(my_input))
    sleepiest = None
    sleepiest_minute = None
    min_sleep = 0
    for g, minutes in guards.items():
        g_minutes = 0
        g_sleepiest_minute = (0,0)
        for minute, num in minutes.items():
            if num > g_sleepiest_minute[1]:
                g_sleepiest_minute = (minute, num)
            g_minutes += num
        if g_minutes > min_sleep:
            min_sleep = g_minutes
            sleepiest_minute = g_sleepiest_minute
            sleepiest = g
    return sleepiest*sleepiest_minute[0]
    
    
def calc_strategy2(my_input):
    guards = build_guard_dict(parse_entries(my_input))
    sleepiest = (0, 0, 0) # (guard, minute, number of minutes)
    
    for g, minutes in guards.items():
        if len(minutes) <= 0:
            continue
        max = sorted(minutes.items(), key=operator.itemgetter(1), reverse=True)[0]
        if max[1] > sleepiest[2]:
            sleepiest = (g, max[0], max[1])
    return sleepiest[0]*sleepiest[1]
