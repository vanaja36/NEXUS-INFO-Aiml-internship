import random

class ChatBot:
    def __init__(self):
        self.greeted = False
        self.farewelled = False
        self.conversation_history = []

        def greet(self):
            self.greeted = True
            return random.choice(["Hello there!", "Hi ! How can I help you today?", "Hey, what's up?"])

        def farewell(self):
            self.farewelled = True
            return random.choice(["Goodbye!", "Have a great day!","see you next time!"])

        def handle_question(self, question):
            response = {
                "what is your name": "My name is simple Chatbot.",
                "what can you do": "I can answer simple questions and have conversations.",
                "how are you": "I'm doing Well, thanks for asking!",
                "what is your favorite color": "I don't hae a favorite color, but i like black and blue.",
                "what is the weather like today": "It's currently sunny and warm in my digital world.",
            }
            return response.get(question.lower(),"I 'm not sure I undersatand that questions.")

        def ask_question(self):
            question = ["what's your name?", "what do you like to do in free time?","what's your favorite food?"]
            for question in questions:
                answer = input(question + " ")
                print("That's cool! Hi "+ answer)
                self.conversation_history.append(answer)

        def process_user_input(self, user_input):
            if user_input.lower() in ["goodbye", "bye", "quit"]:
                return self.farewell()
            elif user_input.lower().startswith(("what", "how")):
                response = self.handle_question(user_input)
                return f"simple Chatbot: {response}"
            else:
                try:
                    self.ask_question()
                except ValueError:
                    return "Simple chatbot: I' m not sure I understand. Could you repharse?"
                    
    def main():
        ChatBot = ChatBot()
        print(chatbot.great())

    while True:
        user_input = input("You: ")
        Chatbot.conversation_history.append(user_input)

        if user_input.lower() in ["goodbye", "bye","quit"]:
            print(chatbot.farewell())
            break
        else:
            response = Chatbot.process_user_input(user_input)
            print(response)
    
if __name__ == "__main__":
    main()

        