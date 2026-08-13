# 🌤️ Weather App

A simple and lightweight **Command-Line Weather Application** built with **Python**. This app allows users to search for any city worldwide and instantly view its current weather conditions using the **Open-Meteo API** and **Open-Meteo Geocoding API**.

---

## 📖 Features

- 🌍 Search weather by city name
- 📍 Displays city information
  - City
  - Country
  - Latitude & Longitude
  - Timezone
  - Population
- 🌡️ Current temperature
- 💧 Relative humidity
- 💨 Wind speed
- ⚠️ Handles invalid city names gracefully
- 🔌 Handles API/network connection errors
- ⚡ Fast and lightweight
- 🖥️ Simple terminal-based interface

---

## 🛠️ Built With

- **Python 3**
- **Requests** library
- **Open-Meteo Weather API**
- **Open-Meteo Geocoding API**

---

## 📂 Project Structure

```text
Weather-App/
│
├── main.py          # Entry point of the application
├── weather.py       # Weather fetching & display logic
├── README.md
└── requirements.txt (optional)
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/kashish06-code/Weather-app.git
```

### 2. Navigate to the project

```bash
cd Weather-app
```

### 3. Install dependencies

```bash
pip install requests
```

---

## ▶️ Usage

Run the application:

```bash
python main.py
```

Example:

```text
========================================
🌤️ Weather App
========================================

🏙️ Enter city name: Delhi

📍 Location Found!

━━━━━━━━━━ 📋 Details ━━━━━━━━━━

🏙️ City:         Delhi
🌍 Country:      India
📌 Latitude:     28.6517
📍 Longitude:    77.2219
🕒 Timezone:     Asia/Kolkata
👥 Population:   16787941

━━━━━━━━ 🌤️ Current Weather ━━━━━━━━

🌡️ Temperature:  33.4 °C
💧 Humidity:     56%
💨 Wind Speed:   11.2 km/h
```

---

## 🌐 APIs Used

### Open-Meteo Geocoding API

Used to convert a city name into geographical coordinates.

```
https://geocoding-api.open-meteo.com/v1/search
```

### Open-Meteo Weather API

Used to retrieve current weather information.

```
https://api.open-meteo.com/v1/forecast
```

---

## 📦 Requirements

- Python 3.8+
- requests

Install manually:

```bash
pip install requests
```

Or create a `requirements.txt` file:

```text
requests
```

Then install using:

```bash
pip install -r requirements.txt
```

---

## ✨ Future Improvements

- 🌦️ Weather condition descriptions
- 🌅 Sunrise & sunset information
- 📅 7-day weather forecast
- ⏰ Hourly forecast
- 🌍 Automatic location detection
- 🖥️ GUI version using Tkinter or PyQt
- 🌐 Web version using Flask or Django
- 🎨 Better terminal formatting with Rich

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push to your branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 👨‍💻 Author

**Kashish**

GitHub: **https://github.com/kashish06-code**

---

## ⭐ Support

If you found this project useful, consider giving it a **⭐ Star** on GitHub. It helps others discover the project and motivates future improvements.

---

## 📄 License

This project is licensed under the **MIT License**. Feel free to use, modify, and distribute it.