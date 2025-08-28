# technical-challenge-thoughtful

# 📦 Sorting Robot

This project contains a simple Python function that helps a robotic arm in a factory decide where to send packages based on their **size** and  **weight** .

## 🧠 What It Does

The robot uses the `sort()` function to classify packages into **three** categories:

1. **STANDARD** – normal packages (not too big or heavy)
2. **SPECIAL** – packages that are **either** too big or too heavy
3. **REJECTED** – packages that are **both** too big **and** too heavy

---

## 🧮 How It Works

### Rules:

A package is:

* **Bulky** if:
  * Volume ≥ **1,000,000 cm³** (Width × Height × Length)
  * **OR** any side is ≥ **150 cm**
* **Heavy** if:
  * Mass ≥ **20 kg**

### Sorting logic:

| Bulky | Heavy | Result       |
| ----- | ----- | ------------ |
| No    | No    | `STANDARD` |
| Yes   | No    | `SPECIAL`  |
| No    | Yes   | `SPECIAL`  |
| Yes   | Yes   | `REJECTED` |

---

## 🧪 Example Usage

```
from sort import sorting_stack as sort
print(sort(99, 100, 100, 19) 	# "STANDARD"
print(sort(100, 100, 100, 19)	# "SPECIAL")  volume
print(sort(150, 100, 100, 5) 	# "SPECIAL")  width
print(sort(100, 150, 100, 5)	# "SPECIAL")  height
print(sort(100, 100, 150, 5)	# "SPECIAL")  length
print(sort(25, 25, 25, 25) 	# "SPECIAL")  heavy
print(sort(100, 100, 100, 20)	# "REJECTED") bulky & heavy
```

## 🛠️ How to Use

1. Clone this repo:

   ```
   git clone <repo_Url>
   ```
2. Run the code in Python:

   ```
   cd technical-challange-thoughtful
   python sort.py
   ```

## 📁 File Structure

<pre class="overflow-visible!" data-start="1564" data-end="1740"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary text-token-text-secondary flex items-center gap-4 rounded-sm px-2 font-sans text-xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span></span><span>sorting-robot/
│
├── sort.py        </span><span># Contains the sorting_stack() function</span><span>
├── test.py          </span><span># Optional: file to test the function</span><span>
└── README.md        </span><span># This file</span><span>
</span></span></code></div></div></pre>

---

## ✅ Requirements

* Python 3.x
* No external libraries needed

---

## 📌 Summary

This function helps automate package sorting in a warehouse based on **volume** and  **weight** . It's simple, fast, and easy to use in any logistics or robotics project.
