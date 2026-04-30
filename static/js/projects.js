
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

  function update() {
    const wrapperRect = wrapper.getBoundingClientRect();

    const scrolled = -wrapperRect.top;

    const total = wrapper.offsetHeight - window.innerHeight;

    const progress = Math.min(Math.max(scrolled / total, 0), 1);

    const maxScroll = track.scrollWidth - track.clientWidth;
    track.scrollLeft = progress * maxScroll;
  }

  window.addEventListener("scroll", update, { passive: true });
  update();

})();