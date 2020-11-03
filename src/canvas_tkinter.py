import tkinter as tk
import canvas_api_handler

class access_window():

	def __init__(self):
		self.root = tk.Tk()
		self.root.title("Canvas Student Companion")
		self.root.geometry("400x400")
		self.root.configure(bg='#262626')
		self.token = ""

	#returns the access token entered at the start window
	def get_access_token(self):
		return self.token

	#Creates the start window with widgets
	def draw_window(self):	

		#sets access token, if access token is valid, window is destroyed and class window displayed
		def set_access_token():

			self.token = entry.get()

			if self.token != "":
				self.root.destroy()  
			
		#creates student companion label
		label = tk.Label(
    		text="CANVAS STUDENT COMPANION",
    		foreground="#8c8c8c",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai 17 bold")
		)
		label.place(x=20, y=100)


		#creates enter access token label
		label = tk.Label(
    		text="Enter access token here.",
    		foreground="#e6e6e6",  
    		background="#262626",  
    		font = ("Monokai",8)
		)
		label.place(x=138, y=225)


		#creates access token entry 
		entry_frame = tk.Frame(
    		master=self.root,
    		relief=tk.SUNKEN,
    		borderwidth=2
		)
		entry_frame.place(x=50, y=200)

		entry = tk.Entry(
    		master=entry_frame,
    		justify="center",
    		fg="#ffa31a",
    		bg="#333333",
    		width=50)
		entry.insert(0, "")
		entry.pack()


		#creates button
		button = tk.Button(
    		text="Submit Token",
    		width=10,
    		height=1,
    		bg="#262626",
    		fg="#e6e6e6",
    		command = set_access_token
    	
		)
		button.place(x=250, y=280)

		self.root.mainloop()



class courses_window():

	def __init__(self, token, course_dictionary):
		self.root = tk.Tk()
		self.root.title("Canvas Courses")
		self.root.geometry("500x500")
		self.root.configure(bg='#262626')
		self.token = token
		self.course_dictionary = course_dictionary


	def draw_window(self):				

		course_name_pos = 60

		label = tk.Label(
    		text="CANVAS COURSES:",
    		foreground="#8c8c8c",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai 17 bold")
		)
		label.place(x=20, y=20)


		for name in course_dictionary['course_names']:

			label = tk.Label(
    			text= name,
    			foreground="#e6e6e6",  # Set the text color to white
    			background="#262626",  # Set the background color to black
    			font = ("Monokai",9)
			)
			label.place(x=30, y=course_name_pos)
			course_name_pos += 30


		self.root.mainloop()




institution_url = "https://ecu.instructure.com"


access_win = access_window()
access_win.draw_window()

token = access_win.get_access_token()
course_dictionary = canvas_api_handler.return_course_info(institution_url, token)


courses_win = courses_window(token, course_dictionary)
courses_win.draw_window()


