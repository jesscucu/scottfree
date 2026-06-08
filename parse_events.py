import csv  
import sys  
  
SUCCEED_SCORE_KEYS = ["savings", "relationships", "career", "happiness", "health"]  
SUCCEED_BUFF_KEYS  = ["savings", "income", "luck", "charisma", "fitness", "time", "intelligence"]  
FAIL_KEYS          = ["relationships", "career", "happiness", "health", "savings",  
                      "income", "luck", "charisma", "fitness", "time", "intelligence"]  
  
def parse_int(val):  
    try:  
        return int(val)  
    except (ValueError, TypeError):  
        return 0  
  
def build_result(keys, values):  
    result = {}  
    for key, val in zip(keys, values):  
        n = parse_int(val)  
        if n != 0:  
            result[key] = result.get(key, 0) + n  
    return result  
  
def repr_dict(d):  
    if not d:  
        return "{}"  
    inner = ", ".join(f'"{k}": {v}' for k, v in d.items())  
    return "{" + inner + "}"  
  
def convert(filepath):  
    with open(filepath, newline="", encoding="utf-8") as f:  
        reader = csv.reader(f)  
        next(reader)  # skip header row 1  
        next(reader)  # skip header row 2  
  
        events = []  
        for row in reader:  
            if not row or not row[0].strip():  
                continue  
  
            row += [""] * (34 - len(row))  
  
            description      = row[0].strip()  
            optional         = row[1].strip().upper() == "T"  
            requires         = parse_int(row[2])  
            event_type       = row[3].strip().lower() or None  
            buff_stat        = row[4].strip().lower() or None  
            succeed_msg      = row[6].strip()  
            fail_msg         = row[7].strip()  
            succeed_function = row[8].strip() or None  
            fail_function    = row[22].strip() or None  
            if fail_function == "0":  
                fail_function = None  
  
            succeed_scores = row[9:14]  
            succeed_buffs  = row[14:21]  
            fail_vals      = row[23:34]  
  
            succeed = build_result(SUCCEED_SCORE_KEYS, succeed_scores)  
            for key, val in zip(SUCCEED_BUFF_KEYS, succeed_buffs):  
                n = parse_int(val)  
                if n != 0:  
                    succeed[key] = succeed.get(key, 0) + n  
  
            fail = build_result(FAIL_KEYS, fail_vals)  
  
            events.append({  
                "description":      description,  
                "optional":         optional,  
                "requires":         requires,  
                "type":             event_type,  
                "buff_stat":        buff_stat,  
                "succeed_msg":      succeed_msg,  
                "fail_msg":         fail_msg,  
                "succeed_function": succeed_function,  
                "fail_function":    fail_function,  
                "succeed":          succeed,  
                "fail":             fail,  
            })  
  
        return events  
  
def print_events(events):  
    print("life_events = [")  
    for e in events:  
        print("    {")  
        print(f'        "description":      {repr(e["description"])},')  
        print(f'        "optional":         {e["optional"]},')  
        print(f'        "requires":         {e["requires"]},')  
        print(f'        "type":             {repr(e["type"])},')  
        print(f'        "buff_stat":        {repr(e["buff_stat"])},')  
        print(f'        "succeed_msg":      {repr(e["succeed_msg"])},')  
        print(f'        "fail_msg":         {repr(e["fail_msg"])},')  
        if e["succeed_function"]:  
            print(f'        "succeed_function": {repr(e["succeed_function"])},')  
        if e["fail_function"]:  
            print(f'        "fail_function":    {repr(e["fail_function"])},')  
        print( '        "results": {')  
        if e["optional"]:  
            print( '            "pass":    {},')  
        print(f'            "succeed": {repr_dict(e["succeed"])},')  
        print(f'            "fail":    {repr_dict(e["fail"])},')  
        print( '        },')  
        print("    },")  
    print("]")  
  
if __name__ == "__main__":  
    filepath = sys.argv[1] if len(sys.argv) > 1 else "events.csv"  
    events = convert(filepath)  
    print_events(events)