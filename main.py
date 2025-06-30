import os
import sys
import time
from datetime import datetime
import google.generativeai as genai
from dotenv import load_dotenv

def initialize_gemini():
    """
    Load API key from .env and initialize Gemini Flash model.
    Returns:
        model: Configured Gemini model object
    """
    print(f"[{datetime.now()}] Loading .env file...")
    load_dotenv()
    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not found in .env file")

    print(f"[{datetime.now()}] Configuring Gemini with API key...")
    genai.configure(api_key=GOOGLE_API_KEY)

    print(f"[{datetime.now()}] Initializing Gemini Flash model...")
    model = genai.GenerativeModel("gemini-1.5-flash")
    return model

def generate_hashtags(model, caption: str, k: int):
    """
    Sends caption to Gemini and gets 'k' hashtags.
    Args:
        model: Gemini model object
        caption (str): Caption for which hashtags are to be generated
        k (int): Number of hashtags
    """
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
        print(f"\nHashtags:\n{hashtags}")
    else:
        print("Failed to get hashtags.")

def main():
    start_time = time.time()
    print(f"[{datetime.now()}] Starting program")

    if len(sys.argv) != 3:
        print("Usage: python main.py <caption> <k>")
    else:
        caption_input = sys.argv[1]
        try:
            k_input = int(sys.argv[2])
            model = initialize_gemini()
            generate_hashtags(model, caption_input, k_input)
        except ValueError:
            print("Error: <k> should be an integer.")

    end_time = time.time()
    total_duration = end_time - start_time
    print(f"\n[{datetime.now()}] Program completed. Total time taken: {total_duration:.2f} seconds")

if __name__ == "__main__":
    main()
