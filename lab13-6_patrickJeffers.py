# Patrick Jeffers   Lab 13-6   4/17/2022
# Based on chapter 13 exercise 6 in the book. This program uses a GUI with 
# check buttons to allow a user to select from a list of automotive services.
# The program then calculates and displays the total of the services selected.

# Import the tkinter module, and messagebox.
import tkinter
import tkinter.messagebox

class JoesAutoGUI:
    def __init__(self):
        # Create the window.
        self.main_window = tkinter.Tk()
        
        # Title for window.
        self.main_window.title("Joe's Automotive")        
        
        # Create 2 frames for check buttons and program buttons.
        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)
        
        # Create 7 IntVar objects for check buttons.
        self.cb_var1 = tkinter.IntVar()
        self.cb_var2 = tkinter.IntVar()
        self.cb_var3 = tkinter.IntVar()
        self.cb_var4 = tkinter.IntVar()
        self.cb_var5 = tkinter.IntVar()
        self.cb_var6 = tkinter.IntVar()
        self.cb_var7 = tkinter.IntVar()
        
        # Set IntVar objects.
        self.cb_var1.set(0)
        self.cb_var2.set(0)
        self.cb_var3.set(0)
        self.cb_var4.set(0)
        self.cb_var5.set(0)
        self.cb_var6.set(0)
        self.cb_var7.set(0)
        
        # Create checkbutton widgets.
        self.cb1 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Oil Change',
                                       variable = self.cb_var1)
        self.cb2 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Lube Job',
                                       variable = self.cb_var2)
        self.cb3 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Radiator Flush',
                                       variable = self.cb_var3)
        self.cb4 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Transmission Flush',
                                       variable = self.cb_var4)
        self.cb5 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Inspection',
                                       variable = self.cb_var5)
        self.cb6 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Muffler Replacement',
                                       variable = self.cb_var6)
        self.cb7 = tkinter.Checkbutton(self.top_frame,
                                       text = 'Tire Rotation',
                                       variable = self.cb_var7)
        
        # Pack Checkbuttons.
        self.cb1.pack(padx=(5,5), pady=(5,5))
        self.cb2.pack(padx=(5,5), pady=(5,5))
        self.cb3.pack(padx=(5,5), pady=(5,5))
        self.cb4.pack(padx=(5,5), pady=(5,5))
        self.cb5.pack(padx=(5,5), pady=(5,5))
        self.cb6.pack(padx=(5,5), pady=(5,5))
        self.cb7.pack(padx=(5,5), pady=(5,5))
        
        # Create submit and quit buttons.
        self.submit_button = tkinter.Button(self.bottom_frame,
                                            text = 'Submit',
                                            command = self.show_total)
        self.quit_button = tkinter.Button(self.bottom_frame,
                                          text = 'Quit',
                                          command = self.main_window.destroy)
        
        # Pack Buttons.
        self.submit_button.pack(side = 'left')
        self.quit_button.pack(side = 'left')
        
        # Pack Frames.
        self.top_frame.pack()
        self.bottom_frame.pack(padx=(10,10), pady=(10,10))
        
        # Enter tkinter main loop.
        tkinter.mainloop()
        
    # Callback function for Submit button.
    def show_total(self):
        # Create variable to hold total.
        total = 0
        
        # Determine with checkbuttons are selected and ad value to total if
        # selected.
        if self.cb_var1.get() == 1:
            total += 30
        if self.cb_var2.get() == 1:
            total += 20
        if self.cb_var3.get() == 1:
            total += 40
        if self.cb_var4.get() == 1:
            total += 100
        if self.cb_var5.get() == 1:
            total += 35
        if self.cb_var6.get() == 1:
            total += 200
        if self.cb_var7.get() == 1:
            total += 20
            
        # Create output message.
        self.output_message = 'Total Charges: $'
        tkinter.messagebox.showinfo('Total Cost',
                                    self.output_message + str(total))
        
# Create an instance of the above class / run program.
if __name__ == '__main__':
    joes_Auto = JoesAutoGUI()