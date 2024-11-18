#!/usr/bin/awk -f

# BEGIN block to print header
BEGIN {
    printf "%-10s %-15s %-20s %-40s\n", "StudentID", "Name", "Overall Grade", "Subject Grades"
    printf "%-10s %-15s %-20s %-40s\n", "---------", "---------------", "-------------------", "----------------------------------------"
}

# Main block to process each line
{
    student_id = $1;
    name = $2;

    # Calculate total and average
    total = 0;
    subject_grades = "";
    for (i = 3; i <= 5; i++) {
        total += $i;

        # Check individual subject grade
        if ($i < 40) {
            grade = "Fail";
        } else if ($i >= 40 && $i < 60) {
            grade = "First Class";
        } else {
            grade = "Distinction";
        }
        subject_grades = subject_grades sprintf("Subject%d: %s, ", i - 2, grade);
    }

    average = total / 3;  # Calculate average marks

    # Classify overall performance
    if (average < 40) {
        overall_grade = "Fail";
    } else if (average >= 40 && average < 60) {
        overall_grade = "First Class";
    } else {
        overall_grade = "Distinction";
    }

    # Print the result
    printf "%-10s %-15s %-20s %-40s\n", student_id, name, overall_grade, subject_grades;
}

# END block for cleanup (optional)
END {
    print "\nProcessing complete!";
}




data.txt:
101 Mohit 75 85 65
102 Atharva 55 60 50
103 Neel 35 45 40
104 Mustafa 80 90 85
105 Parth 60 65 62
