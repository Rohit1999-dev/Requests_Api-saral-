import requests
import json

# print(a)
# def functions():
# 	url="http://saral.navgurukul.org/api/courses"
# 	r=requests.get(url)
# 	a=r.text
# 	with open("courses.json","w") as f :
# 		var=f.write(a)

# 	with open("courses.json") as f:
# 		c=json.load(f)

		# print(b)

# 	fun()
def fun():

	with open("courses.json","r") as f:
		c=json.load(f)

		availablecourses=c["availableCourses"]
		number=0
		for i in availablecourses:
			Name=i["name"]
			print (number,Name)
			number+=1

		user=int(input("enter the number:"))
		Id=availablecourses[user]["id"]
		print (Id)


		link = "http://saral.navgurukul.org/api/courses/"+str(Id)+"/exercises"
		req = requests.get(link)
		text = req.text
		# print (text)
		var = json.loads(text)
		data = var['data']
		number=0
		for i in data:
			# childExercises=i["childExercises"]
			name=i["name"]
			print (number,name)
			number+=1
	
		user=int(input("choose your exercise:"))
		def navigation(user):
			slug=data[user]["slug"]
			print (slug)
			link2 = "http://saral.navgurukul.org/api/courses/"+str(Id)+"/exercise/getBySlug?slug="+slug
			# print (link2)
			r=requests.get("http://saral.navgurukul.org/api/courses/75/exercise/getBySlug?slug="+slug)
			a=r.text
			print (a)

			user1= str(input("enter your direction:"))
			if user1 == "up":
				fun()
			elif user1=="p":
				user=user-1
				navigation(user)
			elif user1=="n":
				user=user+1
				navigation(user)
			else:
				print()
		navigation(user)
			
fun()



