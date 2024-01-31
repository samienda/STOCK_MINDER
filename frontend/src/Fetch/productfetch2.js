const token = localStorage.getItem('token');
const dropdown = document.getElementById('product-type');
const supplierDropdown = document.getElementById('Supplier-name');
const propertyDropdown = document.getElementById('property-name');
const formE1 = document.getElementById('form');
let search = '';

const searchInput = document.getElementById('search-bar');
searchInput.addEventListener('input', (event) => { 
  search = event.target.value;
  const tableBody = document.querySelector('#productTable tbody');
  tableBody.innerHTML = '';
  fetchData(search);
})


function fetchData(search = '' ) 
{fetch(`http://localhost:8000/stock/products/?search=${search}`, {
  method: 'GET',
  headers:{
    'Content-type': 'application/json',
    'Authorization': `Token ${token}`,
  }
})
  .then(response => response.json())
  .then(data => {
    const tableBody = document.querySelector('#productTable tbody');

    data.forEach(product => {
      const row = document.createElement('tr');

      const codeCell = document.createElement('td');
      codeCell.textContent = product.id;
      row.appendChild(codeCell);

      const nameCell = document.createElement('td');
      nameCell.textContent = product.productname;
      row.appendChild(nameCell);

      const supplierCell = document.createElement('td');
      supplierCell.textContent = product.supplier_str;
      row.appendChild(supplierCell);

      
      const ProductTypeCell = document.createElement('td');
      ProductTypeCell.textContent = product.product_type_str;
      row.appendChild(ProductTypeCell);

      
      const quantityCell = document.createElement('td');
      quantityCell.textContent = product.quantity;
      row.appendChild(quantityCell);

      
      const priceCell = document.createElement('td');
      priceCell.textContent = product.price;
      row.appendChild(priceCell);

      
      const propertyCell = document.createElement('td');
      propertyCell.textContent = product.property_str;
      row.appendChild(propertyCell);
      propertyCell.id= 'propertycell'

      const actionsCell = document.createElement('td');
      const updateLink = document.createElement('button');

      updateLink.textContent = 'Update';
      actionsCell.appendChild(updateLink);
      updateLink.id = 'updatelink2'

      updateLink.addEventListener('click', (event) => {
        event.preventDefault();
        populate(product.id, product.productname, product.quantity, product.price, product.threshold, product.supplier_str , product.product_type_str, product.property_str, row); // Call the deleteSupplier function passing the supplier ID and row element
       });

      const deleteLink = document.createElement('button');
      deleteLink.textContent = 'Delete';
      actionsCell.appendChild(deleteLink);
      deleteLink.id= 'deletelink2'

      deleteLink.addEventListener('click', (event) => {
        event.preventDefault();
        deleteProduct(product.id, row);
      });
      actionsCell.appendChild(deleteLink);
      actionsCell.id= 'actioncell'

      row.appendChild(actionsCell);
                                                                                         
      tableBody.appendChild(row);
    });
  })
  .catch(error => {
    console.error('Error fetching product data:', error);
  });
}

fetchData(search);

  function deleteProduct(productId, row) {
    const token = localStorage.getItem('token');
  
    fetch(`http://localhost:8000/stock/products/${productId}`, {
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
          alert('You can not delete this product, Product is related to Sale')
          throw new Error('Failed to delete the supplier.');
        }
      })
      .catch(error => {
        console.error('Error deleting supplier:', error);
      });
  }

  //Update Product
  //Update Product
  //Update Product
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

  const productcode = document.getElementById('updatecode') 
  const productname = document.getElementById('updatedname') 
  const productprice = document.getElementById('updatedPrice') 
  const productquantity  = document.getElementById('updatedQuantity')
  const productThreshold = document.getElementById('updatedThreshold')
  const productsupplier = document.getElementById('Supplier-name')
  const productpropertyDrop = document.getElementById('property-name')
  const producttypeDrop = document.getElementById('product-type')

  function populate(id, name , quantity, price, threshold, supplier , product_type, productproperty,  row){
    console.log(id, name,  quantity,price, threshold)

    productcode.value = id;
    console.log(productsupplier.value)
    productname.value = name;
    productprice.value = price;
    productquantity.value = quantity;
    productThreshold.value = threshold;
    // productsupplier.value = supplier;
    // productpropertyDrop.value = product_type;
    // producttypeDrop.value = productproperty;

    // productsupplier.value =  supplierDropdown.value;
    // productpropertyDrop.value = propertyDropdown.value;
    // producttypeDrop.value = dropdown.value;
    const productTypeOption = Array.from(dropdown.options).find(option => option.text === product_type);
  if (productTypeOption) {
    producttypeDrop.value = productTypeOption.value;
  }

  const supplierOption = Array.from(supplierDropdown.options).find(option => option.text === supplier);
  if (supplierOption) {
    productsupplier.value = supplierOption.value;
  }

  const propertyOption = Array.from(propertyDropdown.options).find(option => option.text === productproperty);
  if (propertyOption) {
    productproperty.value = propertyOption.value;
  }
    
  }
  formE1.addEventListener('submit', (event) => {
    event.preventDefault();

    const id = productcode.value;
    const name = productname.value;
    const price = productprice.value;
    const quantity = productquantity.value;
    const threshold = productThreshold.value;
    const supplier = productsupplier.value;
    const productproperty = productpropertyDrop.value;
    const producttype = producttypeDrop.value;

    const data = {
      productname: name,
      quantity:quantity,
      price:price,
      threshold:threshold,
      supplier:supplier,
      product_type:producttype,
      property: productproperty
    };

    fetch(`http://localhost:8000/stock/products/${id}/`, {
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
          location.reload()
          alert('Product updated successfully!');
        } else {
          alert('There was a problem updating the product');
        }
      })
      .then(data => {
        console.log(data);
      })
      .catch(error => console.log(error));
  });




  






// const producttype = document.querySelector('.producttype')
// let output = ''


// const renderPosts = (posts) =>{
//     posts.forEach(post => {
//         output += `
//         <div class="form-group" id="producttype">
//         <label for="sell-code">Product Type:</label>
//         <select id="sell-code" name="sell-code" required>
//           <option value="option3">${post.name}</option>
//         </select>
//       </div>;`
//     })
//     producttype.innerHTML = output;
// }
// fetch('http://localhost:8000/stock/producttypes/', {
//     method: 'GET',
//     headers:{
//       'Content-type': 'application/json'
//     },
//   })
//     .then(res => res.json())
//     .then(data => {renderPosts(data);
//     })
//     .catch(error => {
//       // Handle any errors
//       console.error('Error:', error);
//     });


  