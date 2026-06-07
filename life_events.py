def format_result(result):  
    """Convert a result dict to a readable string."""  
    if not result:  
        return "No effect"  
    parts = []  
    for stat, value in result.items():  
        sign = "+" if value >= 0 else ""  
        unit = "$" if stat == "savings" else ""  
        parts.append(f"{sign}{unit}{value:,} {stat}")  
    return ", ".join(parts)  
  
  
def apply_result(scott, result):  
    """Apply a result dict to scott's scores and stats."""  
    for stat, value in result.items():  
        if stat in scott.scores:  
            scott.scores[stat] += value  
        elif stat in scott.stats:  
            scott.scores[stat] = min(6, scott.stats[stat] + value) 
        elif stat == "savings":  
            scott.savings += value  

def married(scott):  
    scott.is_married = True   # or whatever side effect you need  
    print("  You are now married!")  
  
life_events = [  
    {  
        "description": "Get Married",  
        "optional":    True,  
        "requires":    15,  
        "type":        "relationships",  
        "buff_stat":   "charisma",  
        "results": {  
            "pass":    {},  
            "succeed": {"happiness": 2, "savings": -30000, "charisma": 1},  
            "fail":    {"relationships": -1},  
        },  
        "callbacks": {  
            "succeed": married,   # reference, not married()  
            "fail":    None,  
            "pass":    None,  
        }  
    },  
    {  
        "description": "Run a Half Marathon",  
        "optional":    True,  
        "requires":    6,  
        "type":        "health",  
        "buff_stat":   "fitness",  
        "results": {  
            "pass":    {},  
            "succeed": {"happiness": 1, "health": 1, "time": -1},  
            "fail":    {"health": -1},  
        },  
    },  
    {  
        "description": "Buy an apartment",  
        "optional":    True,  
        "requires":    10,  
        "type":        "",  
        "buff_stat":   "",  
        "results": {  
            "pass":    {"income": 1000},  
            "succeed": {"happiness": 4, "savings": -500000, "income": -4000, "time": -2},  
            "fail":    {"time": -2},  
        },  
    }, 
    {  
        "description": "Buy a new car",  
        "optional":    True,  
        "requires":    4,  
        "type":        "",  
        "buff_stat":   "intelligence",  
        "results": {  
            "pass":    {},  
            "succeed": {"time": 1, "savings": -8000},  
            "fail":    {"time": -1},  
        },  
    }, 
    {  
        "description": "Go on a vacation",  
        "optional":    True,  
        "requires":    6,  
        "type":        "",  
        "buff_stat":   "time",  
        "results": {  
            "pass":    {},  
            "succeed": {"savings": -5000, "happiness": 5},  
            "fail":    {"happiness": -1},  
        },  
    }, 
    {  
        "description": "Adopt a pet",  
        "optional":    True,  
        "requires":    6,  
        "type":        "",  
        "buff_stat":   "time",  
        "results": {  
            "pass":    {},  
            "succeed": {"income": -500, "happiness": 1, "relationships": 1, "time": -1},  
            "fail":    {"luck": -1},  
        },  
    }, 
    {  
        "description": "Become a landlord",  
        "optional":    True,  
        "requires":    15,  
        "type":        "",  
        "buff_stat":   "time",  
        "results": {  
            "pass":    {},  
            "succeed": {"income": 2000, "time": -5, "career": 1},  
            "fail":    {"luck": -1},  
        },  
    }, 
    {  
        "description": "See vulfpeck in concert",  
        "optional":    True,  
        "requires":    7,  
        "type":        "",  
        "buff_stat":   "",  
        "results": {  
            "pass":    {},  
            "succeed": {"savings": -500, "happiness": 5},  
            "fail":    {"happiness": -3},  
        },  
    }, 
    {  
        "description": "Get into metalurgy",  
        "optional":    True,  
        "requires":    7,  
        "type":        "",  
        "buff_stat":   "",  
        "results": {  
            "pass":    {},  
            "succeed": {"savings": -500, "happiness": 5},  
            "fail":    {"happiness": -3},  
        },  
    }, 
    {  
        "description": "Go on a bike trip",  
        "optional":    True,  
        "requires":    7,  
        "type":        "",  
        "buff_stat":   "",  
        "results": {  
            "pass":    {},  
            "succeed": {"savings": -500, "happiness": 5, "health": 3},  
            "fail":    {"happiness": -3},  
        },  
    }, 
    {  
        "description": "Start a side buisness",  
        "optional":    True,  
        "requires":    10,  
        "type":        "career",  
        "buff_stat":   "career",  
        "results": {  
            "pass":    {},  
            "succeed": {"savings": -10000, "income": 20000, "time": -10, "happiness": 5, "career": 8},  
            "fail":    {"happiness": -2, "career": -1},  
        },  
    }, 
    {  
        "description": "Build a house",  
        "optional":    True,  
        "requires":    10,  
        "type":        "",  
        "buff_stat":   "time",  
        "results": {  
            "pass":    {},  
            "succeed": {"savings": -1000000, "income": -5000, "time": -10, "happiness": 12},  
            "fail":    {"luck": -10},  
        },  
    }, 
]