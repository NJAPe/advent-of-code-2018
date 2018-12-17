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
    
    
def calc_strategy1(input):
    guards = build_guard_dict(parse_entries(input))
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
    print(f"answer1: {sleepiest*sleepiest_minute[0]}")
    
    
def calc_strategy2(input):
    guards = build_guard_dict(parse_entries(input))
    sleepiest = (0, 0, 0) # (guard, minute, number of minutes)
    
    for g, minutes in guards.items():
        if len(minutes) <= 0:
            continue
        max = sorted(minutes.items(), key=operator.itemgetter(1), reverse=True)[0]
        if max[1] > sleepiest[2]:
            sleepiest = (g, max[0], max[1])
    print(f"answer2: {sleepiest[0]*sleepiest[1]}")

# input=["[1518-11-05 00:03] Guard #99 begins shift",
# "[1518-11-01 00:00] Guard #10 begins shift",
# "[1518-11-05 00:45] falls asleep",
# "[1518-11-01 00:30] falls asleep",
# "[1518-11-03 00:29] wakes up",
# "[1518-11-04 00:02] Guard #99 begins shift",
# "[1518-11-01 00:55] wakes up",
# "[1518-11-01 23:58] Guard #99 begins shift",
# "[1518-11-02 00:40] falls asleep",
# "[1518-11-02 00:50] wakes up",
# "[1518-11-03 00:05] Guard #10 begins shift",
# "[1518-11-03 00:24] falls asleep",
# "[1518-11-04 00:36] falls asleep",
# "[1518-11-04 00:46] wakes up",
# "[1518-11-01 00:05] falls asleep",
# "[1518-11-01 00:25] wakes up",
# "[1518-11-05 00:55] wakes up",
# ""]
with open("04_input.txt") as f:
    input = f.read().split("\n")
calc_strategy1(input)
calc_strategy2(input)