def get_active_quest():
    try:
        with open(r'C:\ProgramData\Jagex\RuneScape-BETA\plugins\PluginData.db', 'rb') as f:
            data = f.read()
        # Find the LAST occurrence of Quest HelperactiveEntry
        pos = data.rfind(b'Quest HelperactiveEntry')
        if pos != -1:
            rest = data[pos + len(b'Quest HelperactiveEntry'):pos + 120]
            # Format in SQLite row or raw key-value:
            # Often preceded by length byte or null-terminated
            import re
            m = re.search(b'[\x01-\x1f]?([A-Za-z0-9 \':,-]+)\x00', rest)
            if m:
                return m.group(1).decode('utf-8', errors='ignore')
    except Exception as e:
        print("Error:", e)
    return None

print("Active quest:", get_active_quest())
