import streamlit as st

def show_home():
    st.title("🤖 AI Interview Preparation System")
    st.subheader("Welcome to your AI-powered interview practice platform!")

    st.write("""
    Prepare for technical interviews with AI-driven assessments, coding challenges,
    personalized roadmaps, and progress tracking—all in one place.
    """)

    st.divider()

    st.subheader("✨ Features")

    col1, col2 = st.columns(2)

    with col1:
        st.info("👤 **Student Profile**\n\nCreate and manage your profile.")
        st.info("📊 **Skill Assessment**\n\nAnalyze your technical skills.")
        st.info("🛣️ **AI Roadmap**\n\nGet a personalized learning roadmap.")

    with col2:
        st.info("💡 **Interview Questions**\n\nPractice topic-wise interview questions.")
        st.info("📌 **Progress Tracker**\n\nMonitor your improvement over time.")
        st.info("📊 **Dashboard**\n\nView your performance, scores, and overall progress.")
    st.divider()

    st.success("🚀 Start by creating your profile and taking a skill assessment!")