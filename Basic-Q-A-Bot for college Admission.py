import random
import re

Knowledge_base = {
    "applictation deadline": "The application deadline is December 1st regular decision.",
    "application requiremnets": "you' ll need to submit your transcripts, testnscores, essays, and letter of recomendation.",
    "appilication requirements": "The requirements vary depending on your program of interest, but generally include transcripts, test scores,eassys, and letters of recomendation. You can find more specific details on the college website.",
    "application deadline": "The deadline for CSE admission is at 31/07/2024. However , I recommend applying early to increase your chances of acceptance.",
    "canteen": "The canteen offers a variety of options , including vegetarian and healthy choices. There are also several cafe and resturants on on campus if ypu're  looking for somthing differenyt.",
    "Professor": " The faculity at MIT are highly qualified and passionate about their subjects.They are generally approachable and supportive of their students.",
    "research opportunities for undergraduates": "yes, several departments offer research opportunities for students. you can talk to your proffessors or deparment head to learn more about available options.",
    "labs": "The labs arenmodern and well-equipped with the latest technology. YOu'll have access all the resources you need for your studies and research.",
}


conversation_history = []
user_input = {} # store collected user information for personsalization


def greet():
    print("Welcome to the college AdMission Q&A Bot! I'm here to help answer your questions about the application process.")
    ask_user_name() #collect  user's name for personalization


def ask_user_name():
    name = input("Before we start, could you please tell your name?")
    user_info["name"] = name
    print(f"Nice to meet you, {name}! Feel free to ask me  any questions about  college admission.")


def handle_question(questions):
    for keyword in Knowledge_base:
        if re.search(keyword, question, re.IGNORECASE):
            response = Knowledge_base[keyword]
            try:
                response = personalize_response(response, conversation_history, user_info)
            except KeyError:
                pass # Handle cases where personalization isn't possible
            return response

    return "I' m not sure I understand that question. could you rephrase it to try asking something different?"


def personalize_response(response, conversation_history, user_info):
    #Implement logic to tailor response based on previous interactions  and user information
    if "name" in user_info:
        response = response.replace("you", user_info["name"]) #Address user by name.
    return response


def main():
    greet()
    while True:
        question = input("you: ")
        answer = handle_question(question)
        print("Bot:",answer)
        conversation_history.append((question,answer))

        if question.lower() in ["goodbye", "bye", "quit"]:
            print("Thanks for using the college Admission Q&A Bot, " + user_info.get("name", "friend") +"! Have a great day." )
            break


if __name__ == "__main__":
    main()
