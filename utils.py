import sqlite3
from datetime import datetime

def init_db():
    conn = sqlite3.connect('curio_memory.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ts TEXT, 
            query TEXT, 
            response TEXT
        )
    ''')
    conn.commit()
    conn.close()

def log_interaction(query, response):
    conn = sqlite3.connect('curio_memory.db')
    c = conn.cursor()
    c.execute('INSERT INTO logs (ts, query, response) VALUES (?,?,?)', 
              (datetime.now().isoformat(), query, response))
    conn.commit()
    conn.close()

def get_recent_history(limit=5):
    conn = sqlite3.connect('curio_memory.db')
    c = conn.cursor()
    c.execute('SELECT query, response FROM logs ORDER BY ts DESC LIMIT ?', (limit,))
    data = c.fetchall()
    conn.close()
    return data

def build_character_prompt(name, user_description):
    if not user_description:
        user_description = "their standard canonical personality."
        
    refined_prompt = f"""
    ROLEPLAY PROTOCOL:
    1. PRIMARY IDENTITY: You are {name}.
    2. KNOWLEDGE BASE: Access all historical, cultural, and literary data regarding {name}. 
       Adopt their specific speech patterns, vocabulary, and moral compass.
    3. USER OVERRIDE: Integrate these specific traits provided by the user: "{user_description}".
    4. SYNERGY: If {name} is a known figure (e.g., Batman, Sherlock Holmes), value their core 
       canonical traits as much as the user's description. Merge them seamlessly.
    5. GUIDELINE: Never break character. Never refer to yourself as an AI. 
       If asked something outside your lore, answer as {name} would react to that information.
    """
    return refined_prompt.strip()