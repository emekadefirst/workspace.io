async function createUser(username, email, password) {
  try {
    const response = await axios.post("https://localhost:8000/user/create", {
      username,
      email,
      password,
    });
    console.log(response.data);
  } catch (error) {
    console.error("Error:", error);
  }
}

document
  .getElementById("registerForm")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const username = document.getElementById("username").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    createUser(username, email, password);
  });
