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
particlesJS.load('particles-js', '/static/particles.js-master/particles.json', function() {
  console.log('callback - particles.js config loaded');
});

  let element = document.getElementById('element');

  const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()_+=';
  const transitionTime = 2000; // Duration of scramble animation (in ms)
  const frameRate = 30; // Frames per second
  const phrases = ['Full-Stack Developer', 'Web Developer', 'AI Enthusiast'];
  let currentPhraseIndex = 0;

  function matrixTransition(from, to, duration, callback) {
    const frameCount = Math.floor(duration / (1000 / frameRate));
    let frame = 0;
    const maxLength = Math.max(from.length, to.length);

    const interval = setInterval(() => {
      let output = '';
      for (let i = 0; i < maxLength; i++) {
        if (frame >= frameCount) {
          output += to[i] || '';
        } else if (Math.random() < frame / frameCount) {
          output += to[i] || '';
        } else {
          output += characters.charAt(Math.floor(Math.random() * characters.length));
        }
      }

      element.textContent = output;

      frame++;
      if (frame > frameCount) {
        clearInterval(interval);
        callback && callback();
      }
    }, 1000 / frameRate);
  }

  function loopPhrases() {
    const current = phrases[currentPhraseIndex];
    const nextIndex = (currentPhraseIndex + 1) % phrases.length;
    const next = phrases[nextIndex];

    matrixTransition(current, next, transitionTime, () => {
      currentPhraseIndex = nextIndex;
      setTimeout(loopPhrases, 1500); // Wait before next transition
    });
  }

  // Start loop after slight delay
  setTimeout(() => {
    element.textContent = phrases[0];
    setTimeout(loopPhrases, 1500);
  }, 1000);
