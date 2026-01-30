
# MakeIzlyGreatAgain 💳

> A simple, clean, and self-hosted web interface for Izly — because the official app is… let’s say *painful to use*.

---

## ❓ What is this?

**MakeIzlyGreatAgain** is a lightweight Flask web app that lets you:

- View your Izly balance
- Generate your Izly payment QR code
- Use Izly from a clean, responsive web interface
- Run everything locally in a Docker container

It acts as a simple frontend that replicates Izly’s website/app behavior without the bloat.

---

## 🤯 Why does this exist?

Because the official Izly app:

- Is often slow and buggy  
- Has UX issues  
- Randomly logs you out  
- Makes simple tasks frustrating  

This project was built out of pure necessity (and sanity preservation).

If you’ve ever stood in line waiting for Izly to load… this is for you.

---

## ✨ Features

✅ Clean Bootstrap UI  
✅ Mobile-friendly & responsive  
✅ View account balance  
✅ Generate payment QR code  
✅ Dockerized for easy deployment  
✅ Lightweight & fast  

---

## 🔒 Privacy & Disclaimer

**Your privacy matters.**

- This app runs **locally on your machine**
- No data is sent anywhere except to Izly's official services
- No credentials are stored
- No personal data is logged
- No database is used

This project simply replicates Izly's normal web requests.

> ⚠️ This is an unofficial project and is not affiliated with Izly.

Use at your own discretion.

---

## 🐳 Installation (Docker – Recommended)

### 1️⃣ Clone the repo

```bash
git clone https://github.com/SleepInfinity/MakeIzlyGreatAgain.git
cd MakeIzlyGreatAgain
```

---

### 2️⃣ Build the container

```bash
docker compose build
```

---

### 3️⃣ Run it

```bash
docker compose up -d
```

---

### 4️⃣ Open in browser

```
http://localhost:8080
```

Done 🎉

---

## 🛠️ Manual Installation (without Docker)

### Requirements

* Python 3.10+
* pip

---

### Install dependencies

```bash
pip install -r requirements.txt
```

---

### Run the app

```bash
python app.py
```

Open:

```
http://localhost:8080
```

---

## 📱 How to Use

1. Enter your Izly username & password
2. Click:

   * **Check Balance** to view balance
   * **Show QR Code** to generate payment QR
3. Scan & pay like normal

Simple.

---

## 🙌 Acknowledgments

Huge thanks to:

👉 [https://github.com/jeromecst/izly](https://github.com/jeromecst/izly)

This project relies on their reverse-engineered Izly API work.

Without it, this project wouldn’t exist.

---

## 🤝 Contribute

Contributions are welcome!
Feel free to:

* Open issues for bugs, feature suggestions, or compatibility problems
* Submit pull requests to improve the app

---

## ⭐ Support

If this project saved your time or sanity:

Give it a ⭐ on GitHub!

It helps more students discover it.

---

## ⚖️ License

MIT License — do whatever you want, just don’t blame me if Izly gets mad 😉

---

**Make Izly Great Again.**

