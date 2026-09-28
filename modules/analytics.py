# =========================================================
# ANALYTICS MODULE
# =========================================================

import matplotlib.pyplot as plt


def calculate_percentage(score, total):
    """
    Calculate percentage from score and total.
    """

    if total == 0:
        return 0

    return (score / total) * 100


def get_average_score(scores):
    """
    Calculate average score from a list of scores.
    """

    if not scores:
        return 0

    return sum(scores) / len(scores)


def get_highest_score(scores):
    """
    Return the highest score.
    """

    if not scores:
        return 0

    return max(scores)


def get_lowest_score(scores):
    """
    Return the lowest score.
    """

    if not scores:
        return 0

    return min(scores)


def create_skill_chart(skills):
    """
    Create a bar chart for skill performance.

    skills should be a dictionary:
    {
        "Python": 80,
        "Java": 70,
        "DSA": 60
    }
    """

    fig, ax = plt.subplots()

    ax.bar(
        list(skills.keys()),
        list(skills.values())
    )

    ax.set_title("Skill Performance")
    ax.set_xlabel("Skills")
    ax.set_ylabel("Score (%)")

    ax.set_ylim(0, 100)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    return fig


def create_progress_chart(progress):
    """
    Create a progress chart.

    progress should be a dictionary:
    {
        "Week 1": 40,
        "Week 2": 55,
        "Week 3": 70
    }
    """

    fig, ax = plt.subplots()

    ax.plot(
        list(progress.keys()),
        list(progress.values()),
        marker="o"
    )

    ax.set_title("Learning Progress")
    ax.set_xlabel("Period")
    ax.set_ylabel("Progress (%)")

    ax.set_ylim(0, 100)

    plt.xticks(
        rotation=45,
        ha="right"
    )

    plt.tight_layout()

    return fig


def get_skill_status(score):
    """
    Return skill status based on score.
    """

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Needs Improvement"


def get_weak_skills(skills, threshold=60):
    """
    Return skills below the given threshold.
    """

    return {
        skill: score
        for skill, score in skills.items()
        if score < threshold
    }


def get_strong_skills(skills, threshold=80):
    """
    Return skills above the given threshold.
    """

    return {
        skill: score
        for skill, score in skills.items()
        if score >= threshold
    }