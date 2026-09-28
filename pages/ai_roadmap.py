import streamlit as st


def show_ai_roadmap():

    st.title("🛣️ AI Roadmap")
    st.write(
        "Get a personalized learning roadmap based on your current skills."
    )

    st.divider()

    # ---------------------------------
    # Get student data
    # ---------------------------------

    profile = st.session_state.get("student_profile", {})

    if not profile:
        st.warning(
            "⚠️ Please complete your Student Profile first."
        )
        return

    name = profile.get("name", "Student")

    st.subheader(f"👋 Hello, {name}!")

    st.write(
        "Your roadmap is created according to your current skill levels."
    )

    # ---------------------------------
    # Skill data
    # ---------------------------------

    skills = {
        "Python": profile.get("Python", 0),
        "Java": profile.get("Java", 0),
        "DSA": profile.get("DSA", 0),
        "SQL": profile.get("SQL", 0),
        "Web Development": profile.get("Web Development", 0),
        "Communication": profile.get("Communication", 0)
    }

    # ---------------------------------
    # Display current skills
    # ---------------------------------

    st.subheader("📊 Your Current Skills")

    for skill, score in skills.items():

        col1, col2 = st.columns([3, 1])

        with col1:
            st.write(f"**{skill}**")
            st.progress(int(score))

        with col2:
            st.write(f"**{score}%**")

    st.divider()

    # ---------------------------------
    # Generate roadmap
    # ---------------------------------

    st.subheader("🤖 Personalized Roadmap")

    if st.button(
        "🚀 Generate My Roadmap",
        use_container_width=True
    ):

        weak_skills = {
            skill: score
            for skill, score in skills.items()
            if score < 60
        }

        strong_skills = {
            skill: score
            for skill, score in skills.items()
            if score >= 80
        }

        st.session_state["roadmap"] = weak_skills

        # ---------------------------------
        # Strong skills
        # ---------------------------------

        if strong_skills:

            st.success("🌟 Your Strong Skills")

            for skill, score in strong_skills.items():
                st.write(
                    f"✅ **{skill}** — {score}%"
                )

        # ---------------------------------
        # Weak skills
        # ---------------------------------

        if weak_skills:

            st.warning(
                "📚 These skills need more attention:"
            )

            for skill, score in weak_skills.items():

                st.write(
                    f"🔸 **{skill}** — {score}%"
                )

        else:

            st.success(
                "🎉 Great! You don't have any major weak areas."
            )

        st.divider()

        # ---------------------------------
        # Learning Roadmap
        # ---------------------------------

        st.subheader("🗓️ Recommended Learning Plan")

        roadmap_topics = {
            "Python": [
                "Python Basics",
                "Functions & OOP",
                "File Handling",
                "Libraries: NumPy & Pandas",
                "Python Interview Questions"
            ],

            "Java": [
                "Java Fundamentals",
                "OOP Concepts",
                "Exception Handling",
                "Collections Framework",
                "Java Interview Questions"
            ],

            "DSA": [
                "Arrays",
                "Strings",
                "Linked Lists",
                "Stacks & Queues",
                "Trees & Graphs",
                "Sorting & Searching"
            ],

            "SQL": [
                "SQL Basics",
                "SELECT & WHERE",
                "JOINs",
                "Subqueries",
                "Aggregate Functions",
                "SQL Interview Questions"
            ],

            "Web Development": [
                "HTML",
                "CSS",
                "JavaScript",
                "Responsive Design",
                "Frontend Projects"
            ],

            "Communication": [
                "Self Introduction",
                "Technical Vocabulary",
                "HR Interview Questions",
                "Speaking Practice",
                "Mock Interviews"
            ]
        }

        if weak_skills:

            for skill in weak_skills:

                st.markdown(
                    f"### 🔹 {skill}"
                )

                for i, topic in enumerate(
                    roadmap_topics.get(skill, []),
                    start=1
                ):

                    st.write(
                        f"{i}. {topic}"
                    )

        else:

            st.success(
                "🏆 Your skills are at a good level. "
                "Focus on advanced topics and mock interviews."
            )

        st.divider()

        # ---------------------------------
        # Weekly Plan
        # ---------------------------------

        st.subheader("📅 Suggested Weekly Plan")

        weekly_plan = [
            ("Monday", "DSA Practice", "1 hour"),
            ("Tuesday", "Python / Java", "1 hour"),
            ("Wednesday", "SQL & DBMS", "1 hour"),
            ("Thursday", "Coding Challenge", "1 hour"),
            ("Friday", "Interview Questions", "1 hour"),
            ("Saturday", "Mock Interview", "1 hour"),
            ("Sunday", "Revision & Progress Review", "1 hour")
        ]

        for day, activity, duration in weekly_plan:

            st.write(
                f"**{day}** → {activity} ⏱️ {duration}"
            )