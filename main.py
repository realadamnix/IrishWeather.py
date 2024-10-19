import requests
import tkinter as tk
from tkinter import messagebox

def main():
    """
    Sets up the main GUI window and its components.
    """
    root = tk.Tk()
    root.title("Irish National Weather Forecast")
    root.geometry("800x600")
    root.resizable(True, True)  # Allow resizing if the user wants more space.

    # Add a header label with improved styling
    header = tk.Label(
        root, 
        text="Welcome to the Irish National Weather Forecast", 
        font=("Helvetica", 18, "bold"), 
        fg="#007ACC"
    )
    header.pack(pady=15)

    # Frame for buttons to keep layout clean
    button_frame = tk.Frame(root)
    button_frame.pack(pady=10)

    # Define buttons and corresponding functions
    options = [
        ("National Weather Forecast", national_forecast_call),
        ("Munster Weather Forecast", munster_forecast_call),
        ("Connacht Weather Forecast", connacht_forecast_call),
        ("Leinster Weather Forecast", leinster_forecast_call),
        ("Ulster Weather Forecast", ulster_forecast_call),
        ("Dublin Weather Forecast", dublin_forecast_call),
    ]

    for text, command in options:
        button = tk.Button(
            button_frame, 
            text=text, 
            font=("Helvetica", 12),
            width=30,
            command=lambda cmd=command: show_forecast(cmd, forecast_text)
        )
        button.pack(pady=5, padx=10)

    # Text widget for displaying forecast with a larger initial size
    forecast_text = tk.Text(root, height=20, width=80, wrap="word", font=("Helvetica", 12))
    forecast_text.pack(pady=10, padx=10, expand=True, fill=tk.BOTH)
    forecast_text.config(state=tk.DISABLED)

    # Add a status bar for user feedback
    status_var = tk.StringVar()
    status_var.set("Ready")
    status_bar = tk.Label(root, textvariable=status_var, bd=1, relief=tk.SUNKEN, anchor="w", font=("Helvetica", 10))
    status_bar.pack(fill=tk.X, side=tk.BOTTOM, ipady=2)

    root.mainloop()

def show_forecast(forecast_func, text_widget):
    """
    Displays the forecast in the text widget and adjusts its height dynamically.
    
    Parameters:
    forecast_func (function): The function to call to get the forecast.
    text_widget (tk.Text): The text widget to display the forecast.
    """
    forecast = forecast_func()
    text_widget.config(state=tk.NORMAL)
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, forecast)
    text_widget.config(state=tk.DISABLED)

    # Adjust the height of the text widget dynamically based on the number of lines
    num_lines = forecast.count("\n") + 1
    text_widget.config(height=min(max(num_lines, 10), 30))  # Set height between 10 and 30 lines

def get_forecast(url):
    """
    Makes a GET request to the given API URL and returns the available weather forecast.
    
    Parameters:
    url (str): The URL to fetch the forecast from.
    
    Returns:
    str: The weather forecast or an error message.
    """
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()

        forecast_data = data.get("forecasts", [])
        if forecast_data:
            regions = forecast_data[0].get("regions", [])
            forecasts = []
            for region_data in regions:
                today_forecast = region_data.get("today")
                tonight_forecast = region_data.get("tonight")

                if today_forecast:
                    forecasts.append(f"Today's forecast: {today_forecast}")
                if tonight_forecast:
                    forecasts.append(f"Tonight's forecast: {tonight_forecast}")

            return "\n\n".join(forecasts) if forecasts else "No forecast data available."

        return "No forecast data available."
    
    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."
    except requests.exceptions.HTTPError as err:
        return f"HTTP error occurred: {err}"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def national_forecast_call():
    return get_forecast("https://www.met.ie/Open_Data/json/National.json")

def munster_forecast_call():
    return get_forecast("https://www.met.ie/Open_Data/json/Munster.json")

def connacht_forecast_call():
    return get_forecast("https://www.met.ie/Open_Data/json/Connacht.json")

def leinster_forecast_call():
    return get_forecast("https://www.met.ie/Open_Data/json/Leinster.json")

def ulster_forecast_call():
    return get_forecast("https://www.met.ie/Open_Data/json/Ulster.json")

def dublin_forecast_call():
    return get_forecast("https://www.met.ie/Open_Data/json/Dublin.json")

if __name__ == "__main__":
    main()
