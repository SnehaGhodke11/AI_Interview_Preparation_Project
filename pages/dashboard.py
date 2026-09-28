import streamlit as st
import matplotlib.pyplot as plt



def show_dashboard():

    st.title("📈 Student Dashboard")
    st.write("Track your interview preparation performance and skills.")

    st.divider()

    # ---------------------------------
    # Get stored data
    # ---------------------------------

    profile = st.session_state.get("student_profile", {})
    assessment_score = st.session_state.get("assessment_score", 0)

    name = profile.get("name", "Student")

    st.subheader(f"👋 Welcome, {name}!")

    # ---------------------------------
    # Performance Overview
    # ---------------------------------

    st.subheader("📊 Performance Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Assessment Score",
            f"{assessment_score:.0f}%"
        )

    with col2:
        st.metric(
            "Skills Evaluated",
            "6"
        )

    with col3:
        st.metric(
            "Interview Practice",
            "0"
        )


    st.divider()

    # ---------------------------------
    # Skill Performance
    # ---------------------------------

    st.subheader("💻 Skill Performance")

    skills = {
        "Python": profile.get("Python", 0),
        "Java": profile.get("Java", 0),
        "DSA": profile.get("DSA", 0),
        "SQL": profile.get("SQL", 0),
        "Web Development": profile.get("Web Development", 0),
        "Communication": profile.get("Communication", 0)
    }

    col1, col2 = st.columns([1, 1])

    with col1:

        for skill, score in skills.items():

            st.write(f"**{skill} — {score}%**")

            st.progress(int(score))

    # ---------------------------------
    # Skill Chart
    # ---------------------------------

    with col2:

        fig, ax = plt.subplots()

        ax.bar(
            list(skills.keys()),
            list(skills.values())
        )

        ax.set_ylabel("Skill Level (%)")
        ax.set_ylim(0, 100)
        ax.set_title("Skill Analysis")

        plt.xticks(
            rotation=45,
            ha="right"
        )

        plt.tight_layout()

        st.pyplot(fig)

    st.divider()

    # ---------------------------------
    # Overall Performance
    # ---------------------------------

    st.subheader("🎯 Overall Performance")

    if assessment_score >= 80:

        st.success(
            "🌟 Excellent performance! "
            "You are progressing very well."
        )

    elif assessment_score >= 50:

        st.warning(
            "👍 Good progress! "
            "Focus on improving your weaker skills."
        )

    else:

        st.info(
            "📚 Start practicing regularly "
            "to improve your interview readiness."
        )

    # ---------------------------------
    # Quick Actions
    # ---------------------------------

    st.subheader("⚡ Quick Actions")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.info("💡 Practice Interview Questions")

    with col2:
        st.info("🎯 Solve Coding Challenges")

    with col3:
        st.info("🛣️ Follow Your AI Roadmap")