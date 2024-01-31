const formE1 = document.getElementById('login-form');

formE1.addEventListener('submit', (event) => {
    event.preventDefault(); 
  
    const formData = new FormData(formE1);
    const data = Object.fromEntries(formData);
  
    fetch('http://localhost:8000/auth/token/login', {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
    },
    body: JSON.stringify(data),
  })
    .then(response => {
      if (response.ok) {
        window.location.href = '../src/addproduct.html';
        return response.json(); 
      }else {

            document.getElementById('error-message').textContent = 'Invalid email or password';
            document.getElementById('error-message').style.display = 'block';
      }
    })
    .then(data => {
        console.log(data.auth_token)
        localStorage.setItem('token', data.auth_token);
        /* if (data.token !== ""){
            window.location.href = '../addproduct.html';
        } */
    })
    .catch(error => {
      console.error('Error:', error);
    });
  });
