# barcode-interpretation
Barcode interpretation is the process of extracting information from barcodes, which are optical codes consisting of parallel lines of varying widths and spacing.Barcode interpretation is an important application of computer vision and image processing, and requires specialized knowledge and expertise in these areas.


## Libraries:
  Pillow 
  OpenCV
  Pyzbar
## Decoding Function:
   ### static image
   ### webcam
      The decoding function is where the main actions will take place, and it involves three primary tasks.
      The first task is to detect and decode the barcode/QR code that will be presented to the camera.
      The second task is to append the stored information as text to the recognized barcode/QR code.
      Lastly, the decoded information will be exported as a text document
      
## Main Function:
    In this step, we will write the main function, where the application is prompt to work.
    The main function will turn on the video camera of the computer, and the then call the decoding function
  
