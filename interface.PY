import customtkinter as ctk
import tkinter as tk
from tkinter import TclError
from PIL import Image, ImageTk, ImageFont, ImageDraw
from datetime import datetime
import calendar
import pywinstyles
from tkinter import font
from datetime import datetime
from tkinter import messagebox

class TasklyApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Taskly")
        self.geometry("331x717")
        self.resizable(False, False)

        self.splash_page = ctk.CTkFrame(self, fg_color="#F3F4F6")
        self.name_page = ctk.CTkFrame(self, fg_color="#F3F4F6")
        self.menu_page = ctk.CTkFrame(self, fg_color="#F3F4F6")
        self.notes_preview_page = NotesPage(self)
        self.favorites_notes_page = FavoritesNotesPage(self)
        self.new_note_page = NewNotePage(self)
        self.popup_page = PopUpButtons(self)
        self.pagecolor_page = PageColor (self)
        self.todo_preview_page = ToDoPage(self)
        self.favorites_todo_page = FavoritesTodoPage(self)
        self.new_todo_page = NewToDoPage(self)
        self.sched_days_page = SchedulePage(self)
        self.sched_popup_page = SchedPopUpButtons(self)
        self.event_page = EventsPage(self)
        self.sunday_page = SundayPage(self)
        self.monday_page = MondayPage(self)
        self.tuesday_page = TuesdayPage(self)
        self.wednesday_page = WednesdayPage(self)
        self.thursday_page = ThursdayPage(self)
        self.friday_page = FridayPage(self)
        self.saturday_page = SaturdayPage(self)

        for frame in (self.splash_page, self.name_page, self.menu_page, self.notes_preview_page, self.favorites_notes_page,
                      self.new_note_page, self.todo_preview_page, self.favorites_todo_page, self.new_todo_page, 
                      self.sched_days_page, self.event_page, self.sunday_page, self.monday_page, 
                      self.tuesday_page, self.wednesday_page, self.thursday_page, self.friday_page, 
                      self.saturday_page):
            frame.place(relwidth=1, relheight=1)

        self.show_page(self.splash_page)

        self.bg_image = None
        self.logo_image = None
        self.text_image_tk = None
        self.get_started_image_tk = None
        self.profile_image_tk = None
        self.save_button_image_tk = None

    def show_page(self, frame):
        frame.tkraise()

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def splash_page_ui(self):
        self.canvas = ctk.CTkCanvas(self.splash_page, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/background.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.logo_image = Image.open("images/taskly_logo.png").resize((400, 400))
        self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
        self.canvas.create_image(207, 300, image=self.logo_image_tk, anchor=ctk.CENTER)

        custom_font = ImageFont.truetype("fonts/bubbleboddy_neue/bubbleboddyNeue-regular.ttf", 21)
        text_image = Image.new("RGBA", (414, 50), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)

        draw.text((207, 30), "Turning goals into progress.", font=custom_font, fill="#e17a8f", anchor="mm")
        text_image_tk = ImageTk.PhotoImage(text_image)
        self.canvas.create_image(207, 365, image=text_image_tk, anchor=ctk.CENTER)
        self.text_image_tk = text_image_tk

        self.get_started_image = Image.open("images/getstartedbutton.png").resize((240, 60))
        self.get_started_image_tk = ImageTk.PhotoImage(self.get_started_image)
        self.get_started_button = self.canvas.create_image(207, 600, image=self.get_started_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.get_started_button)

        self.canvas.tag_bind(self.get_started_button, "<Button-1>", lambda event: self.open_name_page())

    def open_name_page(self):
        self.show_page(self.name_page)
        self.name_page_ui()

    def name_page_ui(self):
        self.canvas = ctk.CTkCanvas(self.name_page, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/background.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.profile_image = Image.open("images/user_icon.png").resize((250, 250))
        self.profile_image_tk = ImageTk.PhotoImage(self.profile_image)
        self.canvas.create_image(207, 275, image=self.profile_image_tk, anchor=ctk.CENTER)

        self.entername_bg_image = Image.open("images/entername_field.png").resize((270, 50))
        self.entername_bg_image_tk = ImageTk.PhotoImage(self.entername_bg_image)
        self.canvas.create_image(207, 465, image=self.entername_bg_image_tk, anchor=ctk.CENTER)

        self.username_entry = ctk.CTkEntry(self.name_page, font=("Poppins Bold", 14), justify="center", width=195, height=27, border_width=0, fg_color="#fef8d8", text_color="#917660", placeholder_text="Enter your name", placeholder_text_color="#c4a484")
        self.username_entry.place(relx=0.5, rely=0.52, anchor="center")

        self.save_button_image = Image.open("images/savebutton.png").resize((165, 55))
        self.save_button_image_tk = ImageTk.PhotoImage(self.save_button_image)
        self.save_button = self.canvas.create_image(207, 570, image=self.save_button_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.save_button)

        self.canvas.tag_bind(self.save_button, "<Button-1>", self.save_name)

    def save_name(self, event=None):
        name = self.username_entry.get().strip()
        if name:
            print(f"User's name: {name}")
            self.show_page(self.menu_page)
            self.menu_page_ui()
        else:
            messagebox.showwarning("Input Error", "Please enter your name.")

    def menu_page_ui(self):
        self.canvas = ctk.CTkCanvas(self.menu_page, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/menu_page_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.logo_image = Image.open("images/taskly_logo.png").resize((135, 135))
        self.logo_image_tk = ImageTk.PhotoImage(self.logo_image)
        self.canvas.create_image(85, 45, image=self.logo_image_tk, anchor=ctk.CENTER)

        custom_font = ImageFont.truetype("fonts/bubbleboddy_neue/bubbleboddyNeue-regular.ttf", 25)
        name = self.username_entry.get().strip()
        welcome_text = f"Hi, {name}!"

        text_image = Image.new("RGBA", (414, 50), (255, 255, 255, 0))
        draw = ImageDraw.Draw(text_image)
        draw.text((207, 30), welcome_text, font=custom_font, fill="#e17a8f", anchor="mm")

        text_image_tk = ImageTk.PhotoImage(text_image)
        self.canvas.create_image(290, 42, image=text_image_tk, anchor=ctk.CENTER)
        self.text_image_tk = text_image_tk

        self.notes_image = Image.open("images/notes.png").resize((350, 150))
        self.notes_image_tk = ImageTk.PhotoImage(self.notes_image)
        self.notes_button = self.canvas.create_image(207, 195, image=self.notes_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.notes_button, "<Button-1>", lambda e: self.open_notes_page())
        self.set_button_cursor(self.notes_button)
                               
        self.todo_image = Image.open("images/To do list.png").resize((350, 150))
        self.todo_image_tk = ImageTk.PhotoImage(self.todo_image)
        self.todo_button = self.canvas.create_image(207, 370, image=self.todo_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.todo_button, "<Button-1>", lambda e: self.open_todo_preview_page())
        self.set_button_cursor(self.todo_button)

        self.sched_image = Image.open("images/schedule.png").resize((350, 150))
        self.sched_image_tk = ImageTk.PhotoImage(self.sched_image)
        self.sched_button = self.canvas.create_image(207, 545, image=self.sched_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.sched_button, "<Button-1>", lambda e: self.open_sched_days_page())
        self.set_button_cursor(self.sched_button)

        self.event_image = Image.open("images/Event Tracker.png").resize((350, 150))
        self.event_image_tk = ImageTk.PhotoImage(self.event_image)
        self.event_button = self.canvas.create_image(207, 720, image=self.event_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.event_button, "<Button-1>", lambda e: self.open_event_page())
        self.set_button_cursor(self.event_button)

    def open_notes_page(self):
        self.show_page(self.notes_preview_page)

    def open_todo_preview_page(self):
        self.show_page(self.todo_preview_page)

    def open_sched_days_page(self):
        self.show_page(self.sched_days_page)

    def open_event_page(self):
        self.show_page(self.event_page)  

class NotesPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/notes_preview_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.menu_page))
        self.set_button_cursor(self.back_button)

        self.star_button_image = Image.open("images/star_button.png").resize((45, 53))
        self.star_image_tk = ImageTk.PhotoImage(self.star_button_image)
        self.star_button = self.canvas.create_image(360, 113, image=self.star_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.star_button, "<Button-1>", lambda e: self.parent.show_page(self.parent.favorites_notes_page))
        self.set_button_cursor(self.star_button)

        self.write_button_img_tk = ImageTk.PhotoImage(Image.open("images/writebutton.png").resize((75, 75)))
        self.write_button = self.canvas.create_image(370, 850, image=self.write_button_img_tk, anchor=ctk.SE, tag="write_button")
        self.canvas.tag_bind("write_button", "<Button-1>", lambda e: self.add_note_placeholder())
        self.set_button_cursor(self.write_button)

        self.no_notes_text = self.canvas.create_text(
            207, 450,
            text="No notes yet. \nTap icon to create one.",
            fill="#917660",
            font=("Poppins", 14, "bold"),
            anchor=ctk.CENTER,
            justify="center"
        )

        self.search_entry = ctk.CTkEntry(
            self,
            font=("Poppins Bold", 13),
            justify="left",
            width=140,
            height=27,
            border_width=0,
            fg_color="#fef8d8",
            bg_color="#fef8d8",
            text_color="#917660",
            placeholder_text="Enter your search",
            placeholder_text_color="#c4a484",
        )
        self.search_entry.place(relx=0.385, rely=0.129, anchor="center")

        self.search_button_image = Image.open("images/search_button.png").resize((40, 45))
        self.search_button_image_tk = ImageTk.PhotoImage(self.search_button_image)
        self.search_button = self.canvas.create_image(
            60, 113, image=self.search_button_image_tk, anchor="center"
        )

        self.canvas.tag_bind(self.search_button, "<Button-1>", self.perform_search)

        self.note_positions = [
            (115, 250), (300, 250),
            (115, 460), (300, 460),
            (115, 670), (300, 670)
        ]
        self.current_note_index = 0
        self.notes = []

    def perform_search(self, event=None):
        query = self.search_entry.get().strip()
        print(f"User searched: {query}")

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def add_note_placeholder(self):
        if self.current_note_index < len(self.note_positions):
            position = self.note_positions[self.current_note_index]
            notes_preview_image = Image.open("images/notes_preview_placeholder.png").resize((170, 170))
            notes_preview_image_tk = ImageTk.PhotoImage(notes_preview_image)
            note_placeholder = self.canvas.create_image(position, image=notes_preview_image_tk, anchor=ctk.CENTER)
            self.notes.append((note_placeholder, notes_preview_image_tk))
            self.canvas.tag_bind(note_placeholder, "<Button-1>", lambda e: self.open_new_note_page())
            self.set_button_cursor(note_placeholder)
            self.current_note_index += 1

        if self.no_notes_text:
            self.canvas.delete(self.no_notes_text)
            self.no_notes_text = None

    def open_new_note_page(self):
        self.parent.show_page(self.parent.new_note_page)

class FavoritesNotesPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/faves_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.notes_preview_page))
        self.set_button_cursor(self.back_button)

        self.no_favorites_text = self.canvas.create_text(
            207, 450,
            text="No favorites found. \nAdd some by tapping the star icon!",
            fill="#917660",
            font=("Poppins", 14, "bold"),
            anchor=ctk.CENTER,
            justify="center"
        )

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

class NewNotePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/newnote_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.color_bg_image = Image.open("images/yellow_bg.png").resize((380, 836))
        self.color_bg_image_tk = ImageTk.PhotoImage(self.color_bg_image)
        self.canvas.create_image(17, 150, image=self.color_bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.notes_preview_page))
        self.set_button_cursor(self.back_button)

        self.three_dots_image = Image.open("images/3dots.png").resize((45, 15))
        self.three_dots_image_tk = ImageTk.PhotoImage(self.three_dots_image)
        self.three_dots_button = self.canvas.create_image(355, 54, image=self.three_dots_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.three_dots_button)

        self.undo_button_img_tk = ImageTk.PhotoImage(Image.open("images/undo_button.png").resize((27, 23)))
        self.undo_button = self.canvas.create_image(325, 125, image=self.undo_button_img_tk, anchor=ctk.CENTER, tag="undo_button")
        self.canvas.tag_bind("undo_button", "<Button-1>", lambda e: self.undo_action())
        self.set_button_cursor(self.undo_button)

        self.redo_button_img_tk = ImageTk.PhotoImage(Image.open("images/redo_button.png").resize((27, 23)))
        self.redo_button = self.canvas.create_image(365, 125, image=self.redo_button_img_tk, anchor=ctk.CENTER, tag="redo_button")
        self.canvas.tag_bind("redo_button", "<Button-1>", lambda e: self.redo_action())
        self.set_button_cursor(self.redo_button)

        self.title_entry = ctk.CTkEntry(
            self,
            font=("Poppins Bold", 17),
            justify="left",
            width=237,
            height=40,
            border_width=0,
            fg_color="#ffffff",
            bg_color="#ffffff",
            text_color="#917660",
            placeholder_text="Enter your title",
            placeholder_text_color="#c4a484",
        )
        self.title_entry.place(x=20, y=67)
        self.title_entry.bind("<KeyRelease>", self.limit_title)

        self.date_time_label = ctk.CTkLabel(
            self,
            text=self.get_current_datetime(),
            font=("Poppins", 11),
            fg_color="#ffffff",
            bg_color="#ffffff",
            text_color="#c4a484",
            anchor="w"
        )
        self.date_time_label.place(x=28, y=92)

        self.text_entry = ctk.CTkTextbox(
            self,
            font=("Poppins", 13),
            width=290,
            height=550,
            border_width=0,
            fg_color="#ffffff",
            bg_color="#ffffff",
            text_color="#c4a484",
        )
        self.text_entry.place(x=21, y=122)

        self.placeholder_text = "Enter your notes here..."
        self.text_entry.insert("1.0", self.placeholder_text)
        self.text_entry.bind("<FocusIn>", self.remove_placeholder)
        self.text_entry.bind("<FocusOut>", self.add_placeholder)

        self.popup_buttons = PopUpButtons(self)
        self.popup_buttons.place_forget()

        self.pagecolor_page = PageColor(self)
        self.pagecolor_page.place_forget()
        self.canvas.tag_bind(self.three_dots_button, "<Button-1>", self.toggle_popup)

        pywinstyles.set_opacity(self.title_entry, color="#ffffff")
        pywinstyles.set_opacity(self.text_entry, color="#ffffff")
        pywinstyles.set_opacity(self.date_time_label, color="#ffffff")

    def undo_action(self):
        print("Undo button pressed.")

    def redo_action(self):
        print("Redo button pressed.")

    def get_current_datetime(self):
        now = datetime.now()
        return now.strftime("%B %d, %Y | %I:%M %p")

    def update_datetime(self):
        self.date_time_label.configure(text=self.get_current_datetime())

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def limit_title(self, event):
        title = self.title_entry.get()
        if len(title) > 25:
            self.title_entry.delete(25, "end")

    def remove_placeholder(self, event):
        current_text = self.text_entry.get("1.0", "end-1c").strip()
        if current_text == self.placeholder_text:
            self.text_entry.delete("1.0", "end")
            self.text_entry.configure(text_color="#917660")

    def add_placeholder(self, event):
        current_text = self.text_entry.get("1.0", "end-1c").strip()
        if not current_text:
            self.text_entry.insert("1.0", self.placeholder_text)
            self.text_entry.configure(text_color="#c4a484")

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def toggle_popup(self, event):
        if self.popup_buttons.winfo_ismapped():
            self.popup_buttons.place_forget()
        else:
            self.popup_buttons.place(x=170, y=55)
        self.set_button_cursor(self.three_dots_button)

    def update_background(self, color_bg_image_path):
        self.color_bg_image = Image.open(color_bg_image_path).resize((414, 896))
        self.color_bg_image_tk = ImageTk.PhotoImage(self.color_bg_image)
        self.canvas.create_image(0, 0, image=self.color_bg_image_tk, anchor=ctk.NW)

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

class PopUpButtons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configure(fg_color="#ffe3e3", bg_color="#ffe3e3")

        self.save_image = ImageTk.PhotoImage(Image.open("images/popup_save.png").resize((180, 45)))
        self.save_button = ctk.CTkLabel(self, image=self.save_image, text="")
        self.save_button.pack(pady=(10, 10), padx=5)
        self.save_button.bind("<Button-1>", self.on_save_button_click)
        self.save_button.bind("<Enter>", lambda e: self.change_cursor("hand2"))
        self.save_button.bind("<Leave>", lambda e: self.change_cursor(""))

        self.star_image = ImageTk.PhotoImage(Image.open("images/popup_star.png").resize((180, 45)))
        self.star_button = ctk.CTkLabel(self, image=self.star_image, text="")
        self.star_button.pack(pady=5, padx=10)
        self.star_button.bind("<Button-1>", self.on_star_button_click)
        self.star_button.bind("<Enter>", lambda e: self.change_cursor("hand2"))
        self.star_button.bind("<Leave>", lambda e: self.change_cursor(""))

        self.delete_image = ImageTk.PhotoImage(Image.open("images/popup_delete.png").resize((180, 45)))
        self.delete_button = ctk.CTkLabel(self, image=self.delete_image, text="")
        self.delete_button.pack(pady=5, padx=10)
        self.delete_button.bind("<Button-1>", self.on_delete_button_click)

        self.page_color_image = ImageTk.PhotoImage(Image.open("images/popup_pagecolor.png").resize((180, 45)))
        self.page_color_button = ctk.CTkLabel(self, image=self.page_color_image, text="")
        self.page_color_button.pack(pady=(5, 10), padx=10)
        self.page_color_button.bind("<Button-1>", self.on_page_color_button_click)
        self.page_color_button.bind("<Enter>", lambda e: self.change_cursor("hand2"))
        self.page_color_button.bind("<Leave>", lambda e: self.change_cursor(""))

    def change_cursor(self, cursor_type):
        self.configure(cursor=cursor_type)

    def on_save_button_click(self, event):
        print("Save button clicked")

    def on_star_button_click(self, event):
        print("Star button clicked")

    def on_page_color_button_click(self, event):
        self.place_forget()  
        self.parent.pagecolor_page.toggle_visibility()

    def on_delete_button_click(self, event):
        self.hide_menu()
        self.show_popup(event)

    def show_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        popup_x, popup_y = 208, 440
        self.popup = self.parent.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor="center")

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 42))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.parent.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor="center")
        self.parent.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 42))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.parent.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor="center")
        self.parent.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

    def hide_popup(self, event):
        self.parent.canvas.delete(self.popup)
        self.parent.canvas.delete(self.popup_cancel)
        self.parent.canvas.delete(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked")
        self.hide_popup(event)

    def hide_menu(self):
        self.pack_forget()

    def show_menu(self):
        self.pack()

class PageColor(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        self.configure(fg_color="#ffffff", bg_color="#ffffff")

        self.pagecolor_bg = ImageTk.PhotoImage(Image.open("images/pagecolor_bg.png").resize((370, 120))) 
        self.pagecolor_bg_label = ctk.CTkLabel(self, image=self.pagecolor_bg, text="")
        self.pagecolor_bg_label.grid(row=1, column=0, columnspan=6, pady=(5, 2))

        colors = [
            ("Pink", "pink_color.png", "#f4b8b7", "pink_bg.png"),
            ("Blue", "blue_color.png", "#b8cfe1", "blue_bg.png"),
            ("Green", "green_color.png", "#cfe4e5", "green_bg.png"),
            ("Yellow", "yellow_color.png", "#fef8d8", "yellow_bg.png")
        ]
        self.current_color = "#fef8d8"

        for idx, (text, image, color, color_bg_image) in enumerate(colors):
            img = ImageTk.PhotoImage(Image.open(f"images/{image}").resize((50, 45)))
            button = ctk.CTkLabel(self, image=img, text="")
            button.image = img
            button.grid(row=1, column=idx, padx=10, pady=(25, 5))
            button.bind("<Button-1>", lambda e, color=color, color_bg_image=color_bg_image: self.change_color(color, color_bg_image))
            button.bind("<Enter>", lambda e: self.change_cursor("hand2"))
            button.bind("<Leave>", lambda e: self.change_cursor(""))

        self.save_color_bg = ImageTk.PhotoImage(Image.open("images/save_color.png").resize((50, 57)))
        self.save_color_button = ctk.CTkLabel(self, image=self.save_color_bg, text="")
        self.save_color_button.grid(row=1, column=4, columnspan=4, pady=(45, 20), padx=(0, 10)) 
        self.save_color_button.bind("<Button-1>", lambda e: self.save_color())
        self.save_color_button.bind("<Enter>", lambda e: self.change_cursor("hand2"))
        self.save_color_button.bind("<Leave>", lambda e: self.change_cursor(""))

        self.popup_x = None
        self.popup_y = None

    def change_cursor(self, cursor_type):
        self.configure(cursor=cursor_type)

    def change_color(self, color, color_bg_image_path):
        self.current_color = color

        if hasattr(self.parent, "update_taskframes_color"):
            self.parent.update_taskframes_color(self.current_color)

        full_path = f"images/{color_bg_image_path}"
        try:
            self.color_bg_image = Image.open(full_path).resize((380, 836))
            self.color_bg_image_tk = ImageTk.PhotoImage(self.color_bg_image)
            self.parent.canvas.create_image(17, 150, image=self.color_bg_image_tk, anchor=ctk.NW)
        except FileNotFoundError:
            print(f"Error: The image '{full_path}' was not found.")

    def save_color(self):
        print("Save color")  
        self.place_forget()

    def toggle_visibility(self):
        if self.winfo_ismapped():
            self.place_forget()  
        else:
            if self.popup_x is None or self.popup_y is None:
                parent_width = self.parent.winfo_width()
                parent_height = self.parent.winfo_height()
                popup_width = self.winfo_reqwidth()
                popup_height = self.winfo_reqheight()

                self.popup_x = (parent_width - popup_width) // 2.5  
                self.popup_y = parent_height - popup_height - 180  

            self.place(x=self.popup_x, y=self.popup_y)

class ToDoPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/todo_preview_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.menu_page))
        self.set_button_cursor(self.back_button)

        self.star_button_image = Image.open("images/star_button.png").resize((45, 53))
        self.star_image_tk = ImageTk.PhotoImage(self.star_button_image)
        self.star_button = self.canvas.create_image(360, 113, image=self.star_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.star_button, "<Button-1>", lambda e: self.parent.show_page(self.parent.favorites_todo_page))
        self.set_button_cursor(self.star_button)

        self.write_button_img_tk = ImageTk.PhotoImage(Image.open("images/writebutton.png").resize((75, 75)))
        self.write_button = self.canvas.create_image(370, 850, image=self.write_button_img_tk, anchor=ctk.SE, tag="write_button")
        self.canvas.tag_bind("write_button", "<Button-1>", lambda e: self.add_todo_placeholder())
        self.set_button_cursor(self.write_button)

        self.no_todo_text = self.canvas.create_text(
            207, 450,
            text="No tasks yet.\nTap icon to create one.",
            fill="#917660",
            font=("Poppins", 14, "bold"),
            anchor=ctk.CENTER,
            justify="center"
        )

        self.search_entry = ctk.CTkEntry(
            self,
            font=("Poppins Bold", 13),
            justify="left",
            width=140,
            height=27,
            border_width=0,
            fg_color="#fef8d8",
            bg_color="#fef8d8",
            text_color="#917660",
            placeholder_text="Enter your search",
            placeholder_text_color="#c4a484",
        )
        self.search_entry.place(relx=0.385, rely=0.129, anchor="center")

        self.search_button_image = Image.open("images/search_button.png").resize((40, 45))
        self.search_button_image_tk = ImageTk.PhotoImage(self.search_button_image)
        self.search_button = self.canvas.create_image(
            60, 113, image=self.search_button_image_tk, anchor="center"
        )

        self.canvas.tag_bind(self.search_button, "<Button-1>", self.perform_search)

        self.note_positions = [
            (115, 250), (300, 250),
            (115, 460), (300, 460),
            (115, 670), (300, 670)
        ]
        self.current_note_index = 0
        self.todo = []

    def perform_search(self, event=None):
        query = self.search_entry.get().strip()
        print(f"User searched: {query}")

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def add_todo_placeholder(self):
        if self.current_note_index < len(self.note_positions):
            position = self.note_positions[self.current_note_index]
            todo_preview_image = Image.open("images/todolist_preview_placeholder.png").resize((170, 170))
            todo_preview_image_tk = ImageTk.PhotoImage(todo_preview_image)
            note_placeholder = self.canvas.create_image(position, image=todo_preview_image_tk, anchor=ctk.CENTER)
            self.todo.append((note_placeholder, todo_preview_image_tk))
            self.canvas.tag_bind(note_placeholder, "<Button-1>", lambda e: self.open_new_todo_page())
            self.set_button_cursor(note_placeholder)
            self.current_note_index += 1

        if self.no_todo_text:
            self.canvas.delete(self.no_todo_text)
            self.no_todo_text = None

    def open_new_todo_page(self):
        self.parent.show_page(self.parent.new_todo_page)

class FavoritesTodoPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/faves_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.todo_preview_page))
        self.set_button_cursor(self.back_button)

        self.no_favorites_text = self.canvas.create_text(
            207, 450,
            text="No favorites found. \nAdd some by tapping the star icon!",
            fill="#917660",
            font=("Poppins", 14, "bold"),
            anchor=ctk.CENTER,
            justify="center"
        )

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

class NewToDoPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.parent.tasks = []

        self.bg_image = Image.open("images/newtodo_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.color_bg_image = Image.open("images/yellow_bg.png").resize((380, 836))
        self.color_bg_image_tk = ImageTk.PhotoImage(self.color_bg_image)
        self.canvas.create_image(17, 150, image=self.color_bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.todo_preview_page))
        self.set_button_cursor(self.back_button)

        self.add_task_button_img_tk = ImageTk.PhotoImage(Image.open("images/addtask_button.png").resize((160, 55)))
        self.add_task_button = self.canvas.create_image(207, 830, image=self.add_task_button_img_tk, anchor=ctk.CENTER, tag="add_task_button")
        self.canvas.tag_bind("add_task_button", "<Button-1>", self.show_task_popup)
        self.set_button_cursor("add_task_button")

        self.three_dots_image = Image.open("images/3dots.png").resize((45, 15))
        self.three_dots_image_tk = ImageTk.PhotoImage(self.three_dots_image)
        self.three_dots_button = self.canvas.create_image(355, 54, image=self.three_dots_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.three_dots_button)

        self.undo_button_img_tk = ImageTk.PhotoImage(Image.open("images/undo_button.png").resize((27, 23)))
        self.undo_button = self.canvas.create_image(325, 125, image=self.undo_button_img_tk, anchor=ctk.CENTER, tag="undo_button")
        self.canvas.tag_bind("undo_button", "<Button-1>", lambda e: self.undo_action())
        self.set_button_cursor(self.undo_button)

        self.redo_button_img_tk = ImageTk.PhotoImage(Image.open("images/redo_button.png").resize((27, 23)))
        self.redo_button = self.canvas.create_image(365, 125, image=self.redo_button_img_tk, anchor=ctk.CENTER, tag="redo_button")
        self.canvas.tag_bind("redo_button", "<Button-1>", lambda e: self.redo_action())
        self.set_button_cursor(self.redo_button)

        self.title_entry = ctk.CTkEntry(
            self,
            font=("Poppins Bold", 17),
            justify="left",
            width=237,
            height=40,
            border_width=0,
            fg_color="#ffffff",
            bg_color="#ffffff",
            text_color="#917660",
            placeholder_text="Enter your title",
            placeholder_text_color="#c4a484",
        )
        self.title_entry.place(x=20, y=67)
        self.title_entry.bind("<KeyRelease>", self.limit_title)

        self.date_time_label = ctk.CTkLabel(
            self,
            text=self.get_current_datetime(),
            font=("Poppins", 11),
            fg_color="#ffffff",
            bg_color="#ffffff",
            text_color="#c4a484",
            anchor="w"
        )
        self.date_time_label.place(x=28, y=92)

        self.popup_buttons = PopUpButtons(self)
        self.popup_buttons.place_forget()

        self.pagecolor_page = PageColor(self)
        self.pagecolor_page.place_forget()
        self.canvas.tag_bind(self.three_dots_button, "<Button-1>", self.toggle_popup)

        pywinstyles.set_opacity(self.title_entry, color="#ffffff")
        pywinstyles.set_opacity(self.date_time_label, color="#ffffff")

        self.current_color = "#fef8d8"

    def undo_action(self):
        print("Undo button pressed.")

    def redo_action(self):
        print("Redo button pressed.")

    def get_current_datetime(self):
        now = datetime.now()
        return now.strftime("%B %d, %Y | %I:%M %p")

    def update_datetime(self):
        self.date_time_label.configure(text=self.get_current_datetime())

    def limit_title(self, event):
        title = self.title_entry.get()
        if len(title) > 25:
            self.title_entry.delete(25, "end")

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def toggle_popup(self, event):
        if self.popup_buttons.winfo_ismapped():
            self.popup_buttons.place_forget()
        else:
            self.popup_buttons.place(x=170, y=55)
        self.set_button_cursor(self.three_dots_button)

    def update_background(self, color_bg_image_path):
        self.color_bg_image = Image.open(color_bg_image_path).resize((414, 896))
        self.color_bg_image_tk = ImageTk.PhotoImage(self.color_bg_image)
        self.canvas.create_image(0, 0, image=self.color_bg_image_tk, anchor=ctk.NW)  

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def show_task_popup(self, event):
        self.task_popup = ctk.CTkFrame(self, width=300, height=200, bg_color="#ffffff", fg_color="#ffffff")
        self.task_popup.place(x=17, y=430)

        popup_image = Image.open("images/popup_taskdesc.png").convert("RGBA")
        
        resized_popup_image = popup_image.resize((350, 260), Image.Resampling.LANCZOS)
        self.popup_bg_image_tk = ImageTk.PhotoImage(resized_popup_image)
        
        self.popup_bg_label = ctk.CTkLabel(self.task_popup, image=self.popup_bg_image_tk, text="", fg_color="transparent", bg_color="transparent")
        self.popup_bg_label.place(relx=0.48, rely=0.58, anchor=ctk.CENTER)

        self.task_description_entry = ctk.CTkEntry(self.task_popup, font=("Poppins Bold", 13), justify="center", width=215, height=85, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="Enter task description", placeholder_text_color="#c4a484")
        self.task_description_entry.place(relx=0.482, rely=0.528, anchor="center")

        self.save_button_image = ImageTk.PhotoImage(Image.open("images/popup_savee.png").resize((140, 45)))
        self.save_button = ctk.CTkButton(self.task_popup, image=self.save_button_image, text="", fg_color="#ffffff", bg_color="#ffffff", hover_color="#ffffff", command=self.save_task)
        self.save_button.place(relx=0.70, rely=0.925, anchor="center")

        self.cancel_button_image = ImageTk.PhotoImage(Image.open("images/popup_cancel.png").resize((140, 45)))
        self.cancel_button = ctk.CTkButton(self.task_popup, image=self.cancel_button_image, text="", fg_color="#ffffff", bg_color="#ffffff", hover_color="#ffffff", command=self.cancel_task)
        self.cancel_button.place(relx=0.25, rely=0.925, anchor="center")

    def update_taskframes_color(self, color):
        self.current_color = color

        for task in self.parent.tasks:
            if len(task) == 3:
                task_frame, check_var, task_checkbutton = task
                task_frame.configure(bg_color=self.current_color, fg_color=self.current_color)
                task_checkbutton.configure(
                    hover_color=self.current_color, 
                    border_color="#f48098",
                    checkmark_color="#ffffff"
                )
            elif len(task) == 2:
                task_frame, check_var = task
                task_frame.configure(bg_color=self.current_color, fg_color=self.current_color)

        print(f"Task colors updated to {self.current_color}")

    def save_task(self):
        def toggle_strikethrough(*args):
            if check_var.get() == "1":  # Checked state
                task_label.configure(font=("Poppins Bold", 13, "overstrike"))
            else:  # Unchecked state
                task_label.configure(font=("Poppins Bold", 13))  # Normal font

        task_description = self.task_description_entry.get()

        if task_description.strip():
            task_y_position = 150 + (len(self.parent.tasks) * 40)
            task_frame = ctk.CTkFrame(
                self.canvas,
                width=350,
                height=35,
                bg_color="#fef8d8",
                fg_color="#fef8d8"
            )
            task_frame.place(x=30, y=task_y_position)

            check_var = ctk.StringVar()
            check_var.trace_add("write", toggle_strikethrough)

            task_checkbutton = ctk.CTkCheckBox(
                task_frame,
                text="",
                variable=check_var,
                width=20,
                height=20,
                fg_color="#f48098",
                hover_color="#f48098",
                border_color="#f48098",
            )
            task_checkbutton.grid(row=0, column=0, padx=5)

            task_label = ctk.CTkLabel(
                task_frame,
                text=task_description,
                font=("Poppins Bold", 13),
                text_color="#917660",
                fg_color="transparent",
                bg_color="transparent"
            )
            task_label.grid(row=0, column=1, padx=10)

            self.parent.tasks.append((task_frame, check_var, task_checkbutton))

            print(f"Task Added: {task_description}")
            self.task_popup.after(100, self.task_popup.destroy)

    def cancel_task(self):
        print("Task creation cancelled.")
        self.task_popup.after(100, self.task_popup.destroy)
        
class SchedulePage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/sched_days_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.menu_page))
        self.set_button_cursor(self.back_button)

        self.day_images = []
        days = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        y_position = 150

        for day in days:
            day_image_tk = ImageTk.PhotoImage(Image.open(f"images/sched_{day}.png").resize((350, 95)))
            self.day_images.append(day_image_tk)
            self.canvas.create_image(207, y_position, image=day_image_tk, anchor="center", tag=day)
            self.canvas.tag_bind(day, "<Button-1>", lambda e, day=day: self.show_day_page(day))
            y_position += 105

    def show_day_page(self, day):
        page_class = {"sunday": self.parent.sunday_page,
            "monday": self.parent.monday_page,
            "tuesday": self.parent.tuesday_page,
            "wednesday": self.parent.wednesday_page,
            "thursday": self.parent.thursday_page,
            "friday": self.parent.friday_page,
            "saturday": self.parent.saturday_page
        }
        self.parent.show_page(page_class[day])

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

class DayPage(ctk.CTkFrame):
    def __init__(self, parent, day):
        super().__init__(parent)
        self.parent = parent
        self.day = day
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open(f"images/{day}_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.sched_days_page))
        self.set_button_cursor("back_button")

        self.add_sched_button_img_tk = ImageTk.PhotoImage(Image.open("images/add_sched.png").resize((75, 75)))
        self.add_sched_button = self.canvas.create_image(207, 820, image=self.add_sched_button_img_tk, anchor=ctk.CENTER, tag="add_sched_button")
        self.canvas.tag_bind("add_sched_button", "<Button-1>", self.toggle_popup)
        self.set_button_cursor("add_sched_button")

        self.popup_buttons = SchedPopUpButtons(self)
        self.popup_buttons.place_forget()

    def set_button_cursor(self, tag):
        self.canvas.tag_bind(tag, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(tag, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def toggle_popup(self, event):
        if hasattr(self, "popup_buttons") and str(self.popup_buttons):
            try:
                if self.popup_buttons.winfo_ismapped():
                    self.popup_buttons.place_forget()
                else:
                    self.popup_buttons.place(x=30, y=265)
            except TclError:
                self.popup_buttons = SchedPopUpButtons(self)
                self.popup_buttons.place(x=30, y=265)
        else:
            self.popup_buttons = SchedPopUpButtons(self)
            self.popup_buttons.place(x=30, y=265)

class SchedPopUpButtons(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.configure(fg_color="#ffffff", bg_color="#ffffff", width=300, height=400)
        
        self.popup_addsched_image = ImageTk.PhotoImage(Image.open("images/popup_addsched.png").resize((315, 355)))
        self.popup_addsched_image = ctk.CTkLabel(self, image=self.popup_addsched_image, text="")
        self.popup_addsched_image.pack(pady=(1, 1))

        self.event_title_entry = ctk.CTkEntry(self, font=("Poppins Bold", 13), justify="center", width=190, height=20, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="Enter event title", placeholder_text_color="#c4a484")
        self.event_title_entry.place(relx=0.5, rely=0.141, anchor="center")

        self.event_start_time_entry = ctk.CTkEntry(self, font=("Poppins Bold", 13), justify="center", width=70, height=20, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="00:00", placeholder_text_color="#c4a484")
        self.event_start_time_entry.place(relx=0.43, rely=0.36, anchor="e") 

        self.event_end_time_entry = ctk.CTkEntry(self, font=("Poppins Bold", 13), justify= "center", width=70, height=20, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="00:00", placeholder_text_color="#c4a484")
        self.event_end_time_entry.place(relx=0.70, rely=0.398, anchor="s")

        self.event_description_entry = ctk.CTkEntry(self, font=("Poppins Bold", 13), justify="center", width=195, height=75, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="Enter event description", placeholder_text_color="#c4a484")
        self.event_description_entry.place(relx=0.50, rely=0.665, anchor="center")

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=(5, 10))

        self.save_button_image = ImageTk.PhotoImage(Image.open("images/popup_savee.png").resize((125, 45)))
        self.save_button = ctk.CTkButton(self.buttons_frame, image=self.save_button_image, text="", fg_color=self.cget("bg_color"), hover_color=self.cget("bg_color"), command=self.handle_save)
        self.save_button.grid(row=0, column=1, padx=0)

        self.cancel_button_image = ImageTk.PhotoImage(Image.open("images/popup_cancel.png").resize((125, 45)))
        self.cancel_button = ctk.CTkButton(self.buttons_frame, image=self.cancel_button_image, text="", fg_color=self.cget("bg_color"), hover_color=self.cget("bg_color"), command=self.handle_cancel)
        self.cancel_button.grid(row=0, column=0, padx=0)

    def handle_save(self):
        title = self.event_title_entry.get()
        start_time = self.event_start_time_entry.get()
        end_time = self.event_end_time_entry.get()
        description = self.event_description_entry.get()

        print(f"Event Title: {title}")
        print(f"Start Time: {start_time}")
        print(f"End Time: {end_time}")
        print(f"Event Description: {description}")

        self.destroy()

    def handle_cancel(self):
        print("Cancel button pressed.")

        self.destroy()

class SundayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "sunday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class MondayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "monday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class TuesdayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "tuesday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class WednesdayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "wednesday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class ThursdayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "thursday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class FridayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "friday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class SaturdayPage(DayPage):
    def __init__(self, parent):
        super().__init__(parent, "saturday")

        self.placeholder_image = Image.open("images/sched_placeholder.png").resize((340, 100))
        self.placeholder_image_tk = ImageTk.PhotoImage(self.placeholder_image)
        self.placeholder = self.canvas.create_image(208, 155, image=self.placeholder_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.placeholder)

        self.image_label = ctk.CTkLabel(self, text="", fg_color="transparent", bg_color="transparent")
        self.image_label.place_forget()

        self.canvas.tag_bind(self.placeholder, '<Button-1>', self.show_sched_popup)

    def show_sched_popup(self, event):
        popup_image = Image.open("images/popup_sched_options.png").convert("RGBA")
        popup_size = (250, 160) 
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)
        
        popup_x, popup_y = 208, 440 
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        edit_image = Image.open("images/popup_sched_edit.png").resize((185, 55))
        self.edit_image_tk = ImageTk.PhotoImage(edit_image)
        edit_x, edit_y = popup_x, popup_y - 33
        self.popup_edit = self.canvas.create_image(edit_x, edit_y, image=self.edit_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_edit, '<Button-1>', self.edit_action)

        delete_image = Image.open("images/popup_sched_delete.png").resize((185, 55))
        self.delete_image_tk = ImageTk.PhotoImage(delete_image)
        delete_x, delete_y = popup_x, popup_y + 33
        self.popup_delete = self.canvas.create_image(delete_x, delete_y, image=self.delete_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_delete, '<Button-1>', self.show_delete_popup)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_edit)
        self.canvas.tag_raise(self.popup_delete)

    def hide_popup(self, event):
        if hasattr(self, 'popup'):
            self.canvas.delete(self.popup)
        if hasattr(self, 'popup_edit'):
            self.canvas.delete(self.popup_edit)
        if hasattr(self, 'popup_delete'):
            self.canvas.delete(self.popup_delete)
        if hasattr(self, 'popup_cancel'):
            self.canvas.delete(self.popup_cancel)
        if hasattr(self, 'confirm_button'):
            self.canvas.delete(self.confirm_button)

    def show_delete_popup(self, event):
        popup_image = Image.open("images/confirmation_box.png").convert("RGBA")
        popup_size = (300, 165)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        cancel_image = Image.open("images/popup_cancel.png").resize((118, 43))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 40
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        confirm_image = Image.open("images/confirm_button.png").resize((118, 43))
        self.confirm_image_tk = ImageTk.PhotoImage(confirm_image)
        confirm_x, confirm_y = popup_x + 68, popup_y + 40
        self.confirm_button = self.canvas.create_image(confirm_x, confirm_y, image=self.confirm_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.confirm_button, '<Button-1>', self.confirm_action)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.confirm_button)

    def confirm_action(self, event):
        print("Confirm button clicked!")
        self.hide_popup(event)

    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

class EventsPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.canvas = ctk.CTkCanvas(self, width=414, height=896)
        self.canvas.pack()

        self.bg_image = Image.open("images/event_bg.png").resize((414, 896))
        self.bg_image_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_image_tk, anchor=ctk.NW)

        self.back_button_img_tk = ImageTk.PhotoImage(Image.open("images/backbutton.png").resize((45, 45)))
        self.back_button = self.canvas.create_image(35, 31, image=self.back_button_img_tk, anchor=ctk.NW, tag="back_button")
        self.canvas.tag_bind("back_button", "<Button-1>", lambda e: self.parent.show_page(self.parent.menu_page))

        self.buttons_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.buttons_frame.pack(pady=(5, 10))
        
        self.plus_image = Image.open("images/plus_button.png").resize((42, 42))
        self.plus_image_tk = ImageTk.PhotoImage(self.plus_image)
        self.plus_button = self.canvas.create_image(348, 487, image=self.plus_image_tk, anchor=ctk.CENTER)
        self.set_button_cursor(self.plus_button)
        self.canvas.tag_bind(self.plus_button, '<Button-1>', self.show_event_popup)

        self.day_images = []
        days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                "28", "29", "30", "31"]

        x_start = 207
        y_start = 217
        x_gap = 49
        y_gap = 45

        first_row_days = 4
        other_row_days = 7
        for idx, day in enumerate(days):
            if idx < first_row_days:
                x_position = x_start + idx * x_gap
                y_position = y_start
            else:
                row = (idx - first_row_days) // other_row_days + 1
                col = (idx - first_row_days) % other_row_days
                x_position = x_start - 3 * x_gap + col * x_gap
                y_position = y_start + row * y_gap

            day_image_tk = ImageTk.PhotoImage(Image.open(f"images/{day}button.png").resize((48, 40)))
            self.day_images.append(day_image_tk)
            self.canvas.create_image(x_position, y_position, image=day_image_tk, anchor=ctk.CENTER, tag=f"day_{day}")
            self.canvas.tag_bind(f"day_{day}", "<Button-1>", lambda e, day=day: self.show_day_page(day))

        self.current_text_label = None

        self.show_day_page(29)

    def show_event_popup(self, event):
        if self.current_text_label:
            self.current_text_label.place_forget()

        popup_image = Image.open("images/event_popupholder.png").convert("RGBA")
        popup_size = (330, 350)
        resized_popup = popup_image.resize(popup_size, Image.Resampling.LANCZOS)
        self.popup_image_tk = ImageTk.PhotoImage(resized_popup)

        popup_x, popup_y = 208, 440
        self.popup = self.canvas.create_image(popup_x, popup_y, image=self.popup_image_tk, anchor=ctk.CENTER)

        self.event_title_entry = ctk.CTkEntry(self, font=("Poppins Bold", 13), justify="center", width=190, height=20, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="Enter event title", placeholder_text_color="#c4a484")
        self.event_title_entry.place(relx=0.5, rely=0.375, anchor="center")

        self.event_description_entry = ctk.CTkEntry(self, font=("Poppins Bold", 13), justify="center", width=195, height=75, border_width=0, fg_color="#ffffff", bg_color="#ffffff", text_color="#917660", placeholder_text="Enter event description", placeholder_text_color="#c4a484")
        self.event_description_entry.place(relx=0.50, rely=0.525, anchor="center")

        cancel_image = Image.open("images/popup_cancel.png").resize((125, 50))
        self.cancel_image_tk = ImageTk.PhotoImage(cancel_image)
        cancel_x, cancel_y = popup_x - 68, popup_y + 135
        self.popup_cancel = self.canvas.create_image(cancel_x, cancel_y, image=self.cancel_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.popup_cancel, '<Button-1>', self.hide_popup)

        save_image = Image.open("images/popup_savee.png").resize((125, 50))
        self.save_image_tk = ImageTk.PhotoImage(save_image)
        save_x, save_y = popup_x + 68, popup_y + 135
        self.save_button = self.canvas.create_image(save_x, save_y, image=self.save_image_tk, anchor=ctk.CENTER)
        self.canvas.tag_bind(self.save_button, '<Button-1>', self.handle_save)

        self.canvas.tag_raise(self.popup)
        self.canvas.tag_raise(self.popup_cancel)
        self.canvas.tag_raise(self.save_button)

    def hide_popup(self, event):
        self.canvas.delete(self.popup)
        self.canvas.delete(self.popup_cancel)
        self.canvas.delete(self.save_button)

        self.event_title_entry.destroy()
        self.event_description_entry.destroy()

        if self.current_text_label:
            self.current_text_label.place(relx=0.125, rely=0.545, anchor="w")


    def handle_save(self, event=None):
        title = self.event_title_entry.get()
        description = self.event_description_entry.get()

        print(f"Event Title: {title}")
        print(f"Event Description: {description}")

        self.hide_popup(event)
        
    def edit_action(self, event):
        print("Edit button clicked!")
        self.hide_popup(event)

        self.placeholder_image_tk = ImageTk.PhotoImage(Image.open("images/event_placeholder.png").resize((330, 75)))
        
        self.day_images = []
        days = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14",
                "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27",
                "28", "29", "30", "31"]

        x_start = 207  
        y_start = 217  
        x_gap = 49     
        y_gap = 45      
        
        first_row_days = 4  
        other_row_days = 7 
        for idx, day in enumerate(days):
            if idx < first_row_days:
                x_position = x_start + idx * x_gap
                y_position = y_start
            else:
                row = (idx - first_row_days) // other_row_days + 1  
                col = (idx - first_row_days) % other_row_days
                x_position = x_start - 3 * x_gap + col * x_gap  
                y_position = y_start + row * y_gap
            
            day_image_tk = ImageTk.PhotoImage(Image.open(f"images/{day}button.png").resize((48, 40)))
            self.day_images.append(day_image_tk)
            self.canvas.create_image(x_position, y_position, image=day_image_tk, anchor=ctk.CENTER, tag=f"day_{day}")
            self.canvas.tag_bind(f"day_{day}", "<Button-1>", lambda e, day=day: self.show_day_page(day))
                    
        self.current_text_label = None

        self.show_day_page(29)

    def show_day_page(self, day):
        weekday = self.get_weekday_for_january(int(day))
        text = f"Jan {day}, {weekday}"

        if self.current_text_label:
            self.current_text_label.destroy()

        background = ctk.CTkFrame(self.canvas, width=414, height=50, fg_color="#f4b8b7", corner_radius=8)
        background.place(relx=0.125, rely=0.545, anchor="w")

        text_label = ctk.CTkLabel(background, text=text, font=("Poppins Bold", 20), text_color="#917660", bg_color="transparent")
        text_label.pack(expand=True)

        self.current_text_label = background

    def get_weekday_for_january(self, day):
        weekday_index = (day + 1) % 7
        return calendar.day_name[weekday_index]

    def set_button_cursor(self, button):
        self.canvas.tag_bind(button, "<Enter>", lambda e: self.canvas.config(cursor="hand2"))
        self.canvas.tag_bind(button, "<Leave>", lambda e: self.canvas.config(cursor=""))

    def show_placeholder(self, event):
        self.canvas.create_image(207, 555, image=self.placeholder_image_tk, anchor="center", tag="placeholder")

    def hide_placeholder(self):
        self.canvas.delete("placeholder")

if __name__ == "__main__":
    app = TasklyApp()
    app.splash_page_ui()
    app.mainloop()