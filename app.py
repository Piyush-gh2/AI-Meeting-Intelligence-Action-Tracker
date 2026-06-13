import streamlit as st

from src.parser import load_transcript
from src.summarizer import generate_summary
from src.action_items import extract_action_items
from src.risk_detector import detect_risks

st.title("🎙️ AI Meeting Intelligence & Action Tracker")

transcript = load_transcript(
    "data/meeting_transcript.txt"
)

st.subheader("Meeting Transcript")

st.text_area(
    "Transcript",
    transcript,
    height=250
)

if st.button("Analyze Meeting"):

    summary = generate_summary(transcript)

    st.subheader("📝 Meeting Summary")

    for item in summary:
        st.write(item)

    actions = extract_action_items(transcript)

    st.subheader("✅ Action Items")

    for action in actions:
        st.write(action)

    risks = detect_risks(transcript)

    st.subheader("⚠️ Risks & Blockers")

    for risk in risks:
        st.write(risk)