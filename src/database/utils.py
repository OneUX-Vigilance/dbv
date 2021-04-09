import sqlite3
def verify_if_file_is_valid(path: str) -> bool: 
    try: 
        sqlite3.connect(path);
        return True;
    except:
        return False;
