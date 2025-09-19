let currentIndex = 0;
const slides = document.querySelectorAll('.slider li');
const totalSlides = slides.length;

// Function to change the slide to the next one
function nextSlide() {
    currentIndex = (currentIndex + 1) % totalSlides; // Loop back to the first slide
    updateSlider();
}

// Function to change the slide to the previous one
function prevSlide() {
    currentIndex = (currentIndex - 1 + totalSlides) % totalSlides; // Loop back to the last slide
    updateSlider();
}

// Function to update the slider position
function updateSlider() {
    const slider = document.querySelector('.slider');
    const offset = -currentIndex * 100; // Move by 100% per slide
    slider.style.transform = `translateX(${offset}%)`;

    // Update pagination
    updatePagination();
}

// Function to update pagination dots
function updatePagination() {
    const dots = document.querySelectorAll('.slider_pager div');
    dots.forEach(dot => dot.classList.remove('active'));
    if (dots[currentIndex]) {
        dots[currentIndex].classList.add('active');
    }
}

// Function to create pagination dots dynamically
function createPagination() {
    const pager = document.querySelector('.slider_pager');
    for (let i = 0; i < totalSlides; i++) {
        const dot = document.createElement('div');
        dot.addEventListener('click', () => {
            currentIndex = i;
            updateSlider();
        });
        pager.appendChild(dot);
    }
    updatePagination(); // Set the first dot as active
}

// Initialize the slider with pagination and auto slide change every 5 seconds
function initializeSlider() {
    createPagination();
    setInterval(nextSlide, 5000); // Change slide every 5 seconds
}

initializeSlider();
