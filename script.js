async function ask() {
  const query = document.getElementById("query").value;
  const responseDiv = document.getElementById("response");
  responseDiv.innerHTML = "Thinking... 🤖";

  const response = await fetch("https://api.openai.com/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer YOUR_API_KEY",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "gpt-4o-mini",
      messages: [{ role: "user", content: query }]
    })
  });

  const data = await response.json();
  responseDiv.innerHTML = data.choices[0].message.content;
}

