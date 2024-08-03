"""
this is a simple python program that gets the weather forecast from the met.ie api.
it has a main function that calls the forecast_call function to get the weather forecast.
the forecast_call function makes a get request to the met.ie api and returns the weather forecast.
"""

import requests


def main():
    """
    This function is the main function that runs the program.
    """

    print("Welcome to the irish national weather forecast")
    print("---------------------------------------------")
    print("select 1. Get the weather forecast for today/tonight")
    print("---------------------------------------------")
    print("select 2. Get the weather forecast for Munster")
    print("---------------------------------------------")
    print("select 3. Get the weather forecast for Connacht")
    print("---------------------------------------------")
    print("select 4. Get the weather forecast for Leinster")
    print("---------------------------------------------")
    print("select 5. Get the weather forecast for Ulster")
    print("---------------------------------------------")
    print("select 6. Get the weather forecast for Dublin")
    print("---------------------------------------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(national_forecast_call()) 
    elif choice == "2":
        print(munster_forecast_call())
    elif choice == "3":
        print(Connacht_forecast_call())
    elif choice == "4":
        print(Leinster_forecast_call())
    elif choice == "5":
        print(Ulster_forecast_call())
    elif choice == "6":
        print(Dublin_forecast_call())
    else:
        print("Invalid choice")
        main()

def get_forecast(url):
    """
    This function makes a get request to the given API URL and returns the available weather forecast.
    """

    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  
        data = response.json()

        
        forecast_data = data.get("forecasts", [])
        if forecast_data:
            regions = forecast_data[0].get("regions", [])
            for region_data in regions:
                today_forecast = region_data.get("today")
                tonight_forecast = region_data.get("tonight")
                
                if today_forecast:
                    return f"Today's forecast: {today_forecast}"
                elif tonight_forecast:
                    return f"Tonight's forecast: {tonight_forecast}"
                
        return "No forecast data available"

    except (requests.RequestException, KeyError) as e:
        return f"An error occurred: {e}"


def national_forecast_call():
    """
    This function gets the weather forecast from the met.ie API for National.
    """
    return get_forecast("https://www.met.ie/Open_Data/json/National.json")

def munster_forecast_call():
    """
    This function gets the weather forecast from the met.ie API for Munster.
    """
    return get_forecast("https://www.met.ie/Open_Data/json/Munster.json")

def Connacht_forecast_call():
    """
    This function gets the weather forecast from the met.ie API for Connacht.
    """
    return get_forecast("https://www.met.ie/Open_Data/json/Connacht.json")

def Leinster_forecast_call():
    """
    This function gets the weather forecast from the met.ie API for Leinster.
    """
    return get_forecast("https://www.met.ie/Open_Data/json/Leinster.json")

def Ulster_forecast_call():
    """
    This function gets the weather forecast from the met.ie API for Ulster.
    """
    return get_forecast("https://www.met.ie/Open_Data/json/Ulster.json")

def Dublin_forecast_call():
    """
    This function gets the weather forecast from the met.ie API for Dublin.
    """
    return get_forecast("https://www.met.ie/Open_Data/json/Dublin.json")


if __name__ == "__main__":
    main()