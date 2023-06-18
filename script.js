document.addEventListener('DOMContentLoaded', function () {
  const addItemForm = document.getElementById('add-item-form');
  const itemList = document.getElementById('item-list');
  const searchInput = document.getElementById('search-input');
  const searchResults = document.getElementById('search-results');
  const quantityList = document.getElementById('quantity-list');
  const expiredList = document.getElementById('expired-list');
  const generateListBtn = document.getElementById('generate-list-btn');
  const shoppingList = document.getElementById('shopping-list');
  let fridgeItems = [];

  addItemForm.addEventListener('submit', function (e) {
    e.preventDefault();

    const itemName = document.getElementById('item-name').value;
    const expirationDate = document.getElementById('expiration-date').value;
    const quantity = document.getElementById('quantity').value;

    const item = {
      name: itemName,
      expiration: expirationDate,
      quantity: quantity
    };

    fridgeItems.push(item);

    renderItemList();
    renderQuantityList();
    renderExpiredList();
    clearAddItemForm();
  });

  function renderItemList() {
    itemList.innerHTML = '';

    fridgeItems.forEach(function (item, index) {
      const listItem = document.createElement('li');
      listItem.textContent = `${item.name} - Exp: ${item.expiration} - Qty: ${item.quantity}`;

      const removeButton = document.createElement('button');
      removeButton.textContent = 'Remove';
      removeButton.addEventListener('click', function () {
        removeItem(index);
      });

      listItem.appendChild(removeButton);
      itemList.appendChild(listItem);
    });
  }

  function removeItem(index) {
    fridgeItems.splice(index, 1);
    renderItemList();
    renderQuantityList();
    renderExpiredList();
  }

  function renderQuantityList() {
    quantityList.innerHTML = '';

    const quantities = {};

    fridgeItems.forEach(function (item) {
      const itemName = item.name;
      const quantity = parseInt(item.quantity);

      if (quantities[itemName]) {
        quantities[itemName] += quantity;
      } else {
        quantities[itemName] = quantity;
      }
    });

    for (const itemName in quantities) {
      const quantityItem = document.createElement('li');
      quantityItem.textContent = `${itemName} - Qty: ${quantities[itemName]}`;
      quantityList.appendChild(quantityItem);
    }
  }

  function renderExpiredList() {
    expiredList.innerHTML = '';

    const currentDate = new Date();

    fridgeItems.forEach(function (item) {
      const expirationDate = new Date(item.expiration);

      if (expirationDate < currentDate) {
        const expiredItem = document.createElement('li');
        expiredItem.textContent = `${item.name} - Exp: ${item.expiration} - Qty: ${item.quantity}`;
        expiredList.appendChild(expiredItem);
      }
    });
  }

  function clearAddItemForm() {
    document.getElementById('item-name').value = '';
    document.getElementById('expiration-date').value = '';
    document.getElementById('quantity').value = '';
  }

  searchInput.addEventListener('input', function () {
    const query = searchInput.value.toLowerCase();
    const results = fridgeItems.filter(function (item) {
      return item.name.toLowerCase().includes(query);
    });

    renderSearchResults(results);
  });

  function renderSearchResults(results) {
    searchResults.innerHTML = '';

    if (results.length > 0) {
      results.forEach(function (item) {
        const searchResultItem = document.createElement('li');
        searchResultItem.textContent = `${item.name} - Exp: ${item.expiration} - Qty: ${item.quantity}`;
        searchResults.appendChild(searchResultItem);
      });
    } else {
      const noResults = document.createElement('li');
      noResults.textContent = 'No matching items found.';
      searchResults.appendChild(noResults);
    }
  }

  itemList.addEventListener('click', function (e) {
    const target = e.target;
    if (target.tagName === 'BUTTON') {
      const listItem = target.parentNode;
      const index = Array.from(itemList.children).indexOf(listItem);
      removeItem(index);
    }
  });

  generateListBtn.addEventListener('click', function () {
    shoppingList.innerHTML = '';

    fridgeItems.forEach(function (item) {
      if (parseInt(item.quantity) > 0) {
        const listItem = document.createElement('li');
        listItem.textContent = item.name;
        shoppingList.appendChild(listItem);
      }
    });
  });
});



// USER CLASS AND FUNCTIONS
class User {
  constructor(userId, userName, userEmail, userPassword) {
    this.userId = userId;
    this.userName = userName;
    this.userEmail = userEmail;
    this.userPassword = userPassword;
  }

  DisplayUserInfo() {
    console.log(this.userId);
    console.log(this.userName);
    console.log(this.userEmail);
    console.log(this.userPassword);
  }
}

class UserManager {
  constructor() {
    this.UserManager = []; // create array of Users
  }

  registerUser(userId, userName, userEmail, userPassword) {
    // add new User to array of UserManager
    let u = new User(userId, userName, userEmail, userPassword);
    this.UserManager.push(u);
  }

}

let Users = new UserManager(); // create array of User objects

}

// Authentication






