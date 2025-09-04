const addCartButtons = document.querySelectorAll(".addcart");
const cartIcon = document.getElementById("cart-icon");

addCartButtons.forEach((button) => {
  button.addEventListener("click", () => {
    let count = parseInt(cartIcon.innerText) || 0;
    count += 1;
    cartIcon.innerText = count;
  });
});

function addToCart(productId) {
  fetch(`/add-to-cart/${productId}/`)
    .then((res) => res.json())
    .then((data) => {
      document.getElementById("cart-icon").innerText = data.cart_count;
    });
}

// // Exemplo para todos os botões:
document.querySelectorAll(".addcart").forEach((btn) => {
  btn.addEventListener("click", () => {
    const productId = btn.dataset.productId;
    addToCart(productId);
  });
});
