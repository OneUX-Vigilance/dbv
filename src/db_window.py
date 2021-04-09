from ui.db import Ui_MainWindow
from PySide6.QtWidgets import *


class DbWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def ok(self, d: dict):
        self.db = d
        self.ui.btn_ok.clicked.connect(self.tabl)
        self.show()
    def tabl(self):
        table = self.ui.le_table_name.text()
        found = False
        for t in self.db['tables']:
            if t == table:
                found = True
        if not found:
            return
        self.add_columns(table)

    def add_columns(self, table_name: str):
        r = self.db['rows'][table_name]
        tw = self.ui.tw_table_info
        tw.clear()
        tw.setHeaderLabels([]);
        self.ui.tw_table_info.setHeaderLabels(r)
       
        dt = []
        ch = []
        for row in r:
            dtt = self.convert_list_to_str_list(r[row])
            ch.append(dtt)
            
    
        c = 0
        i = 0
        c = len(ch[0])
        while i < c:
            obj = []
            for it in ch:
                obj.append(it[i]);
            dt.append(obj)
            i += 1;
    
        for it in dt:
            QTreeWidgetItem(tw, it)

    def convert_list_to_str_list(self, inp: list):
        result = []
        for it in inp:
            result.append(str(it))
        return result
