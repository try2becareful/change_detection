import PySimpleGUI as sg

sg.theme('DarkAmber')  # theme color


# First window
def make_win1():
    layout = [
        [sg.Text('File before'), sg.InputText(), sg.FileBrowse(),
         ],
        [sg.Text('File after'), sg.InputText(), sg.FileBrowse(),
         ],
        [sg.Button("OK"), sg.Button("Exit")]
    ]
    return sg.Window('Change Detection', layout, location=(800, 600), finalize=True)


# Result window
def make_win2():
    layout = [
        [
            sg.Image("ggg.png", size=(800, 600), key="-IMAGE-"), sg.Button("Exit")
        ]
    ]
    return sg.Window('Result', layout, finalize=True)


# Main
window1, window2 = make_win1(), None  # start off with 1 window open
while True:  # Event Loop
    window, event, values = sg.read_all_windows()
    f1 = open(values[0], 'r')
    f2 = open(values[1], 'r')
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:  # if closing win 2, mark as closed
            window2 = None
        elif window == window1:  # if closing win 1, exit program
            break
    elif event == 'OK' and not window2:
        window2 = make_win2()
window.close()
