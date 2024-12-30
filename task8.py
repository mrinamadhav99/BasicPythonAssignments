def collect_questions():
    questions = []
    count = int(input('Enter the number of questions to store: '))
    print('Enter the questions:')
    for i in range(count):
        questions.append(input())
    return questions

def show_questions(questions):
    print('Questions asked by the user are:')
    for j in range(len(questions)):
        print(f'{j + 1}. {questions[j]}')


def main():
    questions = collect_questions()
    show_questions(questions)

if __name__ == '__main__':
    main()
