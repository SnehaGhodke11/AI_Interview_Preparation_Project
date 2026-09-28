import streamlit as st

from modules.questions import question_bank
from modules.interview_logic import get_random_questions


def show_interview_questions():

    st.title("💡 Interview Questions")

    st.write(
        "Practice technical interview questions topic-wise "
        "and improve your interview preparation."
    )

    st.divider()

    # ---------------------------------------------
    # Select Topic
    # ---------------------------------------------

    st.subheader("📚 Select Topic")

    topic = st.selectbox(
        "Choose a topic:",
        list(question_bank.keys())
    )

    # ---------------------------------------------
    # Practice Settings
    # ---------------------------------------------

    st.divider()

    st.subheader("🎯 Practice Mode")

    col1, col2 = st.columns(2)

    with col1:

        number_of_questions = st.selectbox(
            "Number of Questions",
            [5, 10]
        )

    with col2:

        difficulty = st.selectbox(
            "Difficulty",
            ["Easy", "Medium", "Hard"]
        )

    st.write(
        f"**Topic:** {topic}  \n"
        f"**Difficulty:** {difficulty}"
    )

    # ---------------------------------------------
    # Generate Questions
    # ---------------------------------------------

    if st.button(
        "🎲 Generate Questions",
        use_container_width=True
    ):

        selected_questions = get_random_questions(
            question_bank,
            topic,
            number_of_questions
        )

        st.session_state["interview_questions"] = (
            selected_questions
        )

        st.session_state["interview_topic"] = topic

        st.session_state["interview_difficulty"] = difficulty

    # ---------------------------------------------
    # Display Questions
    # ---------------------------------------------

    if st.session_state.get("interview_questions"):

        st.divider()

        st.subheader(
            f"💡 {st.session_state.get('interview_topic', topic)} Questions"
        )

        questions = st.session_state["interview_questions"]

        # -----------------------------------------
        # Display Each Question
        # -----------------------------------------

        for i, question in enumerate(
            questions,
            start=1
        ):

            st.write(
                f"### Q{i}. {question}"
            )

            st.text_area(
                "✍️ Write your answer:",
                key=f"interview_answer_{i}",
                placeholder="Type your answer here..."
            )

        st.divider()

        # -----------------------------------------
        # Finish Practice
        # -----------------------------------------

        if st.button(
            "✅ Finish Practice",
            use_container_width=True
        ):

            unanswered = []

            # Check every question
            for i in range(1, len(questions) + 1):

                answer = st.session_state.get(
                    f"interview_answer_{i}",
                    ""
                ).strip()

                if not answer:
                    unanswered.append(i)

            # -------------------------------------
            # If questions are unanswered
            # -------------------------------------

            if unanswered:

                question_numbers = ", ".join(
                    map(str, unanswered)
                )

                st.warning(
                    f"✍️ Please write your answer for "
                    f"Question {question_numbers} "
                    f"before finishing the practice."
                )

            # -------------------------------------
            # If all questions are answered
            # -------------------------------------

            else:

                st.success(
                    "🎉 Practice session completed successfully!"
                )

                st.info(
                    "💡 Great! Review your answers and "
                    "continue with another topic."
                )