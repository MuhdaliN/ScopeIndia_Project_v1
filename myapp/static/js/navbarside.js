function toggleUserMenu() {
    const userMenu = document.querySelector('.user-menu');
    userMenu.classList.toggle('active');
}

// Optional: Close dropdown when clicking outside (for better UX)
document.addEventListener('click', function(event) {
    const userMenu = document.querySelector('.user-menu');
    if (!userMenu.contains(event.target)) {
        userMenu.classList.remove('active');
    }
});
