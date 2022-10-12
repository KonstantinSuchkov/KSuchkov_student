"use strict";

const basketCount = document.querySelector('.cartIconWrap span');
const basketValue = document.querySelector('.basketTotalValue');
const basketTotal = document.querySelector('.basketTotal');
const basket = document.querySelector('.basket');

document.querySelector('.cartIconWrap').addEventListener('click', () => {
    basket.classList.toggle('hidden');
});

const itemsAll = {};

document.querySelector('.featuredItems').addEventListener('click', event => {
    if (event.target.tagName !== 'BUTTON') {
        return;
    }
    const featuredItem = event.target.closest('.featuredItem');
    const id = featuredItem.dataset.id;
    const price = featuredItem.dataset.price;
    const name = featuredItem.dataset.name;
    addItems(id, name, price);
});

function addItems(id, name, price) {
    if (!(id in itemsAll)) {
        itemsAll[id] = {
            id: id,
            name: name,
            price: price,
            count: 0,
        }
    };
    itemsAll[id].count++;
    console.log(itemsAll);
    basketCount.textContent = getCount().toString();
    basketValue.textContent = getPrice();
    productList(id);

}

function getCount() {
    return Object.values(itemsAll).reduce((acc, product) => acc + product.count, 0);
}

function getPrice() {
    return Object.values(itemsAll).reduce((acc, product) => acc + product.count * product.price, 0);
}

function productList(id) {
    const basketRow = basket.querySelector(`.basketRow[data-productId="${id}"]`);
    if (!basketRow) {
        renderNewProduct(id);
        return;
    }

    basketRow.querySelector('.productCount').textContent = itemsAll[id].count;
    basketRow.querySelector('.totalRow').textContent = itemsAll[id].count * itemsAll[id].price;

}

function renderNewProduct(id) {
    const row = `
        <div class="basketRow" data-productID="${id}">
            <div>${itemsAll[id].name}</div>
            <div>
                <span class="productCount">${itemsAll[id].count}</span> шт.
            </div>
            <div>$${itemsAll[id].price}</div>
            <div>
                $<span class="totalRow">${(itemsAll[id].price * itemsAll[id].count)}</span>
            </div>
        </div>
    `;
    basketTotal.insertAdjacentHTML('beforebegin', row);
}