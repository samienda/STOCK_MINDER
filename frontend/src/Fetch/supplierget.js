const token = localStorage.getItem('token');  
const formE1 = document.getElementById('form');


fetch('http://localhost:8000/stock/suppliers/', {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  }
})
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#supplierTable tbody');

    data.forEach(supplier => {
      const row = document.createElement('tr');

      const codeCell = document.createElement('td');
      codeCell.textContent = supplier.id;
      row.appendChild(codeCell);

      const nameCell = document.createElement('td');
      nameCell.textContent = supplier.name;
      row.appendChild(nameCell);

      const contactCell = document.createElement('td');
      contactCell.textContent = supplier.contact_info;
      row.appendChild(contactCell);

      const actionsCell = document.createElement('td');

      const updateLink = document.createElement('button');
      
      updateLink.textContent = 'Update';
      actionsCell.appendChild(updateLink);
      updateLink.id = 'updatelink';

      updateLink.addEventListener('click', (event) => {
        event.preventDefault();
        populate(supplier.id, supplier.name, supplier.contact_info, row);
      });
        

      const deleteLink = document.createElement('button');
      // deleteLink.href = `http://localhost:8000/stock/suppliers/${supplier.id}`; 
      deleteLink.textContent = 'Delete';
      actionsCell.appendChild(deleteLink);
      deleteLink.id = 'deletelink'

      deleteLink.addEventListener('click', (event) => {
        event.preventDefault();
        deleteSupplier(supplier.id, row);
      });

      actionsCell.appendChild(deleteLink);
      

      row.appendChild(actionsCell);
    
      tableBody.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error fetching supplier data:', error);
  });

  function deleteSupplier(supplierId, row) {
    const token = localStorage.getItem('token');
  
    fetch(`http://localhost:8000/stock/suppliers/${supplierId}`, {
      method: 'DELETE',
      headers: {
        'Content-type': 'application/json',
        'Authorization': `Token ${token}`,
      }
    })
      .then(response => {
        if (response.ok) {
         
          row.remove();
        } else {
          alert ('You can not delete this supplier ,Supplier is related to product')
          throw new Error('Failed to delete the supplier.');
        }
      })
      .catch(error => {
        console.error('Error deleting supplier:', error);
      });
}

const suppliercode = document.getElementById('updatecode')
const suppliername = document.getElementById('updatename')
const suppliercontact = document.getElementById('updatecontact')


function populate(id, name, contact, row) {
  console.log(id, name, contact);

  suppliercode.value = id;
  console.log(suppliercode.value)
  suppliername.value = name;
  suppliercontact.value = contact;
}

  formE1.addEventListener('submit', (event) => {
    event.preventDefault();

    const id = suppliercode.value;
    const name = suppliername.value;
    const contact = suppliercontact.value;

    const data = {
      name: name,
      contact_info: contact
    };

    fetch(`http://localhost:8000/stock/suppliers/${id}/`, {
      method: 'PATCH',
      headers: {
        'Content-type': 'application/json',
        'Authorization': `Token ${token}`,
      },
      body: JSON.stringify(data)
    })
      .then(response => {
        response.json();
        if (response.ok) {
          location.reload();
          alert('Supplier updated successfully!');
        } else {
          alert('There was a problem updating Supplier');
        }
      })
      .then(data => {
        
        console.log(data);
      })
      .catch(error => console.log(error));
  });

  // const searchInput = document.getElementById('searchInput');
  // const searchButton = document.getElementById('searchButton');
  // const tableBody = document.querySelector('#supplierTable tbody');
  
  // function fetchAndRenderFilteredData(searchTerm) {
  //   const token = localStorage.getItem('token');
  //   const url = `http://localhost:8000/stock/suppliers/?search=${encodeURIComponent(searchTerm)}`;
  
  //   fetch(url, {
  //     method: 'GET',
  //     headers: {
  //       'Content-type': 'application/json',
  //       'Authorization': `Token ${token}`,
  //     }
  //   })
  //     .then(response => response.json())
  //     .then(data => {
  //       renderData(data);
  //     })
  //     .catch(error => {
  //       console.error('Error fetching filtered supplier data:', error);
  //     });
  // }
  
  // function handleSearch() {
  //   const searchTerm = searchInput.value.trim();
  
  //   if (searchTerm !== '') {
  //     fetchAndRenderFilteredData(searchTerm);
  //   } else {
  //     fetchAndRenderFilteredData('');
  //   }
  // }
  
  // searchButton.addEventListener('click', handleSearch);
  
  // searchInput.addEventListener('keypress', (event) => {
  //   if (event.key === 'Enter') {
  //     handleSearch();
  //   }
  // });