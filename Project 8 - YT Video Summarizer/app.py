import streamlit as st
from dotenv import load_dotenv
load_dotenv()

import os
import google.generativeai as genai
from youtube_transcript_api import YouTubeTranscriptApi

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """
You are a YouTube video summarizer. Summarize the transcript in 250 words.
Return the points in bullet format.
"""

# ------------------- Extract Transcript -------------------
def extract_transcript_details(video_id):
    try:
        # Try English first, then Hindi if English not available
        transcript = YouTubeTranscriptApi().fetch(video_id, languages=['en', 'hi'])
        transcript_text = " ".join([item.text for item in transcript])
        return transcript_text
    except Exception as e:
        raise e


# ------------------- Gemini Response -------------------
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("models/gemini-2.0-flash")
    response = model.generate_content(prompt + transcript_text)
    return response.text


# ------------------- Streamlit UI -------------------
st.title("🎥 YouTube Video Summarizer using Gemini")

youtube_link = st.text_input("Enter YouTube Video Link:")

# Extract video ID
def get_video_id(link):
    if "v=" in link:
        return link.split("v=")[1]
    elif "youtu.be/" in link:
        return link.split("youtu.be/")[1]
    else:
        return None


if youtube_link:
    video_id = get_video_id(youtube_link)
    if video_id:
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

if st.button("Generate Summary"):
    video_id = get_video_id(youtube_link)

    if not video_id:
        st.error("Invalid YouTube link.")
    else:
        transcript_text = extract_transcript_details(video_id)

        if transcript_text:
            st.session_state.transcript = transcript_text
            summary = generate_gemini_content(transcript_text, prompt)
            st.subheader("📌 Video Summary")
            st.write(summary)

# ------------------- Chat with Video -------------------
if 'transcript' in st.session_state:
    st.subheader("💬 Ask Questions About This Video")
    
    user_question = st.text_input("Ask a question about the video:")
    
    if st.button("Ask") and user_question:
        chat_prompt = f"Based on this video transcript: {st.session_state.transcript}\n\nQuestion: {user_question}\n\nAnswer:"
        answer = generate_gemini_content("", chat_prompt)
        st.write("**Answer:**")
        st.write(answer)
