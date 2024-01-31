const token = localStorage.getItem('token');   
const formE1 = document.getElementById('form');

console.log(token)

formE1.addEventListener('submit', (event) => {
  event.preventDefault(); 

  const formData = new FormData(formE1);
  const data = Object.fromEntries(formData);
  console.log(data)
  /* const token = localStorage.getItem('token'); */

  fetch('http://localhost:8000/stock/suppliers/', {
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
        location.reload()
        alert('Supplier added successfully!');
      }else{
        alert('There was a problem adding Supplier')
      }
    } )
    .then(data => {

      console.log(data);
      })
    .catch(error => console.log(error));
});

 