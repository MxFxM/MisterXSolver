import solver
import cities

# zero for unknown start station
start_station = 0

# possible moves:
# 1 = taxi
# 2 = bus
# 3 = subway
# 4 = black-ticket (any)
tickets = []


def taxi_ticket_clicked():
    tickets.append(1)
    ticket_label.setText(str(tickets))
def bus_ticket_clicked():
    tickets.append(2)
    ticket_label.setText(str(tickets))
def subway_ticket_clicked():
    tickets.append(3)
    ticket_label.setText(str(tickets))
def black_ticket_clicked():
    tickets.append(4)
    ticket_label.setText(str(tickets))
def solve_button_clicked():
    global start_station
    start_station = int(start_station_input.text())
    solver.solve(cities.london, start_station, tickets)
    result_label.setText(str(solver.solve(cities.london, start_station, tickets)))
def reset_button_clicked():
    global tickets
    tickets = []
    ticket_label.setText(str(tickets))

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout

app = QApplication([])
window = QWidget()

# textbox to enter starting location
start_station_input = QLineEdit()
start_station_input.setText('0')

taxi_ticket_button = QPushButton('Taxi')
taxi_ticket_button.clicked.connect(taxi_ticket_clicked)
bus_ticket_button = QPushButton('Bus')
bus_ticket_button.clicked.connect(bus_ticket_clicked)
subway_ticket_button = QPushButton('Subway')
subway_ticket_button.clicked.connect(subway_ticket_clicked)
black_ticket_button = QPushButton('Black')
black_ticket_button.clicked.connect(black_ticket_clicked)

# label to show tickets
ticket_label = QLabel('[]')

# button to reset
reset_button = QPushButton('Reset tickets')
reset_button.clicked.connect(reset_button_clicked)

# button to solve
solve_button = QPushButton('Solve')
solve_button.clicked.connect(solve_button_clicked)

# result label
result_label = QLabel('[]')

ticketmasterlayout = QVBoxLayout()

ticketslavelayout1 = QHBoxLayout()
ticketslavelayout1.addWidget(taxi_ticket_button)
ticketslavelayout1.addWidget(bus_ticket_button)

ticketslavelayout2 = QHBoxLayout()
ticketslavelayout2.addWidget(subway_ticket_button)
ticketslavelayout2.addWidget(black_ticket_button)

ticketmasterlayout.addWidget(QLabel('Start station (0 = unknown)'))
ticketmasterlayout.addWidget(start_station_input)
ticketmasterlayout.addLayout(ticketslavelayout1)
ticketmasterlayout.addLayout(ticketslavelayout2)
ticketmasterlayout.addWidget(ticket_label)
ticketmasterlayout.addWidget(reset_button)
ticketmasterlayout.addWidget(solve_button)
ticketmasterlayout.addWidget(result_label)

window.setLayout(ticketmasterlayout)
window.show()

app.exec_()