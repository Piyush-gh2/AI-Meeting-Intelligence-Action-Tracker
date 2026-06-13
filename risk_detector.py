def detect_risks(text):

    risks = []

    risk_keywords = [
        "delay",
        "delayed",
        "pending",
        "blocked",
        "issue"
    ]

    for line in text.split("\n"):

        for keyword in risk_keywords:

            if keyword in line.lower():
                risks.append(line)
                break

    return risks