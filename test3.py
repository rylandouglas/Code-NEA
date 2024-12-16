import customtkinter as customtkinter
import calendar
from tkinter import messagebox

class CalendarApp:
    def __init__(app, window):
        app.window = window
        app.window.title("Calendar")
        
        app.current_month = 1
        app.current_year = 2024

        # Create and pack widgets
        app.create_widgets()
        app.display_month(app.current_month, app.current_year)

    def create_widgets(app):
        # Main frame layout with two parts: Left for months and right for the calendar
        main_frame = customtkinter.CTkFrame(app.window)
        main_frame.pack(padx=10, pady=10, fill="both", expand=True)

        # Left frame for month buttons
        left_frame = customtkinter.CTkFrame(main_frame)
        left_frame.pack(side="left", fill="y", padx=10)

        # Buttons for months (Jan-Dec)
        app.month_buttons = []
        for i in range(1, 13):
            month_button = customtkinter.CTkButton(left_frame, text=calendar.month_name[i], width=20,
                                                   command=lambda month=i: app.select_month(month))
            month_button.pack(pady=5, padx=5, fill="x")
            app.month_buttons.append(month_button)

        # Right frame for the calendar grid
        app.calendar_frame = customtkinter.CTkFrame(main_frame)
        app.calendar_frame.pack(side="left", padx=10, fill="both", expand=True)

    def display_month(app, month, year):
        """Display the calendar for the selected month."""
        app.current_month = month
        app.current_year = year
        
        # Update the calendar in the right frame
        # Clear the previous calendar if any
        for widget in app.calendar_frame.winfo_children():
            widget.destroy()

        # Month and year label at the top
        month_label = customtkinter.CTkLabel(app.calendar_frame, text=f"{calendar.month_name[month]} {year}", font=("Helvetica", 16))
        month_label.grid(row=0, column=0, columnspan=7, pady=10)

        # Create the calendar for the month
        month_days = calendar.monthcalendar(year, month)

        # Create day headers (Sun, Mon, etc.)
        day_names = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for col, day_name in enumerate(day_names):
            label = customtkinter.CTkLabel(app.calendar_frame, text=day_name, font=("Helvetica", 12, "bold"))
            label.grid(row=1, column=col, padx=5, pady=5)

        # Add the days of the month
        for row, week in enumerate(month_days, 2):
            for col, day in enumerate(week):
                if day != 0:
                    day_button = customtkinter.CTkButton(app.calendar_frame, text=str(day), width=4, height=2,
                                                       command=lambda d=day: app.on_day_click(d))
                    day_button.grid(row=row, column=col, padx=5, pady=5)

    def select_month(app, month):
        """Update the calendar to the selected month."""
        app.display_month(month, app.current_year)

    def on_day_click(app, day):
        """Display a message when a day is clicked."""
        messagebox.showinfo("Day Selected", f"You selected {calendar.month_name[app.current_month]} {day}, {app.current_year}")

if __name__ == "__main__":
    # Use customtkinter to create the app window
    app = customtkinter.CTk()
    CalendarApp(app)
    app.mainloop()
