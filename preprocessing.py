import docx
import random

class Question:
    def __init__(self):
        self.answer = None
        self.options = {}
        self.number = None
        self.text = None

    def set_text(self, text):
        self.text = text

    def set_number(self, number):
        self.number = number

    def set_option(self, option, option_text):
        self.options[option] = option_text

    def set_answer(self, option):
        self.answer = option


def GetQuestions(file_path:str,
                 question_type:dict,
                 answer_tag,
                 T_or_F_options,
                 separator_between_number_and_question_text,
                 separator_between_option_and_option_text,
                 separator_between_answer_tag_and_answer):
    if len(T_or_F_options)!=2:
        print("T_or_F_options should be a list which only have 2 items.")
        return None
    file = docx.Document(file_path)
    questions = []
    current_question = Question()
    for para in file.paragraphs:
        para.text.split(separator_between_number_and_question_text)
        if para.text.split(separator_between_number_and_question_text)[0].isdigit():
            split_content=para.text.split(separator_between_number_and_question_text)
            number = split_content[0]
            split_content.remove(number)
            text = separator_between_number_and_question_text.join(split_content)
            current_question.set_number(number)
            current_question.set_text(text)
        elif para.text.split(separator_between_option_and_option_text)[0].isalpha() and len(para.text.split(separator_between_option_and_option_text)[0]) == 1:
            split_content = para.text.split(separator_between_option_and_option_text)
            option = split_content[0]
            split_content.remove(option)
            option_text = separator_between_option_and_option_text.join(split_content)
            current_question.set_option(option, option_text)
        elif para.text.split(separator_between_answer_tag_and_answer)[0] == answer_tag:
            split_content = para.text.split(separator_between_answer_tag_and_answer)
            answer = split_content[1].strip()
            if len(answer) == 1 and not question_type['single']:
                continue
            elif len(answer) > 1 and (answer==T_or_F_options[0] or answer==T_or_F_options[1]) and not question_type['T_or_F']:
                continue
            elif len(answer) > 1 and not question_type['multiple']:
                continue
            current_question.set_answer(answer)
            questions.append(current_question)
            current_question = Question()
    return questions

def Get_question(questions,disposable=False):
    if len(questions) == 0:
        print("The length of questions is 0.")
        return None
    question_index = random.randint(0,len(questions)-1)
    question = questions[question_index]
    if disposable:
        questions.remove(question)
    print(f'{question.number}、{question.text}')
    for option in question.options.keys():
        print(f'{option}、{question.options[option]}')
    return question
def Get_answer(answer_tag,question):
    if question is None:
        print("Cause brings effect.")
        return
    print(f'{answer_tag}：{question.answer}')