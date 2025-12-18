# Kasparro Content Engine - Project Documentation

## 1. Problem Statement
The goal was to build an automated system that takes raw, messy product notes and turns them into three marketing assets:
1.  A Product Page (JSON)
2.  An FAQ Page with 15+ questions (JSON)
3.  A Competitor Comparison Page (JSON)

The main requirement was to use an **"Agentic" approach**—meaning different AI workers handling different tasks—rather than just asking ChatGPT to write everything in one go.

---

## 2. Solution Overview
I built a **Linear Pipeline**. Instead of one big AI trying to do it all, I split the work into specialized roles, just like a real content team:

1.  **Analyst Agent:** Reads the raw text and pulls out the hard facts (Price, Ingredients).
2.  **Strategist Agent:** Uses those facts to think of 15 helpful customer questions.
3.  **Competitor Bot:** invents a realistic rival product to compare against.
4.  **Template Engine:** Puts all this data into the final clean JSON format.

This method is safer. If the FAQs are bad, I only fix the Strategist, without breaking the Product Page.

---

## 3. Scopes & Assumptions
* **Input Data:** The system expects text that has at least a Name, Price, and Ingredients.
* **The "15 FAQs" Rule:** The input data was very short (only 8 lines), but the assignment required **15 FAQs**.
    * *My Decision:* To reach 15 meaningful questions without repeating myself, I allowed the AI to include standard industry advice (like "Store in a cool place" or "Patch test recommended"). These are safe, common-sense additions needed to make the list complete.
* **Competitor Data:** Since no competitor data was provided, the system "simulates" a market rival based on the main product's price.

---

## 4. System Design

The system flows in one direction (a simple pipeline). Data gets refined at each step.

### How it flows:
`Raw Text` → **[Analyst cleans it]** → `Structured Data` → **[Strategist & Competitor Bot add ideas]** → `Final JSON Output`

### Component Breakdown

#### A. The Agents (The Brains)
Located in `src/agents/`.
* **Data Analyst:** The "Gatekeeper." It makes sure we don't start with bad data. It extracts the facts.
* **Content Strategist:** The "Creative." It takes the facts and writes the Q&A.
* **Competitor Bot:** The "Simulator." It looks at our price and invents a competitor that is slightly cheaper or different.

#### B. The Template Engine (The Body)
Located in `src/templates/`.
* AI is great at writing, but bad at keeping strict brackets `{ }` for code.
* I separated them: **The AI writes the text, but Python code builds the JSON structure.**
* This guarantees the code never crashes due to missing commas or wrong keys.

#### C. The Orchestrator
Located in `src/core/orchestrator.py`.
* This is the manager script that runs the agents in the right order (1, 2, then 3).

---

## 5. Tech Stack
* **Python:** For the logic.
* **Google Gemini 2.5 Flash:** Chosen because it is very fast and cheap for this kind of repetitive task.
* **Streamlit:** For the user interface demo.