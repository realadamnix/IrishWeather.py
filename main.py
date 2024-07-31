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
    print("select 1. Get the weather forecast for today")
    print("---------------------------------------------")
    print("select 2. Get the weather forecast for Munster")
    print("---------------------------------------------")
    choice = input("Enter your choice: ")

    if choice == "1":
        print(national_forecast_call())    
    elif choice == "2":
        print(munster_forecast_call())
    else:
        print("Invalid choice")
        main()


def national_forecast_call():
    """
    this function makes a get request to the met.ie api and returns the weather forecast.
    """

    national_forecast = requests.get(
        "https://www.met.ie/Open_Data/json/National.json", timeout=5
    )
    national_forecast = national_forecast.json()
    today = national_forecast["forecasts"][0]["regions"][2]["today"]
    return today


def munster_forecast_call():
    """
    this function makes a get request to the met.ie api and returns the weather forecast.
    """

    munster_forecast = requests.get(
        "https://www.met.ie/Open_Data/json/Munster.json", timeout=5
    )
    munster_forecast = munster_forecast.json()
    today = munster_forecast["forecasts"][0]["regions"][2]["today"]
    return today

if __name__ == "__main__":
    main()
