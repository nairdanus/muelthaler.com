
(function () {
  "use strict";

  const cards = document.querySelectorAll(".project-card");

  if ("IntersectionObserver" in window) {
    const revealObserver = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-visible");
            revealObserver.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.12 }
    );
    cards.forEach((card) => revealObserver.observe(card));
  } else {
    // Fallback: just show everything
    cards.forEach((c) => c.classList.add("is-visible"));
  }

  function applyParallax() {
    cards.forEach((card) => {
      const img = card.querySelector(".project-card__img");
      if (!img || img.classList.contains("project-card__img--placeholder")) return;

      const rect = card.getBoundingClientRect();
      const windowH = window.innerHeight;

      const progress = 1 - (rect.bottom / (windowH + rect.height));
      const shift = (progress - 0.5) * 60;

      img.style.transform = `translateY(${shift}px)`;
    });
  }

  window.addEventListener("scroll", applyParallax, { passive: true });
  applyParallax(); // run once on load

})();