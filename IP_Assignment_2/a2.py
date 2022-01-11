# Assignment - 2
# Name - Anas Ahmad
# Roll No - 2020023
import json
'''
- This is the skeleton code, wherein you have to write the logic for each of the
functions defined below.
- DO NOT modify/delete the given functions. 
- DO NOT import any python libraries, except for the ones already included.
- DO NOT create any global variables in this module.
- DO NOT add print statements anywhere in this module.
- Make sure to return value as specified in the function description.
- Remove the pass statement from the functions when you implement them.
'''
def read_data_from_file(file_path="data.json"):
	"""
	**** DO NOT modify this function ****
	Description: Reads the data.json file, and converts it into a dictionary.
	Parameters:
	- file_path (STRING): The path to the file (with .json extension) which contains the initial database.
	 You can pass the file_path parameter as "data.json".
	Returns:
	- A dictionary containing the data read from the file
	"""
	with open(file_path, 'r') as data:
		records = json.load(data)
	return records

def filter_by_first_name(records, first_name):
	"""
	Description: Searches the records to find all persons with the given first name (case-insensitive)
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- first_name (STRING): The first name
	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given first name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	"""
	f = []
	if len(first_name) == 0:
		return f
	else:
		first_name = first_name.capitalize()
		for i in range(len(records)):
			if records[i]["first_name"] == first_name:
				f.append(records[i]["id"])
		return f

def filter_by_last_name(records, last_name):
	"""
	Description: Searches the records to find all persons with the given last name (case-insensitive)
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- last_name (STRING): The last name
	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given last name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	"""
	l1 = []
	if len(last_name) == 0:
		return l1
	else:
		last_name = last_name.capitalize()
		for i in range(len(records)):
			if records[i]["last_name"] == last_name:
				l1.append(records[i]["id"])
		return l1

def filter_by_full_name(records, full_name):
	"""
	Description: Searches the records to find all persons with the given full name (case-insensitive)
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- full_name (STRING): The full name (a single string with 2 space-separated words,
	 the first name and the last name respectively)
	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	"""
	fn = list(full_name.split())
	code = []
	if len(fn) == 0:
		return fn
	else:
		fn[0] = fn[0].capitalize()
		fn[1] = fn[1].capitalize()
		for i in range(len(records)):
			if records[i]["first_name"] == fn[0] and records[i]["last_name"] == fn[1]:
				code.append(records[i]["id"])
		return code

def filter_by_age_range(records, min_age, max_age):
	"""
	Description: Searches the records to find all persons whose age lies in the given age range [min_age, max_age]
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- min_age (INTEGER): The minimum age (inclusive)
	- max_age (INTEGER): The maximum age (inclusive)
	Note: 0 < min_age <= max_age
	Returns:
	- A list of INTEGERS denoting the IDs of the persons with the given full name
		Case 1: No person found => Returns an empty list
		Case 2: At least one person found => Returns a list containing the IDs of all the persons found
	"""
	code = []
	if 0 < min_age <= max_age:
		for i in range(len(records)):
			if min_age <= records[i]["age"] <= max_age:
				code.append(records[i]["id"])
		#if len(code) == 0:
		#	return code
		#else:
		return code
	else:
		return code

def count_by_gender(records):
	"""
	Description: Counts the number of males and females
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	Returns:
	- A dictionary with the following two key-value pairs:
		KEY        VALUE
		"male"     No of males (INTEGER)
		"female"   No of females (INTEGER)
	"""
	gender = {}
	count_m = 0
	count_f = 0
	for i in range(len(records)):
		if records[i]["gender"] == "male":
			count_m += 1
		elif records[i]["gender"] == "female":
			count_f += 1
	gender.update({"male": count_m, "female": count_f})
	return gender

def filter_by_address(records, address):
	"""
	Description: Filters the person records whose address matches the given address.
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- address (DICTIONARY): The keys are a subset of { "house_no", "block", "town", "city", "state", "pincode" }
	(case-insensitive)
		Some examples are:
			Case 1: {}
				=> All records match this case
			Case 2: { "block": "AD", "city": "Delhi" }
				=> All records where the block is "AD" and the city is "Delhi"
				(the remaining address fields can be anything)
			Case 3: { "house_no": 24, "block": "ABC", "town": "Vaishali",
			          "city": "Ghaziabad", "state": "Uttar Pradesh", "pincode": 110020 }
	Returns:
	- A LIST of DICTIONARIES with the following two key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
	"""
	l_d0 = []
	for v in address:
		if v == "block" or v == "city" or v == "state":
			address[v] = address[v].capitalize()
		elif v == "town":
			l0 = list(address[v].split(" "))
			for w in range(len(l0)):
				l0[w] = l0[w].capitalize()
			address[v] = " ".join(l0)
	for x in records:
		flag = 0
		for y in address:
			dic = {}
			if type(address[y]) == str:
				if address[y] == x["address"][y]:
					flag += 1
			elif type(address[y]) == int:
				if address[y] == x["address"][y]:
					flag += 1
			if flag == len(address):
				dic.update({"first_name": x["first_name"], "last_name": x["last_name"]})
				l_d0.append(dic)
	return l_d0

def find_alumni(records, institute_name):
	"""
	Description: Find all the alumni of the given institute name (case-insensitive).
	Note: A person is an alumnus of an institute only if the value of the "ongoing" field for that particular
	institute is False.
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- institute_name (STRING): Name of the institute (case-insensitive)
	Returns:
	- A LIST of DICTIONARIES with the following three key-value pairs:
		KEY            VALUE
		"first_name"   first name (STRING)
		"last_name"    last name (STRING)
		"percentage"   percentage (FLOAT)
	"""
	lste = []
	institute_name = institute_name.upper()
	for i in range(len(records)):
		for j in range(len(records[i]["education"])):
			if records[i]["education"][j]["institute"] == institute_name and records[i]["education"][j]["ongoing"] == False:
				dic9 = {"first_name": records[i]["first_name"], "last_name": records[i]["last_name"],
						"percentage": records[i]["education"][j]["percentage"]}
				lste.append(dic9)
				break
			else:
				continue
	return lste
def find_topper_of_each_institute(records):
	"""
	Description: Find topper of each institute
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	Returns:
	- A DICTIONARY with the institute name (STRING) as the keys and the ID (INTEGER) of the topper of that institute.
	Note: If there are `N` distinct institutes in records, the dictionary will contain `N` key-value pairs.
	The ongoing status does NOT matter. It is guaranteed that each institute will have exactly one topper.
	"""

	inst = {'TKRYTU': 0, 'LLDVY': 0, 'KVGLHL': 0, 'JWBTYC': 0, 'MAQZIES': 0, 'APTASAJ': 0, 'QNERCSS': 0,
			'EMCUYFH': 0, 'GSMJS': 0, 'NXTECJC': 0, 'SYLUH': 0, 'AKUZM': 0, 'KFBQTR': 0, 'EBUNL': 0, 'WGRCR': 0, 'ABCDEF':0, 'XGRCR':0}
	inst1 = {'TKRYTU': 0, 'LLDVY': 0, 'KVGLHL': 0, 'JWBTYC': 0, 'MAQZIES': 0, 'APTASAJ': 0, 'QNERCSS': 0,
			 'EMCUYFH': 0, 'GSMJS': 0, 'NXTECJC': 0, 'SYLUH': 0, 'AKUZM': 0, 'KFBQTR': 0, 'EBUNL': 0, 'WGRCR': 0, 'ABCDEF':0, 'XGRCR':0}
	for i in range(len(records)):
		for j in range(len(records[i]["education"])):
			if not records[i]["education"][j]["ongoing"]:
				if records[i]["education"][j]["institute"]:
					if records[i]["education"][j]["percentage"] > inst[records[i]["education"][j]["institute"]]:
						inst1[records[i]["education"][j]["institute"]] = records[i]["id"]
						inst[records[i]["education"][j]["institute"]] = records[i]["education"][j]["percentage"]
	return inst1

def find_blood_donors(records, receiver_person_id):
	"""
	Description: Find all donors who can donate blood to the person with the given receiver ID.
		Note:
		- Possible blood groups are "A", "B", "AB" and "O".
		Rules:
		BLOOD GROUP      CAN DONATE TO
		A                A, AB
		B                B, AB
		AB               AB
		O                A, B, AB, O
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- receiver_person_id (INTEGER): The ID of the donee
		Note: It is guaranteed that exactly one person in records will have the ID as receiver_person_id
	Returns:
	- A DICTIONARY with keys as the IDs of potential donors and values as a list of strings,
	denoting the contact numbers of the donor
	"""
	dic5 = {}
	for i in range(len(records)):
		if records[i]["id"] == receiver_person_id:
			blood = records[i].get("blood_group")
			del records[i]
			break

	for j in range(len(records)):
		if blood == "O":
			dic5.update({records[j]["id"]: records[j]["contacts"]})
		elif blood == "A":
			if records[j]["blood_group"] == "A" or records[j]["blood_group"] == "O":
				dic5.update({records[j]["id"]: records[j]["contacts"]})
		elif blood == "B":
			if records[j]["blood_group"] == "B" or records[j]["blood_group"] == "O":
				dic5.update({records[j]["id"]: records[j]["contacts"]})
		elif blood == "AB":
			if records[j]["blood_group"] == "AB" or records[j]["blood_group"] == "O":
				dic5.update({records[j]["id"]: records[j]["contacts"]})
		else:
			return dic5
	return dic5

def get_common_friends(records, list_of_ids):
	"""
	Description: Find the common friends of all the people with the given IDs
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- list_of_ids (LIST): A list of IDs (INTEGER) of all the people whose common friends are to be found
	Returns:
	- A LIST of INTEGERS containing the IDs of all the common friends of the specified list of people
	"""
	id_common = []
	for i in range(len(list_of_ids)):
		for j in range(i+1):
			if i != j and list_of_ids[i] != list_of_ids[j]:
				for e in records[list_of_ids[i]]["friend_ids"]:
					if e in records[list_of_ids[j]]["friend_ids"]:
						id_common.append(e)
			elif i != j and list_of_ids[i] == list_of_ids[j]:
				for e in records[list_of_ids[i]]["friend_ids"]:
					id_common.append(e)
		if len(id_common) >= 1:
			break
	for j in range(len(list_of_ids)):
		for i in id_common:
			if i in records[list_of_ids[j]]["friend_ids"]:
				continue
			else:
				id_common.remove(i)
				break
	return id_common

def is_related(records, person_id_1, person_id_2):
	"""
	**** BONUS QUESTION ****
	Description: Check if 2 persons are friends
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id_1 (INTEGER): first person ID
	- person_id_2 (INTEGER): second person ID
	Returns:
	- A BOOLEAN denoting if the persons are friends of each other, directly or indirectly
	(if A knows B, B knows C and C knows D, then A knows B, C and D).
	"""
	z = []
	def related(a, c):
		for b in records:
			if b["id"] == a:
				if c in b["friend_ids"]:
					z.append(person_id_1)
					return True
			elif len(b["friend_ids"]) == 0:
				return False
			else:
				for i in b["friend_ids"]:
					if i not in z:
						z.append(i)

						for j in records:
							if i == j["id"]:
								x = j["friend_ids"]
								for y in x:
									if y in z:
										x.remove(y)
								for v in x:
									if v != c:
										return related(v, c)
									elif v == c:
										z.append(v)
										return True

	return related(person_id_1, person_id_2)

def delete_by_id(records, person_id):
	"""
	Description: Given a person ID, this function deletes them from the records.Note that the given person can also
	be a friend of any other person(s),so also delete the given person ID from other persons friend list.
	If the person ID is not available in the records, you can ignore that case.
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	"""

	for i in range(len(records)):
		if records[i]["id"] == person_id:
			del records[i]
			break
	for j in range(len(records)):
		if person_id in records[j]["friend_ids"]:
			records[j]["friend_ids"].remove(person_id)

	return records

def add_friend(records, person_id, friend_id):
	"""
	Description: Given a person ID and a friend ID, this function makes them friends of each other.
	 If any of the IDs are not available, you can ignore that case.
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	"""
	for e in range(len(records)):
		if records[e]["id"] == person_id:
			if friend_id not in records[e]["friend_ids"]:
				records[e]["friend_ids"].extend([friend_id])
				records[e]["friend_ids"].sort()
				break
	for e in range(len(records)):
		if records[e]["id"] == friend_id:
			if person_id not in records[friend_id]["friend_ids"]:
				records[friend_id]["friend_ids"].extend([person_id])
				records[friend_id]["friend_ids"].sort()
	return records
def remove_friend(records, person_id, friend_id):
	"""
	Description: Given a person ID and a friend ID, this function removes them as friends of each other.
	 If any of the IDs are not available, you can ignore that case.
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- friend_id (INTEGER): The friend id
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	"""
	for e in range(len(records)):
		if records[e]["id"] == person_id:
			if friend_id in records[e]["friend_ids"]:
				records[person_id]["friend_ids"].remove(friend_id)
		else:
			continue
	for e in range(len(records)):
		if records[e]["id"] == friend_id:
			if person_id in records[e]["friend_ids"]:
				records[friend_id]["friend_ids"].remove(person_id)
		else:
			continue
	return records

def add_education(records, person_id, institute_name, ongoing, percentage):
	"""
	Description: Adds an education record for the person with the given person ID. The education record constitutes
	 of institute name, the person's percentage and if that education is currently ongoing or not.
	 Please look at the format of an education field from the PDF.
	 If the person ID is not available in the records, you can ignore that case.
	Parameters:
	- records (LIST): A list of person records (each of which is a dictionary)
	- person_id (INTEGER): The person id
	- institute_name (STRING): The institute name (case-insensitive)
	- ongoing (BOOLEAN): The ongoing value representing if the education is currently ongoing or not
	- percentage (FLOAT): The person's score in percentage
	Returns:
	- A LIST of Dictionaries representing all the records (the updated version).
	In case there were no updates, return the original records.
	"""
	if records[person_id]["education"]:
		if not ongoing:
			dic = {"institute": institute_name, "ongoing": ongoing, "percentage": percentage}
			records[person_id]["education"].append(dic)
		elif ongoing:
			dic = {"institute": institute_name, "ongoing": ongoing}
			records[person_id]["education"].append(dic)
	return records
