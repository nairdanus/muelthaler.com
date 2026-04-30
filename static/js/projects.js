(function () {
  "use strict";

  const wrapper = document.querySelector(".projects-wrapper");
  const section = document.querySelector(".projects-section");
  const track   = document.querySelector(".projects-track");
  const cards   = document.querySelectorAll(".project-card");

  if (!wrapper || !section || !track) return;

  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((e) => {
          if (e.isIntersecting) {
            e.target.classList.add("is-visible");
            observer.unobserve(e.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    cards.forEach((c) => observer.observe(c));
  } else {
    cards.forEach((c) => c.classList.add("is-visible"));
  }

  function isMobile() {
    return window.innerWidth <= 768;
  }

  function setScrollLength() {
    const maxScroll = track.scrollWidth - track.clientWidth;

    const multiplier = 1.5;

    wrapper.style.height =
      `calc(100vh + ${maxScroll * multiplier}px)`;
  }

  function update() {
    if (isMobile()) {
      track.scrollLeft = 0;
      return;
    }

    const wrapperRect = wrapper.getBoundingClientRect();
    const scrolled = -wrapperRect.top;

    const maxScroll = track.scrollWidth - track.clientWidth;

    const total = wrapper.offsetHeight - window.innerHeight;

    const progress = Math.min(Math.max(scrolled / total, 0), 1);

    track.scrollLeft = progress * maxScroll;
  }

  function init() {
    setScrollLength();
    update();
  }

  window.addEventListener("scroll", update, { passive: true });
  window.addEventListener("resize", init);

  init();

})();