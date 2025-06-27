document.addEventListener("DOMContentLoaded", () => {
  const carousels = document.querySelectorAll(".carousel");

  carousels.forEach((carousel, index) => {
    const rawData = carousel.getAttribute("data-images");
    const imageUrls = JSON.parse(rawData); // ahora es un array de URLs
    const imageObjects = imageUrls.map(url => ({ url }));
    initCarousel(carousel.id, imageObjects);
  });
});

  function initCarousel(containerId, images) {
    let current = 0;
    let autoSlideTimer;

    const container = document.getElementById(containerId);
    const blurBackground = container.querySelector(".blur-background");
    const carouselTrack = container.querySelector(".carousel-track");
    const nextBtn = container.querySelector(".nextBtn");
    const prevBtn = container.querySelector(".prevBtn");

function showImage(index, direction = "right") {
    const newImg = document.createElement("img");
    newImg.src = images[index].url;
    newImg.className = "carousel-img";
    newImg.classList.add(direction === "right" ? "slide-in-right" : "slide-in-left");

    const currentImg = carouselTrack.querySelector(".carousel-img");
    if (currentImg) {
    carouselTrack.insertBefore(newImg, currentImg);
    currentImg.classList.add(direction === "right" ? "slide-out-left" : "slide-out-right");
    currentImg.addEventListener("animationend", () => {
        currentImg.remove();
    }, { once: true });
    } else {
    carouselTrack.appendChild(newImg);
    }

    blurBackground.style.backgroundImage = `url(${images[index].url})`;
}

function nextImage() {
    current = (current + 1) % images.length;
    showImage(current, "right");
}

function prevImage() {
    current = (current - 1 + images.length) % images.length;
    showImage(current, "left");
}

function resetAutoSlide() {
    clearInterval(autoSlideTimer);
    autoSlideTimer = setInterval(nextImage, 5000);
}

// Inicializar eventos
showImage(current);

nextBtn.addEventListener("click", () => {
    nextImage();
    resetAutoSlide();
});

prevBtn.addEventListener("click", () => {
    prevImage();
    resetAutoSlide();
});

autoSlideTimer = setInterval(nextImage, 5000);
}
