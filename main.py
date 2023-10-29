from PyQt5. QtWidgets import QApplication
from random import choice, shuffle
from time import sleep
app = QApplication([])

from m2 import *
from m3 import *

class Question:
    def __init__(self,question, answer, wrong_answer1, wrong_answer2, wrong_answer3):
        self.question = question
        self.answer = answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3
q1 = Question('Де знаходиться вавилон?', 'Ірак', 'Іран', 'Індія','Франція' )
q2 = Question('Коли почалася перша світова війна', 'В 1914 р.','В 1913 р.', 'В 1924 р.', 'В 1916')
q3 = Question('Що можна утримувати не торкаючись його руками','Дихання', 'Мовчання', 'Світло', '')
q4 = Question('З якого посуду нічого не можна їсти','З порожнього','З перевернутого', 'З гарячого', "З кам'яного")
q5 = Question('','','','','')
q6 = Question('','','','','')
q7 = Question('','','','','')
q8 = Question('','','','','')
q9 = Question('','','','','')
q10 = Question('','','','','')
radio_buttons = [rb_ans1, rb_ans2, rb_ans3, rb_ans4]
questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10]
def new_question():
    global cur_q
    cur_q = choice(questions)
    lb_question.setText(cur_q.question)
    lb_right_answer.setText(cur_q.question)
    shuffle(radio_buttons)
    radio_buttons[0].setText(cur_q.wrong_answer1)
    radio_buttons[1].setText(cur_q.wrong_answer2)
    radio_buttons[2].setText(cur_q.wrong_answer3)
    radio_buttons[3].setText(cur_q.answer)
    new_question()
def check():
    RadioGroup.setExclusive(False)
    for answer in radio_buttons:
        if answer.isChecked():
            if answer.text() == lb_right_answer.text():
                lb_result.setText('Правильно!')
                answer.setChecked(False)
                break
        else:
                lb_result.setText('Неправильно!')
    RadioGroup.setExclusive(True)
def click_ok():
    if btn_next.text() == 'Відповісти':
        check()
        gb_question.hide()
        gb_answer.show()
        btn_next.setText('Наступне питання')
    else:
        new_question()
        gb_question.show()
        gb_answer.hide()
        btn_next.setText('Відповісти')
btn_next.clicked.connecct(click_ok)
def rest():
    window.hide()
    n = sp_rest.value() * 60
    sleep(n)
    window.show()
btn_rest.clicked.connect(rest)
def clear():
    le_question.clear()
    le_right_ans.clear()
    le_wrong_ans1.clear()
    le_wrong_ans2.clear()
    le_wrong_ans3.clear()
btn_clear.clicked.connect(clear)
def add_question():
    new_q = Question(le_question.text(), le_right_ans.text(),
                     le_wrong_ans1.text(),
                     le_wrong_ans2.text(),
                     le_wrong_ans3.text(),)
    questions.append(new_q)
    clear()
btn_add_question.clicked.connect(add_question)
def menu_generation():
    menu_win.show()
    window.hide()
btn_menu.clicked.connect(menu_generation)
def back_menu():
    menu_win.hide()
    window.show()
btn_back.clicked.connect(back_menu)

window.show()
app.exec_()
