import cv2

def read_image(image_path):
    """Reads an image from a file."""
    image = cv2.imread(image_path)
    return image

def detect_edges(image):
    """Detects edges in an image using the Canny edge detector."""
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray_image, 100, 200)
    return edges
