# Course Projects

This repository covers digital image processing, technical writing, and embedded systems development. Each project is organized in dedicated directories with relevant materials.

## 📂 Repository Structure

```
Repository
├── Digital_Image_Processing  # GUI-based Image Processing Toolkit
├── Expository_Writing        # Technical Paper on Document Forgery Detection
├── Singlechip                # 8051 MCU-based Music Box System
└── Machine_Learning          # UV Index Prediction with Neural Networks

```

## Digital Image Processing Project

**Intuitive GUI for Image Manipulation**  

![Digital_Image_Processing/demo.png](https://github.com/Mark137131/CollegeCourses/blob/main/Digital_Image_Processing/demo.png)

### Key Features

- Interactive parameter tuning for core algorithms
- Integrated modules
  - Basic function
  - Spatial Filter
  - Frequency Filter
  - Add noise
  - Morphology

---

## Expository Writing

**Research Paper**: *Comprehensive Review on Document Forgery Detection Techniques*  
**Domain**: Digital Document Security · Image Forensics · Text Tampering Detection

### Key Contributions

- Comprehensive review of document forgery detection, emphasizing unique challenges compared to natural image forgery.
- Classification framework outlining forgery types, detection challenges, and evaluation metrics.
- Critical evaluation of seven detection methods, highlighting strengths and limitations.
- Comparative insights to advance research and practical solutions for document authenticity.

---

## Singlechip Music Box System

**8051 Microcontroller-Based Embedded Audio Platform**

![Singlechip/images/welcome.jpg](https://github.com/Mark137131/CollegeCourses/blob/main/Singlechip/images/welcome.jpg)

### System Features

| Mode         | Control Method      | Functionality               |
|--------------|---------------------|-----------------------------|
| 🎹 Manual    | Matrix Keypad       | Real-time LCD note display  |
| ▶️ Autoplay  | IR Remote           | Preloaded melody selection  |

![Singlechip/images/mode_selection.jpg](https://github.com/Mark137131/CollegeCourses/blob/main/Singlechip/images/mode_selection.jpg)

### Modular Design

- **Display module**:
  - LCD(lcd9648) displays screen
- **Input System**:
  - 4×4 matrix keypad (mode selection, etc)
  - Infrared receiver
- **Audio Engine**:
  - PWM-driven buzzer
  - Tempo control

---

## Machine Learning

**UV Index Prediction with Neural Networks**

### Overview
Use neural networks to capture non-linear patterns and boost UV Index prediction accuracy.

### Features
- **Neural Models**: Train feedforward networks for UV Index.
- **Ablation Tests**: Compare variations in layers, neurons, activations, learning rates, batch sizes, and early stopping.
- **PCA Comparison**: Train with and without PCA to see its effect.
- **Evaluation**: Report Mean Squared Error (MSE) and R².

### Results
- Neural networks beat traditional methods on MSE and R².
- Ablation reveals best architecture and training settings.
- PCA offers little benefit for small or specific datasets.

![Predicted vs. Actual UV Index](https://github.com/Mark137131/CollegeCourses/blob/main/Machine_Learning/images/GTvsPrediction.png)  
![Training Loss](https://github.com/Mark137131/CollegeCourses/blob/main/Machine_Learning/images/model_loss.png)

