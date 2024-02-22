import cv2
from functions.read_detect import read_image
from functions.read_detect import detect_edges



def main():
    image_path ='images/photo2.png'
    image = read_image(image_path)
    if image is None:
        print("Error: Image not found.")
        return
    
    edges = detect_edges(image)

    cv2.imshow('Original Image', image)
    cv2.imshow('Edges Detected', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()