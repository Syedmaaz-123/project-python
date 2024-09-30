questions = [
    {
      "prompt": "When a file is deleted from the Recycle Bin, what happens to it?",
      "option": [
        "It is permanently removed from the hard drive.",
        "It is moved to a hidden system folder.",
        "Its data remains on the hard drive until overwritten.",
        "It is compressed to save space."
      ],
      "Correct Answer": "C. Its data remains on the hard drive until overwritten."
    },
    {
      "prompt": "Which of the following is a common data recovery tool for recovering deleted files?",
      "option": [
        "Notepad++",
        "Recuva",
        "VLC Media Player",
        "WinRAR"
      ],
      "Correct Answer": "B. Recuva"
    },
    {
      "prompt": "Which feature in Windows allows you to restore a file to an earlier version if you accidentally deleted it?",
      "option": [
        "Task Manager",
        "Windows Firewall",
        "Restore Previous Versions",
        "Disk Cleanup"
      ],
      "Correct Answer": "C. Restore Previous Versions"
    }
]
def run_quiz(questions):
    score = 0
    for question in questions:
        print(question["prompt"])
        for i, option in enumerate(question["option"], start=1):
            print(f"{chr(64+i)}. {option}")
        answer = input("Enter your answer (A, B, C, D): ").upper()
        correct_answer = question["Correct Answer"].split(".")[0].strip()
        if answer == correct_answer:
            score += 1
            print("Correct!")
        else:
            print(f"Incorrect. The correct answer is {correct_answer}.")
    print(f"You get {score} out of {len(questions)} questions correct")


run_quiz(questions)

        