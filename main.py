#!/usr/bin/env python
import PySimpleGUI as sg
import random
import string
import operator

# Use a 2D Array
sg.theme('Light green 6')

headings = ['Name', 'Class Mark', 'Age', 'Homeroom Class']
data = [
    ['Jason', 31, 15, 'A'],
    ['John', 92, 16, 'B'],
    ['Ann', 77, 17, 'C'],
    ['Charlie', 18, 17, 'D'],
    ['Sarah', 55, 14, 'A'],
]

# table is a 2D array
# col_clicked is the column to sort by
def sort_table(table, col_clicked):
    try:
        # This takes the table and sorts everything given the column number (index)
        # Sorts table in place
        # operator.itemgetter returns column as an object
        table = sorted(table, key=operator.itemgetter(col_clicked))
    except Exception as e:
        sg.popup_error('Error in sort_table', 'Exception in sort_table', e)
    return table

# ------ Window Layout ------
layout = [[sg.Table(values=data, headings=headings, max_col_width=25,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    enable_events=True,
                    expand_x=True,
                    expand_y=True,
                    enable_click_events=True,           # Comment out to not enable header and other clicks
                    tooltip='This is a table')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout,
                   ttk_theme='clam',
                   resizable=True)

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    # If there's an event with a tuple, which can only a table will generate
    if isinstance(event, tuple):
        # TABLE CLICKED Event has value in format ('-TABLE=', '+CLICKED+', (row,col))
        if event[0] == '-TABLE-':
            # event[2][0] is the row
            # event[2][1] is the colum
            # If sure makes sure it's the statement and not the first column
            if event[2][0] == -1 and event[2][1] != -1:           # Header was clicked and wasn't the "row" column
                col_num_clicked = event[2][1]
                new_table = sort_table(data, col_num_clicked)
                window['-TABLE-'].update(new_table)
window.close()
