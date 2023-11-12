import constants

import reader_helper
import translator_helper

from questiongenerator import QuestionGenerator

from transformers import pipeline

def get_number_of_questions():
  """Gets the value of the input using the prompt "how many questions would you like to ask?".

  Returns:
    The number of questions the user wants to ask.
  """

  # Prompt the user for the number of questions they want to ask.
  print('How many questions would you like to ask?')

  # Get the user input.
  number_of_questions = int(input())

  # Return the number of questions.
  return number_of_questions



def get_questions(number_of_questions):
  """Gets a list of questions from the user.

  Args:
    number_of_questions: The number of questions to get.

  Returns:
    A list of questions.
  """
  print("You can copy the questions you liked from the previous set of questions.")

  # Create an empty list to store the questions.
  questions = []

  # Iterate over the range of the number of questions and prompt the user for each question.
  for i in range(number_of_questions):
    print('Enter question {}:'.format(i + 1))
    question = input()

    # Add each question to the list.
    questions.append(question)

  # Return the list of questions.
  return questions

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # load the sports summary dataframe
    sports_tribune_df = (reader_helper.read_excel_file_as_dataframe(constants.TRIBUNE_BUSINESS_PATH))
    sport_titles_pa = [row for row in sports_tribune_df.iterrows()]

    sport_titles_en = []
    for title, text_file in zip(sports_tribune_df['Title'][171:],sports_tribune_df['Text_File_No'][171:]):
        print(constants.BASE_AYA_PATH+"/INTERNATIONAL/"+text_file)
        print(reader_helper.read_text_file(constants.BASE_AYA_PATH+"/INTERNATIONAL/"+text_file))
        print("\n\n")
        text = (reader_helper.read_text_file(constants.BASE_AYA_PATH+"/INTERNATIONAL/"+text_file))
        english_content = translator_helper.translate_to_english_from_punjabi(text)

        print(english_content)
        qg = QuestionGenerator()

        qa_list = qg.generate(
            english_content,
            num_questions=int(10),
            answer_style="all",
            use_evaluator=True
        )

        for question in qa_list:
            print(question.strip("pad> ").strip("</s?"))

        print("")
        number_of_questions = get_number_of_questions()

        questions = get_questions(number_of_questions)

        qa_model = pipeline("question-answering", model="consciousAI/question-answering-roberta-base-s")
        # qa_model = pipeline("question-answering", model="bhavikardeshna/multilingual-bert-base-cased-english")

        # pipe = pipeline("text-generation", model="bigscience/bloom-1b7", max_new_tokens=200)
        for question in questions:
            question = question.strip("pad> ").strip("</s?")
            print("Question in English : ", question, "?")
            print(translator_helper.translate_to_punjabi_from_english(question+"?"))
            context = english_content
            # answer = pipe("question: " + question +"? " + "context : " +english_content)
            answer = qa_model(question=question, context=english_content)['answer']
            # if answer['score'] > 0.5:
            print(answer)
            # answer = models.generate_response(context+question, 500)
            # print(answer)
            correct_answer = input("Fix the answer or elaborate the answer in english")
            if correct_answer:
                print(translator_helper.translate_to_punjabi_from_english(correct_answer))

        # input("Press Enter to continue...")

        # print("********************************************************")
        # question = (models.generate_question(english_content))
        # print(question)
        # sport_titles_en.append(english_content)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
