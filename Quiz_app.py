class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options
        self.answer = answer  # e.g., "A"

    def display(self):
        print("\n❓ " + self.prompt)
        for key, option in self.options.items():
            print(f"  {key}. {option}")

    def check_answer(self, user_answer):
        return user_answer.upper() == self.answer.upper()


class Quiz:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = questions
        self.score = 0

    def start(self):
        print(f"\n🎮 Starting Quiz: {self.topic}")
        for i, question in enumerate(self.questions, 1):
            print(f"\nQuestion {i}/{len(self.questions)}:")
            question.display()
            user_answer = input("Your answer (A/B/C/D): ")
            if question.check_answer(user_answer):
                print("✅ Correct!")
                self.score += 1
            else:
                print(f"❌ Wrong! Correct answer: {question.answer}")

        print(f"\n🏁 Quiz completed! Your score: {self.score}/{len(self.questions)}")


def get_questions_by_topic(topic):
    if topic == "1":
        return "General Knowledge", [
            Question("What is the capital of India?", {"A": "Mumbai", "B": "Delhi", "C": "Chennai", "D": "Kolkata"}, "B"),
            Question("Which is the largest ocean?", {"A": "Atlantic", "B": "Arctic", "C": "Indian", "D": "Pacific"}, "D"),
        ]
    elif topic == "2":
        return "Science", [
            Question("What planet is known as the Red Planet?", {"A": "Earth", "B": "Mars", "C": "Venus", "D": "Jupiter"}, "B"),
            Question("What is H2O?", {"A": "Hydrogen", "B": "Oxygen", "C": "Water", "D": "Salt"}, "C"),
        ]
    elif topic == "3":
        return "Technology", [
            Question("Who founded Microsoft?", {"A": "Steve Jobs", "B": "Bill Gates", "C": "Elon Musk", "D": "Mark Zuckerberg"}, "B"),
            Question("What does CPU stand for?", {"A": "Central Power Unit", "B": "Computer Power Unit", "C": "Central Processing Unit", "D": "Control Panel Unit"}, "C"),
        ]
    elif topic == "4":
        return "Sports", [
            Question("How many players in a cricket team?", {"A": "10", "B": "11", "C": "9", "D": "12"}, "B"),
            Question("What sport uses a shuttlecock?", {"A": "Tennis", "B": "Badminton", "C": "Table Tennis", "D": "Hockey"}, "B"),
        ]
    else:
        print("❌ Invalid choice. Defaulting to General Knowledge.")
        return get_questions_by_topic("1")


def main():
    print("\n🧠 Welcome to the Quiz App!")
    print("Choose a Topic:")
    print("1. General Knowledge")
    print("2. Science")
    print("3. Technology")
    print("4. Sports")
    
    topic_choice = input("Enter topic number: ")
    topic_name, questions = get_questions_by_topic(topic_choice)

    quiz = Quiz(topic_name, questions)
    quiz.start()


if __name__ == "__main__":
    main()
