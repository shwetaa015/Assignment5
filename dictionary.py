marks={
    "Will":98,
    "Mike":80,
    "Dustin":85,
    "Lucas":90
}
name=input("Enter student's name:")
if name in marks:
    print(f"{name}'s marks: {marks[name]}")
else:
    print("Student not found.")