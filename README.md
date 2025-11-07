# WeatherPy
A Python based weather application that provides users with real-time weather information and a 24-hour temperature forecast.

#### Video Demo:  [Click Here](https://youtu.be/hITXuD4pDN0)
#### Description:
For my CS50P final project, I created WeatherPy, a Python based weather application that provides users with real-time weather information and a 24-hour temperature forecast. The project demonstrates how Python can interact with APIs, process data, and present it in both table and graphical formats. My goal was to build a tool that is both practical and a good opportunity to showcase the programming concepts I had learned throughout the CS50P course.

WeatherPy retrieves data from two free public APIs. First, the program uses the OpenStreetMap Nominatim API to translate user input (a city name) into geographical coordinates. This step is important because most free weather services where you do not have to make an account require latitude and longitude coordinates rather than actual city names. Once the coordinates are returned, the program calls the Open-Meteo API to fetch live weather data including temperature, wind speed, wind direction, and a weather condition code.

I created a CSV file containing mappings between weather codes and human readable descriptions. For example, “1” = “Clear sky”). This gives the user a better visual idea of what the weather is like rather than just going off a number. This adds a layer of accessibility for the user and demonstrates file handling in Python.

The main results are presented in a formatted table using the tabulate library which gives the terminal output an easy to read organised structure. Users can see the current temperature, wind details, description, and the time the request was made. To make the program interactive the user is asked whether they would like to view a 24-hour forecast. If they respond “yes” the program retrieves hourly temperature data from the API, extracts the most recent 24 hours, and plots the values on a line graph using Matplotlib. The graph clearly shows the temperature across the day providing more depth than just a single snapshot of current conditions.

Throughout development, I made use of several programming concepts introduced in CS50P. These include functions for modular design, exception handling for invalid city names or API issues, external libraries for visualization and formatting, and file I/O for reading the weather code descriptions. The project also highlights how Python can work with the internet when pulling live data into a local program.

There were a few challenges along the way. For example, handling invalid user input required careful error checking. I also experimented with different graphing styles in Matplotlib to improve readability. These challenges gave me valuable practice in debugging, testing, and refining code.

In conclusion, WeatherPy is a practical demonstration of how Python can be used to build real world applications that combine APIs, data processing, and user interaction. It not only serves as a weather tool but also reflects the skills I have gained in CS50P, including problem-solving, code organization and making programs both functional and user-friendly.
