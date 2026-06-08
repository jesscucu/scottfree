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
        "description": "Get Sick",  
        "optional":    False,  
        "requires":    8,  
        "type":        "",  
        "buff_stat":   "luck",  
        "results": {  
            "succeed": {},  
            "fail":    {"health": -3},  
        },  
    },  
    {  
        "description": "Global Pandemic",  
        "optional":    False,  
        "requires":    18,  
        "type":        "",  
        "buff_stat":   "luck",  
        "results": {  
            "succeed": {"happiness": 5, "health": 3},  
            "fail":    {"happiness": -3, "health": -3},  
        },  
    }, 
    {  
        "description": "Stock Market Crash",  
        "optional":    False,  
        "requires":    15,  
        "type":        "career",  
        "buff_stat":   "luck",  
        "results": {  
            "succeed": {},  
            "fail":    {"savings": -10000},  
        },  
    }, 
    {  
        "description": "Canada invaded by US",  
        "optional":    False,  
        "requires":    8,  
        "type":        "",  
        "buff_stat":   "luck",  
        "results": {  
            "succeed": {},  
            "fail":    {"happiness": -10},  
        }, 
    }, 
    {  
        "description": "Wins lottery",  
        "optional":    False,  
        "requires":    19,  
        "type":        "",  
        "buff_stat":   "luck",  
        "results": {  
            "succeed": {"savings": 1000000, "relationships": -4},  
            "fail":    {},  
        }, 
    }, 
    {  
        "description": "Layoffs",  
        "optional":    False,  
        "requires":    12,  
        "type":        "",  
        "buff_stat":   "career",  
        "results": {  
            "succeed": {"career": 2},  
            "fail":    {"income": -10000, "happiness": -4},  
        }, 
    }, 
    {  
        "description": "Becomes an uncle",  
        "optional":    False,  
        "requires":    3,  
        "type":        "relationships",  
        "buff_stat":   "relationships",  
        "results": {  
            "succeed": {"savings": -300, "time": -1, "happiness": 1},  
            "fail":    {},  
        }, 
    }, 


    Canada is invaded by US
    Wins lottery
    Looses his job
    New job opprotunity 
    Takes a surendered animal 
    Sees Vupflack in concert
    Vacation 
    Builds a house
    Become a landlord 
    Becomes an unlce
    Goes camping 
    Takes up metalurgy 

]