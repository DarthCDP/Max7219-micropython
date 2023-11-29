from LEDMatrix import ledmatrix


#DIN (Here Pin 3) = Data In (mosi pin) // CS (Here Pin 5) = Chip Select // CLK (Here Pin 2) = Clock - MC = Module Count (Number of LEDMatrixes in chain)
Matrix = ledmatrix(3, 5, 2, 4)	#Initialize the class

PixelOutput = [1] * 256	#Initialize an array for your pixels (64 pixels per 8x8 display * 4 Displays in a chain = 256)

PixelOutput[54] = 0	#Setting one pixel to 0 (Off) to show how it works
                
Matrix.pixels = PixelOutput	#Map the pixels to the buffer inside the LEDMatrix class
        
Matrix.Show()				#Update the display