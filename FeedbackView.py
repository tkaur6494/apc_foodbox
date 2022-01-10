from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from Person import Person
from Week import Week
from Plate import Plate
from Stock import Stock
from UserView import UserView
from ViewOrder import ViewOrder
from orders_summary import *
from tkinter import messagebox


class FeedbackView:
    # feedback view questions to be show for feedback
    # Showing name of person who has logged in and asking 4 questions for feedback
    def __init__(self, frame_feedback_user_view, person):
        self.frame_feedback_user_view = frame_feedback_user_view
        self.person = person
        self.response = []
        welcome_text_label = Label(
            frame_feedback_user_view, text="Hi "+person.get_name())  # displaying name of person who has logged in
        welcome_text_label.grid(row=0, column=0, pady=10)
        question1_text_label = Label(
            frame_feedback_user_view, text="Q1) What do you love the most about our food?")  # labels for questions
        question1_text_label.grid(row=1, column=0, pady=10)
        self.question1_answer_choice = ttk.Combobox(frame_feedback_user_view,  values=(  # using combobox for dropdown
            "A. Protein",  "B. Vegetables",  "C. Dessert",  "D. Spice"))
        self.question1_answer_choice.grid(row=1, column=2)
        question2_text_label = Label(
            frame_feedback_user_view, text="Q2) How do you rate our quality?")  # labels for questions
        question2_text_label.grid(row=3, column=0)
        self.question2_answer_choice = ttk.Combobox(frame_feedback_user_view,  values=(  # using combobox for dropdown
            "A. *",  "B. **",  "C. ***",  "D. ****"))
        self.question2_answer_choice.grid(row=3, column=2, pady=10)
        question3_text_label = Label(  # labels for questions
            frame_feedback_user_view, text="Q3) Which segment do you consider worth improving for our service?")
        question3_text_label.grid(row=4, column=0)
        self.question3_answer_choice = ttk.Combobox(frame_feedback_user_view,  values=(
            "A. Protein",  "B. Vegetables",  "C. Dessert",  "D. Spice"))  # using combobox for dropdown
        self.question3_answer_choice.grid(row=4, column=2,  pady=10)
        question4_text_label = Label(
            frame_feedback_user_view, text="Q4) Was the packaging intact when you did the takeout from the restaurant? ")
        question4_text_label.grid(row=5, column=0)
        self.question4_answer_choice = ttk.Combobox(frame_feedback_user_view,  values=(
            "A. Yes",  "B. No",))
        self.question4_answer_choice.grid(row=5, column=2,  pady=10)
        self.button_submit = Button(  # submit button
            frame_feedback_user_view,
            text="Submit",
            command=lambda: self.submit_feedback(),  # function called on click
        )
        self.button_submit.grid(row=6, column=2)

    # submitting feedback and storing it in the feedback file
    # clearing the form after feedback has been submitted successfully
    def submit_feedback(self):
        # adding the response to the end of list
        self.response.append(self.question1_answer_choice.get())
        # adding the response to the end of list
        self.response.append(self.question2_answer_choice.get())
        # adding the response to the end of list
        self.response.append(self.question3_answer_choice.get())
        # adding the response to the end of list
        self.response.append(self.question4_answer_choice.get())
        messagebox.showinfo(
            "Success", "Your feedback has been submitted successfully")  # notification for successful submission
        self.question1_answer_choice.delete("0", "end")  # clearing the form
        self.question2_answer_choice.delete("0", "end")  # clearing the form
        self.question3_answer_choice.delete("0", "end")  # clearing the form
        self.question4_answer_choice.delete("0", "end")  # clearing the form
        # setting the feedback in the main person class
        self.person.set_response(self.response)
        feedback_complete[self.person.name] = self.response
        # adding feedback to the file so that admin can view all feedbacks
        pickle.dump(feedback_complete, open(FEEDBACK_USER_FILE, "wb"))
