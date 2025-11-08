import os
import streamlit as st
from dotenv import load_dotenv
from google import genai

load_dotenv()

# Backend

client = genai.Client()


def readme_generator(repo_url):
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"""
Generate a professional, high-quality README.md file for the project at the following repository URL: {repo_url}. 

Include the following sections if applicable:

1. Project Title  
2. Description  
3. Features  
4. Installation  
5. Usage  
6. Configuration (if applicable)  
7. Examples (if applicable)  
8. API Documentation (if applicable)  
9. Contributing  
10. License  
11. Contact / Author  

Use proper markdown formatting, headings, badges (like build, license, version), and code blocks for commands or code snippets. Make the content clear, concise, and professional.  

**Output only the README.md content. Do not include any explanations, instructions, or extra text.**  

""",
    )
    return response.text


# UI
st.title("Codebase Genius – an Agentic Code‑DocumentationSystem")
repo_link = st.text_input("Enter GitHub repo link:", placeholder="https://github.com/username/repo.git")
button = st.button('Generate Documentation')

if button:
    if repo_link == "":
        st.warning("Repo link cannot be empty")
    elif not (repo_link.startswith("https://github.com") and repo_link.endswith(".git")):
        st.warning("Enter a valid GitHub repository URL (e.g., https://github.com/username/repo.git)")
    else:
        ai_response = readme_generator(repo_link)
        st.code(ai_response, language="markdown")
        st.download_button(
            label="Download README.md",
            data=ai_response,
            file_name="README.md",
            on_click="ignore",
            type="primary",
        )
