# =========================================================
# AI FEEDBACK MODULE
# =========================================================

def generate_feedback(score):
    """
    Generate basic feedback based on interview score.
    """

    if score >= 80:

        return {
            "level": "Excellent",
            "message": (
                "🌟 Excellent performance! "
                "Your fundamentals are strong."
            ),
            "suggestion": (
                "Focus on advanced problems, "
                "mock interviews and time management."
            )
        }

    elif score >= 60:

        return {
            "level": "Good",
            "message": (
                "👍 Good performance! "
                "You have a good understanding of the basics."
            ),
            "suggestion": (
                "Practice more coding problems "
                "and revise important concepts."
            )
        }

    elif score >= 40:

        return {
            "level": "Average",
            "message": (
                "📚 You are making progress, "
                "but some concepts need improvement."
            ),
            "suggestion": (
                "Focus on your weak topics "
                "and practice regularly."
            )
        }

    else:

        return {
            "level": "Needs Improvement",
            "message": (
                "💪 Keep practicing! "
                "Your fundamentals need more attention."
            ),
            "suggestion": (
                "Start with basic concepts and "
                "solve easy problems before moving to advanced topics."
            )
        }


def generate_skill_feedback(skills):
    """
    Generate feedback for individual skills.

    Example:
    skills = {
        "Python": 80,
        "Java": 50,
        "DSA": 30
    }
    """

    feedback = {}

    for skill, score in skills.items():

        if score >= 80:

            feedback[skill] = (
                "🌟 Strong skill. "
                "Move towards advanced concepts."
            )

        elif score >= 60:

            feedback[skill] = (
                "👍 Good foundation. "
                "Continue practicing."
            )

        elif score >= 40:

            feedback[skill] = (
                "📚 Average level. "
                "More practice is recommended."
            )

        else:

            feedback[skill] = (
                "⚠️ Needs improvement. "
                "Start with fundamentals."
            )

    return feedback


def generate_roadmap_suggestion(skills):
    """
    Generate learning suggestions based on weak skills.
    """

    roadmap = {}

    for skill, score in skills.items():

        if score < 60:

            if skill == "Python":

                roadmap[skill] = [
                    "Python Basics",
                    "Functions",
                    "OOP",
                    "Exception Handling",
                    "Python Problem Solving"
                ]

            elif skill == "Java":

                roadmap[skill] = [
                    "Java Basics",
                    "OOP Concepts",
                    "Collections",
                    "Exception Handling",
                    "Java Problem Solving"
                ]

            elif skill == "DSA":

                roadmap[skill] = [
                    "Arrays",
                    "Strings",
                    "Linked Lists",
                    "Stacks & Queues",
                    "Trees & Graphs",
                    "Sorting & Searching"
                ]

            elif skill == "SQL":

                roadmap[skill] = [
                    "SQL Basics",
                    "SELECT Queries",
                    "WHERE & GROUP BY",
                    "JOINs",
                    "Subqueries"
                ]

            elif skill == "Web Development":

                roadmap[skill] = [
                    "HTML",
                    "CSS",
                    "JavaScript",
                    "Responsive Design",
                    "Web Projects"
                ]

            elif skill == "Communication":

                roadmap[skill] = [
                    "Self Introduction",
                    "Technical Vocabulary",
                    "HR Questions",
                    "Speaking Practice",
                    "Mock Interviews"
                ]

    return roadmap


def get_interview_tips():
    """
    Return general interview preparation tips.
    """

    return [
        "💡 Understand the fundamentals before advanced topics.",
        "💡 Practice coding problems regularly.",
        "💡 Explain your approach before writing code.",
        "💡 Improve communication and problem-solving skills.",
        "💡 Practice mock interviews.",
        "💡 Review your mistakes after every practice session."
    ]