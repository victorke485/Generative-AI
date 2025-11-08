# Architecture Overview

## Goal
Provide a simple UI for generating high-quality README documentation using a hosted Gemini model.

## Component Diagram (Conceptual)
```
+------------------+        +-----------------------+
|  User Browser    | --->   |   Streamlit App       |  (main.py)
+------------------+        |  - Input form         |
                            |  - Output renderer    |
                            +-----------+-----------+
                                        |
                                        v
                            +-----------------------+
                            |  Prompt Builder       |
                            |  (static template)    |
                            +-----------+-----------+
                                        |
                                        v
                            +-----------------------+
                            |  Gemini API Client    |
                            |  (google.genai)       |
                            +-----------+-----------+
                                        |
                                        v
                            +-----------------------+
                            |  Generated Markdown   |
                            |  (display + download) |
                            +-----------------------+
```

## Data Flow
1. User enters repository URL.
2. `readme_generator(repo_url)` injects URL into a multi-section prompt.
3. Gemini model `gemini-2.5-flash` generates markdown text.
4. Streamlit displays the result with syntax highlighting.
5. User can download the README as a file.

## Key Function
`readme_generator(repo_url)`
- Input: string (GitHub repository URL)
- Output: string (markdown)
- Errors: Network issues, invalid API key, rate limits.

## Configuration
- `.env` provides `GOOGLE_API_KEY` loaded via `load_dotenv()`.

## Extensibility Ideas
- Add repository preprocessing (clone + analyze code structure)
- Integrate GitHub API for stats (stars, forks, open issues)
- Support multiple documentation templates
- Add retry + exponential backoff for transient API errors
- Provide model switching UI

## Operational Considerations
- Rate limiting: handle HTTP 429 with user messaging.
- Timeout handling: consider wrapping call with custom timeout if needed.
- Caching: simple in-memory or filesystem cache keyed by repo URL.

## Security
- Never expose raw API key in UI.
- Encourage users to use separate restricted key.

## Testing Suggestions
- Unit test prompt assembly.
- Mock Gemini client for deterministic output.
- UI tests for empty input, invalid URL, slow responses.

## Future Enhancements
- Multi-file doc pack (README, ARCHITECTURE, API_REFERENCE)
- Localization (multi-language generation)
- CLI wrapper for headless generation.
