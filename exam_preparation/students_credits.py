def students_credits(*courses_info, needed_credits=240):
    student_book = {}  # course_name: Diyan's credits
    result = []

    for course_info in courses_info:
        course_name, course_credits, max_pts, student_pts = course_info.split("-")

        current_percentage = int(student_pts) / int(max_pts)
        credits_taken = current_percentage * int(course_credits)
        student_book[course_name] = credits_taken

    total_credits = sum(student_book.values())

    if total_credits >= needed_credits:
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
    else:
        result.append(f"Diyan needs {needed_credits - total_credits:.1f} credits more for a diploma.")

    for course, points in sorted(student_book.items(), key=lambda x: -x[1]):
        result.append(f"{course} - {points:.1f}")

    return "\n".join(result)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)

