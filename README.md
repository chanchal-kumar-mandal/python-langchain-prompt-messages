# 💬 LangChain Structured Prompt Messages with Google Gemini

A clean, modular Python starter project demonstrating how to manage chat contexts and multi-turn conversations using **LangChain Structured Messages** (`SystemMessage`, `HumanMessage`, `AIMessage`) integrated with Google's **Gemini 2.5 Flash** model.

## 🌟 Key Features

* **Structured Conversation Control:** Leverages explicit message roles (`SystemMessage` for persona setting, `HumanMessage` for user input, and `AIMessage` for assistant context/history).
* **Gemini `v1beta` API Integration:** Utilizes `api_version="v1beta"` in `ChatGoogleGenerativeAI` to enable system/developer prompt instructions.
* **Environment Security:** Uses `python-dotenv` and `.gitignore` to prevent secret leakage and keep API credentials isolated.
* **Isolated Environment:** Managed cleanly within Python virtual environments (`.venv`).

## Demo

<img width="1480" height="817" alt="Langchain_Prompt_Messages" src="https://github.com/user-attachments/assets/d2ef3edb-5ec3-485a-a2aa-37c46f7e9de0" />
<img width="1481" height="820" alt="Langchain_Dynamic_Prompt_Messages" src="https://github.com/user-attachments/assets/89603415-ef76-494c-931b-a7179eec9b48" />

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.10+
* **Orchestration Framework:** LangChain (`langchain-core`, `langchain-google-genai`)
* **LLM Provider:** Google GenAI (`gemini-2.5-flash`)
* **Environment Configuration:** `python-dotenv`

## 📁 Project Structure

```
python-langchain-prompt-messages/
├── .venv/                      # Isolated Python virtual environment (git-ignored)
├── notebooks/                  # Script execution directory
│   └── langchain_prompt_messages.py  # Prompt message workflow implementation
├── .env                        # Local environment variables & secrets (git-ignored)
├── .gitignore                  # Prevents committing secrets, venv, and cache files
├── README.md                   # Complete project documentation
└── requirement.txt             # Project dependencies
```

## ⚙️ Getting Started & Setup Guide

### 1. Clone the Repository

```bash
git clone https://github.com/chanchal-kumar-mandal/python-langchain-prompt-messages.git
cd python-langchain-prompt-messages
```

### 2. Create and Activate Virtual Environment

**On Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\activate
```

**On macOS/Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirement.txt
```

---

## 🔑 Environment Configuration

Create a `.env` file in the root directory of your project:

```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

> **Note:** Generate your free Gemini API key at [Google AI Studio](https://aistudio.google.com/api-keys).

---

## 🚀 Usage & Execution

Navigate to the `notebooks` directory and run the script:

```bash
cd notebooks
python langchain_prompt_messages.py
```

### Example Code Implementation (`langchain_prompt_messages.py`)

```python
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    api_key=os.getenv("GEMINI_API_KEY"),
    api_version="v1beta"  # Enables developer/system instructions
)

messages = [
    SystemMessage("You are a python expert"),
    HumanMessage("Explain list in 2 lines"),
    AIMessage("Cherry blossoms bloom...")
]

response = llm.invoke(messages)

print(response.content)
```

---

## 🛡️ Best Practices & Troubleshooting

* **Import Source for Messages:** Import message classes from `langchain_core.messages` (e.g., `from langchain_core.messages import SystemMessage, HumanMessage, AIMessage`).
* **System Messages API Version:** If you encounter `GoogleInvalidRequestError` regarding developer instructions, ensure `api_version="v1beta"` is explicitly passed to `ChatGoogleGenerativeAI`.
* **Dependencies File:** Ensure `requirement.txt` lists valid package names (`langchain-core`, `langchain-google-genai`, `python-dotenv`) and not submodules like `langchain.messages`.