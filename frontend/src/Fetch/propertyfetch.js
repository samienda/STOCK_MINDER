const token = localStorage.getItem('token');   
const formE1 = document.getElementById('form');

console.log(token)

formE1.addEventListener('submit', (event) => {
  event.preventDefault();
  const formData = new FormData(formE1);
  const data = Object.fromEntries(formData);
  console.log(data)

  fetch('http://localhost:8000/stock/properties/', {
    method: 'POST',
    headers:{
      'Content-type': 'application/json',
      'Authorization': `Token ${token}`,
    },
    body: JSON.stringify(data)
  })
    .then(response =>{
      response.json()
      if (response.ok) {
        alert('Property added successfully!');
      }else{
        alert('There was a problem adding Property')
      }
    } )
    .then(data => {
      
      console.log(data);
      })
    .catch(error => console.log(error));
});

 