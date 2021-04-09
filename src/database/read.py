import sqlite3;
from PySide6.QtWidgets import QProgressBar,QLabel
def fetch_tables(cursor: sqlite3.Cursor) -> list:
    exec = cursor.execute("select name from sqlite_master where type = 'table';");
    l = exec.fetchall()
    result = []
    for i in l:
        result.append(" ".join(i))
    return result;
def fetch_rows(cursor: sqlite3.Cursor, tables: list) -> dict:
    result = {};
    for table in tables: 
        exec = cursor.execute(f"SELECT * FROM {table}");
        names = list(map(lambda x: x[0], cursor.description))
        rows = exec.fetchall();
        rows_b = []
        r = {}
        current_column = 0;        
        for row in rows:
            for row_name in names:
                rows_b.append({'name': row_name, 'data': row[current_column]})
                r[row_name] = [];
                current_column += 1;
            current_column = 0;
        for row in rows_b:     
           r[row['name']].append(row['data']);    
        result[table] = r;
    return result;
def read_db(path: str):
    db = sqlite3.connect(path);
    cursor = db.cursor()
    tables = fetch_tables(cursor);    
    rows   = fetch_rows(cursor,tables);
def read_db_front(path: str,lbl: QLabel,b: QProgressBar) -> dict:
    lbl.setText("status: carregando arquivo...")
    db = sqlite3.connect(path);
    cursor = db.cursor()
    b.setValue(1)
    lbl.setText("status: carregando tabelas...")
    b.setValue(2)
    tables = fetch_tables(cursor);    
    lbl.setText("status: carregando colunas...")
    rows  = fetch_rows(cursor,tables);
    b.setValue(3)
    return {
        'database': db,
        'tables': tables,
        'rows': rows,
    }
    