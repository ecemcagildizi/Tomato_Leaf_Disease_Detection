import sys
from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from ui.sign_in_ui.sign_in import Ui_Widget
from ui.tomato_ui.tomato_app import TomatoWindow
from utils.supabase_client import get_user_by_email

class SignInWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.login)

        self.tomato_window = None

    def login(self):
        email = self.ui.lineEdit_email.text().strip()
        password = self.ui.lineEdit_password.text()

        user = get_user_by_email(email)
        if user and user.get("password") == password:
            user_id = user.get("id_users")
            self.tomato_window = TomatoWindow(user_id, parent_signin=self)
            self.tomato_window.show()
            
            self.ui.lineEdit_email.clear()
            self.ui.lineEdit_password.clear()
            self.hide()
        else:
            QMessageBox.warning(self, "Login Failed", "E-mail veya şifre yanlış!")

    
    def reset_fields(self):
        self.ui.lineEdit_email.clear()
        self.ui.lineEdit_password.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SignInWindow()
    window.show()
    sys.exit(app.exec())
