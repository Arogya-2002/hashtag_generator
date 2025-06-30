import os
import sys
import time
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

# Step 1: Track overall start time
start_time = time.time()
print(f"[{datetime.now()}] Starting program")

# Step 2: Load environment variables
print(f"[{datetime.now()}] Loading .env file...")
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(" GOOGLE_API_KEY not found in .env file")

# Step 3: Configure Gemini API
print(f"[{datetime.now()}] Configuring Gemini with API key...")
genai.configure(api_key=GOOGLE_API_KEY)

# Step 4: Initialize the Gemini model
print(f"[{datetime.now()}] Initializing Gemini Flash model...")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_hashtags(caption: str, k: int):
    print(f"[{datetime.now()}] Preparing prompt for caption")
    prompt = f"""Generate exactly {k} relevant and trendy hashtags for the following caption.
Return only the hashtags separated by spaces, without any explanation or numbering.

Caption: "{caption}"
Hashtags:"""

    print(f"[{datetime.now()}] Sending prompt to Gemini...")
    t1 = time.time()
    response = model.generate_content(prompt)
    t2 = time.time()
    print(f"[{datetime.now()}] Received response from Gemini (Time taken: {t2 - t1:.2f} sec)")

    if response.text:
        hashtags = response.text.strip().replace("\n", " ")
        print(f"\nCaption: {caption}")
        print(f"\n Hashtags:\n{hashtags}")
    else:
        print(" Failed to get hashtags.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python main.py <caption> <k>")
    else:
        caption_input = sys.argv[1]
        try:
            k_input = int(sys.argv[2])
            generate_hashtags(caption_input, k_input)
        except ValueError:
            print("Error: <k> should be an integer.")

    # Step 5: End time and total duration
    end_time = time.time()
    total_duration = end_time - start_time
    print(f"\n[{datetime.now()}] Program completed. Total time taken: {total_duration:.2f} seconds")
