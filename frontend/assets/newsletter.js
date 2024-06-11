document
  .getElementById("newsletter-form")
  .addEventListener("submit", async function (event) {
    event.preventDefault(); // Prevent the form from submitting in the traditional way

    const emailInput = document.getElementById("email");
    const email = emailInput.value;

    if (email) {
      try {
        const response = await fetch("http://127.0.0.1:8000/newsletter/add", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ email: email }),
        });

        if (response.ok) {
          alert("Email sent successfully!");
          emailInput.value = ""; // Clear the input field after successful submission
        } else {
          alert("Failed to send email.");
        }
      } catch (error) {
        console.error("Error:", error);
        alert("An error occurred while sending the email.");
      }
    } else {
      alert("Please enter a valid email address.");
    }
  });
