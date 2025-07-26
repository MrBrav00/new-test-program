import cv2
import numpy as np
import onnxruntime

def build_model(is_cuda: bool, model_path: str):
    providers = ['CPUExecutionProvider']
    if is_cuda:
        providers = ['CUDAExecutionProvider', 'CPUExecutionProvider']
    return onnxruntime.InferenceSession(model_path, providers=providers)

def results_objects(img, net, model_name):
    input_name = net.get_inputs()[0].name
    output_name = net.get_outputs()[0].name

    # Resize for detection
    img_resized = cv2.resize(img, (640, 640))
    blob = cv2.dnn.blobFromImage(img_resized, 1/255.0, (640, 640), swapRB=True, crop=False)
    net_input = {input_name: blob}
    detections = net.run([output_name], net_input)[0]

    boxes = []
    class_ids = []
    confidences = []

    rows = detections.shape[1]
    img_height, img_width = img.shape[:2]

    for i in range(rows):
        row = detections[0][i]
        confidence = row[4]

        if confidence > 0.4:
            class_scores = row[5:]
            class_id = np.argmax(class_scores)
            if class_scores[class_id] > 0.4:
                cx, cy, w, h = row[0:4]
                x = int((cx - w / 2) * img_width)
                y = int((cy - h / 2) * img_height)
                width = int(w * img_width)
                height = int(h * img_height)

                boxes.append([x, y, width, height])
                confidences.append(float(class_scores[class_id]))
                class_ids.append(class_id)

    return class_ids, confidences, boxes, get_classes(model_name)

def get_center(boxes):
    centers = []
    for box in boxes:
        x, y, w, h = box
        center_x = x + w // 2
        center_y = y + h // 2
        centers.append((center_x, center_y))
    return centers

def get_classes(model_name):
    # Based on model filename, define the right class
    if "stone" in model_name.lower():
        return ["Rough Stone"]
    elif "wood" in model_name.lower():
        return ["Rough Wood"]
    else:
        return ["Unknown"]

def results_frame(img, class_ids, confidences, boxes, class_list):
    for (class_id, confidence, box) in zip(class_ids, confidences, boxes):
        (x, y, w, h) = box
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 2)
        label = f"{class_list[class_id]}: {round(confidence, 2)}"
        cv2.putText(img, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    return img
