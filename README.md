# 🔢 Number to Word Converter (Python)

Turn raw integers into clean, human‑readable English words using **recursion done right**.

This project converts numbers into their word representation by breaking them down logically instead of brute‑forcing cases.

---

## ✨ Features

✅ Supports numbers below 20  
✅ Handles tens (20–99)  
✅ Works with hundreds, thousands, millions  
✅ Fully recursive & scalable  
✅ Zero external libraries  

---

## 📁 Project Structure

```
Number-to-word/
├── README.md
└── src/
    ├── main.py
    └── cons.py
```

### 🧠 `main.py`
Contains:
- `number_to_word(num)` recursive function
- Example executions for large numbers

### 📦 `src/cons.py`
Holds constants only (clean separation of concerns):

- `Under_20` → 0–19
- `Tens` → 20, 30, 40, ...
- `More_than_hundred` → 100, 1000, 1000000, ...

This keeps logic readable and easy to extend.

---

## ⚙️ How It Works (Conceptually)

1️⃣ **Base cases**
- `< 20` → direct lookup  
- `< 100` → split into tens + remainder  

2️⃣ **Recursive breakdown**
- Find the largest valid pivot (hundred, thousand, million…)
- Divide the number into:
  - quotient → recursive call
  - remainder → recursive call
- Combine results into natural language

🧩 Result:
- No repetition
- No hard‑coding
- Clean recursive flow

---

## ▶️ Example Usage

```python
print(number_to_word(1111111))
print(number_to_word(9999999))
print(number_to_word(1000000))
```

### 🖨️ Example Output

```
one million one hundred eleven thousand one hundred eleven
nine million nine hundred ninety nine thousand nine hundred ninety nine
one million
```

---

## 🧪 Requirements

- 🐍 Python 3.8+
- ❌ No third‑party packages

---

## 🧠 Notes (Read This)

- Recursion always goes **down to the base case first**, then resolves **back up**
- Adding billions/trillions = just extend `More_than_hundred`
- Code favors **clarity over premature optimization**

---

## 📜 License

🆓 Free to use, modify, break, and rebuild.


## 👨‍💻Author
💻 Built with ❤️ by Kian Kheiri N. ([@Cnized](https://github.com/Cnized))