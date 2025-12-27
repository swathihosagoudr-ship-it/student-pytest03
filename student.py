def student_details(name,usn,div,age):
    
    result = (
        f"student_name:{name}"
        f"student_usn:{usn}"
        f"student_div:{div}"
        f"student_age:{age}"
    )
    return result
if __name__ == "__main__":
       
      name ="swathi"
      usn = "01FE24BCA304"
      div ="E"
      age = 20

print(student_details("swathi","01FE24BCA304","E",20))     