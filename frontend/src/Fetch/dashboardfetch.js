const token = localStorage.getItem('token');
fetch('http://localhost:8000/stock/products/',
{
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Token ${token}`,
  },
}
)
    .then(response => response.json())
    .then(data => {
      document.getElementById('productCount').textContent = data.length;
    })
    .catch(error => {
      console.error('Error:', error);
    });

fetch('http://localhost:8000/stock/sales/',
{
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Token ${token}`,
  },
}
)
    .then(response => response.json())
  .then(data => {
    let totalSales = data.reduce((acc, sale) => acc + parseFloat(sale.total_price), 0);
    document.getElementById('salesAmount').textContent = `$${totalSales.toFixed(2)}`;
    })
    .catch(error => {
      console.error('Error:', error);
    });
fetch('http://localhost:8000/stock/producttypes/',
{
  method: 'GET',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Token ${token}`,
  },
}
)
    .then(response => response.json())
    .then(data => {
      const categoryCount = data.length;

      document.getElementById('categoryCount').textContent = categoryCount;
    })
    .catch(error => {
      console.error('Error:', error);
    });

    fetchTableData();

        async function fetchTableData() {
            try {
              const response = await fetch('http://localhost:8000/stock/sales/',
                {
                  method: 'GET',
                  headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Token ${token}`,
                  },
              });
              let data = await response.json();
              
              data.sort((a, b) => new Date(b.date) - new Date(a.date));
              
              data = data.slice(0, 5);

                const salesTable = document.getElementById('sales-table');

                data.forEach((row, index) => {
                    console.log(data)
                    const newRow = document.createElement('tr');

                    const indexCell = document.createElement('td');
                    indexCell.textContent = index + 1;
                    newRow.appendChild(indexCell);
                    indexCell.id = 'indexid'

                    const productNameCell = document.createElement('td');
                    productNameCell.textContent = row.product;
                    newRow.appendChild(productNameCell);
                    productNameCell.id = 'productid'

                    const dateCell = document.createElement('td');
                    dateCell.textContent = row.date;
                    newRow.appendChild(dateCell);
                    dateCell.id = 'dateid'


                    const totalSalesCell = document.createElement('td');
                    totalSalesCell.textContent = row.total_price;
                    newRow.appendChild(totalSalesCell);
                    totalSalesCell.id= 'salesid'


                    salesTable.appendChild(newRow);
                });
            } catch (error) {
                console.log('Error fetching table data:', error);
            }
          }
