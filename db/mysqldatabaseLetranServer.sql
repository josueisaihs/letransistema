INSERT INTO Docencia_assistence(dateTime, grouplist, status) VALUES (now(), (SELECT grouplist.id FROM 
	Docencia_studentpersonalinformation as student, 
	Docencia_candidate as candidate, 
    Docencia_raspberrys as rasp, 
    Docencia_grouplist as grouplist, 
	Docencia_groupinformation as groupinfo 
WHERE 
	rasp.name = 'Rasp1' and 
	rasp.classroom_id = groupinfo.classroom_id and 
    grouplist.group_id = groupinfo.id and
    student.numberidentification = '94050830902' and 
    student.id = candidate.student_id and 
    candidate.id = grouplist.student_id), 'a');
