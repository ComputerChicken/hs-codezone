const Kahoot = require("kahoot.js-updated");

function getQuizIdFromPin(pin) {
    const client = new Kahoot();

    client.join(pin, "QuizInspector");

    client.on("Joined", () => {
        console.log("Successfully joined game");
    });

    client.on("QuizStart", () => {
        const quizId = client.quiz.quizID;
        console.log("Quiz ID:", quizId);
        client.leave(); // disconnect
    });

    client.on("Disconnect", (reason) => {
        console.log("Disconnected:", reason);
    });

    client.on("Error", (err) => {
        console.error("Error:", err.message);
    });
}

// Example usage:
getQuizIdFromPin(168289); // Replace with actual live pin
