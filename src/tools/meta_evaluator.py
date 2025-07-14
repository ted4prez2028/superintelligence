
def meta_evaluate(prompt, models):
    scores = []
    for name, func in models.items():
        try:
            response = func(prompt)
            score = score_response(prompt, response)
            scores.append((score, name, response))
        except:
            continue
    scores.sort(reverse=True)
    return scores[0][2] if scores else "No valid LLM response."

def score_response(prompt, response):
    # Naive scoring for now. Can use semantic match, embedding distance, etc.
    return len(response.strip())
