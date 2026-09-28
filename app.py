import streamlit as st
import base64
import os
import textwrap

from pages.student_profile import show_student_profile
from pages.skill_assessment import show_skill_assessment
from pages.dashboard import show_dashboard
from pages.ai_roadmap import show_ai_roadmap
from pages.interview_questions import show_interview_questions
from pages.progress_tracker import show_progress_tracker

st.set_page_config(
    page_title="AI Interview Preparation",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
#MainMenu, footer {
    visibility: hidden;
}

header[data-testid="stHeader"] {
    background: #061e25 !important;
}

.stApp {
    background: #061e25 !important;
    color: white !important;
}

.main .block-container {
    padding-top: 1.2rem !important;
    padding-bottom: 2rem !important;
}

h1, h2, h3, h4, h5, h6 {
    color: white !important;
}

/* Hide duplicate st.title() from module files */
h1 {
    display: none !important;
}

[data-testid="stMarkdownContainer"] p {
    color: #f2fbfc !important;
}

section[data-testid="stSidebar"] {
    background: #08343d !important;
    border-right: 1px solid #155966 !important;
}

section[data-testid="stSidebar"] > div {
    padding: 25px 18px !important;
}

[data-testid="stSidebarNav"] {
    display: none !important;
}

.sidebar-title {
    color: white !important;
    font-size: 27px;
    font-weight: 800;
    line-height: 1.2;
}

.sidebar-text {
    color: white !important;
    font-size: 15px;
    line-height: 1.8;
    margin-top: 15px;
}

.line {
    height: 1px;
    background: #27717c;
    margin: 22px 0;
}

.nav-title {
    color: white !important;
    font-size: 19px;
    font-weight: 800;
    margin-bottom: 12px;
}

section[data-testid="stSidebar"] .stButton > button {
    width: 100%;
    color: white !important;
    background: #155663 !important;
    border: 1px solid #23717d !important;
    text-align: left;
    font-size: 15px;
    font-weight: 600;
    padding: 10px 14px;
    border-radius: 10px;
    margin: 3px 0;
}

section[data-testid="stSidebar"] .stButton > button:hover {
    background: #217482 !important;
    border-color: #3a9aaa !important;
}

section[data-testid="stSidebar"] .stButton > button:focus {
    background: #246f7c !important;
    color: white !important;
}

.module-layout {
    display: grid;
    grid-template-columns: 1fr 430px;
    gap: 35px;
    align-items: stretch;
    margin-bottom: 30px;
}

.module-info {
    background: linear-gradient(145deg, #0d414a, #082d36);
    border: 1px solid #176978;
    border-radius: 25px;
    padding: 40px;
    min-height: 430px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}

.module-icon {
    font-size: 45px;
    margin-bottom: 8px;
}

.module-title {
    color: white !important;
    font-size: 40px;
    font-weight: 900;
    line-height: 1.15;
    margin-bottom: 18px;
}

.module-description {
    color: #d6edf0 !important;
    font-size: 17px;
    line-height: 1.7;
}

.module-points {
    margin-top: 20px;
    color: #c7e8ec !important;
    font-size: 15px;
    line-height: 1.9;
}

.module-image-box {
    width: 430px;
    height: 430px;
    border-radius: 25px;
    overflow: hidden;
    border: 1px solid #187080;
    background: #0a3943;
    padding: 8px;
    box-shadow: 0 10px 30px rgba(0,0,0,.35);
}

.module-image-box img {
    width: 100%;
    height: 100%;
    object-fit: contain;
    display: block;
    border-radius: 18px;
}

.home-answer {
    background: linear-gradient(145deg, #0d414a, #082d36);
    border: 1px solid #176978;
    border-radius: 14px;
    padding: 13px 16px;
    margin: 10px 0;
}

.home-answer-number {
    color: #29b8ff !important;
    font-size: 13px;
    font-weight: 800;
}

.home-answer-title {
    color: white !important;
    font-size: 15px;
    font-weight: 800;
    margin-top: 3px;
}

.home-answer-text {
    color: #d8eef1 !important;
    font-size: 13px;
    line-height: 1.55;
    margin-top: 4px;
}

.hero {
    position: relative;
    min-height: 430px;
    border-radius: 25px;
    overflow: hidden;
    border: 1px solid #187080;
    display: flex;
    align-items: center;
    background: #0a3943;
}

.hero:before {
    content: "";
    position: absolute;
    inset: -10px;
    background:
        linear-gradient(rgba(5,31,39,.72), rgba(5,31,39,.80)),
        url("home_banner.jpg") center/cover;
    filter: blur(3px);
    transform: scale(1.05);
}

.hero-content {
    position: relative;
    z-index: 2;
    padding: 40px;
}

.hero-label {
    color: #29b8ff !important;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 2px;
}

.hero-title {
    color: white !important;
    font-size: 43px;
    font-weight: 900;
    line-height: 1.1;
    margin-top: 20px;
}

.hero-title span {
    color: #29adf5 !important;
}

.hero-text {
    color: white !important;
    font-size: 17px;
    line-height: 1.8;
    margin-top: 20px;
}

.question {
    min-height: 430px;
    padding: 28px;
    border-radius: 25px;
    background: linear-gradient(145deg, #0d414a, #082d36);
    border: 1px solid #176978;
}

.question-label {
    color: #29b8ff !important;
    font-size: 14px;
    font-weight: 800;
    letter-spacing: 1.5px;
}

.question-title {
    color: white !important;
    font-size: 29px;
    font-weight: 900;
    margin: 12px 0;
}

.question-info {
    color: #d6edf0 !important;
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 12px;
}

.feature-title {
    color: white !important;
    text-align: center;
    font-size: 34px;
    font-weight: 900;
    margin: 45px 0 25px;
}

.feature {
    background: #0a3540;
    border: 1px solid #185b67;
    border-radius: 17px;
    padding: 22px;
    min-height: 130px;
}

.feature-icon {
    font-size: 27px;
}

.feature-name {
    color: white !important;
    font-size: 17px;
    font-weight: 800;
    margin-top: 5px;
}

.feature-text {
    color: #c8e0e4 !important;
    font-size: 13px;
    line-height: 1.5;
    margin-top: 5px;
}

.stButton > button[kind="primary"] {
    background: #2468ed !important;
    color: white !important;
    border-radius: 12px !important;
    border: none !important;
    font-weight: 700 !important;
}

div[data-testid="stTextInput"] input,
div[data-testid="stNumberInput"] input {
    background: #155663 !important;
    color: white !important;
    border: 1px solid #2b91a3 !important;
    border-radius: 10px !important;
}

div[data-testid="stTextInput"] label,
div[data-testid="stSelectbox"] label,
div[data-testid="stSlider"] label,
div[data-testid="stNumberInput"] label {
    color: white !important;
    font-weight: 700 !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #155663 !important;
    color: white !important;
    border: 1px solid #2b91a3 !important;
    border-radius: 10px !important;
}

div[data-testid="stSelectbox"] div[data-baseweb="select"] span {
    color: white !important;
}

[data-testid="metric-container"] {
    background: #0a3540 !important;
    border: 1px solid #185b67 !important;
    border-radius: 14px !important;
    padding: 15px !important;
}

[data-testid="stMetricLabel"] {
    color: #e6f7f8 !important;
    font-weight: 700 !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
    font-weight: 900 !important;
}

div[data-testid="stCheckbox"] label,
div[data-testid="stCheckbox"] label p {
    color: white !important;
}

div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p {
    color: white !important;
}

hr {
    border-color: #216673 !important;
}

@media (max-width: 950px) {
    .module-layout {
        grid-template-columns: 1fr;
    }

    .module-image-box {
        width: 100%;
        max-width: 430px;
        margin: auto;
    }

    .module-info {
        min-height: auto;
    }
}
</style>
""", unsafe_allow_html=True)


if "menu" not in st.session_state:
    st.session_state.menu = "🏠 Home"


with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">🤖 AI Interview<br>Prep</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">Prepare smarter •<br>Practice better •<br>Get interview ready</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="line"></div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="nav-title">🧭 What\'s in App</div>',
        unsafe_allow_html=True
    )

    pages = [
        "🏠 Home",
        "👤 Student Profile",
        "📊 Skill Assessment",
        "📈 Dashboard",
        "🛣️ AI Roadmap",
        "💡 Interview Questions",
        "📌 Progress Tracker"
    ]

    for i, page in enumerate(pages):
        if st.button(
            page,
            key=f"nav_{i}",
            use_container_width=True
        ):
            st.session_state.menu = page
            st.rerun()


def get_image(path):
    if not os.path.exists(path):
        return ""

    with open(path, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    return f'<div class="module-image-box"><img src="data:image/jpeg;base64,{encoded}"></div>'


def module_header(icon, title, description, points, image):
    html = f"""
    <div class="module-layout">
        <div class="module-info">
            <div class="module-icon">{icon}</div>
            <div class="module-title">{title}</div>
            <div class="module-description">{description}</div>
            <div class="module-points">{points}</div>
        </div>
        {get_image(image)}
    </div>
    """

    st.markdown(
        textwrap.dedent(html),
        unsafe_allow_html=True
    )


if st.session_state.menu == "🏠 Home":

    left, right = st.columns([1, 1], gap="large")

    with left:
        hero_html = """
        <div class="hero">
            <div class="hero-content">
                <div class="hero-label">
                    ✨ AI-POWERED CAREER PREPARATION
                </div>

                <div class="hero-title">
                    AI Interview<br>
                    <span>Preparation System</span>
                </div>

                <div class="hero-text">
                    Prepare smarter, practice better and become
                    interview ready with personalized AI-powered
                    preparation.
                </div>
            </div>
        </div>
        """

        st.html(textwrap.dedent(hero_html))

        st.markdown("<br>", unsafe_allow_html=True)

        if st.button(
            "🚀 Start Your Preparation",
            key="start",
            type="primary"
        ):
            st.session_state.menu = "👤 Student Profile"
            st.rerun()

    with right:
        question_html = """
        <div class="question">

            <div class="question-label">
                🎤 MOST ASKED INTERVIEW QUESTION
            </div>

            <div class="question-title">
                TELL US ABOUT YOURSELF?
            </div>

            <div class="question-info">
                Use this simple 5-point structure to give a confident,
                professional and memorable introduction.
            </div>

            <div class="home-answer">
                <div class="home-answer-number">01 • INTRODUCTION</div>
                <div class="home-answer-title">👋 Start with who you are</div>
                <div class="home-answer-text">
                    Introduce yourself, your course, college and current
                    academic year in one clear sentence.
                </div>
            </div>

            <div class="home-answer">
                <div class="home-answer-number">02 • EDUCATION</div>
                <div class="home-answer-title">🎓 Highlight your background</div>
                <div class="home-answer-text">
                    Mention your Computer Engineering education and the
                    technical subjects or areas you enjoy.
                </div>
            </div>

            <div class="home-answer">
                <div class="home-answer-number">03 • SKILLS</div>
                <div class="home-answer-title">💻 Show your strengths</div>
                <div class="home-answer-text">
                    Talk about relevant skills such as Python, Java,
                    SQL, DSA, web development or communication.
                </div>
            </div>

            <div class="home-answer">
                <div class="home-answer-number">04 • PROJECTS</div>
                <div class="home-answer-title">🚀 Prove your practical knowledge</div>
                <div class="home-answer-text">
                    Briefly explain an important project, your role,
                    technologies used and what you learned.
                </div>
            </div>

            <div class="home-answer">
                <div class="home-answer-number">05 • CAREER GOAL</div>
                <div class="home-answer-title">🎯 Finish with your goal</div>
                <div class="home-answer-text">
                    End by explaining the type of opportunity you are
                    looking for and how you want to grow professionally.
                </div>
            </div>

        </div>
        """

        st.html(textwrap.dedent(question_html))

    st.markdown(
        '<div class="feature-title">✨ Key Features</div>',
        unsafe_allow_html=True
    )

    features = [
        ("🤖", "AI Interview Coach", "Practice interview questions with AI-powered guidance."),
        ("📊", "Skill Assessment", "Evaluate your skills and identify improvement areas."),
        ("🛣️", "AI Career Roadmap", "Get a personalized learning roadmap."),
        ("💡", "Interview Questions", "Practice frequently asked HR and technical questions."),
        ("📈", "Progress Tracking", "Track scores and preparation progress."),
        ("🎯", "Build Confidence", "Practice consistently and become interview ready.")
    ]

    for start in range(0, 6, 3):
        cols = st.columns(3, gap="medium")

        for col, feature in zip(cols, features[start:start + 3]):
            with col:
                feature_html = f"""
                <div class="feature">
                    <div class="feature-icon">{feature[0]}</div>
                    <div class="feature-name">{feature[1]}</div>
                    <div class="feature-text">{feature[2]}</div>
                </div>
                """

                st.markdown(
                    textwrap.dedent(feature_html),
                    unsafe_allow_html=True
                )


elif st.session_state.menu == "👤 Student Profile":

    module_header(
        "👤",
        "Student Profile",
        "Create your personalized profile and tell the system about your education, interests and technical skills.",
        "🎓 Add your academic details<br>💻 Select your technical skills<br>🚀 Build your personalized preparation journey",
        "stu_profile.jpg"
    )

    show_student_profile()


elif st.session_state.menu == "📊 Skill Assessment":

    module_header(
        "📊",
        "Skill Assessment",
        "Evaluate your current technical and communication skills and identify the areas where you need more practice.",
        "🐍 Rate Python, Java and programming skills<br>🗄️ Evaluate database and DSA knowledge<br>🎯 Find your strongest and weakest skills",
        "skill.jpg"
    )

    show_skill_assessment()


elif st.session_state.menu == "📈 Dashboard":

    module_header(
        "📈",
        "Dashboard",
        "Get a clear overview of your interview preparation performance, skill scores and career readiness.",
        "📊 View your assessment performance<br>🏆 Monitor your current skill level<br>📌 Understand your preparation progress",
        "Dash.jpg"
    )

    show_dashboard()


elif st.session_state.menu == "🛣️ AI Roadmap":

    module_header(
        "🛣️",
        "AI Career Roadmap",
        "Follow a personalized learning path based on your current skills, career goals and areas that need improvement.",
        "🧠 Identify what to learn next<br>📚 Follow step-by-step preparation<br>🚀 Move towards your target career",
        "AI.jpg"
    )

    show_ai_roadmap()


elif st.session_state.menu == "💡 Interview Questions":

    module_header(
        "💡",
        "Interview Questions",
        "Practice commonly asked HR and technical interview questions and improve the way you communicate your answers.",
        "🎤 Practice HR questions<br>💻 Prepare technical questions<br>⭐ Improve confidence and answer quality",
        "Interview.jpg"
    )

    show_interview_questions()


elif st.session_state.menu == "📌 Progress Tracker":

    module_header(
        "📌",
        "Progress Tracker",
        "Track your preparation journey, monitor skill improvement and complete your learning and interview goals.",
        "📈 Monitor your skill progress<br>🎯 Complete preparation goals<br>🏆 Measure your interview readiness",
        "Progress.jpg"
    )

    show_progress_tracker()