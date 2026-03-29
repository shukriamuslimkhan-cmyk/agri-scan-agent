from ultralytics import YOLO
import os

def load_model():
    # Point to your trained weights
    model_path = os.path.join("assets", "best.pt")
    return YOLO(model_path)