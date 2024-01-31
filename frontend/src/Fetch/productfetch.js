const token = localStorage.getItem('token');
const formE1 = document.getElementById('form');
const dropdown = document.getElementById('product-type');
const supplierDropdown = document.getElementById('Supplier-name');
const propertyDropdown = document.getElementById('property-name');

fetch('http://localhost:8000/stock/producttypes/', {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  },
})
  .then(response => response.json())
  .then(data => {
    console.log(data)
    dropdown.innerHTML = '';

    data.forEach(option => {
      console.log(option.name)
      const optionElement = document.createElement('option');
      optionElement.value = option.id;
      optionElement.textContent = option.name;
      dropdown.appendChild(optionElement);
    });
  })
  .catch(error => {
    console.error('Error fetching product types:', error);
});

fetch('http://localhost:8000/stock/suppliers/', {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  },
})
  .then(response => response.json())
  .then(data => {
    console.log(data)
    supplierDropdown.innerHTML = '';

    data.forEach(option => {
      console.log(option.name)
      const optionElement = document.createElement('option');
      optionElement.value = option.id;
      optionElement.textContent = option.name;
      supplierDropdown.appendChild(optionElement);
    });
  })
  .catch(error => {
    console.error('Error fetching product types:', error);
});



fetch('http://localhost:8000/stock/properties/', {
  method: 'GET',
  headers: {
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`
  }
})
  .then(response => response.json())
  .then(data => {
    console.log(data)
    propertyDropdown.innerHTML = '';

    data.forEach(option => {
      const optionElement = document.createElement('option');
      optionElement.value = option.id
      optionElement.textContent = option.brand + " " + option.size;
      propertyDropdown.appendChild(optionElement);
    });
  })
  .catch(error => {
    console.error('Error fetching properties:', error);
  });

//   fetch('http://localhost:8000/stock/properties/', {
//   method: 'GET',
//   headers: {
//     'Authorization': `Token ${token}`
//   }
// })
//   .then(response => response.json())
//   .then(data => {

//     propertyDropdown.innerHTML = '';

//     data.forEach(option => {
//       const optionElement = document.createElement('option');
//       optionElement.value = option.id ;
//       optionElement.textContent = option.brand + " " + option.size;
//       propertyDropdown.appendChild(optionElement);
//     });
//   })
//   .catch(error => {
//     console.error('Error fetching properties:', error);
//   });



  formE1.addEventListener('submit', async (event) => {
    event.preventDefault(); 
  
    const selectedProductType = dropdown.value;
    const formData = new FormData(formE1);
    formData.append('productType', selectedProductType);
    const data = Object.fromEntries(formData);
  
    async function purchase() {
      
      const response = await fetch('http://localhost:8000/stock/purchases/',
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization':` Token ${token}`
          },
        });
      const data = await response.json();
          console.log(data)
          return data.id
    }
  
  
    const purchase_id = await purchase();
  
    fetch(`http://localhost:8000/stock/purchases/${purchase_id}/products/`, {
      method: 'POST',
      headers:{
        'Content-type': 'application/json',
        'Authorization': `Token ${token}`,
      },
      body: JSON.stringify(data)
    })
      .then(response => {
        response.json()
        if (response.ok) {
          alert('Product added successfully!');
        }else{
          alert('There was a problem adding Product')
        }
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => console.log(error));
  });
















// console.log(token)

// formE1.addEventListener('submit', (event) => {
//   event.preventDefault(); 

//   const formData = new FormData(formE1);
//   const data = Object.fromEntries(formData);
//   console.log(data)
//   /* const token = localStorage.getItem('token'); */

//   fetch('http://localhost:8000/stock/purchase/1', {
//     method: 'POST',
//     headers:{
//       'Content-type': 'application/json',
//       'Authorization': `Token ${token}`,
//     },
//     body: JSON.stringify(data)
//   })
//     .then(response => response.json())
//     .then(data => {
//       console.log(data);
//     })
//     .catch(error => console.log(error));
// });