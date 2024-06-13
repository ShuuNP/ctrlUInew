import tkinter
import tkinter.messagebox
import customtkinter
import os

customtkinter.set_appearance_mode("Light")
customtkinter.set_default_color_theme("green")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # resolution
        self.title("CTRL ALT DELETE")
        self.geometry(f"{900}x{480}")

        self.grid_columnconfigure(1, weight=2)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # sidebar buttons
        self.sidebar_frame = customtkinter.CTkFrame(self, width=150, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(4, weight=1)
        
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame,
                                                 text="CTRL ALT DELETE",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=10, pady=(10, 10))
        
        # analyze audio
        self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, 
                                                        text="Analyze Audio",
                                                        command=self.sidebar_button_event)
        self.sidebar_button_1.grid(row=1, column=0, padx=10, pady=10)
        self.sidebar_button_1.configure(state="disabled")
        
        #analyze audio options
        
         #   #tabview
        self.audio_tabview = customtkinter.CTkTabview(self, width=250)
        self.audio_tabview.grid(row=0,column=1,padx=(20,20),
                                pady=(20,20), sticky="nsew")
        self.audio_tabview.add("Files")
        self.audio_tabview.add("Spectogram")
        self.audio_tabview.add("Result")
        
        self.string_input_button = customtkinter.CTkButton(self, text="Open CTkInputDialog",
                                                           command=self.about_button_event)
        self.string_input_button.grid(row=2, column=1, padx=0, pady=(20, 20))
        ###tabbview 1
        self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
        self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(0, 0), sticky="nsew")
        self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
        self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
        self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
        self.progressbar_1.grid(row=1, column=0, padx=(20, 20), pady=(10, 10), sticky="ew")
        
        ##pag working na yung analyze audio gawa lang na method na mag start tong progress bar.
       # self.progressbar_1.configure(mode="indeterminnate")
        #self.progressbar_1.start()
        
        
        #files tabview
        self.audio_tabview.tab("Files").grid_columnconfigure(0,weight=1)
        self.audio_tabview.tab("Spectogram").grid_columnconfigure(0,weight=1)
        
        #About
        self.about_frame = customtkinter.CTkButton(self.sidebar_frame,
                                                   text="About",
                                                   command=self.about_button_event)
        self.about_frame.grid(row=3, column=0, padx=10, pady=10)
        # documentation
        self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, 
                                                        text="Documentation",
                                                        command=self.show_documentation)
        self.sidebar_button_2.grid(row=2, column=0, padx=10, pady=10)
        
        # documentation frame (initially hidden)
        self.documentation_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.documentation_frame.grid(row=0, column=1, rowspan=4, sticky="nsew", padx=10, pady=10)
        self.documentation_frame.grid_remove()
        
        # text widget for displaying documentation content
        self.documentation_text = tkinter.Text(self.documentation_frame, wrap="word")
        self.documentation_text.pack(expand=True, fill="both", padx=10, pady=10)
        self.documentation_text.config(state="disabled") 
        self.documentation_text.tag_configure("font", font=("arial", 12))      
    
    def sidebar_button_event(self):
        self.hide_all_frames()
        print("sidebar_button click")
        self.sidebar_button_1.configure(state="disabled")
        self.sidebar_button_2.configure(state="normal")
        
    def show_documentation(self):
        # Get the current directory and construct the file path
        current_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(current_dir, "Documentation.txt")
        
        # Read content from the text file
        try:
            with open(file_path, "r") as file:
                content = file.read()
                
            # Update text widget with content
            self.documentation_text.config(state="normal")
            self.documentation_text.delete("1.0", tkinter.END)
            self.documentation_text.insert(tkinter.END, content)
            self.documentation_text.config(state="disabled")
        except FileNotFoundError:
            tkinter.messagebox.showerror("Error", "Documentation file not found")
        
        # Show the documentation frame
        self.documentation_frame.grid()
        self.sidebar_button_1.configure(state="normal")
        self.sidebar_button_2.configure(state="disabled")
        
    def about_button_event(self):
        print("test")

    def hide_all_frames(self):
        self.documentation_frame.grid_remove()
        # Add here any other frames that should be hidden

# run
app = App()
app.mainloop()
