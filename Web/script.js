document.addEventListener("DOMContentLoaded", function () {
    const welcomePage = document.querySelector(".welcome-page");

    // Function to redirect to another page
    function redirectToAnotherPage() {
        window.location.href = "./signup&signin/signs.html"; // Replace with the actual URL of your second page
    }

    // Add an event listener to the animation end
    welcomePage.addEventListener("animationend", function (event) {
        // Check if the animation that ended is the "moveTop" animation
        if (event.animationName === "moveTop") {
            // Call the function to redirect to another page
            redirectToAnotherPage();
        }
    });
});
