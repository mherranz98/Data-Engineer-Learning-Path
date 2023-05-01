from tkinter import ttk
from tkinter.messagebox import showinfo
import tkinter


class Credentials:

    def __init__(self) -> None:
        self.getCredentials = "getCredentials"

    def getCredentials(platform, field1, field2):
        """Request login credentials using a GUI."""

        root = tkinter.Tk()
        root.eval('tk::PlaceWindow . center')
        root.title('Access ' + platform)
        uv = tkinter.StringVar(root, value="")
        pv = tkinter.StringVar(root, value="")
        tkinter.Label(root, text=field1)
        tkinter.Label(root, text=field2)
        userEntry = tkinter.Entry(root, bd=3, width=25, textvariable=uv)
        passEntry = tkinter.Entry(
            root, bd=3, width=25, show="*", textvariable=pv)
        btnClose = tkinter.Button(root, text="Submit", command=root.destroy)
        userEntry.pack(padx=100, pady=20)
        passEntry.pack(padx=100, pady=20)
        btnClose.pack(padx=50, pady=5, side=tkinter.TOP, anchor=tkinter.NE)
        root.mainloop()

        return [uv.get(), pv.get()]

    def login_clicked():
        """Request login credentials using a GUI."""

        import tkinter as tk
        # root window
        root = tk.Tk()
        root.geometry("300x150")
        root.resizable(False, False)
        root.title('Access __')
        root.eval('tk::PlaceWindow . center')

        # store email address and password
        email = tk.StringVar()
        password = tk.StringVar()

        # Sign in frame
        signin = ttk.Frame(root)
        signin.pack(padx=10, pady=10, fill='x', expand=True)

        # email
        email_label = ttk.Label(signin, text="Email Address:")
        email_label.pack(fill='x', expand=True)

        email_entry = ttk.Entry(signin, textvariable=email)
        email_entry.pack(fill='x', expand=True)
        email_entry.focus()

        # password
        password_label = ttk.Label(signin, text="Password:")
        password_label.pack(fill='x', expand=True)

        password_entry = ttk.Entry(signin, textvariable=password, show="*")
        password_entry.pack(fill='x', expand=True)

        # login button
        login_button = ttk.Button(signin, text="Submit", command=root.destroy)
        login_button.pack(fill='x', side=tkinter.TOP,
                          anchor=tkinter.NE, expand=True)

        #msg = f'You entered email: {email.get()} and password: {password.get()}'
        #showinfo(title='Information', message=msg)
        root.mainloop()

        return [email.get(), password.get()]
