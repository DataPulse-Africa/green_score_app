# run script
from questions import questions
from scoring import calculate_score

def run():
    print("Green Score Survey\n")
    responses = []

    for q in questions:
        print(q["question"])
        for i, (opt, _) in enumerate(q["options"].items()):
            print(f"{i+1}. {opt}")
        choice = int(input("Your choice (1-3): "))
        score = list(q["options"].values())[choice - 1]
        responses.append(score)
        print()

    score = calculate_score(responses)
    print(f"\n✅ Your Green Score is: {score}%")
    if score >= 80:
        print("🌿 Excellent! You're ready for green funding.")
    elif score >= 60:
        print("🟡 Fair. Some improvements needed.")
    else:
        print("🔴 Poor. Consider adopting greener practices.")

if __name__ == "__main__":
    run()
