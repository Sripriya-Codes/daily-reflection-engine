# Design Write-up: Daily Reflection Tree

## 1. Approach

The goal of this assignment was to design a deterministic reflection system that guides structured thinking rather than generating responses dynamically.

I approached this as a knowledge engineering problem by converting psychological concepts into a structured decision tree.

The system progresses across three axes:

1. Locus of Control
2. Contribution vs Entitlement
3. Radius of Concern

Each axis builds on the previous one, creating a natural flow of reflection.

---

## 2. Question Design

The primary focus was on designing questions that feel realistic and relevant at the end of a workday.

Instead of abstract or academic phrasing, I used:

- Situational prompts
- Simple language
- Clearly distinguishable options

Each question forces a meaningful choice, avoiding overlap between options.

---

## 3. Branching Logic

Branching is deterministic and based on:

- Direct answer mapping
- Signal tagging (e.g., axis1:internal, axis2:contribution)

Decision nodes route the user into different paths depending on their responses.

This ensures:

- No ambiguity
- No randomness
- Full traceability

---

## 4. Psychological Grounding

The design is based on established frameworks:

- Locus of Control (Julian Rotter)
- Growth Mindset (Carol Dweck)
- Organizational Citizenship Behavior
- Self-Transcendence (Maslow)

The questions are designed to surface these dimensions without explicitly naming them.

---

## 5. AI Usage

AI tools were used as a support system for:

- Generating variations of questions
- Testing clarity
- Simulating different user personas

However, all outputs were reviewed and refined manually.

The final system does not rely on AI at runtime.

---

## 6. Controlling AI Hallucination

To prevent hallucination:

- No AI is used in the final product
- All responses are pre-defined
- The tree structure ensures deterministic outputs

Additionally, I avoided directly copying AI-generated content and validated psychological concepts.

---

## 7. Trade-offs

- Simplicity vs depth: kept questions simple for usability
- Limited number of nodes due to time constraint
- Signals are basic and could be expanded further

---

## 8. Future Improvements

- More nuanced signal weighting
- Personalized summaries
- UI-based interaction instead of static CLI
- Expanded question bank for variability

---

## Conclusion

This system demonstrates how structured decision trees can encode psychological insight into a deterministic and auditable reflection process.

It highlights the role of knowledge engineering in building reliable, non-LLM systems.
