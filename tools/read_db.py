import sqlite3

conn = sqlite3.connect(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db')
cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print("Tables:", cursor.fetchall())

try:
    cursor.execute("SELECT * FROM plugin_data LIMIT 50;")
    for row in cursor.fetchall():
        print(row)
except Exception as e:
    print(e)
