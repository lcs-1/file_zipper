import FreeSimpleGUI as sg
from zipcreator import myzip

# Define GUI layout
text1 = sg.Text("Select the Files to compress: ")
input1 = sg.InputText(key='file')  # Key for file input
choose_button1 = sg.FilesBrowse("Choose", key='file')  # Allow multiple files

text2 = sg.Text("Select destination folder: ")
input2 = sg.InputText(key='folder')  # Key for folder input
choose_button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")

window = sg.Window(
    "File Zipper",
    layout=[
        [text1, input1, choose_button1],
        [text2, input2, choose_button2],
        [compress_button]
    ]
)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:  # Close the window
        break

    if event == "Compress":
        # Get selected file paths and destination folder
        filepaths = values['file'].split(';')  # Split multiple files into a list
        folder = values['folder']

        # Check for empty inputs
        if not filepaths or not folder:
            sg.popup("Please select files and a destination folder.")
            continue

        try:
            # Compress selected files
            myzip(filepaths, folder)
            sg.popup("Compression completed successfully!")
        except Exception as e:
            sg.popup(f"An error occurred: {e}")

window.close()
