#start debugging to run


import customtkinter as customtkinter
import calendar
from tkinter import messagebox

class CalendarApp:
    def __init__(app, window):
        app.window = window
        app.window.title("Custom Calendar")
        
        app.current_month = 1
        app.current_year = 2024

        # Set the window to fullscreen on startup
        app.window.attributes("-fullscreen", True)  # Set fullscreen mode
        app.window.bind("<F11>", app.toggle_fullscreen)  # Toggle fullscreen on F11
        app.window.bind("<Escape>", app.exit_fullscreen)  # Exit fullscreen on Escape key

        # Set the background color of the window
        app.window.configure(bg="green")

        # Create and pack widgets
        app.create_widgets()
        app.display_month(app.current_month, app.current_year)

    def create_widgets(app):
        # Frame for menu bar at the top (this will hold the buttons and placeholder text)
        menu_bar_frame = customtkinter.CTkFrame(app.window, fg_color="#257534")  # Set frame color to green
        menu_bar_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Buttons for the menu bar (set background to dark grey)
        menu_button_1 = customtkinter.CTkButton(menu_bar_frame, text="Action 1", command=lambda: app.on_menu_button_click(1), fg_color="darkgrey")
        menu_button_1.pack(side="left", padx=5)
        
        menu_button_2 = customtkinter.CTkButton(menu_bar_frame, text="Action 2", command=lambda: app.on_menu_button_click(2), fg_color="darkgrey")
        menu_button_2.pack(side="left", padx=5)

        menu_button_3 = customtkinter.CTkButton(menu_bar_frame, text="Action 3", command=lambda: app.on_menu_button_click(3), fg_color="darkgrey")
        menu_button_3.pack(side="left", padx=5)

        # Close Window Button (positioned on the right side of the menu bar)
        close_button = customtkinter.CTkButton(menu_bar_frame, text="Close Window", command=app.close_window, fg_color="darkgrey")
        close_button.pack(side="right", padx=5)

        # Placeholder label in the same menu bar frame (set text color to white for contrast)
        placeholder_label = customtkinter.CTkLabel(menu_bar_frame, text="Placeholder", font=("Helvetica", 16), text_color="white")
        placeholder_label.pack(side="top", padx=10, pady=10)  # Ensure the label is centered

        # Main frame for the calendar (below the menu and placeholder)
        main_frame = customtkinter.CTkFrame(app.window, fg_color="green")  # Set frame color to green
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Left frame for month buttons (stacked vertically)
        left_frame = customtkinter.CTkFrame(main_frame, fg_color="green")  # Set frame color to green
        left_frame.pack(side="left", fill="y", padx=10)

        # Buttons for months (Jan-Dec) (set button color to dark grey)
        app.month_buttons = []
        for i in range(1, 13):
            month_button = customtkinter.CTkButton(left_frame, text=calendar.month_name[i], width=20,
                                                   command=lambda month=i: app.select_month(month), fg_color="darkgrey")
            month_button.pack(pady=5, padx=5, fill="x")
            app.month_buttons.append(month_button)

        # Right frame for the calendar grid
        app.calendar_frame = customtkinter.CTkFrame(main_frame, fg_color="green")  # Set frame color to green
        app.calendar_frame.pack(side="left", padx=10, fill="both", expand=True)

        # Configure the calendar grid to expand
        app.calendar_frame.grid_rowconfigure(0, weight=1)
        app.calendar_frame.grid_columnconfigure(0, weight=1)

    def display_month(app, month, year):
        """Display the calendar for the selected month."""
        app.current_month = month
        app.current_year = year
        
        # Update the calendar in the right frame
        # Clear the previous calendar if any
        for widget in app.calendar_frame.winfo_children():
            widget.destroy()

        # Month and year label at the top
        month_label = customtkinter.CTkLabel(app.calendar_frame, text=f"{calendar.month_name[month]} {year}", font=("Helvetica", 20), text_color="white")
        month_label.grid(row=0, column=0, columnspan=7, pady=20, sticky="nsew")

        # Create the calendar for the month
        month_days = calendar.monthcalendar(year, month)

        # Create day headers (Sun, Mon, etc.)
        day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, day_name in enumerate(day_names):
            label = customtkinter.CTkLabel(app.calendar_frame, text=day_name, font=("Helvetica", 14, "bold"), text_color="white")
            label.grid(row=1, column=col, padx=10, pady=10, sticky="nsew")

        # Add the days of the month
        for row, week in enumerate(month_days, 2):
            for col, day in enumerate(week):
                if day != 0:
                    day_button = customtkinter.CTkButton(app.calendar_frame, text=str(day), width=4, height=2,
                                                       command=lambda d=day: app.on_day_click(d), fg_color="darkgrey")
                    day_button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")

        # Dynamically scale grid cells to fill available space
        for i in range(1, 7):  # Rows for the day grid
            app.calendar_frame.grid_rowconfigure(i, weight=1)
        for i in range(7):  # Columns for the day grid (7 days)
            app.calendar_frame.grid_columnconfigure(i, weight=1)

    def select_month(app, month):
        """Update the calendar to the selected month."""
        app.display_month(month, app.current_year)

    def on_day_click(app, day):
        """Display a message when a day is clicked."""
        messagebox.showinfo("Day Selected", f"You selected {calendar.month_name[app.current_month]} {day}, {app.current_year}")

    def on_menu_button_click(app, button_number):
        """Handle menu button clicks."""
        messagebox.showinfo("Button Clicked", f"Button {button_number} clicked!")

    def close_window(app):
        """Close the window."""
        app.window.quit()  # Close the app

    def toggle_fullscreen(app, event=None):
        """Toggle between fullscreen and windowed mode."""
        current_state = app.window.attributes("-fullscreen")
        app.window.attributes("-fullscreen", not current_state)

    def exit_fullscreen(app, event=None):
        """Exit fullscreen mode on Escape key press."""
        app.window.attributes("-fullscreen", False)

if __name__ == "__main__":
    # Use customtkinter to create the app window
    app = customtkinter.CTk()
    CalendarApp(app)
    app.mainloop()
