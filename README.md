# Kasparro Content Engine 🚀

An autonomous AI system that acts like a marketing team. It takes raw product notes and automatically generates structured assets: a **Product Page**, an **FAQ Page (15+ Qs)**, and a **Competitor Analysis**.

---

## 🤖 How It Works
This is not just a wrapper around ChatGPT. It is a **multi-agent orchestration pipeline** where each AI agent has a specific job:

1.  **Analyst Agent:** Reads messy text and extracts the hard facts (Price, Ingredients).
2.  **Strategist Agent:** Brainstorms 15+ helpful customer questions based on those facts.
3.  **Competitor Bot:** Simulates a realistic market rival to generate a comparison table.
4.  **Template Engine:** Takes all this data and compiles it into strict, machine-readable JSON files.

---

## 📂 Documentation
I have written detailed documentation explaining the System Design, Architecture choices, and why I built it this way.
**[👉 Read the Project Documentation here](docs/projectdocumentation.md)**

---

## 🛠️ Run Locally
If you want to run this on your own machine:

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/deepshikhar23/kasparro-agentic-deepshikhar-saxena.git
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up keys:**
    Create a `.env` file and add your Google Gemini API key:
    ```text
    GEMINI_API_KEY=your_key_here
    ```

4.  **Run the app:**
    ```bash
    streamlit run app.py
    ```