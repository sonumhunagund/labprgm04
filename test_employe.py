from employe import employe_details

def test_employe_details():
    result = employe_details("Rahul", "EMP101", "IT", "50000")
    expected = "Name: Rahul\nEmployee ID: EMP101\nDepartment: IT\nsalary: 50000"
    assert result == expected