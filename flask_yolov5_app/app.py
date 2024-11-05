from flask import Flask, render_template, request, redirect, url_for
import cv2
import numpy as np
import os
import torch

app = Flask(__name__)

# Load your YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=r'C:\\ai_projects\\yolo-object-detection-web\\YOLO_training\\yolov5\\runs\\train\\weights\\best.pt')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        if file:
            # Save the uploaded image
            image_path = os.path.join('uploads', file.filename)
            file.save(image_path)

            # Load the image for prediction
            img = cv2.imread(image_path)

            # Perform inference
            results = model(img)

            # Draw results on the image
            results_img = results.render()[0]

            # Save the predicted image
            output_path = os.path.join('static', 'predicted_' + file.filename)
            cv2.imwrite(output_path, results_img)

            return render_template('result.html', original_image=image_path, predicted_image=output_path)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)
