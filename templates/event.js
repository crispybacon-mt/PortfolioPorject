document.addEventListener("DOMContentLoaded", function() {
  const slideshow = document.querySelector(".slideshow");
  const images = slideshow.getElementsByTagName("imgs");
  let currentImageIndex = 0;

  // Function to change the image every 30 seconds
  function changeImage() {
    images[currentImageIndex].classList.remove("active");
    currentImageIndex = (currentImageIndex + 1) % images.length;
    images[currentImageIndex].classList.add("active");
  }

  // Initially show the first image
  images[currentImageIndex].classList.add("active");

  // Fetch images from the News API
  fetchNewsImages()
    .then(newsImages => {
      if (newsImages.length > 0) {
        // Update the image sources with the fetched images
        for (let i = 0; i < newsImages.length && i < images.length; i++) {
          images[i].src = newsImages[i];
        }
      }
    })
    .catch(error => {
      console.error(error);
    });

  // Start the slideshow
  setInterval(changeImage, 30000);
});

function fetchNewsImages() {
  const apiKey = "9ad15860ec644be8a8fefd37f413bb50"; // Replace with your News API key
  const apiUrl = `https://newsapi.org/v2/top-headlines?country=us&apiKey=${'9ad15860ec644be8a8fefd37f413bb50'}`;

  return fetch(apiUrl)
    .then(response => response.json())
    .then(data => {
      // Extract image URLs from the fetched news articles
      const newsImages = data.articles.map(article => article.urlToImage);
      return newsImages.filter(imageUrl => imageUrl !== null);
    });
}
