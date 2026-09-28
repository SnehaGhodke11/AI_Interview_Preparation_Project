import streamlit as st
import matplotlib.pyplot as plt


def show_progress_tracker():

    st.title("📌 Progress Tracker")
    st.write(
        "Track your interview preparation journey and monitor your improvement."
    )

    st.divider()

    # ---------------------------------
    # Get stored data
    # ---------------------------------

    profile = st.session_state.get("student_profile", {})

    assessment_score = st.session_state.get(
        "assessment_score",
        0
    )
    name = profile.get(
        "name",
        "Student"
    )

    # ---------------------------------
    # Progress Overview
    # ---------------------------------

    st.subheader(f"📊 {name}'s Progress")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Assessment Score",
            f"{assessment_score:.0f}%"
        )


    with col3:
        st.metric(
            "Skills Tracked",
            "6"
        )

    with col4:

        if assessment_score >= 80:
            level = "Advanced"
        elif assessment_score >= 50:
            level = "Intermediate"
        else:
            level = "Beginner"

        st.metric(
            "Current Level",
            level
        )

    st.divider()

    # ---------------------------------
    # Skill Progress
    # ---------------------------------

    st.subheader("💻 Skill Progress")

    skills = {
        "Python": profile.get("Python", 0),
        "Java": profile.get("Java", 0),
        "DSA": profile.get("DSA", 0),
        "SQL": profile.get("SQL", 0),
        "Web Development": profile.get(
            "Web Development",
            0
        ),
        "Communication": profile.get(
            "Communication",
            0
        )
    }

    for skill, score in skills.items():

        st.write(
            f"**{skill}: {score}%**"
        )

        st.progress(
            int(score)
        )

    st.divider()

    # ---------------------------------
    # Progress Chart
    # ---------------------------------

    st.subheader("📈 Skill Progress Chart")

    fig, ax = plt.subplots()

    ax.bar(
        skills.keys(),
        skills.values()
    )

    ax.set_ylabel("Progress (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Your Current Skill Levels")

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    st.pyplot(fig)

    st.divider()

    # ---------------------------------
    # Goals
    # ---------------------------------

    st.subheader("🎯 Your Goals")

    col1, col2 = st.columns(2)

    with col1:

        st.write("### 📚 Learning Goals")

        python_goal = st.checkbox(
            "Complete Python revision"
        )

        dsa_goal = st.checkbox(
            "Practice DSA daily"
        )

        sql_goal = st.checkbox(
            "Complete SQL practice"
        )

    with col2:

        st.write("### 💼 Interview Goals")

        interview_goal = st.checkbox(
            "Practice interview questions"
        )

        coding_goal = st.checkbox(
            "Solve coding challenges"
        )

        mock_goal = st.checkbox(
            "Complete a mock interview"
        )

    # ---------------------------------
    # Goal Progress
    # ---------------------------------

    completed_goals = sum([
        python_goal,
        dsa_goal,
        sql_goal,
        interview_goal,
        coding_goal,
        mock_goal
    ])

    total_goals = 6

    goal_percentage = (
        completed_goals / total_goals
    ) * 100

    st.divider()

    st.subheader("🏆 Goal Completion")

    st.progress(
        int(goal_percentage)
    )

    st.write(
        f"**{completed_goals}/{total_goals} goals completed "
        f"({goal_percentage:.0f}%)**"
    )

    if goal_percentage == 100:

        st.success(
            "🎉 Amazing! You completed all your goals!"
        )

    elif goal_percentage >= 50:

        st.info(
            "🔥 Great progress! Keep going."
        )

    else:

        st.warning(
            "💪 Start completing your goals one by one."
        )