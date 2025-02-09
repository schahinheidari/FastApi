document.getElementById("plantForm").addEventListener("submit", (event) => {
    event.preventDefault();

    const description = document.getElementById("description").value;

    fetch("/generate", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
        },
        body: new URLSearchParams({ description }),
    })
        .then((response) => response.json())
        .then((data) => {
            if (data.error) {
                alert(data.error);
                return;
            }

            // Update the result section
            document.getElementById("plantImage").src = data.image_url;
            document.getElementById("plantName").textContent = `Plant Name: ${data.plant_name}`;
            document.getElementById("result").classList.remove("hidden");
        })
        .catch((error) => {
            console.error("Error:", error);
        });
});
