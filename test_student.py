from student import student_details
def test_student_details():
    Expected_output = (
        "student_name = swathi"
        "student_usn = 01FE24BCA304"
        "student_div = E"
        "student_age = 20"
    )
    assert student_details("swathi","01FE24BCA304","E",20) == Expected_output 