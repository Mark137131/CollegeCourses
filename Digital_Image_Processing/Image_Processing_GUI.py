import sys
import cv2
import numpy as np
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QLabel
from PyQt5.QtGui import QPixmap, QImage
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.layout = QtWidgets.QGridLayout(self.centralwidget)

        # Image display labels with titles
        self.inputImageTitle = QLabel("Input Image", self.centralwidget)
        self.inputImageTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.inputImageTitle, 0, 0, 1, 2)

        self.inputImageLabel = QLabel(self.centralwidget)
        self.inputImageLabel.setStyleSheet("border: 1px solid black;")
        self.inputImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.inputImageLabel, 1, 0, 1, 2)

        self.outputImageTitle = QLabel("Output Image", self.centralwidget)
        self.outputImageTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.outputImageTitle, 0, 2, 1, 2)

        self.outputImageLabel = QLabel(self.centralwidget)
        self.outputImageLabel.setStyleSheet("border: 1px solid black;")
        self.outputImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.outputImageLabel, 1, 2, 1, 2)

        self.histogramTitle = QLabel("Histogram", self.centralwidget)
        self.histogramTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.histogramTitle, 0, 4, 1, 2)

        self.histogramCanvas = FigureCanvas(Figure(figsize=(3, 3)))  # Scale down
        self.layout.addWidget(self.histogramCanvas, 1, 4, 1, 2)
        self.hist_ax = self.histogramCanvas.figure.subplots()

        # First column buttons (Basic)
        self.basicLabel = QLabel("Basic", self.centralwidget)
        self.layout.addWidget(self.basicLabel, 2, 0)

        self.grayButton = QtWidgets.QPushButton("Gray Image", self.centralwidget)
        self.layout.addWidget(self.grayButton, 3, 0)

        self.flipVerticalButton = QtWidgets.QPushButton("Flip Upside Down", self.centralwidget)
        self.layout.addWidget(self.flipVerticalButton, 4, 0)

        self.flipHorizontalButton = QtWidgets.QPushButton("Flip Side to Side", self.centralwidget)
        self.layout.addWidget(self.flipHorizontalButton, 5, 0)

        # Second column buttons (Spatial Filter)
        self.spatialLabel = QLabel("Spatial Filter", self.centralwidget)
        self.layout.addWidget(self.spatialLabel, 2, 1)

        self.meanFilterButton = QtWidgets.QPushButton("Mean Filter", self.centralwidget)
        self.layout.addWidget(self.meanFilterButton, 3, 1)

        self.gaussianFilterButton = QtWidgets.QPushButton("Gaussian Filter", self.centralwidget)
        self.layout.addWidget(self.gaussianFilterButton, 4, 1)

        self.medianFilterButton = QtWidgets.QPushButton("Median Filter", self.centralwidget)
        self.layout.addWidget(self.medianFilterButton, 5, 1)

        # Third column buttons (Frequency Filter)
        self.frequencyLabel = QLabel("Frequency Filter", self.centralwidget)
        self.layout.addWidget(self.frequencyLabel, 2, 2)

        self.lowpassFilterButton = QtWidgets.QPushButton("Lowpass Filter (Gaussian)", self.centralwidget)
        self.layout.addWidget(self.lowpassFilterButton, 3, 2)

        self.highpassFilterButton = QtWidgets.QPushButton("Highpass Filter (Gaussian)", self.centralwidget)
        self.layout.addWidget(self.highpassFilterButton, 4, 2)

        self.adaptiveMedianFilterButton = QtWidgets.QPushButton("Adaptive Median Filter", self.centralwidget)
        self.layout.addWidget(self.adaptiveMedianFilterButton, 5, 2)

        # Fourth column buttons (Add noise)
        self.noiseLabel = QLabel("Add noise", self.centralwidget)
        self.layout.addWidget(self.noiseLabel, 2, 3)

        self.gaussianNoiseButton = QtWidgets.QPushButton("Gaussian Noise", self.centralwidget)
        self.layout.addWidget(self.gaussianNoiseButton, 3, 3)

        self.pepperSaltNoiseButton = QtWidgets.QPushButton("Pepper & Salt Noise", self.centralwidget)
        self.layout.addWidget(self.pepperSaltNoiseButton, 4, 3)

        self.poissonNoiseButton = QtWidgets.QPushButton("Poisson Noise", self.centralwidget)
        self.layout.addWidget(self.poissonNoiseButton, 5, 3)

        # Fifth column buttons (Morphology)
        self.morphologyLabel = QLabel("Morphology", self.centralwidget)
        self.layout.addWidget(self.morphologyLabel, 2, 4)

        self.erosionButton = QtWidgets.QPushButton("Erosion", self.centralwidget)
        self.layout.addWidget(self.erosionButton, 3, 4)

        self.dilationButton = QtWidgets.QPushButton("Dilation", self.centralwidget)
        self.layout.addWidget(self.dilationButton, 4, 4)

        # Load image button
        self.loadImageButton = QtWidgets.QPushButton("Load Image", self.centralwidget)
        self.layout.addWidget(self.loadImageButton, 6, 0, 1, 2)

        # Save image button
        self.saveImageButton = QtWidgets.QPushButton("Save Image", self.centralwidget)
        self.layout.addWidget(self.saveImageButton, 6, 2, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Image Processing Toolbox"))


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.image = None
        self.output_image = None  # To store the output image

        # Connect buttons to their functions
        self.loadImageButton.clicked.connect(self.loadImage)
        self.saveImageButton.clicked.connect(self.saveImage)
        self.grayButton.clicked.connect(self.convertToGray)
        self.flipVerticalButton.clicked.connect(self.flipUpsideDown)
        self.flipHorizontalButton.clicked.connect(self.flipSideToSide)
        self.meanFilterButton.clicked.connect(self.applyMeanFilter)
        self.gaussianFilterButton.clicked.connect(self.applyGaussianFilter)
        self.medianFilterButton.clicked.connect(self.applyMedianFilter)
        self.lowpassFilterButton.clicked.connect(self.applyLowpassFilter)
        self.highpassFilterButton.clicked.connect(self.applyHighpassFilter)
        self.adaptiveMedianFilterButton.clicked.connect(self.applyAdaptiveMedianFilter)
        self.gaussianNoiseButton.clicked.connect(self.addGaussianNoise)
        self.pepperSaltNoiseButton.clicked.connect(self.addPepperSaltNoise)
        self.poissonNoiseButton.clicked.connect(self.addPoissonNoise)
        self.erosionButton.clicked.connect(self.applyErosion)
        self.dilationButton.clicked.connect(self.applyDilation)

    def loadImage(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Image", "",
                                                  "All Files (*);;JPEG (*.jpg *.jpeg);;PNG (*.png)", options=options)
        if fileName:
            self.image = cv2.imread(fileName)
            self.displayImage(self.image, self.inputImageLabel)
            self.displayHistogram(self.image)

    def saveImage(self):
        if self.output_image is not None:
            options = QFileDialog.Options()
            fileName, _ = QFileDialog.getSaveFileName(self, "Save Image", "",
                                                      "All Files (*);;JPEG (*.jpg *.jpeg);;PNG (*.png)",
                                                      options=options)
            if fileName:
                cv2.imwrite(fileName, self.output_image)

    def displayImage(self, img, label):
        if img is None:
            label.clear()
            return
        # Resize image to fit the label while keeping the aspect ratio
        height, width = img.shape[:2]
        aspect_ratio = width / height
        new_width = label.width()
        new_height = int(new_width / aspect_ratio)
        if new_height > label.height():
            new_height = label.height()
            new_width = int(new_height * aspect_ratio)
        resized = cv2.resize(img, (new_width, new_height), interpolation=cv2.INTER_AREA)
        qformat = QImage.Format_Indexed8 if len(img.shape) == 2 else QImage.Format_RGB888
        img = QImage(resized, resized.shape[1], resized.shape[0], resized.strides[0], qformat)
        img = img.rgbSwapped()
        label.setPixmap(QPixmap.fromImage(img))

    def displayHistogram(self, img):
        if img is None:
            self.hist_ax.clear()
            self.hist_ax.set_title("Histogram")
            self.histogramCanvas.draw()
            return

        self.hist_ax.clear()
        self.hist_ax.set_title("Histogram")
        if len(img.shape) == 2:  # Grayscale image
            self.hist_ax.hist(img.ravel(), bins=256, color='black', alpha=0.5)
        else:  # Color image
            color = ('b', 'g', 'r')
            for i, col in enumerate(color):
                hist = cv2.calcHist([img], [i], None, [256], [0, 256])
                self.hist_ax.plot(hist, color=col)
        self.histogramCanvas.draw()

    def convertToGray(self):
        if self.image is not None:
            self.output_image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def flipUpsideDown(self):
        if self.image is not None:
            self.output_image = cv2.flip(self.image, 0)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def flipSideToSide(self):
        if self.image is not None:
            self.output_image = cv2.flip(self.image, 1)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyMeanFilter(self):
        if self.image is not None:
            kernel_size = 5
            self.output_image = cv2.blur(self.image, (kernel_size, kernel_size))
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyGaussianFilter(self):
        if self.image is not None:
            kernel_size = 5
            self.output_image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyMedianFilter(self):
        if self.image is not None:
            kernel_size = 5
            self.output_image = cv2.medianBlur(self.image, kernel_size)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyLowpassFilter(self):
        if self.image is not None:
            kernel_size = 5
            self.output_image = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), 0)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyHighpassFilter(self):
        if self.image is not None:
            kernel_size = 15
            sigma = 5.0
            # Applying Gaussian Blur
            low_pass = cv2.GaussianBlur(self.image, (kernel_size, kernel_size), sigma)
            # Subtracting the low pass filtered image from the original image
            high_pass = cv2.addWeighted(self.image, 1.5, low_pass, -0.5, 0)
            self.output_image = np.clip(high_pass, 0, 255).astype(np.uint8)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyAdaptiveMedianFilter(self):
        if self.image is not None:
            self.output_image = cv2.medianBlur(self.image, 3)  # Placeholder for adaptive median filter
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def addGaussianNoise(self):
        if self.image is not None:
            row, col, ch = self.image.shape
            mean = 0
            var = 0.01
            sigma = var ** 0.5
            gauss = np.random.normal(mean, sigma, (row, col, ch))
            gauss = gauss.reshape(row, col, ch)
            noisy = self.image + gauss * 255
            self.output_image = np.clip(noisy, 0, 255).astype(np.uint8)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def addPepperSaltNoise(self):
        if self.image is not None:
            row, col, ch = self.image.shape
            s_vs_p = 0.5
            amount = 0.04
            out = np.copy(self.image)
            # Salt mode
            num_salt = np.ceil(amount * self.image.size * s_vs_p)
            coords = [np.random.randint(0, i - 1, int(num_salt)) for i in self.image.shape]
            out[coords[0], coords[1], :] = 1
            # Pepper mode
            num_pepper = np.ceil(amount * self.image.size * (1.0 - s_vs_p))
            coords = [np.random.randint(0, i - 1, int(num_pepper)) for i in self.image.shape]
            out[coords[0], coords[1], :] = 0
            self.output_image = out
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def addPoissonNoise(self):
        if self.image is not None:
            vals = len(np.unique(self.image))
            vals = 2 ** np.ceil(np.log2(vals))
            noisy = np.random.poisson(self.image * vals) / float(vals)
            self.output_image = np.clip(noisy, 0, 255).astype(np.uint8)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyErosion(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.output_image = cv2.erode(self.image, kernel, iterations=1)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)

    def applyDilation(self):
        if self.image is not None:
            kernel = np.ones((5, 5), np.uint8)
            self.output_image = cv2.dilate(self.image, kernel, iterations=1)
            self.displayImage(self.output_image, self.outputImageLabel)
            self.displayHistogram(self.output_image)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
