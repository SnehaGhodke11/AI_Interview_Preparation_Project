# =========================================================
# UTILITY FUNCTIONS
# =========================================================

import streamlit as st


def initialize_session_state():
    """
    Initialize all required Streamlit session-state variables.
    """

    defaults = {
        "student_profile": {},
        "assessment_score": 0,
        "interview_questions": [],
        "interview_topic": "",
        "coding_attempts": 0,
        "roadmap": {},
        "completed_goals": [],
        "interview_history": [],
        "coding_history": []
    }

    for key, value in defaults.items():

        if key not in st.session_state:
            st.session_state[key] = value


def save_student_profile(profile):
    """
    Save student profile information.
    """

    st.session_state["student_profile"] = profile


def get_student_profile():
    """
    Return the saved student profile.
    """

    return st.session_state.get(
        "student_profile",
        {}
    )


def save_assessment_score(score):
    """
    Save the latest assessment score.
    """

    st.session_state["assessment_score"] = score


def get_assessment_score():
    """
    Get the latest assessment score.
    """

    return st.session_state.get(
        "assessment_score",
        0
    )


def add_coding_attempt(problem, language):
    """
    Store a coding challenge attempt.
    """

    st.session_state["coding_attempts"] = (
        st.session_state.get(
            "coding_attempts",
            0
        ) + 1
    )

    st.session_state["coding_history"].append({
        "problem": problem,
        "language": language
    })


def get_coding_attempts():
    """
    Return number of coding attempts.
    """

    return st.session_state.get(
        "coding_attempts",
        0
    )


def add_interview_result(topic, score):
    """
    Store an interview result.
    """

    st.session_state["interview_history"].append({
        "topic": topic,
        "score": score
    })


def get_interview_history():
    """
    Return interview history.
    """

    return st.session_state.get(
        "interview_history",
        []
    )


def get_skill_scores(profile):
    """
    Extract skill scores from the student profile.
    """

    return {
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


def get_performance_level(score):
    """
    Return performance level from score.
    """

    if score >= 80:
        return "Advanced"

    elif score >= 60:
        return "Intermediate"

    elif score >= 40:
        return "Beginner"

    return "Needs Improvement"


def format_percentage(value):
    """
    Format a number as a percentage.
    """

    return f"{value:.0f}%"


def show_page_header(title, description=None):
    """
    Display a consistent page header.
    """

    st.title(title)

    if description:
        st.write(description)

    st.divider()