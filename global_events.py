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
            scott.stats[stat] += value  
        elif stat == "savings":  
            scott.savings += value  
  
  
global_events = [  
    {  
        "description": "Get Married",  
        "optional":    True,  
        "requires":    15,  
        "type":        "relationships",  
        "buff_stat":   "charisma",  
        "results": {  
            "pass":    {},  
            "succeed": {"happiness": 2, "savings": -20000, "charisma": 1},  
            "fail":    {"relationships": -1},  
        },  
    },  
    {  
        "description": "Run a Half Marathon",  
        "optional":    True,  
        "requires":    6,  
        "type":        "health",  
        "buff_stat":   "fitness",  
        "results": {  
            "pass":    {},  
            "succeed": {"happiness": 2, "fitness": 1, "time": -1},  
            "fail":    {"fitness": -1, "health": -1},  
        },  
    },  
    {  
        "description": "Get Sick",  
        "optional":    False,  
        "requires":    8,  
        "type":        "health",  
        "buff_stat":   "fitness",  
        "results": {  
            "succeed": {"health": -1},  
            "fail":    {"health": -3, "savings": -5000},  
        },  
    },  
]