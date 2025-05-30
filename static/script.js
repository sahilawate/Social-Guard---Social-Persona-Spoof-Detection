document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("profileForm");
  const input = document.getElementById("profile-url");
  const errorMsg = document.getElementById("error-message");

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const url = input.value.trim();
    if (!url) {
      errorMsg.textContent = "Please enter a URL.";
      errorMsg.classList.remove("hidden");
      return;
    }

    try {
      const response = await fetch("/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ url: url }),
      });

      if (!response.ok) {
        throw new Error("Server error");
      }

      const result = await response.json();

      localStorage.setItem("analysisResult", JSON.stringify(result));
      window.location.href = "/results";
    } catch (err) {
      errorMsg.textContent = "Something went wrong. Try again.";
      errorMsg.classList.remove("hidden");
    }
  });
});
