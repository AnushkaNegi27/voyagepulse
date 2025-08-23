async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    if (!fileInput.files.length) {
        alert("Please select a file first!");
        return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
        const res = await fetch("http://127.0.0.1:5000/api/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();
        document.getElementById("output").textContent = JSON.stringify(data, null, 2);
    } catch (err) {
        console.error("Upload failed", err);
    }
}

// attach event listener instead of inline onclick
document.getElementById("uploadBtn").addEventListener("click", uploadFile);
