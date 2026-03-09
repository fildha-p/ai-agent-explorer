# 🤖 AI Agent Explorer

AI Agent Explorer is an interactive application that demonstrates how AI-powered agents can perform different tasks such as generating structured content, conducting web research, and interacting with APIs.

The project uses **OpenAI models**, **Streamlit**, and **Pydantic** to build structured AI outputs and a simple interface for exploring AI agent capabilities.

---

## 🚀 Features

* 🍳 **Recipe Generator**

  * Generates structured recipes from a dish name
  * Returns ingredients, cooking time, and step-by-step instructions
  * Uses Pydantic models to validate AI responses

* 🔍 **Web Research Agent**

  * Retrieves summaries from the web using DuckDuckGo API
  * Demonstrates simple AI + web integration

* 🧠 **Structured AI Output**

  * Uses Pydantic schemas to enforce structured responses from the AI model

* 🎛 **Interactive UI**

  * Built with Streamlit for a simple user interface
  * Allows users to input queries and generate results instantly

---

## 🛠 Tech Stack

* Python
* OpenAI API
* Streamlit
* Pydantic
* Requests
* Jupyter Notebook

---

## 📂 Project Structure

```
ai-agent-explorer
│
├── app.py            # Streamlit application
├── main.ipynb        # Notebook with AI agent experiments
├── requirements.txt  # Python dependencies
├── .gitignore        # Files ignored by Git
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/fildha-p/ai-agent-explorer.git
cd ai-agent-explorer
```

---

### 2️⃣ Create a virtual environment

```bash
python -m venv .venv
```

Activate it:

**Windows**

```bash
.venv\Scripts\activate
```

**Mac/Linux**

```bash
source .venv/bin/activate
```

---

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Set your OpenAI API key

Create a `.env` file:

```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Running the App

Start the Streamlit app:

```bash
streamlit run app.py
```

Then open the URL shown in your terminal (usually):

```
http://localhost:8501
```

---

## 🧪 Example Usage

### Recipe Generator

Input:

```
Pasta Carbonara
```

Output:

```
Ingredients:
- Spaghetti
- Eggs
- Pancetta
- Parmesan cheese
- Black pepper

Cooking Time:
20 minutes

Instructions:
1. Boil pasta
2. Cook pancetta
3. Mix eggs and cheese
4. Combine all ingredients
```

---

## 📌 Learning Goals

This project demonstrates:

* AI-powered task automation
* Structured AI responses using Pydantic
* API integrations with Python
* Building simple AI applications with Streamlit

---

## 🔐 Security Note

API keys are stored in `.env` and **not committed to the repository** to protect sensitive credentials.

---

## 📈 Future Improvements

* Add more AI agents
* Integrate external APIs
* Implement agent orchestration
* Add chat-style interface
* Deploy the app online

---

## 👩‍💻 Author

**Fildha**

GitHub:
https://github.com/fildha-p

---

⭐ If you found this project useful, feel free to star the repository.
