# 🛡 SecureCheck — Advanced Password Security Analyzer

> **Tagline:** *"Understand your password. Improve your security."*

**SecureCheck** is a premium, professional-grade desktop cybersecurity application built with **Python** and **CustomTkinter**. Designed as a portfolio-quality cybersecurity project for BCA/CS students, it provides real-time multi-dimensional password security scoring, common leak detection, entropy analysis, and cryptographically secure password generation with a modern dark dashboard UI.

---

## 🌟 Key Features

- **⚡ Real-Time Multi-Factor Analysis**: Live scoring as you type, evaluating length, character set diversity, entropy (bits), and pattern sequences.
- **🎨 Modern Dark Cybersecurity UI**: Custom glassmorphism cards, electric cyan accents, interactive circular gauge canvas, and pulsing system status indicator.
- **🧠 Advanced Pattern & Common Password Engine**:
  - Substring & exact matching against common leaked credential datasets (`common_passwords.json`).
  - L33t-speak normalization (`P@ssw0rd` → `password`).
  - Keyboard walks (`qwerty`, `asdfgh`), sequential numbers (`12345`), repeated blocks, and year patterns.
- **🔑 Cryptographically Secure Password Generator**: Utilizes Python's `secrets` module (CS-PRNG) to generate random passwords or memorable multi-word passphrases (`correct-horse-battery-staple`).
- **📊 Security Insights & Exportable Reports**: Dynamically updates stats and exports sanitized JSON/TXT reports without storing or transmitting actual password text.
- **🔒 100% Local & Privacy-First**: Operates strictly in-memory. Zero network calls, zero password logging, zero plain-text storage.

---

## 🛠 Tech Stack

- **Language**: Python 3.9+
- **GUI Framework**: CustomTkinter, Tkinter Canvas
- **Visual Assets**: Pillow (PIL) for programmatic vector graphics
- **Core Modules**: `secrets`, `hashlib`, `re`, `string`, `json`, `pathlib`, `unittest`

---

## 📸 Screenshots

*(Add screenshots here when showcasing on GitHub / LinkedIn)*

```
screenshots/
├── dashboard.png
├── analyzer.png
├── generator.png
└── report.png
```

---

## 🚀 Quick Start & Installation

### Prerequisites
Make sure you have Python 3.9+ installed on your system.

### 1. Clone Repository
```bash
git clone https://github.com/your-username/SecureCheck.git
cd SecureCheck
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Launch Application
```bash
python main.py
```

---

## 🧪 Running Unit Tests

Run automated security core unit tests using Python's `unittest`:

```bash
python -m unittest discover -s tests
```

---

## 📁 Project Architecture

```
SecureCheck/
│
├── main.py                     # Application entry point & launcher
├── ui/
│   ├── __init__.py
│   ├── dashboard.py            # Master layout & tab navigation controller
│   ├── components.py           # Reusable widgets (Circular Score Gauge, Header, Check Cards)
│   └── animations.py          # Non-blocking animations (pulsing dot, score easing)
│
├── security/
│   ├── __init__.py
│   ├── analyzer.py            # Core entropy & multi-factor security scoring engine
│   ├── password_generator.py  # Cryptographically secure generator using secrets module
│   └── common_passwords.py    # Common password loader, l33t-speak & pattern detector
│
├── utils/
│   ├── __init__.py
│   ├── theme.py               # Dark cybersecurity color palette & font configuration
│   └── helpers.py             # Asset generator, JSON/TXT report exporter
│
├── assets/                     # Programmatically generated logo, shield & status icons
├── data/                       # Curated common passwords & patterns dictionary
├── tests/                      # Automated unit test suite
├── ASSETS.md                   # Asset licensing documentation
├── README.md                   # Showcase-ready GitHub documentation
├── requirements.txt            # Python package dependencies
└── LICENSE                     # MIT License
```

---

## 🔒 Security & Privacy Notice

SecureCheck is designed as an educational password analyzer.
1. **Local Only**: All calculations occur in-memory on your local machine.
2. **Zero Storage**: Entered passwords are never written to disk, saved in logs, or printed to the console.
3. **No External Network Calls**: The app does not send passwords to external APIs.

---

## 🔮 Future Enhancements

- [ ] Have I Been Pwned $k$-Anonymity API integration (optional opt-in mode)
- [ ] Zxcvbn dictionary password estimation
- [ ] Exportable PDF Security Health Certificate
- [ ] Multi-language support (English, Spanish, Hindi)

---

## 📜 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
