from tkinter import *
from tkinter import ttk
from orders_summary import *


class ViewAdminFeedback:
    def __init__(self, frame_view_feedcack):
        self.frame_view_feedcack = frame_view_feedcack
        # self.person = person
        self.treeView = ttk.Treeview(self.frame_view_feedcack)
        style = ttk.Style()
        style.theme_use("clam")
        self.treeView["columns"] = ["Name", "Q1)", "Q2)",
                                    "Q3)", "Q4)"]
        self.treeView.column("#0", width=0, stretch=NO)
        self.treeView.column("Name", minwidth=100, width=80,
                             stretch=NO, anchor=CENTER)
        self.treeView.column("Q1)", minwidth=100, width=100,
                             stretch=NO, anchor=CENTER)
        self.treeView.column("Q2)", minwidth=100, width=100,
                             stretch=NO, anchor=CENTER)
        self.treeView.column("Q3)", minwidth=100,
                             width=100, stretch=NO, anchor=CENTER)
        self.treeView.column("Q4)", minwidth=100,
                             width=120, stretch=YES, anchor=CENTER)
        self.treeView.heading("Name", text="Name")
        self.treeView.heading(
            "Q1)", text="Best category")
        self.treeView.heading("Q2)", text="Quality Rating")
        self.treeView.heading(
            "Q3)", text="Segment improvement")
        self.treeView.heading(
            "Q4)", text="Packaging intact")
        self.treeView.grid(row=0, column=0, sticky="we")
        self.updateText()

    def updateText(self):  # updating the text of feed view
        for i in feedback_complete.keys():
            append_name = list(feedback_complete[i])
            append_name.insert(0, i)
            self.treeView.insert(
                '', 'end', values=tuple(append_name))
