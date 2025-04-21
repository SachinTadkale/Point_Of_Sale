const contactSection = document.getElementById('contact');
const footer = document.getElementById('footer');

window.addEventListener('scroll', function() {
    const contactPos = contactSection.getBoundingClientRect();
    if (contactPos.top <= window.innerHeight) {
        footer.style.display = 'block';
    } else {
        footer.style.display = 'none';
    }
});