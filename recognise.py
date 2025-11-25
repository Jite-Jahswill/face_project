from deepface import DeepFace
import cv2

# Load test image
test_img = "test.jpg"

# Analyze / recognize faces
result = DeepFace.find(img_path=test_img, db_path="known")

print(result)

# Display the result
img = cv2.imread(test_img)
cv2.imshow("Result", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
