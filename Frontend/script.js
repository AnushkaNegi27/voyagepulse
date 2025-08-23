async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const output = document.getElementById("output");
  const uploadBtn = document.getElementById("uploadBtn");

  if (!fileInput.files.length) {
    alert("Please select a file first!");
    return;
  }

  uploadBtn.disabled = true;
  output.innerHTML = `<div class="spinner"></div> Uploading <b>${fileInput.files[0].name}</b>...`;
  

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  try {
    const res = await fetch("http://127.0.0.1:5000/api/upload", {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      output.innerHTML = "<p style='color:red;'>❌ Upload failed.</p>";
      uploadBtn.disabled = false;
      return;
    }

    const blob = await res.blob();
    const url = window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "result.json";
    document.body.appendChild(a);
    a.click();
    a.remove();

    output.innerHTML += "<p style='color:green;'>✅ File processed! Download started.</p>";

  } catch (err) {
    output.innerHTML = "<p style='color:red;'>❌ Upload failed. Check console.</p>";
    console.error("Upload failed", err);
  } finally {
    uploadBtn.disabled = false;
    fileInput.value = ""; // Reset file input so user can upload again
  }
}

document.getElementById("uploadBtn").addEventListener("click", uploadFile);
d
