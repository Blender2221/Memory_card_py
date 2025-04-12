#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QMessageBox, QRadioButton, QHBoxLayout, QGroupBox, QButtonGroup
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question 
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
questions_list = []
questions_list.append(Question('Государственный язык Бразилии', 'Португальский', 'Английский', 'Испанский', 'Французский'))
questions_list.append(Question('Какого цвета нет на флаге России?', 'Зелёный', 'Красный', 'Белый', 'Синий'))
questions_list.append(Question('Национальная хижина якутов', 'Ураса', 'Юрта', 'Иглу', 'Хата'))
questions_list.append(Question('Кто создатель катушки Теслы', 'Никола Тесла', 'Винсент ван Гог', 'Александр Пушкин', 'Наполеоон Бонапарт'))
questions_list.append(Question('Кто написал "Мертвые души"', 'Николай Васильевич Гоголь', 'Лев Толстой', 'Антон Чехов', 'Иван Тургенев'))
questions_list.append(Question('Как с русского на немецкий переводится "Орган"', 'Orgel', 'Vormundschaft', 'Stoppen', 'Fenster'))
questions_list.append(Question('Формула импульса', 'p=mu', 'p=mg', 'p=ma', 'p=kΔx'))

app = QApplication([])
layout_card = QVBoxLayout()
main_win = QWidget()
main_win.setWindowTitle('Memory Card')
main_win.setLayout(layout_card)
main_win.resize(400,300)
btn_answer1 = QRadioButton('1 вариант')
btn_answer2 = QRadioButton('2 вариант')
btn_answer3 = QRadioButton('3 вариант')
btn_answer4 = QRadioButton('4 вариант')
btn_ok = QPushButton('Ответить')
RadioGroup = QButtonGroup()
RadioGroup.addButton(btn_answer1)
RadioGroup.addButton(btn_answer2)
RadioGroup.addButton(btn_answer3)
RadioGroup.addButton(btn_answer4)

lb_Question = QLabel('Самый сложный вопрос в мире!')
RadioGroupBox = QGroupBox('Варианты ответов:')
layoutH1 = QHBoxLayout()
layoutV2 = QVBoxLayout()
layoutV3 = QVBoxLayout()
layoutH1.addWidget(lb_Question)
layoutV2.addWidget(btn_answer1)
layoutV2.addWidget(btn_answer2)
layoutV3.addWidget(btn_answer3)
layoutV3.addWidget(btn_answer4)
layoutH1.addLayout(layoutV2)
layoutH1.addLayout(layoutV3)
RadioGroupBox.setLayout(layoutH1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('Прав ты или нет?')
lb_Correct = QLabel('ответ будет  тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment = (Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment = Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment = (Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
RadioGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_ok, stretch=2)
layout_line3.addStretch(1)

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)


def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_ok.setText('Следующий вопрос')
def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_ok.setText('Ответить')
    RadioGroup.setExclusive(False)
    btn_answer1.setChecked(False)
    btn_answer2.setChecked(False)
    btn_answer3.setChecked(False)
    btn_answer4.setChecked(False)
    RadioGroup.setExclusive(True)
answers = [btn_answer1, btn_answer2, btn_answer3, btn_answer4]
def ask(q: Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    show_question()
def check_answer():
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неправильно')
def show_correct(res):
    lb_Result.setText(res)
    show_result()

main_win.cur_question = -1

def next_question():
    main_win.cur_question += 1
    if main_win.cur_question >= len(questions_list):
         main_win.cur_question = 0
    q = questions_list
    q = questions_list[main_win.cur_question]
    ask(q)

def click_ok():
    if btn_ok.text() == 'Ответить':
        check_answer()
    else:
        next_question()
    

btn_ok.clicked.connect(click_ok)
next_question()
btn_ok.clicked.connect(check_answer)
main_win.show()
app.exec_()
