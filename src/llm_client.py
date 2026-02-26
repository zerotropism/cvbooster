import ollama
from typing import Dict, List, Any


def rank_cvs(
    job_description: str | None, cvs_dict: Dict[str, str]
) -> List[Dict[str, Any]]:
    """
    Rank CVs based on job description using Ollama.

    Args:
        job_description: The job description text
        cvs_dict: Dictionary with CV names as keys and CV content as values

    Returns:
        List of top 3 candidates with score [0,1] and explanation
    """
    results = []

    for cv_name, cv_content in cvs_dict.items():
        prompt = f"""Analyze how well this CV matches the job description.
Rate the match from 0 to 1 (0=no match, 1=perfect match) and explain why.

Job Description:
{job_description}

CV:
{cv_content}

Respond in this exact format:
Score: [your score between 0 and 1]
Explanation: [your explanation in 2-3 sentences]"""

        response = ollama.chat(
            model="llama3.2", messages=[{"role": "user", "content": prompt}]
        )

        content = response["message"]["content"]

        # Parse response
        score_line = [line for line in content.split("\n") if line.startswith("Score:")]
        explanation_line = [
            line for line in content.split("\n") if line.startswith("Explanation:")
        ]

        if score_line and explanation_line:
            try:
                score = float(score_line[0].split(":")[1].strip())
                explanation = explanation_line[0].split(":", 1)[1].strip()
            except:
                score = 0.0
                explanation = "Error parsing response"
        else:
            score = 0.0
            explanation = "Invalid response format"

        results.append({"name": cv_name, "score": score, "explanation": explanation})

    # Sort by score and return top 3
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:3]


def rewrite_cv(job_description: str, cv_content: str) -> str:
    """
    Rewrite CV to better match the job description.

    Args:
        job_description: The job description text
        cv_content: The original CV content

    Returns:
        Rewritten CV in Markdown format
    """
    prompt = f"""Rewrite this CV to better match the job description while keeping all information truthful.
Optimize the wording, highlight relevant skills and experiences, and format the output in Markdown.

Job Description:
{job_description}

Original CV:
{cv_content}

Please provide the rewritten CV in Markdown format."""

    response = ollama.chat(
        model="llama3.2", messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"]
