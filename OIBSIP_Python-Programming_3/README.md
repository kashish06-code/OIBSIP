# Random Password Generator using Python 🔐

A simple and secure **Random Password Generator** built with Python. It uses Python's `secrets` module to generate cryptographically strong random passwords.

## ✨ Features

* Generates random passwords securely using `secrets.choice()`
* Supports uppercase and lowercase letters
* Includes numbers and special characters
* Allows password lengths from **8 to 15 characters**
* Handles invalid password lengths with a clear error message
* Uses Python's built-in `string` and `secrets` modules

## 🛠️ Requirements

* Python 3.x
* No external packages are required

## 📁 Project Structure

```text
Random-Password-Generator/
│
├── main.py
└── README.md
```

## 🚀 How to Run

1. Clone the repository:

```bash
git clone https://github.com/kashish06-code/Random-Password-Generator.git
```

2. Navigate to the project directory:

```bash
cd Random-Password-Generator
```

3. Run the Python program:

```bash
python main.py
```

4. Enter a password length between **8 and 15** when prompted.

### Example

```text
Enter password length(8-15):12
Generated Password: aB7!xQ2@mP9#
```

> The generated password will be different each time.

## 🔍 How It Works

The program creates a character pool containing:

* `string.ascii_letters` — uppercase and lowercase letters
* `string.digits` — numbers from `0` to `9`
* `string.punctuation` — special characters

It then uses:

```python
secrets.choice(chrs)
```

to securely select random characters until the requested password length is reached.

## ⚠️ Input Validation

The program only accepts password lengths between **8 and 15**.

If a value outside this range is entered, the program displays an error:

```text
Error! Password length must be b/w (8-15)!
```

Non-numeric input is also handled through the `ValueError` exception.

## 🔐 Security

This project uses Python's [`secrets`](https://docs.python.org/3/library/secrets.html) module rather than the standard `random` module. `secrets` is designed for generating random values suitable for security-sensitive applications such as passwords and tokens.

**Tip:** For real-world accounts, use a trusted password manager and avoid reusing passwords.

## 📚 Technologies Used

* **Python 3**
* `string`
* `secrets`

## 👩‍💻 Author

**Kashish**

GitHub: [@kashish06-code](https://github.com/kashish06-code)

## 📄 License

This project is open source and available for personal and educational use.
