const token = localStorage.getItem('token');  

fetch('http://localhost:8000/stock/purchases/', {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  }
})
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#purchaseTable tbody');

    data.forEach(purchase => {
      console.log(purchase);
      const row = document.createElement('tr');

        const codeCell = document.createElement('td');
        codeCell.textContent = purchase.id;
        row.appendChild(codeCell);

        const productCell = document.createElement('td');
        productCell.textContent = purchase.productslist[0].productname;
        row.appendChild(productCell);


        const quantityCell = document.createElement('td');
        quantityCell.textContent = purchase.quantity;
        row.appendChild(quantityCell);

        const priceCell = document.createElement('td');
        priceCell.textContent = purchase.total_price;
        row.appendChild(priceCell);

        const dateCell = document.createElement('td');
        dateCell.textContent = purchase.date;
        row.appendChild(dateCell);

        

    
      tableBody.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error fetching sell data:', error);
  });