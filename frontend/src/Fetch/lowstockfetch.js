const token = localStorage.getItem('token');  

fetch('http://localhost:8000/stock/lowstocks/', {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  }
})
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#lowstockTable tbody');

    data.forEach(low => {
      if (low.error) {
        console.error('Error fetching low stock data:', low.error);
        return; 
      }

      const row = document.createElement('tr');

      const codeCell = document.createElement('td');
      codeCell.textContent = low.id;
      row.appendChild(codeCell);

      const nameCell = document.createElement('td');
      nameCell.textContent = low.productname;
      row.appendChild(nameCell);

      const contactCell = document.createElement('td');
      contactCell.textContent = low.quantity;
      row.appendChild(contactCell);

      const product_typeCell = document.createElement('td');
      product_typeCell.textContent = low.product_type_str;
      row.appendChild(product_typeCell);

      const propertyCell = document.createElement('td');
      propertyCell.textContent = low.property_str;
      row.appendChild(propertyCell);

      const thresholdCell = document.createElement('td');
      thresholdCell.textContent = low.threshold;
      row.appendChild(thresholdCell);

      tableBody.appendChild(row);
    });
      const row = document.createElement('tr');

      const codeCell = document.createElement('td');
      codeCell.textContent = low.id;
      row.appendChild(codeCell);

      const nameCell = document.createElement('td');
      nameCell.textContent = low.productname;
      row.appendChild(nameCell);

      const contactCell = document.createElement('td');
      contactCell.textContent = low.quantity;
      row.appendChild(contactCell);

      
      const product_typeCell = document.createElement('td');
      product_typeCell.textContent = low.product_type_str;
      row.appendChild(product_typeCell);
      
      const propertyCell = document.createElement('td');
      propertyCell.textContent = low.property_str;
      row.appendChild(propertyCell);

      
      const thresholdCell = document.createElement('td');
      thresholdCell.textContent = low.threshold;
      row.appendChild(thresholdCell);

    //   const combinedCell = document.createElement('td');
    //   combinedCell.textContent = `${low.property.brand} - ${low.property.size}`;

    // row.appendChild(combinedCell);

      

    //   const actionsCell = document.createElement('td');
    //   const updateLink = document.createElement('a');
    //   updateLink.href = `/update-supplier/${low.code}`; 
    //   updateLink.textContent = 'Update';
    //   actionsCell.appendChild(updateLink);

    //   const deleteLink = document.createElement('a');
    //   deleteLink.href = `/delete-supplier/${low.code}`;
    //   deleteLink.textContent = 'Delete';
    //   actionsCell.appendChild(deleteLink);

    //   row.appendChild(actionsCell);
    
      tableBody.appendChild(row);
    })
    .catch(error => {
      console.error('Error fetching low stock data:', error);
    });
  
  