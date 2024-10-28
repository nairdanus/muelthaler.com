
let ring_0 = document.getElementById("rings_0")
let ring_1 = document.getElementById("rings_1")
let ring_2 = document.getElementById("rings_2")
let ring_3 = document.getElementById("rings_3")
let ring_4 = document.getElementById("rings_4")
let ring_5 = document.getElementById("rings_5")
let ring_6 = document.getElementById("rings_6")

let ticking = false;

window.addEventListener('scroll', function() {
    if (!ticking) {
        window.requestAnimationFrame(() => {
            var value = window.scrollY;

            ring_1.style.top = window.innerHeight * 0.5 + -value * 0.35 + 'px';
            ring_2.style.top = window.innerHeight * 0.7 + -value * 0.50 + 'px';
            ring_3.style.top = window.innerHeight * 0.9 + -value * 0.65 + 'px';
            ring_4.style.top = window.innerHeight * 1.1 + -value * 0.78 + 'px';
            ring_5.style.top = window.innerHeight * 1.3 + -value * 0.92 + 'px';
            ring_6.style.top = window.innerHeight * 1.5 + -value * 1.05 + 'px';

            ticking = false;
        });
        ticking = true;
    }
});
