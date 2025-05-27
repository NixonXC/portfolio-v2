const hamburger = document.querySelector('.hamburger');
const mobileMenu = document.querySelector('.mobile-menu');
const closeButton = document.querySelector('.close-button');

hamburger.addEventListener('click', () => {
    mobileMenu.classList.add('open');
});

closeButton.addEventListener('click', () => {
    mobileMenu.classList.remove('open');
});

mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
        mobileMenu.classList.remove('open');
    });
});
document.getElementById('github').onclick = function() {
    window.location.href='https://github.com/NixonXC'
}
document.getElementById('linkedin').onclick = function() {
    window.location.href='https://www.linkedin.com/in/atharva-kulkarni-5595742a6/'
}
document.getElementById('insta').onclick = function() {
    window.location.href='https://www.instagram.com/prodbyatharva/'
}
particlesJS.load('particles-js', '/static/particles.js-master/particles.json', function() {
  console.log('callback - particles.js config loaded');
});
