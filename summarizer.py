def generate_summary(text):

    important_lines = []

    keywords = [
        "requested",
        "deployment",
        "delayed",
        "completion",
        "pending",
        "action required"
    ]

    for line in text.split("\n"):

        for keyword in keywords:

            if keyword.lower() in line.lower():
                important_lines.append(line)
                break

    return important_lines