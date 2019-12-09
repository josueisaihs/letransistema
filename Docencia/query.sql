SELECT Gl.id
FROM 
    Docencia_StudentPersonalInformation AS Student, 
    Docencia_Candidate AS Candidate, 
    Docencia_Raspberrys AS Rasp, 
    Docencia_GroupInformation AS Gp, 
    Docencia_GroupList AS Gl 
WHERE 
    Student.numberidentification = '95010628970' AND 
    Rasp.name = 'Rasp1' AND 
    Rasp.classroom_id = Gp.classroom_id AND 
    Candidate.student_id = Student.id AND 
    Candidate.course_id = Gp.course_id AND 
    Candidate.id = Gl.student_id AND 
    Gp.id = Gl.group_id;