// Firebase configuration
const firebaseConfig = {
    apiKey: "AIzaSyCzJD4l7KEUBeniiNpNoz86PQFm7cM-k20",
    authDomain: "plant-1b3c0.firebaseapp.com",
    projectId: "plant-1b3c0",
    storageBucket: "plant-1b3c0.appspot.com",
    messagingSenderId: "428114318860",
    appId: "1:428114318860:web:dc090e7d8b7497ae158029",
    measurementId: "G-NND7ZHYNXW"
  };
  
  // Initialize Firebase
  firebase.initializeApp(firebaseConfig);
  
  // Get references to the HTML elements
  const signUpForm = document.querySelector('.sign-up form');
  const signInForm = document.querySelector('.sign-in form');
  const container = document.getElementById('container');
  const registerBtn = document.getElementById('register');
  const loginBtn = document.getElementById('login');
  
  registerBtn.addEventListener('click', () => {
    container.classList.add("active");
  });
  
  loginBtn.addEventListener('click', () => {
    container.classList.remove("active");
  });
  
  // Sign up
  signUpForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const name = signUpForm.querySelector('input[placeholder="Name"]').value;
    const email = signUpForm.querySelector('input[placeholder="Email"]').value;
    const password = signUpForm.querySelector('input[placeholder="Password"]').value;
  
    firebase.auth().createUserWithEmailAndPassword(email, password)
      .then((userCredential) => {
        const user = userCredential.user;
        user.updateProfile({ displayName: name });
        alert('Account created successfully');
      })
      .catch((error) => {
        console.error(error);
        alert(error.message);
      });
  });
  
  // Sign in
  signInForm.addEventListener('submit', (e) => {
    e.preventDefault();
    const email = signInForm.querySelector('input[placeholder="Email"]').value;
    const password = signInForm.querySelector('input[placeholder="Password"]').value;
  
    firebase.auth().signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        alert('Signed in successfully');
        window.location.href = "../Home/home.html";
      })
      .catch((error) => {
        console.error(error);
        alert(error.message);
      });
  });
  