let processedBlob = null; // Store processed file for download

async function uploadFile() {
  const fileInput = document.getElementById("fileInput");
  const output = document.getElementById("output");
  const uploadBtn = document.getElementById("uploadBtn");
  const downloadBtn = document.getElementById("downloadBtn");

  if (!fileInput.files.length) {
    alert("Please select a file first!");
    return;
  }

  uploadBtn.disabled = true;
  downloadBtn.disabled = true;
  output.innerHTML = "";

  // Spinner
  const spinner = document.createElement("div");
  spinner.className = "spinner";
  output.appendChild(spinner);
  const textNode = document.createTextNode(` Uploading ${fileInput.files[0].name}...`);
  output.appendChild(textNode);

  const formData = new FormData();
  formData.append("file", fileInput.files[0]);

  try {
    const res = await fetch("http://127.0.0.1:5000/api/upload", {
      method: "POST",
      body: formData
    });

    if (!res.ok) {
      spinner.remove();
      const errMsg = await res.text();
      output.innerHTML = `<p style="color:red;">❌ Upload failed: ${errMsg}</p>`;
      return;
    }

    const blob = await res.blob();
    processedBlob = blob; // store the blob for download

    // Stop spinner and show success
    spinner.remove();
    output.innerHTML = `<p style="color:green;">✅ File uploaded successfully!</p>`;
    downloadBtn.disabled = false; // enable download

  } catch (err) {
    spinner.remove();
    output.innerHTML = "<p style='color:red;'>❌ Upload failed. Check console.</p>";
    console.error("Upload failed", err);
  } finally {
    uploadBtn.disabled = false;
    fileInput.value = ""; // reset file input
  }
}

function downloadFile() {
  if (!processedBlob) return;

  const a = document.createElement("a");
  a.href = window.URL.createObjectURL(processedBlob);
  a.download = "result.json";
  document.body.appendChild(a);
  a.click();
  a.remove();
}

document.getElementById("uploadBtn").addEventListener("click", uploadFile);
document.getElementById("downloadBtn").addEventListener("click", downloadFile);
