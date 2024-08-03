# Weather Forecast Program

This program retrieves and displays weather forecasts for various regions in Ireland using the [Met Éireann API](https://www.met.ie/Open_Data/json/National.json). It provides a user-friendly interface to view forecasts for different periods and regions.

## Features

- Fetches the latest weather forecast for today or tonight based on availability.
- Retrieves forecasts for specific regions including Munster, Connacht, Leinster, Ulster, and Dublin.
- Uses the Met Éireann API for accurate and up-to-date information.
- Provides a simple, interactive menu for users to select the forecast they want to view.
- Improved error handling and user feedback.

## How It Works

1. **Fetch the Forecast**: The program makes an API request to Met Éireann to retrieve the current weather forecast for the selected region and period.
2. **Display the Forecast**: The available forecast (today or tonight) is extracted and displayed to the user based on the chosen option.
3. **User Interaction**: The program greets the user with a menu and allows them to select which forecast to view. It handles user inputs and displays relevant forecasts or error messages.

## Getting Started

To use the program, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/weather-forecast.git
   cd weather-forecast
