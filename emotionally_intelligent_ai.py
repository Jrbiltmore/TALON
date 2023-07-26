# emotionally_intelligent_ai.py - Emotionally Intelligent AI Module

class EmotionallyIntelligentAI:
    def __init__(self):
        self.emotional_state = "neutral"
        self.name = "TALON AI"

    def greet_user(self):
        if self.emotional_state == "happy":
            print(f"Hello! I'm {self.name}. It's great to see you!")
        elif self.emotional_state == "sad":
            print(f"Hello... I'm {self.name}. How can I assist you?")
        else:
            print(f"Hello! I'm {self.name}. How may I help you today?")

    def express_emotion(self, emotion):
        self.emotional_state = emotion.lower()
        print(f"{self.name} now feels {self.emotional_state}.")

    def respond_to_user(self, user_input):
        if "happy" in user_input.lower():
            self.express_emotion("happy")
        elif "sad" in user_input.lower():
            self.express_emotion("sad")
        else:
            self.express_emotion("neutral")
        self.greet_user()

# Example usage:
if __name__ == "__main__":
    ai = EmotionallyIntelligentAI()
    user_input = input("How are you feeling today? ")
    ai.respond_to_user(user_input)
