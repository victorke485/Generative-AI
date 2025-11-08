# Contributing to Codebase Genius

Thanks for your interest in contributing! This guide outlines the process to propose changes.

## Development Setup
1. Fork the repository and clone your fork.
2. Create a virtual environment and install dependencies:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Create a feature branch:
   ```bash
   git checkout -b feat/short-description
   ```

## Commit Convention
- Use conventional commits:
  - feat: new feature
  - fix: bug fix
  - docs: documentation only changes
  - refactor: code change that neither fixes a bug nor adds a feature
  - chore: build process or auxiliary tool changes

## Pull Request
- Provide a clear description and screenshots (if UI changes)
- Reference related issues (e.g., "Closes #123")
- Ensure the app starts: `streamlit run main.py`

## Code Style
- Keep functions small and focused
- Add type hints where reasonable
- Handle errors gracefully with user-friendly messages

## Testing
- Mock external API calls where possible
- Test edge cases: empty input, invalid URLs, network errors

## Security
- Do not commit real API keys. Use `.env` with placeholders.

Thank you for helping improve Codebase Genius!
