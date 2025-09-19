let currentIndex = 0;
const slides = document.querySelectorAll('.slider li');
const totalSlides = slides.length;

function showSlide(index) {
  const offset = -index * (slides[0].offsetWidth + 20); // 20px margin between slides
  document.querySelector('.slider').style.transform = `translateX(${offset}px)`;
  updatePager(index);
}

function nextSlide() {
  currentIndex = (currentIndex + 1) % totalSlides;
  showSlide(currentIndex);
}

function prevSlide() {
  currentIndex = (currentIndex - 1 + totalSlides) % totalSlides;
  showSlide(currentIndex);
}

function updatePager(index) {
  const pagerDots = document.querySelectorAll('.slider_pager span');
  pagerDots.forEach(dot => dot.classList.remove('active'));
  pagerDots[index].classList.add('active');
}

// Initialize pager dots
function createPager() {
  const pagerContainer = document.querySelector('.slider_pager');
  for (let i = 0; i < totalSlides; i++) {
    const dot = document.createElement('span');
    dot.addEventListener('click', () => showSlide(i));
    pagerContainer.appendChild(dot);
  }
  updatePager(currentIndex); // Set the first dot as active
}

// Initialize slider
createPager();
showSlide(currentIndex);
