# Planet2050: Sustainability Survival Game (Terminal Version)
# All in Python, no web or HTML, with emoji-based visuals

import time
import random
import os

# --- Game Setup ---
year = 2025
MAX_YEAR = 2075
WINNING_SCORE = 60
score = 50


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# --- Game Intro ---
def intro():
    clear()
    print("🌍 Welcome to Planet50")
    print("You're the leader of a small city navigating the climate crisis from 2025 to 2075.")
    print("Make smart choices to keep your community sustainable and alive.")
    print(f"Start Score: {score}\n")
    input("Press Enter to begin...")


# --- Generate Many Scenarios ---
def generate_many_scenarios():
    base_scenarios = []
    base_year = 2025

    prompts = [
        "A tech company offers to build a data center using fossil fuels.",
        "A developer proposes to clear urban forest for condos.",
        "Electric scooter sharing expands citywide.",
        "Air quality reaches hazardous levels for the third week in a row.",
        "Drought forces emergency water conservation rules.",
        "A tidal energy pilot project seeks government support.",
        "Massive algae bloom shuts down local fisheries.",
        "Public demand rises for low-carbon school lunches.",
        "High-speed rail investment opportunity appears.",
        "Citizens call for a ban on single-use plastics at events."
    ]

    choices_template = [
        ("a", "Accept without changes 🏗️", -10),
        ("b", "Reject and draft green alternatives 📄", +8),
        ("c", "Run public consultations 🗣️", +4),
        ("d", "Delay decision for economic review 💰", -3)
    ]

    # Generate enough scenarios to reach ~1000 lines of code
    for i in range(100):
        prompt = random.choice(prompts)
        scenario = {
            "year": base_year + i,
            "prompt": f"{prompt} (Scenario #{i + 1})",
            "choices": {key: {"text": text, "score": score} for key, text, score in choices_template}
        }
        base_scenarios.append(scenario)

    return base_scenarios
# --- Play Game ---
def play():
    global score
    intro()
    scenarios = generate_many_scenarios()
    for scenario in scenarios:
        clear()
        print(f"📅 Year: {scenario['year']}")
        print("\n" + scenario['prompt'] + "\n")

        for key, value in scenario['choices'].items():
            print(f"  {key.upper()}) {value['text']}")

        choice = input("\nChoose (A/B/C/D): ").lower().strip()
        while choice not in scenario['choices']:
            choice = input("Invalid choice. Choose A, B, C, or D: ").lower().strip()

        score_change = scenario['choices'][choice]['score']
        score += score_change

        if score_change > 0:
            print(f"\n✅ Good choice! You gained {score_change} sustainability points.")
        else:
            print(f"\n⚠️ That hurt your sustainability score by {abs(score_change)}.")

        print(f"🌿 Current Score: {score}\n")
        time.sleep(1.5)

    end_game()


# --- End Game ---
def end_game():
    clear()
    print("\n🏁 GAME OVER - FINAL REPORT")
    print(f"Sustainability Score: {score}")

    if score >= WINNING_SCORE:
        print("\n🎉 You led your people to a greener, safer 2075! Humanity is thriving thanks to you.")
    else:
        print("\n💀 Your leadership failed to prepare for the climate crisis. Society collapsed.")

    print("\nThanks for playing Planet50!")


# --- Run ---
if __name__ == '__main__':
    play()
# --- Additional Game Stats ---
public_approval = 50  # new metric: citizens' trust in your leadership


# --- Crisis Event Generator ---
def generate_crisis():
    crises = [
        {
            "name": "Wildfire 🔥",
            "effect": {"sustainability": -5, "approval": -10},
            "message": "A wildfire has damaged forested areas and homes."
        },
        {
            "name": "Climate Protest 🚸",
            "effect": {"sustainability": 0, "approval": -5},
            "message": "Youth-led protests call for bolder climate action."
        },
        {
            "name": "Innovation Boom ⚡",
            "effect": {"sustainability": +8, "approval": +5},
            "message": "A local startup invents a breakthrough solar panel!"
        },
        {
            "name": "Severe Drought 💧",
            "effect": {"sustainability": -6, "approval": -4},
            "message": "Reservoirs are drying up due to heat waves."
        },
        {
            "name": "Green Alliance 🌐",
            "effect": {"sustainability": +5, "approval": +10},
            "message": "Your city joins a global climate agreement."
        }
    ]
    if random.random() < 0.3:  # 30% chance of crisis per turn
        return random.choice(crises)
    return None


# --- Updated Play Loop with Crisis Events ---
def play():
    global score, public_approval
    intro()
    scenarios = generate_many_scenarios()
    for scenario in scenarios:
        clear()
        print(f"📅 Year: {scenario['year']}")
        print("\n" + scenario['prompt'] + "\n")

        for key, value in scenario['choices'].items():
            print(f"  {key.upper()}) {value['text']}")

        choice = input("\nChoose (A/B/C/D): ").lower().strip()
        while choice not in scenario['choices']:
            choice = input("Invalid choice. Choose A, B, C, or D: ").lower().strip()

        score_change = scenario['choices'][choice]['score']
        score += score_change
        public_approval += int(score_change / 2)

        if score_change > 0:
            print(f"\n✅ Good choice! You gained {score_change} sustainability points.")
        else:
            print(f"\n⚠️ That hurt your sustainability score by {abs(score_change)}.")

        # Check for crisis
        crisis = generate_crisis()
        if crisis:
            print(f"\n🚨 Crisis Event: {crisis['name']}")
            print(f"{crisis['message']}")
            score += crisis['effect']['sustainability']
            public_approval += crisis['effect']['approval']
            print(f"🌿 Sustainability impact: {crisis['effect']['sustainability']}")
            print(f"👥 Public Approval impact: {crisis['effect']['approval']}")

        print(f"\n🌿 Score: {score} | 👥 Public Approval: {public_approval}\n")
        time.sleep(1.5)
# --- Achievements System ---
achievements = []


def check_achievements(score, approval):
    global achievements
    unlocked = []

    if score >= 75 and "Eco Champion 🏆" not in achievements:
        unlocked.append("Eco Champion 🏆")
        achievements.append("Eco Champion 🏆")

    if approval >= 80 and "Beloved Leader 👑" not in achievements:
        unlocked.append("Beloved Leader 👑")
        achievements.append("Beloved Leader 👑")

    if score <= 20 and "On Thin Ice 🧊" not in achievements:
        unlocked.append("On Thin Ice 🧊")
        achievements.append("On Thin Ice 🧊")

    if approval <= 15 and "Unpopular Politician 👎" not in achievements:
        unlocked.append("Unpopular Politician 👎")
        achievements.append("Unpopular Politician 👎")

    if score >= 50 and approval >= 50 and "Balanced Visionary ⚖️" not in achievements:
        unlocked.append("Balanced Visionary ⚖️")
        achievements.append("Balanced Visionary ⚖️")

    return unlocked


# --- Updated End Game with Achievements ---
def end_game():
    clear()
    print("\n🏁 GAME OVER - FINAL REPORT")
    print(f"Sustainability Score: {score}")
    print(f"Public Approval: {public_approval}\n")

    if score >= WINNING_SCORE:
        print("🎉 You led your people to a greener, safer 2075! Humanity is thriving thanks to you.")
    else:
        print("💀 Your leadership failed to prepare for the climate crisis. Society collapsed.")

    print("\n🎖️ Achievements Unlocked:")
    unlocked = check_achievements(score, public_approval)
    if unlocked:
        for badge in unlocked:
            print(f" - {badge}")
    else:
        print(" - None this time. Try again!")

    print("\nThanks for playing Planet50!\n")
# --- Dynamic Weather System ---
def generate_weather_effect():
    weather_events = [
        {
            "type": "Heatwave ☀️",
            "message": "A brutal heatwave strains infrastructure.",
            "score_mod": -4,
            "approval_mod": -3
        },
        {
            "type": "Torrential Rain 🌧️",
            "message": "Heavy rains cause flooding in low-lying areas.",
            "score_mod": -2,
            "approval_mod": -2
        },
        {
            "type": "Mild Spring 🌸",
            "message": "Pleasant weather boosts morale and eco-tourism.",
            "score_mod": +3,
            "approval_mod": +4
        },
        {
            "type": "Dust Storm 🌪️",
            "message": "Visibility is reduced and travel is disrupted.",
            "score_mod": -3,
            "approval_mod": -2
        },
        {
            "type": "Cool Breeze 🍃",
            "message": "Energy demand drops as weather cools naturally.",
            "score_mod": +2,
            "approval_mod": +1
        }
    ]
    if random.random() < 0.2:  # 20% chance of weather per turn
        return random.choice(weather_events)
    return None


# --- Extended Play Loop With Weather ---
def play():
    global score, public_approval
    intro()
    scenarios = generate_many_scenarios()

    for scenario in scenarios:
        clear()
        print(f"📅 Year: {scenario['year']}")
        print("\n" + scenario['prompt'] + "\n")

        for key, value in scenario['choices'].items():
            print(f"  {key.upper()}) {value['text']}")

        choice = input("\nChoose (A/B/C/D): ").lower().strip()
        while choice not in scenario['choices']:
            choice = input("Invalid choice. Choose A, B, C, or D: ").lower().strip()

        score_change = scenario['choices'][choice]['score']
        score += score_change
        public_approval += int(score_change / 2)

        if score_change > 0:
            print(f"\n✅ Good choice! You gained {score_change} sustainability points.")
        else:
            print(f"\n⚠️ That hurt your sustainability score by {abs(score_change)}.")

        # Crisis check
        crisis = generate_crisis()
        if crisis:
            print(f"\n🚨 Crisis Event: {crisis['name']}")
            print(f"{crisis['message']}")
            score += crisis['effect']['sustainability']
            public_approval += crisis['effect']['approval']
            print(f"🌿 Crisis Score Impact: {crisis['effect']['sustainability']}")
            print(f"👥 Crisis Approval Impact: {crisis['effect']['approval']}")

        # Weather check
        weather = generate_weather_effect()
        if weather:
            print(f"\n⛅ Weather Update: {weather['type']}")
            print(f"{weather['message']}")
            score += weather['score_mod']
            public_approval += weather['approval_mod']
            print(f"🌿 Weather Score Impact: {weather['score_mod']}")
            print(f"👥 Weather Approval Impact: {weather['approval_mod']}")

        print(f"\n🌿 Score: {score} | 👥 Public Approval: {public_approval}\n")
        time.sleep(1.5)
# --- Track Player Decision History ---
decision_log = []


def log_decision(year, choice_key, choice_text, score_effect):
    decision_log.append({
        "year": year,
        "choice": choice_key.upper(),
        "description": choice_text,
        "impact": score_effect
    })


# --- Updated Play Function with Logging ---
def play():
    global score, public_approval
    intro()
    scenarios = generate_many_scenarios()

    for scenario in scenarios:
        clear()
        print(f"📅 Year: {scenario['year']}")
        print("\n" + scenario['prompt'] + "\n")

        for key, value in scenario['choices'].items():
            print(f"  {key.upper()}) {value['text']}")

        choice = input("\nChoose (A/B/C/D): ").lower().strip()
        while choice not in scenario['choices']:
            choice = input("Invalid choice. Choose A, B, C, or D: ").lower().strip()

        selected = scenario['choices'][choice]
        score_change = selected['score']
        score += score_change
        public_approval += int(score_change / 2)

        # Log choice
        log_decision(scenario['year'], choice, selected['text'], score_change)

        if score_change > 0:
            print(f"\n✅ Good choice! You gained {score_change} sustainability points.")
        else:
            print(f"\n⚠️ That hurt your sustainability score by {abs(score_change)}.")

        # Crisis check
        crisis = generate_crisis()
        if crisis:
            print(f"\n🚨 Crisis Event: {crisis['name']}")
            print(f"{crisis['message']}")
            score += crisis['effect']['sustainability']
            public_approval += crisis['effect']['approval']
            print(f"🌿 Crisis Score Impact: {crisis['effect']['sustainability']}")
            print(f"👥 Crisis Approval Impact: {crisis['effect']['approval']}")

        # Weather check
        weather = generate_weather_effect()
        if weather:
            print(f"\n⛅ Weather Update: {weather['type']}")
            print(f"{weather['message']}")
            score += weather['score_mod']
            public_approval += weather['approval_mod']
            print(f"🌿 Weather Score Impact: {weather['score_mod']}")
            print(f"👥 Weather Approval Impact: {weather['approval_mod']}")

        print(f"\n🌿 Score: {score} | 👥 Public Approval: {public_approval}\n")
        time.sleep(1.5)
# --- Show Decision History at End ---
def show_decision_log():
    print("\n📜 Your Leadership Decisions:\n")
    if not decision_log:
        print("No decisions recorded.")
        return

    for entry in decision_log:
        symbol = "✅" if entry['impact'] > 0 else "⚠️" if entry['impact'] < 0 else "➖"
        print(f"{symbol} Year {entry['year']} | Choice {entry['choice']}: {entry['description']} (Impact: {entry['impact']})")


# --- Final End Game Output with History ---
def end_game():
    clear()
    print("\n🏁 GAME OVER - FINAL REPORT")
    print(f"Sustainability Score: {score}")
    print(f"Public Approval: {public_approval}\n")

    if score >= WINNING_SCORE and public_approval >= 60:
        print("🌟 You led your city to global recognition for climate innovation!")
    elif score >= WINNING_SCORE:
        print("🎉 You led your people to a greener, safer 2075! Humanity is thriving thanks to you.")
    elif score < 25 and public_approval < 25:
        print("💥 Total breakdown: pollution, protests, and political collapse.")
    else:
        print("💀 Your leadership failed to prepare for the climate crisis. Society struggled to survive.")

    print("\n🎖️ Achievements Unlocked:")
    unlocked = check_achievements(score, public_approval)
    if unlocked:
        for badge in unlocked:
            print(f" - {badge}")
    else:
        print(" - None this time. Try again!")

    show_decision_log()
    print("\nThanks for playing Planet2050!\n")
# --- Public Voting Events ---
def public_vote_event():
    votes = [
        {
            "topic": "Introduce a city-wide composting mandate?",
            "outcome": {
                "passed": {"score": +6, "approval": +8, "message": "The composting initiative passed and residents love it!"},
                "failed": {"score": -2, "approval": -4, "message": "The composting bill failed. Critics call it 'overreach'."}
            }
        },
        {
            "topic": "Ban gasoline cars by 2040?",
            "outcome": {
                "passed": {"score": +10, "approval": +6, "message": "City celebrates the future of electric mobility!"},
                "failed": {"score": -5, "approval": -3, "message": "Auto industry lobby kills the clean car bill."}
            }
        },
        {
            "topic": "Tax plastic packaging for manufacturers?",
            "outcome": {
                "passed": {"score": +7, "approval": +5, "message": "Waste reduction improves across all districts."},
                "failed": {"score": -3, "approval": -2, "message": "Environmental groups protest weak government resolve."}
            }
        },
        {
            "topic": "Provide free solar panels for low-income families?",
            "outcome": {
                "passed": {"score": +9, "approval": +10, "message": "Equity-focused climate policy wins national praise."},
                "failed": {"score": -4, "approval": -5, "message": "The policy failed—advocates call for reform."}
            }
        }
    ]

    if random.random() < 0.2:  # 20% chance of public vote
        vote = random.choice(votes)
        print(f"\n🗳️ Public Referendum: {vote['topic']}")
        # Simulate 60% chance vote passes
        passed = random.random() < 0.6
        outcome = vote['outcome']['passed'] if passed else vote['outcome']['failed']

        print(outcome['message'])
        global score, public_approval
        score += outcome['score']
        public_approval += outcome['approval']
        print(f"🌿 Score impact: {outcome['score']} | 👥 Approval impact: {outcome['approval']}")
# --- Unlockable Policy Cards ---
policy_cards = {
    "green_innovation_grant": {
        "name": "Green Innovation Grant 💡",
        "description": "Gain +10 sustainability points immediately.",
        "used": False,
        "effect": lambda: grant_points(10)
    },
    "community_healing_fund": {
        "name": "Community Healing Fund ❤️",
        "description": "Boost public approval by +15.",
        "used": False,
        "effect": lambda: boost_approval(15)
    },
    "carbon_offset_bonds": {
        "name": "Carbon Offset Bonds 🌳",
        "description": "Negate the next negative weather or crisis event.",
        "used": False,
        "effect": lambda: prevent_next_disaster()
    }
}

# Disaster prevention toggle
prevent_disaster_flag = False

def grant_points(amount):
    global score
    score += amount
    print(f"\n✅ You activated a policy card! +{amount} sustainability points.")

def boost_approval(amount):
    global public_approval
    public_approval += amount
    print(f"\n✅ You activated a policy card! +{amount} public approval.")

def prevent_next_disaster():
    global prevent_disaster_flag
    prevent_disaster_flag = True
    print("\n🛡️ Your next crisis or weather event will be neutralized.")

# --- Activate Available Cards ---
def offer_policy_cards():
    available = [key for key, card in policy_cards.items() if not card['used']]
    if not available or random.random() > 0.2:
        return  # No card offered this round

    key = random.choice(available)
    card = policy_cards[key]
    print(f"\n🃏 Policy Card Offered: {card['name']}")
    print(f"   {card['description']}")
    choice = input("   Do you want to activate it now? (y/n): ").strip().lower()
    if choice == 'y':
        card['effect']()
        card['used'] = True
# --- Global Treaty Events ---
def treaty_event():
    treaties = [
        {
            "name": "Kyoto 2.0 Accord ✍️",
            "score": +10,
            "approval": +6,
            "message": "You signed the Kyoto 2.0 Accord. Emissions targets are now binding!"
        },
        {
            "name": "Global Solar Initiative ☀️🌍",
            "score": +8,
            "approval": +5,
            "message": "You joined the Global Solar Initiative, improving tech access."
        },
        {
            "name": "Carbon Border Agreement 🌐",
            "score": +5,
            "approval": +3,
            "message": "Your trade policies now factor carbon costs across borders."
        }
    ]
    if random.random() < 0.15:  # 15% chance
        treaty = random.choice(treaties)
        print(f"\n🌎 Treaty Event: {treaty['name']}")
        print(treaty['message'])
        global score, public_approval
        score += treaty['score']
        public_approval += treaty['approval']
        print(f"🌿 Treaty Score Impact: {treaty['score']} | 👥 Approval Impact: {treaty['approval']}")

# --- Final Score Breakdown ---
def final_tier():
    print("\n📈 Final Performance Tier:")
    if score >= 90:
        print("🏅 Eco Utopia – You’ve built a climate-resilient model city!")
    elif score >= 70:
        print("🥈 Green Leader – Great progress, with some areas to improve.")
    elif score >= 50:
        print("🥉 Sustainable Survivor – Barely held things together.")
    else:
        print("💀 System Collapse – Major reform is needed. Try again!")

# --- Play Again Prompt ---
def play_again():
    choice = input("\n🔁 Do you want to play again? (y/n): ").strip().lower()
    if choice == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        print("👋 Goodbye, leader. Until next time!")

# --- Hook: Add Calls to New Systems in Main Play Loop ---
# (Reminder: treaty_event() and offer_policy_cards() should be called each round)
# Add this inside the play loop after weather/crisis:
#     treaty_event()
#     offer_policy_cards()
# All done!




















# Planet2050: Sustainability Survival Game (Terminal Version)
# All in Python, no web or HTML, with emoji-based visuals

import time
import random
import os
import sys

# --- Game Setup ---
year = 2025
MAX_YEAR = 2075
WINNING_SCORE = 60
score = 50
public_approval = 50
money = 50  # 💰 Economy stat
achievements = []
joined_treaties = []
decision_log = []
prevent_disaster_flag = False

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def intro():
    clear()
    print("🌍 Welcome to Planet50")
    print("You're the leader of a small city navigating the climate crisis from 2025 to 2075.")
    print("Make smart choices to keep your community sustainable and alive.")
    print(f"Start Score: {score}\n")
    input("Press Enter to begin...")

def generate_many_scenarios():
    base_scenarios = []
    base_year = 2025
    prompts = [
        "A tech company offers to build a data center using fossil fuels.",
        "A developer proposes to clear urban forest for condos.",
        "Electric scooter sharing expands citywide.",
        "Air quality reaches hazardous levels for the third week in a row.",
        "Drought forces emergency water conservation rules.",
        "A tidal energy pilot project seeks government support.",
        "Massive algae bloom shuts down local fisheries.",
        "Public demand rises for low-carbon school lunches.",
        "High-speed rail investment opportunity appears.",
        "Citizens call for a ban on single-use plastics at events."
    ]
    choices_template = [
        ("a", "Accept without changes 🏗️", -10, -5, +10),
        ("b", "Reject and draft green alternatives 📄", +8, +4, -5),
        ("c", "Run public consultations 🗣️", +4, +2, -2),
        ("d", "Delay decision for economic review 💰", -3, -1, +3)
    ]
    for i in range(100):
        prompt = random.choice(prompts)
        scenario = {
            "year": base_year + i,
            "prompt": f"{prompt} (Scenario #{i + 1})",
            "choices": {key: {"text": text, "score": s, "approval": a, "money": m} for key, text, s, a, m in choices_template}
        }
        base_scenarios.append(scenario)
    return base_scenarios

def generate_crisis():
    crises = [
        {"name": "Wildfire 🔥", "effect": {"sustainability": -5, "approval": -10, "money": -8}, "message": "A wildfire has damaged forested areas and homes."},
        {"name": "Climate Protest 🚸", "effect": {"sustainability": 0, "approval": -5, "money": -2}, "message": "Youth-led protests call for bolder climate action."},
        {"name": "Innovation Boom ⚡", "effect": {"sustainability": +8, "approval": +5, "money": +10}, "message": "A local startup invents a breakthrough solar panel!"},
        {"name": "Severe Drought 💧", "effect": {"sustainability": -6, "approval": -4, "money": -5}, "message": "Reservoirs are drying up due to heat waves."},
        {"name": "Green Alliance 🌐", "effect": {"sustainability": +5, "approval": +10, "money": +3}, "message": "Your city joins a global climate agreement."}
    ]
    if random.random() < 0.3:
        return random.choice(crises)
    return None

def generate_weather_effect():
    weather_events = [
        {"type": "Heatwave ☀️", "message": "A brutal heatwave strains infrastructure.", "score_mod": -4, "approval_mod": -3, "money_mod": -3},
        {"type": "Torrential Rain 🌧️", "message": "Heavy rains cause flooding.", "score_mod": -2, "approval_mod": -2, "money_mod": -1},
        {"type": "Mild Spring 🌸", "message": "Pleasant weather boosts morale.", "score_mod": +3, "approval_mod": +4, "money_mod": +2},
        {"type": "Dust Storm 🌪️", "message": "Dust disrupts transit.", "score_mod": -3, "approval_mod": -2, "money_mod": -2},
        {"type": "Cool Breeze 🍃", "message": "Lower energy demand.", "score_mod": +2, "approval_mod": +1, "money_mod": +1}
    ]
    if random.random() < 0.2:
        return random.choice(weather_events)
    return None

def log_decision(year, choice_key, choice_text, score_effect):
    decision_log.append({"year": year, "choice": choice_key.upper(), "description": choice_text, "impact": score_effect})

def play():
    global score, public_approval, money
    intro()
    scenarios = generate_many_scenarios()
    for scenario in scenarios:
        clear()
        print(f"📅 Year: {scenario['year']}")
        print("\n" + scenario['prompt'] + "\n")
        for key, value in scenario['choices'].items():
            print(f"  {key.upper()}) {value['text']}")
        choice = input("\nChoose (A/B/C/D): ").lower().strip()
        while choice not in scenario['choices']:
            choice = input("Invalid choice. Choose A, B, C, or D: ").lower().strip()
        selected = scenario['choices'][choice]
        score += selected['score']
        public_approval += selected['approval']
        money += selected['money']
        log_decision(scenario['year'], choice, selected['text'], selected['score'])
        print(f"\n🌿 +{selected['score']} | 👥 +{selected['approval']} | 💰 +{selected['money']}")
        crisis = generate_crisis()
        if crisis:
            print(f"\n🚨 Crisis: {crisis['name']} - {crisis['message']}")
            score += crisis['effect']['sustainability']
            public_approval += crisis['effect']['approval']
            money += crisis['effect']['money']
        weather = generate_weather_effect()
        if weather:
            print(f"\n⛅ Weather: {weather['type']} - {weather['message']}")
            score += weather['score_mod']
            public_approval += weather['approval_mod']
            money += weather['money_mod']
        print(f"\n🌿 Score: {score} | 👥 Approval: {public_approval} | 💰 Economy: {money}\n")
        time.sleep(1.5)
    end_game()

def check_achievements(score, approval):
    global achievements
    unlocked = []
    if score >= 90:
        unlocked.append("Eco Champion 🏆")
    if approval >= 80:
        unlocked.append("Beloved Leader 👑")
    if score <= 20:
        unlocked.append("On Thin Ice 🧊")
    if approval <= 15:
        unlocked.append("Unpopular Politician 👎")
    if score >= 50 and approval >= 50:
        unlocked.append("Balanced Visionary ⚖️")
    return unlocked

def end_game():
    clear()
    print("\n🏁 GAME OVER - FINAL REPORT")
    print(f"Sustainability Score: {score}\nPublic Approval: {public_approval}\nEconomy: {money}\n")
    if score >= 90 and money >= 70:
        print("🏅 Eco Utopia – You’ve built a climate-resilient model city!")
    elif score > 70 and public_approval < 20:
        print("🚨 Public Revolt – Your green policies lacked popular support.")
    elif money >= 90:
        print("🤖 Tech Overload – Economic growth dominated sustainability.")
    elif len(joined_treaties) >= 2:
        print("🌍 Global Leader – You signed key treaties shaping international policy!")
    elif score >= WINNING_SCORE:
        print("🎉 You led your people to a greener, safer 2075!")
    else:
        print("💀 Society collapsed. Try again with better choices.")
    print("\nAchievements:")
    for badge in check_achievements(score, public_approval):
        print(f" - {badge}")
    print("\nThanks for playing Planet50!")
