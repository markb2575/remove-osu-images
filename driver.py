import online, backgrounds, thumbnails

import PySimpleGUI as sg

def select_directory():
    layout = [
        [sg.Text('Remove All OSU! Images')],
        [sg.Text('Look in your "AppData\Local" directory.')],
        [sg.InputText(key='-DIR-'), sg.FolderBrowse()],
        [sg.Button('OK')]
    ]

    window = sg.Window('Select OSU! Directory', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED:
            window.close()
            return None
        if event == 'OK':
            # Ask for confirmation
            confirm = sg.PopupYesNo('Warning', 'This action cannot be reset. Do you want to proceed?', title='Confirm Action')
            if confirm == 'Yes':
                window.close()
                return values['-DIR-']
            else:
                window.close()
                return None

osudir = select_directory()
if osudir != None and osudir != "":
    backgrounds.remove_backgrounds(osudir)
    online.remove_online(osudir)
    thumbnails.remove_thumbnails(osudir)
