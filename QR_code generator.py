import qrcode
import cv2 as cv
def qrgen():
    a=input('do you want a custom size QR?(say yes or no):')
    if a.lower()=='yes':
            b=int(input('Enter version number (1-40):'))
            c=int(input('Enter box size (1-50):'))
            d=int(input('Enter border size (0-20):'))
            qr=qrcode.QRCode(version=b, box_size=c, border=d)
    elif a.lower()=='no':
        qr=qrcode.QRCode(version=1, box_size=10, border=4)
    else:
         print('say yes or no')
    qr.add_data(website)
    qr.make(fit=True)
    img = qr.make_image(fill_color='black', back_color='white')
    img.save('website.png')
    img1 = cv.imread('website.png')
    cv.imshow('Qr code',img1)
    cv.waitKey(0)
while True:
    website = input('Enter website URL(e to exit):')
    if website.lower()=='e':
        break
    else:
        qrgen()
#The version parameter is an integer from 1 to 40 that controls the size of the QR code.
#The box_size parameter controls how many pixels each “box” of the QR code is.
#The border parameter controls how many boxes thick the border should be.