import requests
import json

#user_token1 = "enter access token string here"

institution_url = "https://ecu.instructure.com"


#returns a dictionary, with a list of courses, and a list of course ids. 
#Parameters are the unique url for users institution, and unique user access token.
def return_course_info(institution_url, user_token):
	info_dict = {}
	url = institution_url + "/api/v1/courses?enrollment_type=student&enrollment_state=active&" + "access_token=" +  user_token 
	requestPackage = requests.get(url)
	json_list = json.loads(requestPackage.text)

	info_dict['course_names'] = []
	info_dict['course_ids'] = []

	for item in json_list:
		for key,value in item.items():
			if key == "name" and item["name"] != "Student Affairs Resources":
				info_dict['course_names'].append(value)
			elif item["name"] == "Student Affairs Resources":
				break
			elif key == "id":
				info_dict['course_ids'].append(value)

	return info_dict


#Returns a dictionary, with a list of a single course's information.
#Information is the description, due date, submission status, type, and point value.
#Parameters are the unique url for users institution, and unique user access token, and the course id.
def return_assignment_info(institution_url, user_token, course_id):
	info_dict = {}
	url = institution_url + "/api/v1/courses/" + course_id + "/assignments?" + "access_token=" +  user_token 
	requestPackage = requests.get(url)
	json_list = json.loads(requestPackage.text)

	info_dict['descriptions'] = []
	info_dict['due_dates'] = []
	info_dict['sub_status'] = []
	info_dict['types'] = []
	info_dict['points'] = []
	info_dict['link'] = []

	for item in json_list:
		for key,value in item.items():
			if key == "description":
				info_dict['descriptions'].append(value)
			elif key == "due_at":
				info_dict['due_dates'].append(value)
			elif key == "has_submitted_submissions":
				info_dict['sub_status'].append(value)
			elif key == "submission_types":
				info_dict['types'].append(value)
			elif key == "points_possible":
				info_dict['points'].append(value)
			elif key == "html_url":
				info_dict['link'].append(value)

	return info_dict

#Returns a dictionary, with a list of a single course's announcement information.
#Announcement information is the title, date posted, and the message.
#Parameters are the unique url for users institution, and unique user access token, and the course id.
def return_announcement_info(institution_url, user_token, course_id):
	info_dict = {}
	url = institution_url + "/api/v1/announcements?context_codes[]=course_" + course_id + "&" + "access_token=" + user_token 
	requestPackage = requests.get(url)
	json_list = json.loads(requestPackage.text)

	info_dict['title'] = []
	info_dict['date'] = []
	info_dict['message'] = []

	for item in json_list:
		for key,value in item.items():
			if key == "title":
				info_dict['title'].append(value)
			elif key == "posted_at":
				info_dict['date'].append(value)
			elif key == "message":
				info_dict['message'].append(value)

	return info_dict			





