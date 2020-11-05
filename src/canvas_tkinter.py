import tkinter as tk
import canvas_api_handler
from functools import partial
import webbrowser
import ciso8601
import time
import datetime
from PIL import ImageTk, Image



class access_window():

	def __init__(self):
		self.token = ""
		self.window_choice = -1


	def get_window_choice(self):
		return self.window_choice

	#returns the access token entered at the start window
	def get_access_token(self):
		return self.token

	#Creates the start window with widgets
	def draw_window(self):
		self.root = tk.Tk()
		self.root.title("Canvas Student Companion")
		self.root.geometry("400x400")

		self.root.configure(bg='#262626')

		path = "canvas_pic.png"
		img = ImageTk.PhotoImage(Image.open("canvas_pic.png"))
		panel = tk.Label(self.root,background="#262626", image = img)
		panel.place(x=100 ,y=280)

		#sets access token, if access token is valid, window is destroyed and class window displayed
		def set_access_token():

			self.token = entry.get()
			if self.token != "":
				self.window_choice = 1
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
		self.token = token
		self.course_dictionary = course_dictionary
		self.window_choice = -1
		self.course_name_id = []
		self.course_name_id.append("")
		self.course_name_id.append("")

	def get_window_choice(self):
		return self.window_choice


	def get_course_name_id(self):
		return self.course_name_id


	def draw_window(self):
		self.window_choice = -1
		self.root = tk.Tk()
		self.root.title("Canvas Courses")
		self.root.geometry("550x400")
		self.root.configure(bg='#262626')				

		def assignment_click(self, index):
			self.course_name_id[0] = (course_dictionary['course_names'][index])
			self.course_name_id[1] = (course_dictionary['course_ids'][index])
			self.window_choice = 2
			self.root.destroy() 

		def announcement_click(self, index):
			self.course_name_id[0] = (course_dictionary['course_names'][index])
			self.course_name_id[1] = (course_dictionary['course_ids'][index])
			self.window_choice = 3
			self.root.destroy()


		path = "canvas_pic.png"
		img = ImageTk.PhotoImage(Image.open("canvas_pic.png"))
		panel = tk.Label(self.root,background="#262626", image = img)
		panel.place(x=450 ,y=15)

		course_name_pos = 80

		label = tk.Label(
    		text="CANVAS COURSES",
    		foreground="#8c8c8c",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai 20 bold")
		)
		label.place(x=20, y=20)

		

		for index, name in enumerate(course_dictionary['course_names']):

			label = tk.Label(
    			text= name,
    			foreground="#ffa31a",  
    			background="#262626",  
    			font = ("Monokai",8)
			)

			label.place(x=20, y=course_name_pos)

			button = tk.Button(
    			text= "assignments",
    			foreground="#ffa31a",  # Set the text color to white
    			background="#262626",  # Set the background color to black
    			font = ("Monokai",9),
    			command = partial(assignment_click, self, index)
			)
			button.place(x=325, y=course_name_pos)
			button1 = tk.Button(
    			text= "announcements",
    			foreground="#ffa31a",  # Set the text color to white
    			background="#262626",  # Set the background color to black
    			font = ("Monokai",9),
    			command = partial(announcement_click, self, index)
			)

			button1.place(x=325 + 100, y=course_name_pos)
			course_name_pos += 60
			

		self.root.mainloop()


class assignments_window():


	def __init__(self):
		self.course_name_id = []
		self.window_choice = -1
		self.assignment_dictionary = {}

	def set_assignment_dictionary(self, assignment_dictionary):
		self.assignment_dictionary = assignment_dictionary

	def set_course_name_id(self, course_name_id):
		self.course_name_id	= course_name_id

	def get_window_choice(self):
		return self.window_choice


	def draw_window(self):
		self.window_choice = -1				
		self.root = tk.Tk()
		self.root.title("Canvas assignments")
		

		label = tk.Label(
			text="CANVAS COURSES:",
    		foreground="#8c8c8c",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai 20 bold")
    	)

		def back_button_click(self):
			self.window_choice = 1
			self.root.destroy()

		def link_button_click(self, link):
			webbrowser.open(link, new=2)



		label = tk.Label(self.root, text = self.course_name_id[0] + " assignments", bg='#262626', fg='#ffa31a',font = ("Monokai 10 bold"))
		label.grid(row = 0, column = 0, sticky = "w",padx = 1, pady = 1)
		
		button = tk.Button(
    		text= "previous window",
    		foreground="#bb33ff",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai",9),
    		command = partial(back_button_click, self)
		)

		button.grid(row = 0, column = 2, sticky = "w",padx = 1, pady = 1)


		self.root.configure(bg='#262626')

		#for index, name in enumerate(self.assignment_dictionary['descriptions']):
		for index, name in enumerate(self.assignment_dictionary['link']):
			self.root.columnconfigure(0, weight=1)
			self.root.rowconfigure(index + 1, weight=1)

			button = tk.Button(self.root, text = name, bg='#262626', fg='#e60073', command = partial(link_button_click, self, name))
			button.grid(rowspan = 1 ,columnspan = 1, row = index + 1, column = 0, sticky = "w",padx = 1, pady = 1)

		for index, name in enumerate(self.assignment_dictionary['types']):
			self.root.columnconfigure(1, weight=1)
			self.root.rowconfigure(index + 1, weight=1)

			label = tk.Label(self.root, text= name, bg ='#262626', fg = '#00ccff' )
			label.grid(row = index + 1, column = 1, sticky = "w",padx = 1, pady = 1)

		for index, name in enumerate(self.assignment_dictionary['sub_status']):
			self.root.columnconfigure(2, weight=1)
			self.root.rowconfigure(index, weight=1)

			if name == True:
				label = tk.Label(self.root, text= 'submitted: ✓', bg ='#262626', fg = 'green' )
				label.grid(row = index + 1, column = 2, sticky = "w",padx = 1, pady = 1)
			else:
				label = tk.Label(self.root, text= 'submitted: X', bg ='#262626', fg = 'red' )
				label.grid(row = index + 1, column = 2, sticky = "w",padx = 1, pady = 1)

		self.root.mainloop()


class announcements_window():


	def __init__(self):
		self.course_name_id = []
		self.window_choice = -1
		self.announcements_dictionary = {}

	def set_announcements_dictionary(self, announcements_dictionary):
		self.announcements_dictionary = announcements_dictionary

	def set_course_name_id(self, course_name_id):
		self.course_name_id	= course_name_id

	def get_window_choice(self):
		return self.window_choice


	def draw_window(self):
		self.window_choice = -1				
		self.root = tk.Tk()
		self.root.title("Canvas announcements")
		

		label = tk.Label(
			text="CANVAS COURSES:",
    		foreground="#8c8c8c",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai 20 bold")
    	)

		def back_button_click(self):
			self.window_choice = 1
			self.root.destroy()

		def link_button_click(self, link):
			webbrowser.open(link, new=2)



		label = tk.Label(self.root, text = self.course_name_id[0] + " announcements", bg='#262626', fg='#ffa31a',font = ("Monokai 10 bold"))
		label.grid(row = 0, column = 0, sticky = "w",padx = 1, pady = 1)
		
		button = tk.Button(
    		text= "previous window",
    		foreground="#bb33ff",  # Set the text color to white
    		background="#262626",  # Set the background color to black
    		font = ("Monokai",9),
    		command = partial(back_button_click, self)
		)

		button.grid(row = 0, column = 2, sticky = "w",padx = 1, pady = 1)

		self.root.configure(bg='#262626')

		if self.announcements_dictionary['link']:
			for index, name in enumerate(self.announcements_dictionary['link']):
				self.root.columnconfigure(0, weight=1)
				self.root.rowconfigure(index + 1, weight=1)

				button = tk.Button(self.root, text = name, bg='#262626', fg='#e60073', command = partial(link_button_click, self, name))
				button.grid(rowspan = 1 ,columnspan = 1, row = index + 1, column = 0, sticky = "w",padx = 1, pady = 1)
		else:
			label = tk.Label(self.root, text = "No recent " + self.course_name_id[0] + " announcements", bg='#262626', fg= 'red',font = ("Monokai 15 bold"))
			label.grid(row = 1, column = 0, sticky = "w",padx = 1, pady = 3)

		if self.announcements_dictionary['date']:
			for index, name in enumerate(self.announcements_dictionary['date']):

				self.root.columnconfigure(1, weight=1)
				self.root.rowconfigure(index + 1, weight=1)

				label = tk.Label(self.root, text = "Date posted: " + str(ciso8601.parse_datetime(name).date().strftime('%m-%d-%y')), bg='#262626', fg='#00ccff')
				label.grid(rowspan = 1 ,columnspan = 1, row = index + 1, column = 1, sticky = "w",padx = 1, pady = 3)

				if (((ciso8601.parse_datetime(name).date().strftime('%m-%d-%y')) == ((datetime.date.today() - datetime.timedelta(days = 1)).strftime('%m-%d-%y'))) or ((ciso8601.parse_datetime(name).date().strftime('%m-%d-%y')) == (datetime.date.today().strftime('%m-%d-%y'))) or ((ciso8601.parse_datetime(name).date().strftime('%m-%d-%y')) == ((datetime.date.today() + datetime.timedelta(days = 1)).strftime('%m-%d-%y')))) :
					label = tk.Label(self.root, text = "new!", bg='#262626', fg='green')
					label.grid(rowspan = 1 ,columnspan = 2, row = index + 1, column = 2, sticky = "w",padx = 1, pady = 3)


		self.root.mainloop()





token = ""
course_dictionary = {}
institution_url = "https://ecu.instructure.com"

window_num = 0
access_win = access_window()
courses_win = courses_window(token, course_dictionary)
assignments_win = assignments_window()
announcements_win = announcements_window()

while window_num != -1:

	if window_num == 0:
		access_win.draw_window()
		token = access_win.get_access_token()
		course_dictionary = canvas_api_handler.return_course_info(institution_url, token)
		window_num = access_win.get_window_choice()

	elif window_num == 1:
		courses_win.draw_window()
		window_num = courses_win.get_window_choice()

	elif window_num == 2:
		assignments_win.set_course_name_id(courses_win.get_course_name_id())
		assignments_win.set_assignment_dictionary(canvas_api_handler.return_assignment_info(institution_url,token,str(courses_win.get_course_name_id()[1])))
		assignments_win.draw_window()
		window_num = assignments_win.get_window_choice()

	elif window_num == 3:
		announcements_win.set_course_name_id(courses_win.get_course_name_id())
		announcements_win.set_announcements_dictionary(canvas_api_handler.return_announcement_info(institution_url,token,str(courses_win.get_course_name_id()[1])))
		announcements_win.draw_window()
		window_num = announcements_win.get_window_choice()






