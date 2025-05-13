 # EMG-to-Joint-Angle Decoding

Predict finger joint angles from surface EMG signals using machine learning, designed for prosthetic control applications.

## Features
- Multi-Layer Perceptron (MLP) for joint angle prediction (`model.py`)
- EMG-Joint Angle Alignment with convolving RMS windows (`align_emg.py`)
- MediaPipe-based Kinematics Extraction** from video input (`extract_joint_angles.py`)
- Real-time compatible processing pipeline (1000Hz EMG → 60Hz joint angles)

## Installation
```bash
git clone https://github.com/risray700/EMG_Joint_Decode.git
cd EMG_Joint_Decode
pip install -r requirements.txt

## Instructions
python extract_joint_angles.py --input hand_movement.mp4 --output angles.csv
