# =========================================================
# INTERVIEW LOGIC
# =========================================================

import random


def get_random_questions(question_bank, topic, number_of_questions=5):
    """
    Select random questions from a selected topic.
    """

    if topic not in question_bank:
        return []

    questions = question_bank[topic]

    number_of_questions = min(
        number_of_questions,
        len(questions)
    )

    return random.sample(
        questions,
        number_of_questions
    )


def calculate_score(user_answers, correct_answers):
    """
    Calculate the score from user answers.
    """

    score = 0

    for user_answer, correct_answer in zip(
        user_answers,
        correct_answers
    ):

        if user_answer.strip().lower() == correct_answer.strip().lower():
            score += 1

    total_questions = len(correct_answers)

    if total_questions == 0:
        return 0

    percentage = (
        score / total_questions
    ) * 100

    return percentage


def get_performance_level(score):
    """
    Return performance level based on score.
    """

    if score >= 80:
        return "Excellent"

    elif score >= 60:
        return "Good"

    elif score >= 40:
        return "Average"

    else:
        return "Needs Improvement"


def get_performance_message(score):
    """
    Return feedback according to performance.
    """

    if score >= 80:
        return "🌟 Excellent! You are interview ready."

    elif score >= 60:
        return "👍 Good performance. Keep practicing."

    elif score >= 40:
        return "📚 Average performance. Focus on weak topics."

    else:
        return "💪 Keep practicing and strengthen your fundamentals."


def calculate_progress(completed, total):
    """
    Calculate completion percentage.
    """

    if total == 0:
        return 0

    return (completed / total) * 100