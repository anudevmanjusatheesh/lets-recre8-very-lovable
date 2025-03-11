document.addEventListener('DOMContentLoaded', function() {
  "use strict";

  // --------------------------
  // Responsive Hamburger Menu
  // --------------------------
  // Select hamburger icon and navigation list elements
  const hamburger = document.querySelector('.hamburger');
  const navList = document.querySelector('.nav-list');

  if (hamburger && navList) {
    hamburger.addEventListener('click', function() {
      navList.classList.toggle('nav-active');
      // Optionally animate hamburger icon appearance
      hamburger.classList.toggle('toggle');
    });
  }

  // ---------------------------------------
  // Smooth Scrolling for Navigation Links
  // ---------------------------------------
  // Although CSS handles smooth scrolling, we provide a fallback that also closes the mobile menu.
  const navLinks = document.querySelectorAll('nav a[href^="#"]');
  navLinks.forEach(function(link) {
    link.addEventListener('click', function(e) {
      const targetId = link.getAttribute('href');
      const targetElement = document.querySelector(targetId);
      if (targetElement) {
        e.preventDefault();
        targetElement.scrollIntoView({
          behavior: 'smooth'
        });
        // If mobile menu is open, close it after click
        if (navList && navList.classList.contains('nav-active')) {
          navList.classList.remove('nav-active');
          if (hamburger) {
            hamburger.classList.remove('toggle');
          }
        }
      }
    });
  });

  // ----------------------------------------
  // Contact Form Validation with Feedback
  // ----------------------------------------
  // Check if a contact form exists within the #contact section.
  const contactForm = document.querySelector('#contact form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      e.preventDefault();

      // Suppose our contact form contains these required fields.
      const nameField = contactForm.querySelector('input[name="name"]');
      const emailField = contactForm.querySelector('input[name="email"]');
      const messageField = contactForm.querySelector('textarea[name="message"]');
      const feedbackEl = contactForm.querySelector('.form-feedback');

      let isValid = true;
      let errors = [];

      if (!nameField || !nameField.value.trim()) {
        isValid = false;
        errors.push("Name is required");
      }

      if (
        !emailField ||
        !emailField.value.trim() ||
        !/\S+@\S+\.\S+/.test(emailField.value)
      ) {
        isValid = false;
        errors.push("A valid email is required");
      }

      if (!messageField || !messageField.value.trim()) {
        isValid = false;
        errors.push("Message cannot be empty");
      }

      if (!isValid) {
        if (feedbackEl) {
          feedbackEl.innerText = errors.join('. ');
          feedbackEl.style.display = 'block';
        } else {
          alert(errors.join('. '));
        }
        return;
      }

      if (feedbackEl) {
        feedbackEl.innerText = 'Sending...';
        feedbackEl.style.display = 'block';
      }
      // Simulate asynchronous submission (replace with real API integration if needed)
      setTimeout(function() {
        if (feedbackEl) {
          feedbackEl.innerText = 'Thank you for contacting us!';
        }
        contactForm.reset();
      }, 1500);
    });
  }

  // ------------------------------------------------------
  // Fetching and Rendering Dynamic Data from Backend APIs
  // ------------------------------------------------------
  // Check if there is a target container for dynamic content (e.g., blog posts or similar)
  const dynamicContentContainer = document.getElementById('dynamic-content');
  if (dynamicContentContainer) {
    // Indicate loading state
    dynamicContentContainer.innerHTML = '<p>Loading data...</p>';

    // Fetch data from the backend API endpoint. Replace '/api/data' with the actual endpoint.
    fetch('/api/data')
      .then(function(response) {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(function(data) {
        // Suppose data is an array of items with title, excerpt, and link properties.
        let contentHTML = '';
        data.forEach(function(item) {
          contentHTML += `
            <article class="blog-entry fade-in">
              <h3>${item.title}</h3>
              <p>${item.excerpt}</p>
              <a href="${item.link}" class="read-more">Read More</a>
            </article>
          `;
        });
        dynamicContentContainer.innerHTML = contentHTML;
        // Reinitialize fade-in animations for new content.
        initFadeInAnimations();
      })
      .catch(function(error) {
        dynamicContentContainer.innerHTML = '<p>Error loading data: ' + error.message + '</p>';
      });
  }

  // -------------------------------------
  // Fade-in on Scroll using IntersectionObserver
  // -------------------------------------
  // This function applies a "visible" class to elements as they scroll into view.
  function initFadeInAnimations() {
    const faders = document.querySelectorAll('.fade-in');
    // Use IntersectionObserver if supported; otherwise, fallback (not provided here for brevity).
    const appearOptions = {
      threshold: 0.2
    };

    const appearOnScroll = new IntersectionObserver(function(entries, observer) {
      entries.forEach(function(entry) {
        if (!entry.isIntersecting) {
          return;
        }
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      });
    }, appearOptions);

    faders.forEach(function(fader) {
      appearOnScroll.observe(fader);
    });
  }

  // Initialize fade-in animations on page load.
  initFadeInAnimations();
});