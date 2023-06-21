const express = require('express');

const app = express();
const port = 8000;

app.use(express.json());

app.post('/login', (req, res) => {
  const { email, password, save_id, auto_login } = req.body;

  // 로그인 기능 구현
  // ...
  console.log(email)
  // 예시: Firebase에 로그인 정보 저장
  const userRef = db.collection('users').doc();
  userRef.set({
    email,
    password,
    save_id,
    auto_login
  });

  // 로그인 정보 틀리면 다시 돌려줘야함
  // Firebase에서 확인
  // 임시
  if (email === 'kamal' && password === '123') {
    res.json({ message: 'Logged in successfully' });
  } else {
    res.status(401).json({ error: 'Invalid email or password' });
  }
});

app.post('/signup', (req, res) => {
  const { email, password, name, dob } = req.body;

  // Perform signup validation logic here
  // ...

  // 예시: Firebase에 회원가입 정보 저장
  const userRef = db.collection('users').doc();
  userRef.set({
    email,
    password,
    name,
    dob
  });

  // 이메일 인증 해야함

  res.json({ message: 'Signed up successfully' });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
