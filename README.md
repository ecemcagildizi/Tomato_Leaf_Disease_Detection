##Tomato Leaf Disease Detection with CNN & Transfer Learning  

## Project Description  
This project focuses on developing a model that predicts whether tomato leaves are healthy or diseased based on their images. To achieve this, a **CNN-based Transfer Learning model, MobileNetV2**, was employed. The dataset was obtained from **Kaggle** and contains a total of **23,304 image samples**.  

In the project, the data was first preprocessed, followed by model training for a total of **30 epochs**. During training, the pre-trained layers of MobileNetV2 were initially frozen, and only the added classifier layers were trained for **20 epochs**. Afterwards, the entire network was fine-tuned with a lower learning rate for an additional **10 epochs**.  

To ensure efficient training, **ModelCheckpoint** was used to save the best-performing model, and **EarlyStopping** was implemented to prevent unnecessary overfitting. As a result, a model achieving **84% accuracy** was obtained.  

Additionally, a **desktop application** was built using **PySide6** to provide a user-friendly interface where users can upload leaf images and receive instant predictions. For storing user information and query history, the **Supabase cloud database** was integrated.  

---

## Features  
- High-accuracy classification with **MobileNetV2**  
- User-friendly **desktop application** (PySide6)  
- **Supabase integration** for user authentication & query history  
- Image upload and real-time predictions  

---

## Tech Stack  
- **Python**  
- **TensorFlow / Keras**  
- **MobileNetV2**  
- **PySide6**  
- **Supabase**
