# Sign Language Detection Using ASL Dataset

This project implements a **Sign Language Detection System** using the **Synthetic ASL Alphabet Dataset**. The goal of the project is to classify images of American Sign Language (ASL) hand gestures into their corresponding alphabet classes.

---

## Project Overview
The project uses deep learning techniques to train a model that can recognize ASL alphabets from images. The dataset consists of 27 classes, including letters A-Z and a **Blank** class, which is used to represent no sign.

This repository includes:
- Code for data preprocessing, model training, and evaluation.
- Instructions to download and set up the dataset.
- Scripts for making predictions on new images.

---

## Dataset
The **Synthetic ASL Alphabet Dataset** is used for training and testing. Due to the large size of the dataset, it is not included directly in this repository.

You can download the dataset manually from Kaggle:

🔗 [**Synthetic ASL Dataset**](https://www.kaggle.com/datasets/lexset/synthetic-asl-alphabet)

After downloading, extract the dataset and place it in the `dataset/` directory:
```
<project-root>/dataset/
    A/  -> Images of the letter A
    B/  -> Images of the letter B
    ...
    Z/  -> Images of the letter Z
    Blank/ -> Images representing the blank class
```

---

## Requirements
To run this project, ensure you have the following dependencies installed:

### Python Libraries
- TensorFlow / Keras
- NumPy
- OpenCV
- Matplotlib
- Pandas

Install all the dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

## Project Structure
```
<project-root>/
│   README.md                 -> Project overview (this file)
│   requirements.txt          -> List of Python dependencies
│
├── dataset/                  -> Dataset folder (downloaded separately)
│
├── models/                   -> Saved models
│
├── notebooks/                -> Jupyter notebooks for experimentation
│
├── src/                      -> Source code
│   ├── data_preprocessing.py -> Script for preprocessing dataset
│   ├── model_training.py     -> Script for training the model
│   ├── prediction.py         -> Script for predicting new images
│
└── results/                  -> Results and evaluation metrics
```

---

## How to Run the Project
Follow these steps to set up and run the project:

1. **Download Dataset**: Download the dataset from Kaggle and place it in the `dataset/` folder as described above.
2. **Install Dependencies**: Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. **Train the Model**: Run the model training script:
   ```bash
   python src/model_training.py
   ```
4. **Make Predictions**: Use the prediction script to test the model on new images:
   ```bash
   python src/prediction.py --image <path-to-image>
   ```

---

## Results
The trained model achieves high accuracy on the test dataset, making it suitable for real-world sign language recognition tasks.

**Example Results:**
| True Label | Predicted Label | Confidence |
|------------|-----------------|------------|
| A          | A               | 99.2%      |
| B          | B               | 98.7%      |

---

## Future Improvements
- Integrate real-time detection using a webcam.
- Expand the dataset for more complex gestures.
- Use transfer learning for improved accuracy and performance.

---

## License
This project is open-source and available under the MIT License.

---

## Credits
- **Dataset**: Provided by LexSet on Kaggle.
- **Libraries**: TensorFlow, Keras, OpenCV, and others.

---

## Contact
For any questions or suggestions, feel free to reach out:
- **Name**: Nitesh Kumar
- **Email**: nk7003361@gmail.com

---

**Thank you for using this project!** 🚀
