#Import library
import customtkinter

# Initialize the main application window
app = customtkinter.CTk()
app.geometry("700x300")
app.title("Main Menu with Simulated Nested Dropdowns")
app.configure(fg_color="#73B12F")  # Set background to green
app.attributes("-fullscreen", True) # Auto set to fullscreen

# Defining font styles
title_font = ("Arial", 16, "bold")
menu_font = ("Arial", 12)

# Main menu dropdown options
menu_data = {
    "Book a new job":[], # Not needed- should take to calendar page
    "Existing Appointments": ["June 18th - 8:30-12:30", "August 12th - 12:30-5:30"], #placeholder figures
    "Application Process": ["Zoom In", "Zoom Out", "Full Screen"],
    "Business Overview": ["FAQS", "Mission Statement", "Company Information"],
    "Reviews": ["5* From Bert F", "3* From John P", "4* From Samba B"]
}

# Nested submenus options
sub_options_data = {
    "August 12th - 12:30-5:30": ["Job price -560", "Estimated employees 4", "Vehicles 1 chipper & 1 van"],
    "June 18th - 8:30-12:30": ["Job price - £350", "Estimated employees=3", "Vehicles=1 chipper & 1 van"],
    "5* From Bert F": ["Absolutely fantastic service! The team at JPL Tree Care were professional, efficient, and friendly from start to finish"],
    "3* From John P": ["Overall, the service was good, but there were a few things that could have been improved. The team at JPL Tree care were friendly and knowledgeable, and they completed the tree removal safely. However, there were some delays in the scheduling, and the cleanup could have been a bit more thorough."],
    "4* From Samba B": ["Very happy with the service from JPL Tree Care. The team was professional, arrived on time, and efficiently removed a large tree from our property."],
    



}

# Add a "menu bar" with buttons at the top of the window
top_menu_bar = customtkinter.CTkFrame(app, height=40, corner_radius=0, fg_color="#2F2F2F")
top_menu_bar.pack(fill="x", side="top")

# Set the grid for top menu bar with 4 columns (including the close button)
top_menu_bar.grid_columnconfigure(0, weight=1)  # Allow the first column to stretch (left)
top_menu_bar.grid_columnconfigure(1, weight=1)  # Allow the second column to stretch (center)
top_menu_bar.grid_columnconfigure(2, weight=1)  # Allow the third column to stretch (right)
top_menu_bar.grid_columnconfigure(3, weight=0)  # Fixed column for the close button

# Add "Button 1" to the far left of the menu
button1 = customtkinter.CTkButton(
    top_menu_bar, text="Button 1", font=menu_font, fg_color="#464646", hover_color="#2F2F2F", text_color="white", command=lambda: print("Button 1 clicked"))
button1.grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Align to the left (west)

# Add "Button 2" next to Button 1 (in column 1), closer to Button 1
button2 = customtkinter.CTkButton(
    top_menu_bar, text="Button 2", font=menu_font, fg_color="#464646", hover_color="#2F2F2F", text_color="white", command=lambda: print("Button 2 clicked"))
button2.grid(row=0, column=1, padx=5, pady=5, sticky="w")  # Adjust padding to bring closer

# Add "Main Menu" text label to the center of the top menu bar
main_menu_label = customtkinter.CTkLabel(top_menu_bar, text="Main Menu", font=("Arial", 18, "bold"), text_color="white", bg_color="#2F2F2F")
main_menu_label.grid(row=0, column=1, padx=10, pady=5, sticky="nsew")  # Centered in the middle column

# Add "Button 3" to the far right of the menu
button3 = customtkinter.CTkButton(
    top_menu_bar, text="Button 3", font=menu_font, fg_color="#464646", hover_color="#2F2F2F", text_color="white", command=lambda: print("Button 3 clicked"))
button3.grid(row=0, column=2, padx=10, pady=5, sticky="e")  # Align to the right (east)

# Add "Close Window" button to the far right of the menu bar
close_button = customtkinter.CTkButton(
    top_menu_bar, text="Close Window", font=menu_font, fg_color="#FF0000", hover_color="#CC0000", text_color="white", command=lambda: close_window())
close_button.grid(row=0, column=3, padx=10, pady=5)  # Place in the last column

# Add the text label "JPL TREE CARE" above the dropdown menu bar
header_label = customtkinter.CTkLabel(app, text="JPL TREE CARE", font=("Arial", 24, "bold"), text_color="white")
header_label.pack(pady=20)  # Add some space above the header

# Initialize a frame for the main menu bar 
menu_bar = customtkinter.CTkFrame(app, height=50, corner_radius=0, fg_color="#73B12F")
menu_bar.pack(fill="x")

# Center the buttons in the menu bar
menu_bar.grid_rowconfigure(0, weight=1, uniform="equal")  # Uniformly distribute buttons across columns
menu_bar.grid_columnconfigure(0, weight=1)  # Column for first button
menu_bar.grid_columnconfigure(1, weight=1)  # Column for second button
menu_bar.grid_columnconfigure(2, weight=1)  # Column for third button
menu_bar.grid_columnconfigure(3, weight=1)  # Column for fourth button
menu_bar.grid_columnconfigure(4, weight=1)  # Column for fifth button

# Create main menu buttons 
for idx, menu_name in enumerate(menu_data.keys()):
    button = customtkinter.CTkButton(
        menu_bar,
        text=menu_name,
        font=menu_font,
        fg_color="#2F2F2F",         # Dark grey button color
        hover_color="#464646",      # Slightly lighter grey for hover
        text_color="white",
        command=lambda name=menu_name: display_main_menu(name)
    )
    button.grid(row=0, column=idx, padx=10, pady=10, sticky="nsew")

# Frame to display the "nested" dropdown options
dropdown_frame = customtkinter.CTkFrame(app, width=600, height=200, corner_radius=10, fg_color="#73B12F")
dropdown_frame.pack(pady=10, padx=10)

# Label for displaying selected options (simulate menu interaction)
selected_label = customtkinter.CTkLabel(dropdown_frame, text="Select an option from the menu above", font=menu_font, text_color="black")
selected_label.pack(pady=10)

#create close window function
def close_window():
    """Close the application window."""
    app.destroy()

def display_main_menu(menu_name):
    """Display options for the selected main menu."""
    # Clear previous widgets in dropdown_frame
    for widget in dropdown_frame.winfo_children():
        widget.destroy()

    # Display options for the selected main menu
    options = menu_data.get(menu_name, [])
    for option in options:
        button = customtkinter.CTkButton(
            dropdown_frame,
            text=option,
            font=menu_font,
            fg_color="#2F2F2F",       # Dark grey button color
            hover_color="#464646",
            text_color="white",
            command=lambda opt=option: display_sub_menu(menu_name, opt)
        )
        button.pack(pady=5)

def display_sub_menu(menu_name, option):
    """Display sub-options for the selected main menu option if available."""
    # Clear previous widgets in dropdown_frame
    for widget in dropdown_frame.winfo_children():
        widget.destroy()

    # Check if sub-options exist for the selected option
    sub_options = sub_options_data.get(option)
    if sub_options:
        for sub_option in sub_options:
            button = customtkinter.CTkButton(
                dropdown_frame,
                text=sub_option,
                font=menu_font,
                fg_color="#2F2F2F",   # Dark grey button color
                hover_color="#464646",
                text_color="white",
                command=lambda sub=sub_option: display_selection(menu_name, option, sub)
            )
            button.pack(pady=5)
    else:
        # If no sub-options, directly display the selection
        display_selection(menu_name, option)

def display_selection(menu_name, option, sub_option=None):
    """Update label to show the final selection."""
    # Clear previous widgets in dropdown_frame
    for widget in dropdown_frame.winfo_children():
        widget.destroy()

    # Display final selection message
    if sub_option:
        text = f"Selected: {menu_name} > {option} > {sub_option}"
    else:
        text = f"Selected: {menu_name} > {option}"
    
    selected_label.config(text=text)
    selected_label.pack(pady=20)

# Run the application
app.mainloop()
