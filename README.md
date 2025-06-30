# Gemini Flash Hashtag Generator

A Python tool that uses Google's Gemini 1.5 Flash model to generate relevant hashtags for social media captions. Perfect for content creators, marketers, and social media managers to automate hashtag creation.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
  - [Command-Line Example](#command-line-example)
  - [Sample Output](#sample-output)
- [Requirements](#requirements)
- [Dependencies](#dependencies)
- [Important Notes](#important-notes)
- [License](#license)

---

## Overview

The Gemini Flash Hashtag Generator leverages the Google Generative AI API to produce a specified number of hashtags based on a given caption. It includes logging for process tracking and execution time measurement, making it suitable for social media content automation.

---

## Features

- Generates user-defined number of hashtags using Gemini 1.5 Flash.
- Securely loads Google API key from a `.env` file.
- Accepts caption and hashtag count via command-line arguments.
- Logs timestamps for each processing step.
- Displays total execution time for performance tracking.

---

## Project Structure

hash_generator/
├── .env                # Stores Google API key
├── main.py             # Core script for hashtag generation
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation


---

## Installation

Follow these steps to set up the project:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/hash_generator.git
   cd hash_generator

Set Up a Virtual Environment (optional, recommended):

```bash
   python3.10 -m venv venv
   source venv/bin/activate  # macOS/Linux
   venv\Scripts\activate     # Windows
```

Install Dependencies:
```bash
   pip install -r requirements.txt
```

Configure the API Key:
```bash
   Create a .env file in the project root.
```

Add your Google API key:
```bash
GOOGLE_API_KEY=your_actual_gemini_api_key_here
```

Usage
Run the script from the command line, providing a caption and the number of hashtags to generate.
Command-Line Example
```bash
python main.py "Exploring the ancient ruins of Hampi" 10
```

This command generates 10 hashtags for the given caption, displaying them with timestamps and execution time.
Sample Output
```bash
[2025-06-30 16:05:12] Starting program
[2025-06-30 16:05:12] Loading .env file...
[2025-06-30 16:05:12] Configuring Gemini with API key...
[2025-06-30 16:05:12] Initializing Gemini Flash model...
[2025-06-30 16:05:12] Preparing prompt for caption
[2025-06-30 16:05:12] Sending prompt to Gemini...
[2025-06-30 16:05:13] Received response from Gemini (Time taken: 1.62 sec)

Caption: Exploring the ancient ruins of Hampi

Hashtags:
#Hampi #TravelIndia #AncientRuins #HistoricalSites #Wanderlust
#BackpackingIndia #IncredibleIndia #CulturalHeritage #AdventureTravel #HiddenGems

[2025-06-30 16:05:13] Program completed. Total time taken: 1.63 seconds
```

Requirements
```bash
Python 3.10 or higher
```
Access to Google Generative AI API

Valid API key for Gemini 1.5 Flash model

Dependencies
```bash
google-generativeai

python-dotenv
```
Install them using:
```bash
pip install -r requirements.txt
```
Important Notes
Security: Add .env to .gitignore to prevent exposing your API key in version control.

API Usage: Be aware of Google API quotas or billing, depending on your account.

Customization: For integrations like Streamlit, Flask, or GitHub Pages, contact the maintainer for tailored guidance.

License
This project is licensed under the MIT License (LICENSE).


---

### Improvements Made
1. **Structured Headings**:
   - Used a clear hierarchy with `#` for the main title, `##` for primary sections, and `###` for subsections.
   - Added horizontal lines (`---`) to visually separate major sections.
   - Included a concise **Overview** section to introduce the project.
2. **Enhanced Table of Contents**:
   - Linked all sections for easy navigation.
   - Nested subsections (e.g., Command-Line Example, Sample Output) under Usage.
3. **Consistent Formatting**:
   - Standardized code blocks with triple backticks and `bash` or plain text as needed.
   - Used bullet points for lists and bold text for key instructions.
4. **Streamlined Content**:
   - Condensed repetitive information while keeping all critical details.
   - Organized installation steps numerically for clarity.
5. **Professional and Clear**:
   - Adopted a professional yet approachable tone.
   - Grouped related information (e.g., Requirements and Dependencies) for logical flow.

### Notes for You
- Replace `your-username` in the clone command with your actual GitHub username.
- If you don’t have a `LICENSE` file, create one for the MIT License or remove the license link.
- The dataset context from earlier (e.g., `instagram-images-with-captions`) isn’t referenced here, as the `README` is for the Gemini-based project. If you want a `README` for the transformer-based hashtag generator (with the dataset), I can create a separate version.
- For Streamlit, Flask, or GitHub Pages integration, let me know, and I can provide a customized `README` or additional code.

