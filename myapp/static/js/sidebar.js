pdocument.addEventListener("DOMContentLoaded", () => {
    const sidebar = document.getElementById("sidebar");
    const toggleBtn = document.getElementById("toggle-btn");
    const content = document.querySelector(".content");

    toggleBtn.addEventListener("click", () => {
        sidebar.classList.toggle("open");
        content.classList.toggle("shift");
    });
});