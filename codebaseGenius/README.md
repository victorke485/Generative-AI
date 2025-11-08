<div align="center">

# Codebase Genius – Agentic Code Documentation System

Generate high‑quality, professional README files for any public repository using Google's Gemini models through a simple Streamlit interface.

![Status](https://img.shields.io/badge/status-active-success) ![Python](https://img.shields.io/badge/python-3.10+-blue) ![Streamlit](https://img.shields.io/badge/Framework-Streamlit-ff4b4b) ![License](https://img.shields.io/badge/license-TBD-lightgrey)

</div>

## Table of Contents
- [Codebase Genius – Agentic Code Documentation System](#codebase-genius--agentic-code-documentation-system)
  - [Table of Contents](#table-of-contents)
  - [Overview](#overview)
  - [Features](#features)
  - [Architecture](#architecture)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Examples](#examples)
  - [Extensibility](#extensibility)
  - [Contributing](#contributing)
  - [Roadmap](#roadmap)
  - [FAQ](#faq)
  - [License](#license)
  - [Acknowledgments](#acknowledgments)

## Overview
Codebase Genius is a lightweight tool that leverages Google's Generative AI (Gemini) to auto‑generate professional documentation (README.md) for GitHub repositories. Provide a repository URL and receive well‑structured markdown with sections such as description, features, installation, usage, and more.

## Features
- 🔮 Automated README generation using Gemini models
- 🖥️ Simple, responsive Streamlit UI
- 🧩 Structured section templates (features, install, usage, examples, API, contributing, license)
- 🔐 Environment-based configuration (API key management via `.env`)
- 📥 One‑click download of the generated README
- 🛠 Easily extensible prompt for custom sections

## Architecture
See detailed architecture in `docs/architecture.md`.

High level:
| Layer | Purpose |
|-------|---------|
| UI (Streamlit) | Accepts repo URL input; displays generated markdown and download button |
| Prompt Builder | Static multi‑section template injected with user repo URL |
| Gemini Client | Calls `models.generate_content` on `gemini-2.5-flash` |
| Output Renderer | Formats AI response in a code block and enables download |

## Prerequisites
- Python 3.10+
- A Google AI Studio / Gemini API key (exported as environment variable)
- Internet access

## Installation
```bash
git clone https://github.com/victorke485/Generative-AI.git
cd Generative-AI/codebaseGenius

# (Optional) create virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Configuration
Create a `.env` file (or copy from `.env.example`) and set:
```
GOOGLE_API_KEY=your_api_key_here
```
The app loads environment variables via `python-dotenv`.

## Usage
Run the Streamlit app:
```bash
streamlit run main.py
```
Steps:
1. Enter a public GitHub repository URL (e.g. `https://github.com/psf/requests`).
2. Click "Generate Documentation".
3. Review the AI‑generated README.
4. Download the file if satisfied.

## Examples
Sample prompt (internal):
```text
Generate a professional, high-quality README.md file for the project at the following repository URL: <repo_url> ...
```
Example output sections include: Title, Description, Features, Installation, Usage, Configuration, Contributing, License.

## Extensibility
You can customize the prompt in `main.py` (`readme_generator`) to:
- Add badges (tests, coverage, Docker pulls)
- Include API reference parsing
- Inject repository metrics (stars, issues) via GitHub API pre‑processing

## Contributing
Contributions welcome! Please read `CONTRIBUTING.md` for guidelines (branch naming, PR style, commit messages).

## Roadmap
- [ ] Add GitHub API integration for dynamic stats
- [ ] Support multi‑file documentation bundle (ARCHITECTURE, API, CHANGELOG)
- [ ] Add model selection (flash / pro / thinking)
- [ ] Add template customization UI
- [ ] Caching for previously generated READMEs

## FAQ
**Does it modify the target repo?** No, it only generates markdown locally.

**Is output always accurate?** It relies on model inference; validate critical technical claims.

**Can I use private repos?** Only if you extend the app to clone and analyze locally; current version just forwards the URL.

## License
License is currently TBD. Recommend adding an OSI‑approved license (e.g., MIT) in a `LICENSE` file.

## Acknowledgments
- Google Gemini API
- Streamlit
- `.env` management via `python-dotenv`

---
For questions or support, open an issue or reach out to the repository owner.

