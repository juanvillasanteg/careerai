# CareerAI Implementation Tasks

## MVP-First, UI-Driven Approach (2024-06-14)

### Phase 1: Foundation & Data (Completed)

- [x] Create GitHub repository for the project
- [x] Set up Python 3.12.10 development environment
- [x] Configure Ruff for linting and pytest for testing
- [x] Set up dependency management and virtual environment
- [x] Create project structure and documentation templates
- [x] Design JSON/YAML schema for resume data
- [x] Create sample resume data files for testing

### Phase 2: UI MVP (In Progress)

- [ ] Set up Streamlit app structure (see `src/app.py`)
- [x] Modularize app entrypoint to `src/main.py` for clarity and future expansion
- [x] Implement basic chat interface (user input, message display, chat history)
- [x] Add static profile/overview panel (placeholder)
- [x] Mock conversation responses (hardcoded for now)
- [x] Add session state for chat history

### Phase 3: Minimal Backend (Parallel)

- [ ] Set up minimal backend logic (can be a Python module or FastAPI endpoint)
- [ ] Prepare interface for connecting UI to backend (function or API call)
- [ ] Ensure backend can be swapped from mock to real AI agent easily

### Phase 4: Backend Integration

- [ ] Connect chat UI to backend (replace hardcoded responses)
- [ ] Integrate LangChain agent for basic Q&A using sample resume data
- [ ] Replace mock responses with real AI-powered answers

### Phase 5: Data & Features

- [ ] Load and display real resume data (JSON/YAML)
- [ ] Add question suggestions
- [ ] Implement resume download
- [ ] Add error handling and basic edge cases

### Phase 6: Polish & Expand

- [ ] Responsive/mobile tweaks
- [ ] Connect LinkedIn/GitHub (optional)
- [ ] Polish UI and UX

---

## Future/Optional Features

- Multi-language support
- Voice interface option
- Customizable agent personality
- Integration with job application systems
- Analytics for interview performance and common questions
- Advanced retrieval, chunking, and scoring
- System scaling and optimization

---

## Discovered During Work

- [ ] (Add new sub-tasks or TODOs here as they are discovered)
