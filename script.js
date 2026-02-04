document.addEventListener('DOMContentLoaded', () => {
    // Mobile Navigation Toggle
    const navToggle = document.querySelector('.nav-toggle');
    const navLinks = document.querySelector('.nav-links');
    const links = document.querySelectorAll('.nav-links a');

    if (navToggle) {
        navToggle.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            const icon = navToggle.querySelector('i');
            if (navLinks.classList.contains('active')) {
                icon.classList.remove('fa-bars');
                icon.classList.add('fa-times');
            } else {
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    }

    // Close mobile menu when a link is clicked
    links.forEach(link => {
        link.addEventListener('click', () => {
            if (navLinks.classList.contains('active')) {
                navLinks.classList.remove('active');
                const icon = navToggle.querySelector('i');
                icon.classList.remove('fa-times');
                icon.classList.add('fa-bars');
            }
        });
    });

    // Scroll Effect for Navbar
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.style.background = 'rgba(10, 10, 22, 0.95)';
            navbar.style.padding = '10px 0';
            navbar.style.boxShadow = '0 5px 20px rgba(0,0,0,0.5)';
        } else {
            navbar.style.background = 'rgba(22, 22, 37, 0.7)';
            navbar.style.padding = '15px 0';
            navbar.style.boxShadow = 'none';
        }
    });

    // Intersection Observer for Fade-in Animations
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('visible');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    // Animate elements
    const animatedElements = document.querySelectorAll('.section-title, .project-card, .blog-card, .about-text h3, .about-text p, .skill-category, .contact-wrapper');
    
    // Add initial styles and observe
    animatedElements.forEach((el, index) => {
        el.style.opacity = '0';
        el.style.transform = 'translateY(30px)';
        el.style.transition = 'all 0.6s ease-out';
        
        // Stagger delay for cards
        if (el.classList.contains('project-card') || el.classList.contains('blog-card')) {
             el.style.transitionDelay = `${(index % 3) * 0.1}s`;
        }
        
        observer.observe(el);
    });

    // Handle class addition for visible state
    // We can't put the CSS in JS easily for the 'visible' class without dirtying clean JS, 
    // so let's append a style block or inline styles in the loop. 
    // preferred: keep style logic in CSS, but since I can't edit CSS again easily right now without another tool call, 
    // I will dynamically add the class logic here using inline styles interaction in the observer callback above? 
    // NO, I should assume I can't restart CSS. 
    // Actually, I can just inject a style tag.
    
    const style = document.createElement('style');
    style.innerHTML = `
        .visible {
            opacity: 1 !important;
            transform: translateY(0) !important;
        }
    `;
    document.head.appendChild(style);
});
