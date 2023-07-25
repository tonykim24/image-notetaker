import cv2
import pytesseract
from transfer import transfer

img = cv2.imread('Screen Shot 2023-06-18 at 10.11.05 AM.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
readingText = pytesseract.image_to_string(img)
# print(readingText)
# print(pytesseract.image_to_boxes(img))
with open("note.txt", "w") as file:
    file.write(readingText)

data = pytesseract.image_to_data(
    img, output_type=pytesseract.Output.DICT)
words = data["text"]
sizes = pytesseract.image_to_osd(img).split("\n")[1:]
for word, size in zip(words, sizes):
    print(f"Word: {word}, Font Size: {size}")

hImg, wImg, c = img.shape
boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
    b = b.split(' ')
    # print(b)
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg-y), (w, hImg-h), (0, 0, 225), 3)
cv2.imshow('Result', img)
# transfer()
cv2.waitKey(0)

# might add more
