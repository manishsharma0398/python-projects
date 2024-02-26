"""image resizer app"""

import cv2

src = cv2.imread("./image_resizer/my_image.jpg", cv2.IMREAD_UNCHANGED)


scale_percent = 10

width = int(src.shape[1] * scale_percent / 100)
height = int(src.shape[0] * scale_percent / 100)

output = cv2.resize(src, (width, height))

cv2.imwrite("./image_resizer/resized_image.jpg", output)
cv2.waitKey(0)
