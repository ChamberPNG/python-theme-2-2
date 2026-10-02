def get_nested(data, *keys, default="не указано"):
    current = data
    for key in keys:
        if not isinstance(current, dict) or key not in current:
            return default
        current = current[key]
    return default if current is None else current


class Course:
    def __init__(self, profile):
        self.title = profile.get("title", "без названия")
        self.category = profile.get("category", "не указана")
        self.active = profile.get("active", False)
        self.teacher_email = get_nested(
            profile, "teacher", "email", default="email не указан"
        )

    def summary(self):
        status = "активен" if self.active else "неактивен"
        return f"{self.title}; {self.category}; {status}; {self.teacher_email}"



defaults = {"active": True, "category": "обязательный"}

course_data_1 = {"title": "Основы Python", "teacher": {"name": "Анна Сергеевна"}}

course_data_2 = {"title": "Git для начинающих"}

course_1 = defaults | course_data_1
course_2 = defaults | course_data_2

courses_profiles = [course_1, course_2]
course_objects = []

for profile in courses_profiles:
    course_objects.append(Course(profile))

for course in course_objects:
    print(course.summary())