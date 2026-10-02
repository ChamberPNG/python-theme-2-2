def get_nested(data, *keys, default="не указано"):
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return default if current is None else current

class Student:
    def __init__(self, profile):
        self.name = profile.get("name", "без имени")
        self.group = profile.get("group", "не указана")
        self.active = profile.get("active", False)
        self.city = get_nested(
            profile,
            "contacts",
            "address",
            "city",
            default="не указан"
        )
        
    def summary(self):
        status = "активен" if self.active else "неактивен"
        return f"{self.name}; {self.group}; {self.city}; {status}"

defaults = {"role": "student", "active": True}


profiles = [
    defaults | {
        "name": "Анна",
        "group": "ИСП-21",
        "contacts": {"address": {}} 
    },

    defaults | {
        "name": "Иван",
        "group": "ИСП-22",
        "active": False
    },
    
    defaults | {
        "name": "Сергей",
        "group": "ИСП-23"
    }
]

defaults["active"] = False 

student_objects = []
for profile in profiles:
    student_objects.append(Student(profile))

for student in student_objects:
    print(student.summary())