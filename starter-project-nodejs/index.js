const express = require('express');

const app = express();
const port = 3000;

const generatePassword = () => {
  const chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const length = 8;
  let password = '';
  for (let i = 0; i < length; i++) {
    const randomIndex = Math.floor(Math.random() * chars.length);
    password += chars[randomIndex];
  }
  return password;
}

app.get('/', (req, res) => {
  const password = generatePassword();
  res.send(`password: ${password}`);
});

app.listen(port, () => {
  console.log(`Server is runing on port: ${port}`);
});