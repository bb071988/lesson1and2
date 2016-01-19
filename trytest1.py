# lesson 1 data science

phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

try:
	user_number = phone_book["Jamie"]
	print("their number is {}".format(user_number))
except:
	print("sorry can't find that person")

