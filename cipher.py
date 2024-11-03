import tkinter as tk
#main function for the encryption and decryption
def caesar_cipher(text, shift):
    encrypted_text = ""
    #checks if the input is valid
    for char in text:
        #checks if the character is a letter
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted_text += shifted_char
        else:
            #if the character is not a letter, it will be added to the encrypted text as is
            encrypted_text += char
    return encrypted_text
#main function for the encryption and decryption
def encrypt_decrypt():
    #gets the input text, shift, and operation
    text = input_text.get()
    shift = int(shift_entry.get())
    operation = operation_var.get()
    #checks if the operation is encryption or decryption
    if operation == "Encrypt":
        create_tape_labels(text)
        animate_encryption(text, shift)
    else:
        create_tape_labels(text)
        animate_decryption(text, shift)
#animation for the encryption and decryption
def animate_encryption_or_decryption(text, shift, is_encrypting):
    tape = list(text)
    tape_length = len(tape)
    current_index = 0 if is_encrypting else tape_length - 1
    #checks if the operation is encryption or decryption
    def move_right_or_left():
        nonlocal current_index
        current_index = (current_index + 1 if is_encrypting else current_index - 1) % tape_length
        label_tape[current_index].configure(bg='green' if is_encrypting else 'yellow')
        root.after(500, process_character)
    #processes the character in the tape
    def process_character():
        nonlocal current_index
        #checks if the character is a letter and shifts it
        char = tape[current_index]
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            if not is_encrypting:
                #if the operation is decryption, the shift will be subtracted (to the left)
                shifted_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            else:
                #if the operation is encryption, the shift will be added (to the right)
                shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            tape[current_index] = shifted_char
            label_tape[current_index].configure(text=shifted_char)
        label_tape[current_index].configure(bg='white')

        #this segment of the code handles the logic on when to stop the animation
        #checks if the current index is the last index of the tape
        if current_index == tape_length - 1 and is_encrypting:
            print("current ind: ", current_index, " haba ng tape: ", tape_length - 1)
            return  # Stop animation
        elif current_index == 0 and not is_encrypting:
            #checks if the current index is the first index of the tape
            print("current ind: ", current_index, " tape length: ", tape_length - 1)
            return
        #moves the tape to the right or left
        move_right_or_left()
    #starts the animation
    label_tape[current_index].configure(bg='green' if is_encrypting else 'yellow')
    root.after(500, process_character)
#animation for the encryption
def animate_encryption(text, shift):
    animate_encryption_or_decryption(text, shift, True)
#animation for the decryption
def animate_decryption(text, shift):
    animate_encryption_or_decryption(text, shift, False)


# Set up window
root = tk.Tk()
root.title("Automatoes - Final Project")
root.geometry("400x350")
root.configure(bg="black")

# Set window icon
icon_path = "F:\Modules\AUTOMATO\\tomatoicon.png"  # Replace with the actual path to your icon file
icon_image = tk.PhotoImage(file=icon_path)
root.iconphoto(True, icon_image)

# Header
header_label = tk.Label(root, text="Caesar Cipher x Turing Machine", font=("Gotham", 16, "bold"), bg="black", fg="white")
header_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#808080")
input_frame.pack(pady=10)

input_label = tk.Label(input_frame, text="Enter Text:", font=("Gotham", 12), bg="#282828", fg="white")
input_label.pack(side="left")

input_text = tk.Entry(input_frame, width=30, font=("Gotham", 12))
input_text.pack(side="left")

shift_frame = tk.Frame(root, bg="#808080")
shift_frame.pack(pady=10)

shift_label = tk.Label(shift_frame, text="Shift:", font=("Gotham", 12), bg="#282828", fg="white")
shift_label.pack(side="left")

shift_entry = tk.Entry(shift_frame, width=5, font=("Gotham", 12))
shift_entry.pack(side="left")

operation_var = tk.StringVar()
operation_var.set("Encrypt")

operation_frame = tk.Frame(root, bg="#808080")
operation_frame.pack(pady=10)

encrypt_radio = tk.Radiobutton(operation_frame, text="Encrypt", variable=operation_var, value="Encrypt", font=("Gotham", 12), bg="white", fg="Green")
encrypt_radio.pack(side="left")

decrypt_radio = tk.Radiobutton(operation_frame, text="Decrypt", variable=operation_var, value="Decrypt", font=("Gotham", 12), bg="white", fg="Green")
decrypt_radio.pack(side="left")

tape_frame = tk.Frame(root, bg="#808080")
tape_frame.pack(pady=10)

label_tape = []

def create_tape_labels(text):
    tape_length = len(text)
    for i in range(tape_length):
        label = tk.Labellabel = tk.Label(tape_frame, text=text[i], relief="solid", width=3, padx=10, pady=10, bg="#E0E0E0", font=("Gotham", 12))
        label.grid(row=0, column=i)
        label_tape.append(label)


encrypt_decrypt_button = tk.Button(root, text="Encrypt/Decrypt", command=encrypt_decrypt)
encrypt_decrypt_button.pack()

root.mainloop()
