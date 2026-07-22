function runEmotionAnalysis() {
  const textToAnalyze = document.getElementById("textToAnalyze").value;
  const responseElement = document.getElementById("system_response");
  const requestUrl = `/emotionDetector?textToAnalyze=${encodeURIComponent(textToAnalyze)}`;

  responseElement.textContent = "Analyzing...";

  fetch(requestUrl)
    .then((response) => response.text())
    .then((text) => {
      responseElement.textContent = text;
    })
    .catch(() => {
      responseElement.textContent = "Unable to analyze the text. Please try again.";
    });
}
