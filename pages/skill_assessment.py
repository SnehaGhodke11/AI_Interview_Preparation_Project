import streamlit as st
import pandas as pd
import joblib
import os


# =========================================================
# PATHS
# =========================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(os.path.abspath(__file__))
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "career_recommendation_model.pkl"
)

ENCODER_PATH = os.path.join(
    BASE_DIR,
    "label_encoder.pkl"
)


# =========================================================
# LOAD MODEL
# =========================================================

@st.cache_resource
def load_model():

    model = joblib.load(MODEL_PATH)
    encoder = joblib.load(ENCODER_PATH)

    return model, encoder


# =========================================================
# PAGE
# =========================================================

def show_skill_assessment():

    st.title("📊 Skill Assessment")

    st.markdown(
        """
        ### 🎯 Assess Your Skills

        Rate each skill from **0 to 10**:

        - **0** = No knowledge
        - **1–2** = Beginner
        - **3–4** = Basic
        - **5–6** = Intermediate
        - **7–8** = Good
        - **9–10** = Excellent
        """
    )

    st.info(
        "💡 The AI model was trained using skill scores "
        "on a 0–10 scale, so please use the same scale here."
    )

    st.divider()

    # =====================================================
    # TECHNICAL SKILLS
    # =====================================================

    st.subheader("💻 Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:

        python = st.slider(
            "🐍 Python",
            0, 10, 0
        )

        java = st.slider(
            "☕ Java",
            0, 10, 0
        )

        sql = st.slider(
            "🗄️ SQL",
            0, 10, 0
        )

        html = st.slider(
            "🌐 HTML",
            0, 10, 0
        )

    with col2:

        cpp = st.slider(
            "⚙️ C++",
            0, 10, 0
        )

        dbms = st.slider(
            "🗃️ DBMS",
            0, 10, 0
        )

        javascript = st.slider(
            "📜 JavaScript",
            0, 10, 0
        )

    with col3:

        data_structures = st.slider(
            "🌳 Data Structures",
            0, 10, 0
        )

        problem_solving = st.slider(
            "🧠 Problem Solving",
            0, 10, 0
        )

        communication = st.slider(
            "🗣️ Communication",
            0, 10, 0
        )

    st.divider()

    # =====================================================
    # PREDICTION
    # =====================================================

    if st.button(
        "🔮 Predict My Career",
        type="primary",
        use_container_width=True
    ):

        # =================================================
        # INPUT VALUES
        # =================================================

        skill_values = [
            python,
            java,
            sql,
            html,
            cpp,
            problem_solving,
            dbms,
            javascript,
            data_structures,
            communication
        ]

        total_score = sum(skill_values)
        average_score = total_score / 10
        percentage = (total_score / 100) * 100

        # =================================================
        # CASE 1: ALL ZERO
        # =================================================

        if total_score == 0:

            st.error(
                "❌ Career recommendation is not possible."
            )

            st.warning(
                "You have rated every skill as 0."
            )

            st.info(
                "Please develop some basic skills first "
                "and then take the assessment again."
            )

            return

        # =================================================
        # CASE 2: TOO LOW
        # =================================================

        if average_score < 2.5:

            st.warning(
                "⚠️ Your current skill level is below "
                "the range used to train the AI model."
            )

            st.write(
                f"Your average skill score: "
                f"**{average_score:.2f}/10**"
            )

            st.info(
                "📚 Improve your basic technical skills "
                "before requesting an AI career recommendation."
            )

            return

        # =================================================
        # CREATE DATAFRAME
        # =================================================

        input_data = pd.DataFrame({

            "Python": [python],

            "Java": [java],

            "SQL": [sql],

            "HTML": [html],

            "C++": [cpp],

            "Problem_Solving": [problem_solving],

            "DBMS": [dbms],

            "JavaScript": [javascript],

            "Data_Structures": [data_structures],

            "Communication": [communication]

        })

        # =================================================
        # LOAD MODEL
        # =================================================

        try:

            model, encoder = load_model()

        except FileNotFoundError:

            st.error(
                "❌ Model files were not found."
            )

            st.info(
                "Make sure these files are in the "
                "same folder as app.py:"
            )

            st.code(
                "career_recommendation_model.pkl\n"
                "label_encoder.pkl"
            )

            return

        # =================================================
        # PREDICT
        # =================================================

        prediction = model.predict(input_data)

        predicted_career = encoder.inverse_transform(
            prediction
        )[0]

        probabilities = model.predict_proba(
            input_data
        )[0]

        # =================================================
        # TOP 3
        # =================================================

        top_indices = probabilities.argsort()[
            -3:
        ][::-1]

        # =================================================
        # RESULT
        # =================================================

        st.divider()

        st.subheader(
            "🎯 AI Career Recommendation"
        )

        st.success(
            f"Recommended Career: "
            f"**{predicted_career}**"
        )

        # =================================================
        # SCORE SUMMARY
        # =================================================

        st.subheader(
            "📊 Your Skill Summary"
        )

        c1, c2, c3 = st.columns(3)

        with c1:
            st.metric(
                "Total Score",
                f"{total_score}/100"
            )

        with c2:
            st.metric(
                "Average",
                f"{average_score:.1f}/10"
            )

        with c3:
            st.metric(
                "Skill Level",
                f"{percentage:.0f}%"
            )

        st.divider()

        # =================================================
        # TOP 3 CAREERS
        # =================================================

        st.subheader(
            "🏆 Top 3 Career Recommendations"
        )

        for rank, index in enumerate(
            top_indices,
            start=1
        ):

            career_name = encoder.inverse_transform(
                [index]
            )[0]

            probability = probabilities[index]

            st.markdown(
                f"### {rank}. {career_name}"
            )

            st.progress(
                float(probability)
            )

            st.caption(
                f"Prediction probability: "
                f"{probability:.2%}"
            )

        # =================================================
        # SAVE RESULTS
        # =================================================

        st.session_state[
            "predicted_career"
        ] = predicted_career

        st.session_state[
            "career_probabilities"
        ] = probabilities

        st.session_state[
            "skill_score"
        ] = total_score

        st.session_state[
            "skill_percentage"
        ] = percentage

        st.session_state[
            "skill_assessment_completed"
        ] = True

        # =================================================
        # FEEDBACK
        # =================================================

        if percentage < 40:

            st.warning(
                "⚠️ Your skills are still developing. "
                "Follow the AI Roadmap to improve."
            )

        elif percentage < 70:

            st.info(
                "📚 Good start! Continue practicing "
                "to become career-ready."
            )

        else:

            st.success(
                "🚀 Strong skill profile! "
                "Now practice interview questions "
                "and coding challenges."
            )