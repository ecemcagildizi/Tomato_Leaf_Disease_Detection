
## Project Description  
This project involves developing a model that predicts whether tomato leaves are healthy or diseased based on their images. For this purpose, **MobileNetV2**, a CNN-based Transfer Learning model, was chosen. The dataset was obtained from **Kaggle** and contains a total of **23,304 image samples**.  

In the project, **data preprocessing** was performed first, followed by model training for a total of **30 epochs**. During training, the pre-trained layers of the model were initially frozen, and only the added classifier layers were trained for **20 epochs**. Afterwards, the entire network was unfrozen and trained with a lower learning rate for an additional **10 epochs**.  

To save the best model, **ModelCheckpoint** was used, and to prevent unnecessary long training, **EarlyStopping** was applied. As a result, a model with **84% accuracy** was obtained.  

In addition, a **desktop interface** was developed using **PySide6** to allow users to easily upload images and view predictions. To store user information and query history, the **Supabase cloud database** was integrated.

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
