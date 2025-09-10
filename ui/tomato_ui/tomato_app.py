import cv2
import numpy as np
from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtGui import QPixmap
from tensorflow.keras.models import load_model

from ui.tomato_ui.tomato_ui import Ui_Widget

from PySide6.QtGui import QStandardItemModel, QStandardItem
from utils.supabase_client import get_user_history, insert_history


class TomatoWindow(QWidget):
    def __init__(self,user_id,parent_signin=None):
        super().__init__()
        self.user_id = user_id
        self.parent_signin = parent_signin 

        self.ui = Ui_Widget()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.sign_out)

        self.load_history()


        
        self.ui.widget_predict.hide()
        self.ui.pushButton_2_visible.clicked.connect(self.show_predict_area)

        
        self.model = load_model("/Users/ecemcagildizi/Desktop/Tomato_Project/model/mobilenetv2_best.keras")

        
        self.class_names = [
            "Tomato___Bacterial_spot",
            "Tomato___Early_blight",
            "Tomato___Late_blight",
            "Tomato___Leaf_Mold",
            "Tomato___Septoria_leaf_spot",
            "Tomato___Spider_mites Two-spotted_spider_mite",
            "Tomato___Target_Spot",
            "Tomato___Tomato_Yellow_Leaf_Curl_Virus",
            "Tomato___Tomato_mosaic_virus",
            "Tomato___healthy"
        ]

        self.ui.pushButton_load.clicked.connect(self.load_image)
        self.ui.pushButton_predict.clicked.connect(self.predict_image)

        self.image_path = None
       
        self.ui.label_image.setScaledContents(True)

    def sign_out(self):
        self.close() 
        if self.parent_signin:
            self.parent_signin.reset_fields()
            self.parent_signin.show()

    def show_predict_area(self):
        self.ui.widget_predict.show()

    def load_image(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg)")
        if file_name:
            self.image_path = file_name
            self.ui.label_image.setPixmap(QPixmap(file_name))

    def predict_image(self):
        if not self.image_path:
            self.ui.label_result.setText("Please select image for predict!")
            return

        img = cv2.imread(self.image_path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (224, 224))
        img = img.astype("float32") / 255.0
        img = np.expand_dims(img, axis=0)

        prediction = self.model.predict(img)
        class_idx = np.argmax(prediction[0])
        predicted_class = self.class_names[class_idx]

        if predicted_class == "Tomato___healthy":
            result_text = "The Leaf is Healthy"
            self.ui.label_result.setText(result_text)
            self.ui.textEdit_advice.clear()
        else:
            result_text = f"The Leaf is Unhealthy ~ {predicted_class} ~"
            self.ui.label_result.setText(result_text)
            self.show_ai_advice()

        
        insert_history(self.user_id, result_text)

        
        self.load_history()

    def show_ai_advice(self):
        advice = (
            "The leaf look like unhealthy. Suggestions:\n"
            "- Make to water regularly\n"
            "- Provide sunlight exposure\n"
            "- Apply a fungicide if needed"
        )
        self.ui.textEdit_advice.setText(advice)


    def load_history(self):
        data = get_user_history(self.user_id)
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(["Response", "Created At"])

        for row in data:
            items = [
                QStandardItem(row["response"]),
                QStandardItem(row["created_at"])
            ]
            model.appendRow(items)

        self.ui.tableView.setModel(model)
    


