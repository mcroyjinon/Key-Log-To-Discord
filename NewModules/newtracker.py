import customtkinter as CTk


class TrackerApp(CTk.CTk):

    def __init__(self,app) -> None:

        if self.activate(app): return

        if app.settings_file['settings']['tracker'] == 'false': return

        super().__init__()
        self.attributes("-topmost", True)  # Always Ontop
        self.title('')
        self.wm_attributes("-toolwindow", "true")  # Toolwindow Mode
        self.protocol('WM_DELETE_WINDOW',lambda: None)
        self.resizable(False,False)

        self.string_var = CTk.StringVar(self,'')

        self.textbox = CTk.CTkLabel(self,textvariable=self.string_var)
        self.textbox.pack()

        app.tracker = self

        self.mainloop()

    def activate(self, app) -> bool:
        app.settings_file.read('Saves/settings.ini')
        app.start_key = app.settings_file['activation']['start']
        app.stop_key = app.settings_file['activation']['stop']

        if app.activated:
            app.activate_button.configure(text='Activate')
        else:
            app.activate_button.configure(text="Activated")        
        
        app.activated = not app.activated

        if app.tracker: 
            app.tracker.destroy()
            app.tracker = None
            return True
        return False