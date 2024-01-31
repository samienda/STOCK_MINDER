const token = localStorage.getItem("token");
function fetchData() {
  return fetch("http://127.0.0.1:8000/stock/sales/",
  {
    method: 'GET',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Token ${token}`,
    },
}
  ).then((response) =>
    response.json()
  );
}

function processData(data, dateRange) {
  const currentDate = new Date();
  const token = localStorage.getItem("token");

  if (!token) {
    throw new Error("Token is missing or empty");
  }


  const aggregatedData = {};

  data.forEach((sale) => {
    const saleDate = new Date(sale.date);

    let startDate;
    if (dateRange === "weekly") {
      startDate = new Date(
        currentDate.getFullYear(),
        currentDate.getMonth(),
        currentDate.getDate() - 7
      );
    } else if (dateRange === "monthly") {
      startDate = new Date(
        currentDate.getFullYear(),
        currentDate.getMonth() - 1,
        currentDate.getDate()
      );
    } else if (dateRange === "daily") {
      startDate = new Date(
        currentDate.getFullYear(),
        currentDate.getMonth(),
        currentDate.getDate() - 1
      );
    } else {
      throw new Error("Invalid date range");
    }

    if (saleDate >= startDate && saleDate <= currentDate) {
      if (!aggregatedData[sale.product_str]) {
        aggregatedData[sale.product_str] = 0;
      }
      if (sale.quantity != 0){
      aggregatedData[sale.product_str] += sale.quantity;
    }
  }
  });

  const productIds = Object.keys(aggregatedData);
  const quantitiesSold = Object.values(aggregatedData);

  const trace1 = {
    x: productIds,
    y: quantitiesSold,
    type: "bar",
    marker: {
      color: "skyblue",
    },
  };

  //  const trace2 = {
  //   values: quantitiesSold,
  //   labels: productIds,
  //   type: "pie",
  // };

  // console.log(trace2)



  return [trace1];
}

function updateGraph(dateRange) {
  fetchData()
    .then((data) => {
      const processedData1 = processData(data, dateRange);
      // const processedData2 = processData(data, dateRange)[1];

      // console.log(processedData1);

      const graphDiv1 = document.getElementById("graph1");
      Plotly.newPlot(graphDiv1, processedData1);

      // var layout = {
      //   height: 1000,
      //   width: 1000
      // };

      // const graphDiv2 = document.getElementById("graph2");
      // Plotly.newPlot(graphDiv2, processedData2, layout);
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
}

updateGraph("weekly");


// function downloadTable(version) {
//     const apiUrl = 'http://localhost:8000/stock/products/'; // Replace with the actual API endpoint that provides the table data
//     const filename = `table_version_${version}.csv`;
  
//   fetch(apiUrl,{
//     method: 'GET',
//     headers: {
//       'Content-Type': 'application/json',
//       'Authorization': `Token ${token},`,
//     }}
//   )
//       .then(response => response.json())
//       .then(data => {
//         // Extract table headers
//         const headers = Object.keys(data[0]);
  
//         // Convert table data into CSV format
//         let csvContent = headers.join(',') + '\n';
//         data.forEach(row => {
//           const rowData = headers.map(header => {
//             const value = row[header];
//             if (typeof value === 'string') {
//               return value.replace(/,/g, '');
//             }
//             return String(value);
//           });
//           csvContent += rowData.join(',') + '\n';
//         });
  
//         // Create and download CSV file
//         const csvDataUri = 'data:text/csv;charset=utf-8,' + encodeURIComponent(csvContent);
//         const csvLink = document.createElement('a');
//         csvLink.href = csvDataUri;
//         csvLink.download = filename;
//         csvLink.style.display = 'none';
//         document.body.appendChild(csvLink);
//         csvLink.click();
//         document.body.removeChild(csvLink);
  
//         const htmlContent = `<table><thead><tr>${headers.map(header => `<th>${header}</th>`).join('')}</tr></thead><tbody>${data.map(row => `<tr>${headers.map(header => `<td>${row[header]}</td>`).join('')}</tr>`).join('')}</tbody></table>`;
//         const htmlDataUri = 'data:text/html;charset=utf-8,' + encodeURIComponent(htmlContent);
//         const htmlLink = document.createElement('a');
//         htmlLink.href = htmlDataUri;
//         htmlLink.download = `table_version_${version}.html`;
//         htmlLink.style.display = 'none';
//         document.body.appendChild(htmlLink);
//         htmlLink.click();
//         document.body.removeChild(htmlLink);
//       })
//       .catch(error => {
//         console.error('Error:', error);
//       });
//   }

