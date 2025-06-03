import tkinter as tk
from tkinter import messagebox
from random import randint
import pygame
import os

# Initialize pygame mixer for sound
pygame.mixer.init()

# Sound file paths (add your own .wav files in the sound folder)
CORRECT_SOUND = os.path.join('sound', 'correct.wav')
WRONG_SOUND = os.path.join('sound', 'wrong.wav')

class NumberGuessApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Number Guessing Game')
        self.root.geometry('400x500')
        self.root.configure(bg='#22223b')
        self.number = randint(1, 100)
        self.tries = 0
        self.create_widgets()

    def create_widgets(self):
        self.title_label = tk.Label(self.root, text='🎲 Number Guessing Game 🎲', font=('Arial Rounded MT Bold', 22, 'bold'), fg='#f2e9e4', bg='#22223b')
        self.title_label.pack(pady=25)

        self.instruction = tk.Label(self.root, text='Guess a number between 1 and 100', font=('Arial', 15, 'italic'), fg='#c9ada7', bg='#22223b')
        self.instruction.pack(pady=8)

        self.entry = tk.Entry(self.root, font=('Arial', 18, 'bold'), width=8, justify='center', bg='#f2e9e4', fg='#22223b', relief='solid', bd=2)
        self.entry.pack(pady=8)
        self.entry.focus()

        self.guess_btn = tk.Button(self.root, text='🎯 Guess', font=('Arial', 15, 'bold'), bg='#06d6a0', fg='#22223b', activebackground='#f9c74f', activeforeground='#22223b', command=self.check_guess, relief='raised', bd=4, cursor='hand2')
        self.guess_btn.pack(pady=10)
        self.guess_btn.bind('<Enter>', lambda e: self.guess_btn.config(bg='#f9c74f'))
        self.guess_btn.bind('<Leave>', lambda e: self.guess_btn.config(bg='#06d6a0'))

        self.result_label = tk.Label(self.root, text='', font=('Arial', 15, 'bold'), fg='#9a8c98', bg='#22223b')
        self.result_label.pack(pady=10)

        self.tries_label = tk.Label(self.root, text='Attempts: 0', font=('Arial', 13, 'bold'), fg='#c9ada7', bg='#22223b')
        self.tries_label.pack(pady=5)

        self.reset_btn = tk.Button(self.root, text='🔄 Restart Game', font=('Arial', 12, 'bold'), bg='#22223b', fg='#f2e9e4', activebackground='#f28482', activeforeground='#22223b', command=self.reset_game, relief='groove', bd=3, cursor='hand2')
        self.reset_btn.pack(pady=18)
        self.reset_btn.bind('<Enter>', lambda e: self.reset_btn.config(bg='#f28482'))
        self.reset_btn.bind('<Leave>', lambda e: self.reset_btn.config(bg='#22223b'))

        self.root.bind('<Return>', lambda event: self.check_guess())

    def play_sound(self, sound_path, loops=0):
        if os.path.exists(sound_path):
            pygame.mixer.music.load(sound_path)
            pygame.mixer.music.play(loops=loops)

    def animate_button(self, button):
        orig_color = button.cget('bg')
        button.config(bg='#f9c74f')
        button.after(150, lambda: button.config(bg=orig_color))

    def check_guess(self):
        self.animate_button(self.guess_btn)
        guess = self.entry.get()
        if not guess.isdigit():
            self.result_label.config(text='❗ Please enter a valid number!', fg='#f28482')
            self.play_sound(WRONG_SOUND)
            return
        guess = int(guess)
        self.tries += 1
        self.tries_label.config(text=f'Attempts: {self.tries}')
        if guess == self.number:
            self.result_label.config(text=f'🎉 Correct! You guessed it in {self.tries} tries.', fg='#06d6a0')
            self.play_sound(CORRECT_SOUND)
            self.animate_button(self.guess_btn)
            messagebox.showinfo('Congratulations!', f'You guessed the number in {self.tries} tries!')
            self.reset_game()
        elif guess < self.number:
            self.result_label.config(text='⬇️ Too low! Try again.', fg='#f28482')
            self.play_sound(WRONG_SOUND)
        else:
            self.result_label.config(text='⬆️ Too high! Try again.', fg='#f28482')
            self.play_sound(WRONG_SOUND)

    def reset_game(self):
        self.animate_button(self.reset_btn)
        self.number = randint(1, 100)
        self.tries = 0
        self.tries_label.config(text='Attempts: 0')
        self.result_label.config(text='')
        self.entry.delete(0, tk.END)
        self.entry.focus()

if __name__ == '__main__':
    root = tk.Tk()
    app = NumberGuessApp(root)
    root.mainloop()
