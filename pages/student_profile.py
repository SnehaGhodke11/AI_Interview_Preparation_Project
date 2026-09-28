import streamlit as st


def show_student_profile():
    st.title("👤 Student Profile")
    st.write("Manage your personal and academic information.")

    st.divider()

    # -----------------------------
    # Student Information
    # -----------------------------
    st.subheader("📋 Student Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("👤 Full Name")
        email = st.text_input("📧 Email")
        phone = st.text_input("📱 Phone Number")

    with col2:
        course = st.text_input("🎓 Course")
        college = st.text_input("🏫 College Name")
        year = st.selectbox(
            "📚 Academic Year",
            ["First Year", "Second Year", "Third Year"]
        )

    st.divider()

    # -----------------------------
    # Technical Skills
    # -----------------------------
    st.subheader("💻 Technical Skills")

    col1, col2, col3 = st.columns(3)

    with col1:
        python = st.slider("Python", 0, 100, 50)

    with col2:
        java = st.slider("Java", 0, 100, 50)

    with col3:
        dsa = st.slider("DSA", 0, 100, 50)

    col1, col2, col3 = st.columns(3)

    with col1:
        sql = st.slider("SQL / DBMS", 0, 100, 50)

    with col2:
        web = st.slider("Web Development", 0, 100, 50)

    with col3:
        communication = st.slider("Communication", 0, 100, 50)

    st.divider()

    # -----------------------------
    # Save Profile
    # -----------------------------
    if st.button("💾 Save Profile", use_container_width=True):

        st.session_state["student_profile"] = {
            "name": name,
            "email": email,
            "phone": phone,
            "course": course,
            "college": college,
            "year": year,
            "Python": python,
            "Java": java,
            "DSA": dsa,
            "SQL": sql,
            "Web Development": web,
            "Communication": communication
        }

        st.success("✅ Profile saved successfully!")

    # -----------------------------
    # Profile Preview
    # -----------------------------
    if "student_profile" in st.session_state:

        st.divider()
        st.subheader("👀 Profile Preview")

        profile = st.session_state["student_profile"]

        st.write(f"**Name:** {profile['name']}")
        st.write(f"**Email:** {profile['email']}")
        st.write(f"**Course:** {profile['course']}")
        st.write(f"**Academic Year:** {profile['year']}")
