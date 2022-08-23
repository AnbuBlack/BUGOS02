import cv2
dc=cv2.QRCodeDetector()
val, points, straight_qrcode=dc.detectAndDecode(cv2.imread("QRCODE/qrcode001.png"))
print(val)
#print(points)
#print(straight_qrcode)

