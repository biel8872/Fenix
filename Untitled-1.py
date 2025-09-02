<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <title>Para Você ❤️</title>
  <style>
    body {
      background: linear-gradient(135deg, pink, lightblue);
      font-family: Arial, sans-serif;
      text-align: center;
      color: #333;
      margin: 0;
      padding: 50px;
    }
    h1 {
      font-size: 60px;
      color: darkred;
      animation: pulse 1s infinite;
    }
    p {
      font-size: 24px;
      margin-top: 20px;
    }
    .coração {
      font-size: 80px;
      animation: pulse 1s infinite;
    }
    @keyframes pulse {
      0% { transform: scale(1); }
      50% { transform: scale(1.3); }
      100% { transform: scale(1); }
    }
    button {
      margin-top: 30px;
      padding: 15px 30px;
      font-size: 20px;
      border: none;
      border-radius: 10px;
      background-color: darkred;
      color: white;
      cursor: pointer;
      transition: 0.3s;
    }
    button:hover {
      background-color: crimson;
    }
  </style>
</head>
<body>
  <h1>❤️ Oi, meu amor ❤️</h1>
  <p>Fiz este site só pra dizer<br><b>o quanto você é especial pra mim</b>.</p>
  <div class="coração">💖</div>
  <button onclick="alert('Eu te amo muito! 💕')">Clique aqui</button>
</body>
</html>
