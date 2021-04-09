from PySide6.QtCore import QModelIndex, QObject
from PySide6.QtWidgets import QMainWindow,QApplication,QFileDialog,QErrorMessage;
from src.db_window import DbWindow;
import sys
from src.database.read import read_db, read_db_front

from ui.load_file_window import Ui_MainWindow;
import src.database.utils as dbUtils;
def show_err_message(error):
    t = QErrorMessage()
    t.setWindowTitle("ERRO!")
    t.showMessage(f"{error}","error");
    t.show()
    t.exec_()
    exit(1)
class LoadWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = Ui_MainWindow();
        self.ui.setupUi(self);
        self.setWindowTitle("Abrir um arquivo do sqlite");
        self.setFixedSize(self.size());
        self.ui.btn_open_file.clicked.connect(self.on_file_open_button_click);
    def on_file_open_button_click(self):
        self.ui.btn_open_file.setEnabled(False);
        self.fDiag = QFileDialog(self);
        self.fDiag.show()
        self.fDiag.exec_()

        self.on_end()
    def on_end(self):
        slFile = self.fDiag.selectedFiles()
        if (len(slFile)) <= 0: return;
        slFile = slFile[0];
        file_is_valid = dbUtils.verify_if_file_is_valid(slFile);
        if not file_is_valid: return;
        self.on_file_valid(slFile);
        self.ui.btn_open_file.setEnabled(True);
    def on_file_valid(self,path: str):
        self.ui.btn_open_file.setVisible(False);
        self.ui.load_progress.setMaximum(3);
        try:
            self.hide()
            db_JS = read_db_front(path,self.ui.lbl_status,self.ui.load_progress);
            self.ww = DbWindow();
            x = QModelIndex()
            self.ww.ok(db_JS)

        except Exception as e:
            show_err_message(e);
        pass
    
def main():
    app = QApplication(sys.argv)
    window = LoadWindow()
    window.show()


    sys.exit(app.exec_())
main()