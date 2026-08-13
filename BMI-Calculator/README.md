# 🧮 BMI Calculator – Python Tkinter

A simple and user-friendly **BMI (Body Mass Index) Calculator** built with **Python** and **Tkinter**.

The application provides a graphical interface where users can enter their weight and height to calculate their BMI and view their corresponding BMI category.

## 📸 Features

* Calculate BMI using weight and height
* Simple graphical user interface using Tkinter
* BMI classification:

  * Underweight 😕
  * Healthy ✅
  * Overweight ⚠️
  * Obese 🩺
* Color-coded BMI results
* Input validation for invalid or non-positive values
* Reset button to clear entered values
* Exit button to close the application
* Press **Enter/Return** to calculate BMI

## 🛠️ Technologies Used

* **Python 3**
* **Tkinter** – Python's standard GUI library

## 📋 BMI Formula

The application calculates BMI using:

```text
BMI = Weight (kg) / Height (m)²
```

Since the application accepts height in centimeters, it first converts centimeters to meters:

```text
Height (m) = Height (cm) / 100
```

### BMI Classification

| BMI Range      | Category    |
| -------------- | ----------- |
| Below 18.5     | Underweight |
| 18.5 – 24.9    | Healthy     |
| 25.0 – 29.9    | Overweight  |
| 30.0 and above | Obese       |

> **Note:** BMI is a general screening measure and does not account for factors such as muscle mass, body composition, age, or individual health circumstances.

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/kashish06-code/OIBSIP.git
```

### 2. Navigate to the Project

```bash
cd OIBSIP
```

### 3. Run the Application

```bash
python bmi_calculator.py
```

On some systems, you may need:

```bash
python3 bmi_calculator.py
```

## 📁 Project Structure

```text
OIBSIP/
│
├── bmi_calculator.py
└── README.md
```

## 💻 How to Use

1. Enter your **weight in kilograms (kg)**.
2. Enter your **height in centimeters (cm)**.
3. Click **Calculate BMI**.
4. Your BMI and category will be displayed.
5. Click **Reset** to clear the fields.
6. Click **Exit** to close the application.

You can also press **Enter/Return** after entering your details to calculate the BMI.

## ⚠️ Input Validation

The application handles invalid input using an error dialog.

Examples of invalid input include:

* Empty fields
* Text instead of numbers
* Zero weight or height
* Negative weight or height

## 🔮 Future Improvements

Possible improvements include:

* Add metric/imperial unit selection
* Add age and gender information
* Improve the graphical design
* Add BMI history
* Add a visual BMI indicator
* Package the application as a Windows `.exe`
* Add dark mode
* Add a more detailed health information section

## 👨‍💻 Author

**Kashish**

GitHub: [@kashish06-code](https://github.com/kashish06-code)

## 📄 License

This project is open source and available under the **MIT License**.
