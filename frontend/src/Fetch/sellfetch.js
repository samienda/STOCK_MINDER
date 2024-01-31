const token = localStorage.getItem('token');   
const formE1 = document.getElementById('form');

console.log(token)

formE1.addEventListener('submit', (event) => {
  event.preventDefault(); 

  const formData = new FormData(formE1);
  const data = Object.fromEntries(formData);
  console.log(data)
  /* const token = localStorage.getItem('token'); */

  fetch('http://localhost:8000/stock/sales/', {
    method: 'POST',
    headers: {
      'Content-type': 'application/json',
      'Authorization': `Token ${token}`,
    },
    body: JSON.stringify(data)
  })
    .then(response => response.json().then(data => {
      if (response.ok) {
        alert('Sell added successfully!');
        return data;
      } else {

        let errorMessage;
        if (data.quantity) {
          errorMessage = data.quantity;
        } else if (data.product) {
          errorMessage = "The product you're trying to sell doesn't exist.";
        }
        throw new Error(errorMessage);
      }
    }))
    .catch(error => {
      
      alert(error.message);
    });
});