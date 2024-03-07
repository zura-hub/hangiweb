document.addEventListener('DOMContentLoaded', function () {
    // Your code here
    var symbol_one = document.querySelector('.symbol_one');
    var symbol_two = document.querySelector('.symbol_two');
    var nav_list = document.querySelector('.nav-list');
    var social_icon = document.querySelectorAll('.social_icons');

    symbol_one.addEventListener('click', () => {
        symbol_two.style.display = 'flex';
        symbol_one.style.display = 'none';
        nav_list.style.display = 'block';
        social_icon.style.display = 'flex';
    });

    symbol_two.addEventListener('click', () => {
        symbol_two.style.display = 'none';
        symbol_one.style.display = 'flex';
        nav_list.style.display = 'none';
        social_icon.style.display = 'none';
    });
});


// carrousel

document.addEventListener('DOMContentLoaded', function () {
    let currentIndex = 0;
    const slides = document.querySelectorAll('.carousel-slide');

    function showSlide(index) {
        slides.forEach((slide, i) => {
            slide.style.display = i === index ? 'block' : 'none';
        });
    }

    function nextSlide() {
        currentIndex = (currentIndex + 1) % slides.length;
        showSlide(currentIndex);
    }

    function prevSlide() {
        currentIndex = (currentIndex - 1 + slides.length) % slides.length;
        showSlide(currentIndex);
    }


    showSlide(currentIndex);


    setInterval(nextSlide, 3000);
});

// fullscreen photo thumbnail image
function showFullscreen(imgUrl, description) {
    var fullscreenContainer = document.getElementById('fullscreen-container');
    var fullscreenImg = document.getElementById('fullscreen-img');

    fullscreenContainer.style.display = 'block';
    fullscreenImg.src = imgUrl;
    fullscreenImg.alt = description;
}

function closeFullscreen() {
    var fullscreenContainer = document.getElementById('fullscreen-container');
    fullscreenContainer.style.display = 'none';
}


document.addEventListener('DOMContentLoaded', function () {
    var project = document.getElementById('project');
    var projectHided = document.querySelectorAll('[id^="project_inner"]');

    project.addEventListener('click', function () {
        projectHided.forEach(function (element) {
            element.style.display = (element.style.display === 'none' || element.style.display === '') ? 'flex' : 'none';
        });
    });
});









