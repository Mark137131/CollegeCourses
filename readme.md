# University Course Projects Portfolio

This repository showcases core project implementations from undergraduate courses, covering digital image processing, technical writing, and embedded systems development. Each project is organized in dedicated directories with complete codebases, documentation, and demonstration materials.

![Project Banner](assets/banner.png) <!-- Replace with actual banner path -->

## 📂 Repository Structure

Repository/
├── Digital_Image_Processing/ # GUI-based Image Processing Toolkit
├── Expository_Writing/ # Technical Paper on Document Forgery Detection
└── Singlechip/ # 8051 MCU-based Music Box System

---

## 🖼️ Digital Image Processing Project
**Intuitive GUI for Image Manipulation**  
![GUI Demonstration](assets/dip_demo.gif) <!-- Update with actual media path -->

### Key Features
- Interactive parameter tuning for core algorithms
- Multi-format support (JPEG/PNG/BMP)
- Integrated modules: 
  - Edge detection (Sobel/Canny)
  - Spatial filtering (Gaussian/Median)
  - Histogram equalization

---

## 📝 Expository Writing
**Research Paper**: *Comprehensive Review on Document Forgery Detection Techniques*  
**Domain**: Digital Document Security · Image Forensics · Text Tampering Detection

### Abstract
> "With the proliferation of digital documents, forgery detection faces unique challenges in text manipulation compared to natural image alterations. This paper systematically analyzes seven mainstream detection methodologies, establishes evaluation metrics tailored for document authenticity verification, and identifies technical limitations in current forensic approaches. Our comparative study provides theoretical foundations for developing multimodal feature fusion solutions."

### Key Contributions
- Taxonomy of document forgery types (content/format/metadata)
- Quantitative analysis of text region manipulation detection
- Performance benchmarking on ICDAR datasets

---

## 🔊 Singlechip Music Box System
**8051 Microcontroller-Based Embedded Audio Platform**  
![Hardware Architecture](assets/singlechip_diagram.jpg) <!-- Add circuit/prototype photo -->

### System Features
| Mode         | Control Method      | Functionality               |
|--------------|---------------------|-----------------------------|
| 🎹 Manual    | Matrix Keypad       | Real-time LCD note display  |
| ▶️ Autoplay  | IR Remote           | Preloaded melody selection  |

### Modular Design
- **Display Unit**: 
  - LCD9648 with dynamic interface
- **Input System**: 
  - 4×4 matrix keypad (mode selection)
  - IR receiver (NEC protocol)
- **Audio Engine**: 
  - PWM-driven buzzer (12-tone equal temperament)
  - Tempo control (60-180 BPM)
- **Control Logic**: 
  - State machine implementation

---

## 🛠️ Technical Stack
- **Image Processing**: MATLAB App Designer + OpenCV-Python
- **Embedded Development**: 
  - Keil μVision IDE (C51 compiler)
  - Proteus 8 Professional (Circuit simulation)
- **Documentation**: LaTeX (IEEE conference template)

---

## 🚀 Quick Start
### Image Processing GUI
```bash
cd Digital_Image_Processing
matlab -nodisplay -r "run('src/main.m')"