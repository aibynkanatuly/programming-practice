import psycopg2
from config import load_config


def connect():
    cfg = load_config()
    print("CONFIG USED:", cfg)
    return psycopg2.connect(**cfg)


def get_player_id(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT id FROM players WHERE username=%s", (username,))
    row = cur.fetchone()

    if row:
        pid = row[0]
    else:
        cur.execute("INSERT INTO players(username) VALUES(%s) RETURNING id", (username,))
        pid = cur.fetchone()[0]
        conn.commit()

    cur.close()
    conn.close()
    return pid


def save_game(username, score, level):
    pid = get_player_id(username)

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO game_sessions(player_id, score, level_reached) VALUES(%s,%s,%s)",
        (pid, score, level)
    )

    conn.commit()
    cur.close()
    conn.close()


def get_top10():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT p.username, g.score, g.level_reached, g.played_at
        FROM game_sessions g
        JOIN players p ON g.player_id=p.id
        ORDER BY g.score DESC
        LIMIT 10
    """)

    data = cur.fetchall()
    cur.close()
    conn.close()
    return data


def get_best(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        SELECT MAX(score)
        FROM game_sessions g
        JOIN players p ON g.player_id=p.id
        WHERE p.username=%s
    """, (username,))

    row = cur.fetchone()
    cur.close()
    conn.close()

    return row[0] if row[0] else 0