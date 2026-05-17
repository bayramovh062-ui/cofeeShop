# ☕ Coffee Shop Earnings Calculator

This is a functional Python application designed for data integration and financial computing. It fetches coffee shop sales data in JSON format from a remote server, analyzes the quantities sold, and calculates the **total weekly earnings** (including drinks, desserts, and tips).

The project demonstrates clean code practices, modular design, and API/JSON data handling in Python.

---

## 🚀 Features & Architecture

The codebase is completely modularized into dedicated functions to ensure readability and reusability:

* `fetch_data(url)`: Sends an HTTP request to the target URL to retrieve raw data.
* `deserialize_data(raw_data)`: Parses raw JSON data into a structured Python dictionary (`dict`).
* `get_data_from_key(data, key)`: Filters and extracts data for a specific day or specific sections (like prices) from the weekly data.
* `get_price(prices, item)`: Looks up and returns the menu price of a specific drink or dessert.
* `calculate_day(day_data, prices)`: Iterates through all drinks and desserts sold in a single day, multiplies quantities by their respective prices, adds the daily tips, and returns the total daily revenue.
* `calculate_week(data, prices)`: Loops through all days of the week, aggregates their daily totals, and returns the final weekly sum.

---

🛠️ Technologies Used
Python 3.x

Requests Library (For fetching external API data via HTTP requests)

JSON Module (Built-in library used for data deserialization)

💻 How to Run
1.Clone this repository to your local machine:
    Bash
    git clone [https://github.com/istifadeci_adiniz/coffee-shop-calculator.git](https://github.com/istifadeci_adiniz/coffee-shop-calculator.git)

2.Install the required dependencies:
    Bash
    pip install requests
3.Run the script:
    Bash
    python coffeeshop.py

🎯 Expected Output
When executed successfully, the program will process the data and display the calculated weekly revenue in the console:
    Plaintext
    Total Weekly Earnings: 1897.25


## 📊 Data Structure Sample

The application processes structured JSON data formatted as follows:
```json
{
  "prices": { 
    "americano": 2.50, 
    "san_sebastian": 5.50 
  },
  "monday": {
    "drinks": { "americano": 3 },
    "desserts": { "san_sebastian": 3 },
    "tips": 13.00
  }
}



