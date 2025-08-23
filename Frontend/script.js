async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const output = document.getElementById("output");

  if (!fileInput.files.length) {
    alert("Please select a file first!");
    return;
  }

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  output.textContent = "⏳ Uploading...";

  try {
    const res = await fetch("http://127.0.0.1:5000/api/upload", {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      output.innerHTML = "<p style='color:red;'>❌ Upload failed.</p>";
      return;
    }

    // 🔹 Convert response to Blob (file)
    const blob = await res.blob();

    // 🔹 Create download link
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "result.json";  // same name as backend
    document.body.appendChild(a);
    a.click();
    a.remove();

    output.innerHTML = "<p style='color:green;'>✅ File processed! Download started.</p>";

  } catch (err) {
    output.innerHTML = "<p style='color:red;'>❌ Upload failed. Check console.</p>";
    console.error("Upload failed", err);
  }
}

// attach event listener
document.getElementById("uploadBtn").addEventListener("click", uploadFile);
