# Drowsiness Detection Project

This project implements a **Drowsiness Detection System** to identify if a driver or user is drowsy using real-time video streams. By monitoring the user's facial features, the system can detect signs of fatigue and trigger alerts to prevent accidents.

---

## Project Overview
The project uses computer vision and deep learning techniques to detect drowsiness. The system identifies:
- Eye closure
- Yawning
- Head tilts (optional)

If any of these signs persist beyond a defined threshold, an alert (e.g., a beep sound or visual warning) is triggered to notify the user.

This repository includes:
- Code for real-time video processing using OpenCV.
- A deep learning model for eye and mouth detection.
- Scripts for drowsiness detection and triggering alerts.

---

## Dataset
For training and evaluating the model, you can use the following datasets:

1. **MrlEye Dataset** (for eye closure detection)
   - [Download Here](https://github.com/sleepyeye/mrleye)
2. **YawDD Dataset** (for yawning detection)
   - [Download Here](https://www.kaggle.com/datasets/dataturks/yawn-dataset)

After downloading, extract the datasets and structure them as follows:
```
<project-root>/dataset/
    eyes/
        open/
        closed/
    mouth/
        yawning/
        not_yawning/
```

---

## Requirements
To run this project, ensure you have the following dependencies installed:

### Python Libraries
- TensorFlow / Keras
- OpenCV
- NumPy
- Dlib
- Matplotlib
- Pygame (for alert sounds)

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
├── models/                   -> Pre-trained models for detection
│
├── src/                      -> Source code
│   ├── drowsiness_detection.py -> Main script for drowsiness detection
│   ├── eye_detector.py       -> Script for eye detection
│   ├── mouth_detector.py     -> Script for yawning detection
│
├── utils/                    -> Helper scripts (e.g., alert system)
│
└── results/                  -> Results and logs
```

---

## How to Run the Project
Follow these steps to set up and run the project:

1. **Download Dataset**: Download the datasets mentioned above and place them in the `dataset/` folder.
2. **Install Dependencies**: Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```
3. **Run Real-Time Detection**: Execute the main script to start the detection system:
   ```bash
   python src/drowsiness_detection.py
   ```
   Ensure that your webcam is connected and accessible.
4. **Trigger Alerts**: The system will trigger:
   - A beep sound for prolonged eye closure.
   - A visual warning for yawning.

---

## Results
The system detects drowsiness accurately with the following features:
- Real-time monitoring of eyes and mouth.
- Adjustable thresholds for alert sensitivity.

**Example Scenarios:**
| Condition         | Alert Triggered |
|-------------------|-----------------|
| Eyes Closed > 3s  | Beep Sound      |
| Yawning Detected  | Visual Warning  |

---

## Future Improvements
- Integrate head tilt detection for improved accuracy.
- Implement a mobile application version.
- Use deep learning models for better facial landmark detection.

---

## License
This project is open-source and available under the MIT License.

---

## Credits
- **Datasets**: MrlEye Dataset, YawDD Dataset.
- **Libraries**: TensorFlow, Keras, OpenCV, Dlib.

---

## Contact
For any questions or suggestions, feel free to reach out:
- **Name**: Nitesh Kumar
- **Email**: nk7003361@gmail.com

---

**Thank you for exploring this project! Stay safe on the road! 🚗💤**
