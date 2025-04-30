document.addEventListener("DOMContentLoaded", function () {
    const messages = document.querySelectorAll(".message");
    messages.forEach((msg) => {
        setTimeout(() => {
            msg.style.transition = "opacity 0.5s ease";
            msg.style.opacity = "0";
            setTimeout(() => msg.remove(), 500);
        }, 3500);
    });
});
