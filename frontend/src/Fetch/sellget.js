const token = localStorage.getItem('token');  

fetch('http://localhost:8000/stock/sales/', {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  }
})
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#saleTable tbody');

    data.forEach(sale => {
      const row = document.createElement('tr');

      const codeCell = document.createElement('td');
      codeCell.textContent = sale.id;
      row.appendChild(codeCell);

      const productCell  = document.createElement('td');
      productCell.textContent = sale.product_str;
      row.appendChild(productCell);

      const priceCell = document.createElement('td');
      priceCell.textContent = sale.total_price;
      row.appendChild(priceCell);
      
      const quantityCell = document.createElement('td');
      quantityCell.textContent = sale.quantity;
      row.appendChild(quantityCell);

      
      const dateCell = document.createElement('td');
      dateCell.textContent = sale.date;
      row.appendChild(dateCell);

      //! const actionsCell = document.createElement('td');
      // const updateLink = document.createElement('a');
      // updateLink.href = `/update-sale/${sale.code}`; // Replace with the appropriate URL for update
      // updateLink.textContent = 'Update';
      // actionsCell.appendChild(updateLink);

      // const deleteLink = document.createElement('button');
      // deleteLink.href = `/delete-sale/${sale.code}`; 
            // deleteLink.textContent = 'Delete';
      // actionsCell.appendChild(deleteLink);

      // row.appendChild(actionsCell);
    
      tableBody.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error fetching sell data:', error);
  });