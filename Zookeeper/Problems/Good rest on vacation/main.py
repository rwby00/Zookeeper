# put your python code here
duration = int(input())
food = int(input()) * duration
flight = int(input()) * 2
hotel = int(input()) * (duration - 1)
total = food + flight + hotel

print(total)
