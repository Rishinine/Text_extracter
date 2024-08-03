import os
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QDesktopWidget
from PyQt5.QtCore import Qt, QRect
from PyQt5.QtGui import QPainter, QPen, QColor
from PIL import ImageGrab

class TransparentWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        
        screen = QDesktopWidget().screenGeometry()
        self.setGeometry(0, 0, screen.width(), screen.height())
        self.setWindowTitle("Draw Rectangle with Mouse")

        self.drawing = False
        self.start_x = 0
        self.start_y = 0
        self.end_x = 0
        self.end_y = 0

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = True
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseMoveEvent(self, event):
        if self.drawing:
            self.end_x = event.x()
            self.end_y = event.y()
            self.update()

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.drawing = False
            self.end_x = event.x()
            self.end_y = event.y()
            self.update()
            self.capture_area()
            self.close()  # Close the application after taking a screenshot

    def paintEvent(self, event):
        if self.drawing:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)
            pen = QPen(QColor(255, 0, 0), 2, Qt.SolidLine)
            painter.setPen(pen)
            rect = QRect(self.start_x, self.start_y, self.end_x - self.start_x, self.end_y - self.start_y)
            painter.drawRect(rect)

    def capture_area(self):
    # Ensure coordinates are positive and within screen bounds
        left = min(self.start_x, self.end_x)
        top = min(self.start_y, self.end_y)
        right = max(self.start_x, self.end_x)
        bottom = max(self.start_y, self.end_y)

        # Capture the screen area
        screenshot = ImageGrab.grab(bbox=(left, top+30, right, bottom+30))  # Adjusting the bbox to include the right and bottom edges correctly
        screenshot.save("sample.png")
        print(f"Captured area: ({left}, {top}) to ({right}, {bottom})")


if __name__ == "__main__":
    os.environ['QT_QPA_PLATFORM'] = 'wayland'  # Ensure the platform is set for X11 on Linux
    
    app = QApplication(sys.argv)
    window = TransparentWindow()
    window.show()
    sys.exit(app.exec_())
