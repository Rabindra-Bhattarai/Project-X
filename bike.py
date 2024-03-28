import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import os

class BikeTestApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Bike Driving Written Test")  # Updated heading

        self.heading_frame = tk.Frame(self.master)
        self.heading_frame.pack()

        self.questions_frame = tk.Frame(self.master)
        self.questions_frame.pack()

        self.option_var = [tk.IntVar() for _ in range(10)]  # One variable for each question

        self.questions = [
            {
                "prompt": "1. What should you do when approaching a stop sign?",
                "options": ["Stop completely", "Slow down and proceed if clear", "Speed up"],
                "correct_option": 0
            },
            {
                "prompt": "2. What does a yellow traffic light indicate?",
                "options": ["Speed up", "Stop", "Proceed with caution"],
                "correct_option": 2
            },
            {
                "prompt": "3. When should you use your high beams?",
                "options": ["In foggy conditions", "At night when no other cars are present", "In heavy traffic"],
                "correct_option": 1
            },
            {
                "prompt": "4. What should you do if you are being tailgated?",
                "options": ["Speed up", "Brake suddenly", "Move to the right lane if possible and let the vehicle pass"],
                "correct_option": 2
            },
            {
                "prompt": "5. When can you pass a vehicle on the right?",
                "options": ["When the vehicle ahead is making a left turn", "When the vehicle ahead is traveling below the speed limit", "When the vehicle ahead is going straight and there is an open lane"],
                "correct_option": 0
            },
            {
                "prompt": "6. What does a flashing red traffic light mean?",
                "options": ["Stop", "Slow down and proceed with caution", "Proceed if clear"],
                "correct_option": 0
            },
            {
                "prompt": "7. When should you yield the right-of-way to pedestrians?",
                "options": ["At all times", "Only when they are in a marked crosswalk", "Only when traffic lights indicate to yield"],
                "correct_option": 0
            },
            {
                "prompt": "8. What is the first thing you should do if your vehicle starts to skid?",
                "options": ["Brake hard", "Steer in the direction you want to go", "Pump the brakes"],
                "correct_option": 1
            },
            {
                "prompt": "9. When should you use your turn signal?",
                "options": ["Only when changing lanes", "Only when turning", "When changing lanes, turning, or pulling away from the curb"],
                "correct_option": 2
            },
            {
                "prompt": "10. What does a white line across a lane of traffic mean?",
                "options": ["Stop line", "Pedestrian crossing", "Lane change or turn lane ahead"],
                "correct_option": 0
            }
            # Add more questions as needed
        ]

        self.create_widgets()

    def create_widgets(self):
        # Heading
        heading_label = tk.Label(self.heading_frame, text="Bike Driving Written Exam", font=("Arial", 18, "bold"))
        heading_label.pack(pady=10)

        # Go Back Button
        go_back_button = tk.Button(self.master, text="Go Back", command=self.go_back)
        go_back_button.place(relx=1, rely=0, anchor='ne')

        # Questions
        for i, question in enumerate(self.questions):
            question_label = tk.Label(self.questions_frame, text=question["prompt"], wraplength=600, font=("Arial", 12), anchor="w")
            question_label.grid(row=i, column=0, sticky="w", padx=10, pady=5)
            for j, option in enumerate(question["options"]):
                option_button = ttk.Radiobutton(self.questions_frame, text=option, variable=self.option_var[i], value=j)
                option_button.grid(row=i, column=j+1, sticky="w", padx=10, pady=5)

        # Submit Button
        submit_button = tk.Button(self.master, text="Submit", command=self.show_answers)
        submit_button.pack(pady=10)

        # Answers Label
        self.answers_label = tk.Label(self.master, text="", wraplength=800, font=("Arial", 12), anchor="w")
        self.answers_label.pack()

    def show_answers(self):
        num_correct = 0
        answers_text = ""
        for i, question in enumerate(self.questions):
            selected_option = self.option_var[i].get()
            if selected_option == question["correct_option"]:
                num_correct += 1
                answers_text += f"Question {i+1}: Correct\n"
            else:
                correct_option_text = question["options"][question["correct_option"]]
                selected_option_text = question["options"][selected_option]
                answers_text += f"Question {i+1}: Incorrect. Correct answer: {correct_option_text}. Your answer: {selected_option_text}\n"

        answers_text += f"\nYou got {num_correct} out of {len(self.questions)} questions correct."
        self.answers_label.config(text=answers_text)

    def go_back(self):
        # Close the current window
        self.master.destroy()
        
        # Open the dashboard.py file
        os.system('python dashboard.py')

def main():
    root = tk.Tk()
    app = BikeTestApp(root)
    root.geometry("1600x1260")  # Set the initial size of the window
    root.mainloop()

if __name__ == "__main__":
    main()
