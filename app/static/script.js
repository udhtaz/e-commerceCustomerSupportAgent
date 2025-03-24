document.addEventListener("DOMContentLoaded", function () {
    const chatBox = document.getElementById("chat-box");
    const chatForm = document.getElementById("chat-form");
    const userInput = document.getElementById("user-input");
    const typingIndicator = document.getElementById("typing-indicator");
    const toggleTheme = document.getElementById("toggle-theme");
    const clearChat = document.getElementById("clear-chat");

    // 🌙 Dark mode toggle
    if (toggleTheme) {
        toggleTheme.addEventListener("click", () => {
            document.body.classList.toggle("dark-mode");
            toggleTheme.textContent = document.body.classList.contains("dark-mode") ? "☀️ Light Mode" : "🌙 Dark Mode";
        });
    }

    // 🗑 Clear chat
    if (clearChat) {
        clearChat.addEventListener("click", () => {
            chatBox.innerHTML = "";
        });
    }

    // 📩 Append messages
    function appendMessage(text, sender) {
        const messageDiv = document.createElement("div");
        messageDiv.classList.add("chat-message", `${sender}-message`);
        messageDiv.innerText = text;
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight;
    }

    // 🚀 Handle chat submission
    chatForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const message = userInput.value.trim();
        if (!message) return;

        appendMessage(message, "user");
        userInput.value = "";

        // Show typing indicator
        if (typingIndicator) typingIndicator.style.display = "flex";

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message }),
            });

            const data = await response.json();

            // Hide typing indicator
            if (typingIndicator) typingIndicator.style.display = "none";

            // ✅ Extract chatbot output properly
            const botResponse = data.response?.output || "⚠️ Unexpected response format.";
            appendMessage(botResponse, "bot");

        } catch (error) {
            if (typingIndicator) typingIndicator.style.display = "none";
            appendMessage("⚠️ Error: Could not reach server.", "bot");
        }
    });
});
