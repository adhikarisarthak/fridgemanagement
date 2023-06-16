// Fridge items array
let fridgeItems = [];

// Function to add a new item
function addItem() {
  const name = document.getElementById('item-name').value;
  const quantity = parseInt(document.getElementById('item-quantity').value);
  const expiration = document.getElementById('item-expiration').value;
  const category = document.getElementById('item-category').value;
  
  const newItem = {
    name: name,
    quantity: quantity,
    expiration: expiration,
    category: category
  };
  
  fridgeItems.push(newItem);
  updateInventoryList();
  
  // Clear input fields
  document.getElementById('item-name').value = '';
  document.getElementById('item-quantity').value = '';
  document.getElementById('item-expiration').value = '';
  document.getElementById('item-category').value = '';
}

// Function to update the inventory list
function updateInventoryList() {
  const inventoryList = document.getElementById('inventory-list');
  inventoryList.innerHTML = '';
  
  for (let i = 0; i < fridgeItems.length; i++) {
    const item = fridgeItems[i];
    
    const listItem = document.createElement('li');
    listItem.textContent = item.name + ' - Quantity: ' + item.quantity + ' - Expiration: ' + item.expiration + ' - Category: ' + item.category;
    
    inventoryList.appendChild(listItem);
  }
}

// Function to search for
