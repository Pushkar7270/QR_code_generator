# QR_code_generator

A simple program that takes input for a URL and design from the user and then generates a QR code.

The defined function is made in such a way that if the user does not want to write a custom design number, it'll automatically use the default values given to the sizes and borders.

## Development Process & Problem-Solving

In the initial code, I did not use a function. Then I thought, "What if the user does not know what numbers to put or what if they try to put random numbers and the QR looks ugly?" So, I gave default values in the function itself.

The code also had logic errors in the loop after my creation of the function. It turned out I put the `qr` variable inside the function but then did the rest of the code outside it, which made the code not understand what the `qr` variable stood for. To fix this, the entire QR generation is now done through calling the function, and only the exit loop is outside of it.

## Libraries Used

* **qrcode**: This generates the QR code after the user input.
* **OpenCV (cv2)**: This creates the GUI window in which the QR code is visible.

## Future of the Program

* I plan to modify the program so that the output is completely GUI-based.
* This was just a practice code. Its actual implementation will be in my website that I will create for my resume or to share socials through the generated QR.