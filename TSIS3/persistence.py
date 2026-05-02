import json
import os


def load_json(filename, default):
    if not os.path.exists(filename):
        save_json(filename, default)
        return default

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except:
        return default


def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def load_settings():
    return load_json("settings.json", {
        "sound": True,
        "car_color": "red",
        "difficulty": "normal"
    })


def save_settings(settings):
    save_json("settings.json", settings)


def load_leaderboard():
    return load_json("leaderboard.json", [])


def save_score(name, score, distance, coins):
    data = load_leaderboard()

    data.append({
        "name": name,
        "score": score,
        "distance": distance,
        "coins": coins
    })

    data.sort(key=lambda x: x["score"], reverse=True)
    data = data[:10]

    save_json("leaderboard.json", data)