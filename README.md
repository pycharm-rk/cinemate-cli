# 🎬 Cinemate

Cinemate is a simple command-line movie recommender built with Python. It asks a few quick questions and suggests films based on your **mood**, **genre**, and **preferred decade**.

---

## 🚀 Features

- Choose your **genre** (e.g., drama, sci-fi, romance)
- Pick your **mood** (e.g., inspiring, emotional, intense)
- Narrow down by **decade** (e.g., 1990s, 2000s)
- Smart fallback if no exact match is found

---

## 🛠️ Getting Started

Clone the repo:

```bash
git clone https://github.com/your-username/cinemate-cli.git
cd cinemate-cli
```

Install dependencies if needed (none for this version):

```bash
pip install -r requirements.txt
```

---

## 🎮 Usage

Run the CLI from the project root using:

```bash
python -m src.cinemate.main
```

---

## ✅ Run Tests

```bash
python -m unittest discover tests
```

---

## 📂 Project Structure

```
cinemate-cli/
├── src/
│   └── cinemate/
│       ├── __init__.py
│       ├── main.py
│       └── logic.py
├── tests/
│   └── test_logic.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## 🧠 Inspiration

This project was built to practice Python and create a fun, interactive terminal app for movie recommendations.

---

## 📜 License

MIT License

