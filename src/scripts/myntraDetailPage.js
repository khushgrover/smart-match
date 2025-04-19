// Initialize variables for product details
const productName = "Men's Slim Fit Shirt";
const productPrice = 1299;
const productBrand = "Louis Philippe";
const productDescription = "Look sharp and smart by wearing this slim fit shirt from Louis Philippe. Made from premium quality fabric, this shirt is comfortable to wear and easy to maintain. Perfect for any formal occasion, this shirt is a must-have in your wardrobe.";

// Set product details on the page
document.getElementById("product-name").innerText = productName;
document.getElementById("product-price").innerText = `Rs. ${productPrice}`;
document.getElementById("product-brand").innerText = productBrand;
document.getElementById("product-description").innerText = productDescription;

// Add product images to the page
const productImages = ["image1.jpg", "image2.jpg", "image3.jpg"];
const imageContainer = document.getElementById("product-images");
for (let i = 0; i < productImages.length; i++) {
    const image = document.createElement("img");
    image.src = `images/${productImages[i]}`;
    image.alt = `${productName} image ${i + 1}`;
    imageContainer.appendChild(image);
}

// Add event listener for "Add to Cart" button
document.getElementById("add-to-cart").addEventListener("click", () => {
    alert(`You have added ${productName} to your cart.`);
});
