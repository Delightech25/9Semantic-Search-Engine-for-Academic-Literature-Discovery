# Semantic Search Engine for Academic Literature Discovery

An advanced semantic search and information retrieval engine designed to help researchers discover, query, and explore academic literature beyond traditional keyword matching. By leveraging Natural Language Processing (NLP) embeddings and vector search, this tool connects researchers with relevant research papers based on conceptual meaning rather than exact keyword overlap.

---

## Features & Architecture

* **Semantic Search Engine**: Integrates with a custom core model module (`model.py`) to perform vector-based semantic searches using advanced NLP embeddings[cite: 4, 5].
* **User Authentication**: Features secure user registration, login workflows, and session management using local JSON storage (`users.json`)[cite: 4, 5].
* **Interactive Dashboard**: Provides a protected dashboard interface where authenticated users can input natural language queries and instantly render semantic search results.

---

## Project Structure

```text
├── app_2.py          # Main Flask application and routing logic
├── model.py          # NLP embedding and vector search backend
├── users.json        # Local storage for user credentials and sessions
├── templates/        # HTML templates (Login, Register, Dashboard)
└── static/           # CSS stylesheets and assets
