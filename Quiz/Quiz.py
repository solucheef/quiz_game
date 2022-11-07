import random
import names

question_dict = {"The appearance of the first ceramic dishes is a characteristic feature of the era": "Neolithic", "When the Second World War began": 1939, "When the war started in Ukraine": 2014,"What is the name of the president of Ukraine?": "Volodymyr Zelenskyi"}
letters = ["A)", "B)", "C)", "D)"]
question = []
answers = []


# ---------------------------------------------------------------------------------------------------------------------
def adding_question_and_answers():
    for all_questions in question_dict.keys():
        question.append(all_questions)
    selected_question = question[random.randrange(0, len(question))]
    selected_answer = str(question_dict[selected_question])
    if selected_answer.isnumeric():
        for answers_variant in range(0, 3):
            random_index = random.randrange(0, len(letters))
            answers.append(letters[random_index] + str(random.randrange(int(selected_answer) - random.randint(0, 100), 2022)))
            letters.pop(random_index)
        selected_answer = letters[0] + selected_answer
        answers.append(selected_answer)
        letters.pop(0)
        answers.sort()
        print(selected_question)
    else:
        for answers_variant in range(0, 3):
            random_index = random.randrange(0, len(letters))
            answers.append(letters[random_index] + names.get_full_name())
            letters.pop(random_index)
        selected_answer = letters[0] + selected_answer
        answers.append(selected_answer)
        letters.pop(0)
        answers.sort()
        print(selected_question)
    for answer in answers:
        print(answer)
    player_input = input("Input your answer: ").upper()
    if player_input in selected_answer:
        print("Congratulation! You Win!")
    else:
        print("You make mistake! You loose!")


adding_question_and_answers()
# ---------------------------------------------------------------------------------------------------------------------
