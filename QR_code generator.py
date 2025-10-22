import qrcode
import cv2 as cv
while True:
    website = input('Enter website URL(e to exit):')
    a=int(input('Enter version number (1-40):'))
    b=int(input('Enter box size (e.g., 10):'))
    c=int(input('Enter border size (e.g., 4):'))
    qr=qrcode.QRCode(version=a, box_size=b, border=c)         
#The version parameter is an integer from 1 to 40 that controls the size of the QR code.
#The box_size parameter controls how many pixels each “box” of the QR code is.
#The border parameter controls how many boxes thick the border should be.
    qr.add_data(website)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('website.png')
    img1 = cv.imread('website.png')
    cv.imshow('Qr code',img1)
    cv.waitKey(0)
    if website.lower()=='e':
        break
#if i wanna i should remove the loop if it has issues.