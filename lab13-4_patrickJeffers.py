# Patrick Jeffers   Lab 13-4   4/14/2022
# Based on chapter 13 exercise 4 in the book.  This program utilizes a GUI to 
# allow the user to convert temperatures from Celsius to Fahrenheit.

# Import the tkinter module.
import tkinter

class CelsiusFahrenheitConversionGUI:
    def __init__(self):
        
        # Create the window.
        self.main_window = tkinter.Tk()
        
        # Title for window.
        self.main_window.title('Celsius to Fahrenheit Converter')
        
        # Create 3 frames to structure the window with content.
        self.top_frame = tkinter.Frame()
        self.middle_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        # Create content/widgets for top frame.  Prompt and user entry.
        self.prompt_label = tkinter.Label(self.top_frame,
                                          text = 'Enter a temperature in '\
                                                 'Celsius:')
        self.celsius_entry = tkinter.Entry(self.top_frame, width = 10)
        
        # Pack and format the top frame widgets.
        self.prompt_label.pack(side = 'left', ipadx = 10, ipady = 5)
        self.celsius_entry.pack(side = 'left')
        
        # Create widget to label output in middle frame.
        self.converted_label = tkinter.Label(self.middle_frame,
                                             text = 'Converted to Fahrenheit:')
        
        # Create StringVar object to associate with an output label.
        self.value = tkinter.StringVar()
        
        # Create the output label including above StringVar.
        self.out_label = tkinter.Label(self.middle_frame,
                                       textvariable = self.value)
        
        # Pack and format the middle frame widgets.
        self.converted_label.pack(side = 'left', ipadx = 10, ipady = 5)
        self.out_label.pack(side = 'left')
        
        # Create conversion and quit buttons.
        self.calc_button = tkinter.Button(self.bottom_frame,
                                          text = 'Convert',
                                          command = self.convert)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        
        # Pack buttons.
        self.calc_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        # Pack the 3 frames.
        self.top_frame.pack()
        self.middle_frame.pack()
        self.bottom_frame.pack()
        
        # Enter tkinter main loop.
        tkinter.mainloop()
        
    # Convert method / callback function for the Convert button.
    def convert(self):
        celsius = float(self.celsius_entry.get())             # Get users input.
        
        fahrenheit = ((9/5) * celsius) + 32       # Process and calculate for F.
        
        self.value.set(fahrenheit)    # Set the calculated temp and store in the
                                      # StringVar object.
    
# Create an instance of the above class / run program.
if __name__ == '__main__':
    CelsiusFahrenheitConversion = CelsiusFahrenheitConversionGUI()