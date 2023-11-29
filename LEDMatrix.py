import framebuf
from machine import Pin, SPI
from time import sleep_ms

class ledmatrix:
    #DIN = Data In (mosi pin) - CS = Chip Select - CLK = Clock - MC = Module Count (Number of LEDMatrixes in chain)
    def __init__(self, DIN, CS, CLK, MC):
        self.spi = SPI(0, baudrate=10000000, polarity=1, phase=0, sck=Pin(CLK), mosi=Pin(DIN))
        self.cs = Pin(CS, Pin.OUT)
        self.mc = MC
        self.buffer = bytearray(8 * self.mc)
        self.pixels = [0] * (64 * self.mc)
        self.height = (8 * self.mc)
        
        
        #Setup LEDMatrix
        self.cs.value(1)
        sleep_ms(50)
        self.cs.value(0)
        for I in range(self.mc):
            self.Send(12, 0)	#Shutdown
        self.cs.value(1)
        sleep_ms(1)
        self.cs.value(0)
        for I in range(self.mc):
            self.Send(15, 0)	#DisplayTest
        self.cs.value(1)
        sleep_ms(1)
        self.cs.value(0)
        for I in range(self.mc):
            self.Send(11, 7)	#ScanLimit
        self.cs.value(1)
        sleep_ms(1)
        self.cs.value(0)
        for I in range(self.mc):
            self.Send(9, 0)	#DecodeMode
        self.cs.value(1)
        sleep_ms(1)
        self.cs.value(0)
        for I in range(self.mc):
            self.Send(12, 1)	#Shutdown
        self.cs.value(1)
        sleep_ms(1)
        self.Show()
        
    def BitsToByte(self, B0, B1, B2, B3, B4, B5, B6, B7):
        return (B7 + (B6 * 2) + (B5 * 4) + (B4 * 8) + (B3 * 16) + (B2 * 32) + (B1 * 64) + (B0 * 128))
    
    def MapPixelsToBuffer(self):
        for i in range(len(self.buffer)):    
            self.buffer[i] = self.BitsToByte(self.pixels[i * 8], self.pixels[(i * 8) + 1], self.pixels[(i * 8) + 2], self.pixels[(i * 8) + 3], self.pixels[(i * 8) + 4], self.pixels[(i * 8) + 5], self.pixels[(i * 8) + 6], self.pixels[(i * 8) + 7])

    def Show(self):
        self.MapPixelsToBuffer()
        for y in range(8):
            self.cs.value(0)
            for m in range(self.mc):
                self.Send(1 + y, self.buffer[(y * 4) + m])
            self.cs.value(1)
    
    def Send(self, Command, Data):
        Message = bytearray([Command, Data])
        self.spi.write(Message)




