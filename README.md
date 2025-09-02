<!DOCTYPE html>
<html>
<head>
  <title>Flores pra você 🌹</title>
</head>
<body style="background-color:#fff0f5; text-align:center; font-size:40px;">
  <h1>🌹 Essas flores são pra você 🌹</h1>
  <p>Porque você merece o mundo inteiro!</p>
  <div id="flores"></div>

  <script>
    let flores = "";
    for (let i = 0; i < 50; i++) {
      flores += "🌸 ";
    }
    document.getElementById("flores").innerHTML = flores;
  </script>
</body>
</html>
