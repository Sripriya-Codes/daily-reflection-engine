# Daily Reflection Engine

A deterministic decision-tree based reflection system that guides users through structured end-of-day thinking.

This project encodes psychological frameworks into a fixed, auditable tree — not an AI chatbot.

---

## 🧠 Core Idea

The system walks a user through three key psychological axes:

1. **Locus of Control** — Did I act with agency or react to circumstances?
2. **Contribution vs Entitlement** — Did I focus on what I gave or what I received?
3. **Radius of Concern** — Was I focused only on myself or also on others?

Each axis builds on the previous one to create a structured reflection flow.

---

## ⚙️ How It Works

- The user answers fixed-option questions
- Each answer maps to predefined signals
- The system branches deterministically
- Reflections are shown based on the selected path

There is:

- ❌ No free text input
- ❌ No AI at runtime
- ✅ Fully deterministic logic

---

## 📂 Project Structure

tree/
reflection-tree.json → main decision tree

write-up.md → design explanation
README.md → project overview

---

## 🌳 Reflection Flow (Diagram)

````mermaid
flowchart TD
    START --> A1_Q1
    A1_Q1 --> A1_D1

    A1_D1 -->|Productive/Mixed| A1_Q2_HIGH
    A1_D1 -->|Tough/Frustrating| A1_Q2_LOW

    A1_Q2_HIGH --> A1_Q3_HIGH --> A1_R1
    A1_Q2_LOW --> A1_Q3_LOW --> A1_R2

    A1_R1 --> BRIDGE_1_2
    A1_R2 --> BRIDGE_1_2

    BRIDGE_1_2 --> A2_Q1 --> A2_D1

    A2_D1 -->|Helped| A2_Q2_HIGH
    A2_D1 -->|Others| A2_Q2_LOW

    A2_Q2_HIGH --> A2_R1
    A2_Q2_LOW --> A2_R2

    A2_R1 --> BRIDGE_2_3
    A2_R2 --> BRIDGE_2_3

    BRIDGE_2_3 --> A3_Q1 --> A3_D1

    A3_D1 -->|Self| A3_Q2_LOW
    A3_D1 -->|Others| A3_Q2_HIGH

    A3_Q2_HIGH --> A3_R1
    A3_Q2_LOW --> A3_R2

    A3_R1 --> SUMMARY
    A3_R2 --> SUMMARY

    SUMMARY --> END

'''

 ✨ Key Features
Deterministic decision tree
Fixed-option branching
Signal-based state tracking
Structured reflection flow
No dependency on AI at runtime


 🎯 Purpose

This project demonstrates how psychological concepts can be translated into structured systems that guide thinking without relying on generative AI.

It reflects a knowledge engineering approach — turning abstract ideas into navigable decision trees.

🚀 Future Improvements
More nuanced signal scoring
Dynamic summary generation
UI-based interaction
Larger question bank for variation
📌 Note

AI tools were used during development for ideation and refinement, but the final system is fully deterministic and does not rely on AI execution.

---

# ✅ AFTER THIS

1. Save file
2. Run:

```bash
git add .
git commit -m "final readme"
git push
````
