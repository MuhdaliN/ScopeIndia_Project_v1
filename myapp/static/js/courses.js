// Store selected courses in a set to avoid duplicates
let selectedCourses = new Set();

// Function to update the table with the selected courses
function updateSelectedCoursesList() {
    const tableBody = document.getElementById('selectedCourses');
    tableBody.innerHTML = ''; // Clear the table before adding new rows

    selectedCourses.forEach(course => {
        const row = document.createElement('tr');

        // Create a cell for the course name
        const courseNameCell = document.createElement('td');
        courseNameCell.textContent = course;
        row.appendChild(courseNameCell);

        // Create a cell for the remove button
        const removeButtonCell = document.createElement('td');
        const removeButton = document.createElement('button');
        removeButton.textContent = 'Remove';
        removeButton.classList.add('btn', 'btn-danger');
        removeButton.addEventListener('click', () => removeCourse(course)); // Attach event to remove course
        removeButtonCell.appendChild(removeButton);
        row.appendChild(removeButtonCell);

        tableBody.appendChild(row);
    });
}

// Function to remove a course from the selected list
function removeCourse(course) {
    selectedCourses.delete(course); // Remove the course from the set
    updateSelectedCoursesList(); // Refresh the table
}

// Function to handle enrollment
function enrollCourse(event, courseName) {
    event.preventDefault(); // Prevent the default action (link redirect)
    
    if (!selectedCourses.has(courseName)) {
        selectedCourses.add(courseName); // Add course to selected list
        alert(`You have successfully enrolled in ${courseName}!`);
        updateSelectedCoursesList(); // Refresh the list in the table
    } else {
        alert(`You are already enrolled in ${courseName}.`);
    }
}

// Function to handle saving courses (submit form)
function saveCourses(event) {
    event.preventDefault(); // Prevent default form submission

    // Convert selected courses to an array and join them into a string (or you can use JSON)
    const coursesArray = Array.from(selectedCourses);
    const coursesString = coursesArray.join(','); // You can also use JSON.stringify(coursesArray)

    // Check if the courses are the same as the already saved ones (you can get this value from the server)
    const alreadySavedCourses = document.getElementById('alreadySavedCourses').value; // This is a hidden input to pass the already saved courses
    if (alreadySavedCourses && alreadySavedCourses === coursesString) {
        alert('You have already saved these courses.');
        return;
    }

    // Attach the courses data to the form and submit
    const coursesInput = document.createElement('input');
    coursesInput.type = 'hidden';
    coursesInput.name = 'courses_db'; // This matches your model's field name
    coursesInput.value = coursesString;
    document.getElementById('selectedCoursesForm').appendChild(coursesInput);

    // Submit the form
    document.getElementById('selectedCoursesForm').submit();
}

// Add event listeners for all "Enroll Now" buttons
document.addEventListener('DOMContentLoaded', () => {
    const enrollButtons = document.querySelectorAll('.enroll-btn');
    
    enrollButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const courseName = this.getAttribute('data-course');
            enrollCourse(event, courseName); // Trigger enrollment function on button click
        });
    });

    // Reset button to clear selected courses
    const resetButton = document.getElementById('resetCourses');
    resetButton.addEventListener('click', () => {
        selectedCourses.clear(); // Clear selected courses
        updateSelectedCoursesList(); // Refresh the list
    });

    // Add event listener to the Save Courses button
    const saveButton = document.getElementById('saveCourses');
    saveButton.addEventListener('click', saveCourses); // Trigger the save function on button click
});
