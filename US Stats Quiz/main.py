import os
import turtle
import pandas
from create_state import Write_State

os.system('cls')


# Main program
screen = turtle.Screen()
screen.title('U.S States Game')

mapa_path = r'US Stats Quiz\blank_states_img.gif'
file_path = r'US Stats Quiz\50_states.csv'

turtle.bgpic(mapa_path)
read_data = pandas.read_csv(file_path)

score = 0
guessed_states = []

while score < 50:
    answer_state = screen.textinput(title=f'{score}/50 Adivinhe o Estado', prompt="Digite o nome de um estado do EUA ").title()

    data_frame = read_data[read_data.state == answer_state]

    if answer_state == 'Exit':
        missing_states = [state for state in read_data.state if state not in guessed_states]
        new_data = pandas.DataFrame({'not guessed': missing_states})
        new_data.to_csv(r'US Stats Quiz/states_to_learn.csv') # creat file 
        break
    else:
        if not data_frame.empty:
            if not answer_state in guessed_states:
                score += 1
                Write_State(answer_state, (int(data_frame.x), int(data_frame.y)))
                guessed_states.append(answer_state)
            else:
                print(f'{answer_state}, já foi descoberto!')
        else:
            print('OPS! Você deixou em branco e/ou estado não encontrado!')
