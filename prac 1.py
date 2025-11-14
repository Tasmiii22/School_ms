import cv2
import numpy as np
image = cv2.imread(r"https://images.contentstack.io/v3/assets/bltcedd8dbd5891265b/blt134818d279038650/6668df6434f6fb5cd48aac34/beautiful-flowers-rose.jpeg?q=70&width=3840&auto=webp")

if image is None:
    print("Error : If image is not found")
    exit()

beta = 70
bright_image = cv2.convertScaleAbs(image, alpha=1, beta=beta)
combined_image = np.hstack((image, bright_image))

cv2.imshow("Original and Brightness image", combined_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
