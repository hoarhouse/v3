// Centralized Navigation Controller for DCF Hungary Website

// Define menu structure in one place
const menuItems = [
    { text: 'Home', href: 'index.html', page: 'index' },
    { text: 'About', href: 'about.html', page: 'about' },
    { text: 'Initiatives', href: 'initiatives.html', page: 'initiatives' },
    { text: 'Get Involved', href: 'get-involved.html', page: 'get-involved' },
    { text: 'Contact', href: 'contact.html', page: 'contact' }
];

// Generate navigation HTML
function generateNav() {
    const currentPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
    
    const navHTML = `
        <div class="nav-container">
            <div class="nav-brand">
                <a href="index.html">DCF Hungary</a>
            </div>
            <button class="nav-toggle" id="navToggle" aria-label="Toggle navigation">
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
                <span class="hamburger-line"></span>
            </button>
            <div class="nav-overlay" id="navOverlay"></div>
            <div class="nav-menu" id="navMenu">
                <button class="nav-close" id="navClose" aria-label="Close navigation">
                    <span class="close-line"></span>
                    <span class="close-line"></span>
                </button>
                <ul class="nav-list">
                    ${menuItems.map(item => `
                        <li class="nav-item">
                            <a href="${item.href}" class="nav-link ${currentPage === item.page ? 'active' : ''}">
                                ${item.text}
                            </a>
                        </li>
                    `).join('')}
                </ul>
            </div>
        </div>
    `;
    
    return navHTML;
}

// Inject navigation into page
function initNav() {
    const navElement = document.getElementById('main-nav');
    if (navElement) {
        navElement.innerHTML = generateNav();
        
        // Get elements
        const navToggle = document.getElementById('navToggle');
        const navClose = document.getElementById('navClose');
        const navMenu = document.getElementById('navMenu');
        const navOverlay = document.getElementById('navOverlay');
        const body = document.body;
        
        // Open menu
        if (navToggle) {
            navToggle.addEventListener('click', () => {
                navMenu.classList.add('nav-menu--active');
                navOverlay.classList.add('nav-overlay--active');
                body.classList.add('menu-open'); // Add class to body
                body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
            });
        }
        
        // Close menu function
        const closeMenu = () => {
            navMenu.classList.remove('nav-menu--active');
            navOverlay.classList.remove('nav-overlay--active');
            body.classList.remove('menu-open'); // Remove class from body
            body.style.overflow = ''; // Restore scrolling
        };
        
        // Close button
        if (navClose) {
            navClose.addEventListener('click', closeMenu);
        }
        
        // Overlay click
        if (navOverlay) {
            navOverlay.addEventListener('click', closeMenu);
        }
        
        // Close menu when clicking on a link (mobile)
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', closeMenu);
        });
    }
}

// Add navigation styles
const navStyles = `
<style>
/* Navigation Base Styles */
#main-nav {
    background-color: var(--primary);
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
}

.nav-brand a {
    color: var(--white);
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
}

/* Desktop Navigation */
.nav-menu {
    display: block;
}

.nav-list {
    list-style: none;
    display: flex;
    gap: 1rem;
    margin: 0;
    padding: 0;
}

.nav-item {
    margin: 0;
}

.nav-link {
    color: var(--white);
    text-decoration: none;
    padding: 0.75rem 1.25rem;
    border-radius: 4px;
    transition: background-color 0.3s ease;
    display: block;
}

.nav-link:hover {
    background-color: rgba(255,255,255,0.1);
    text-decoration: none;
}

.nav-link.active {
    background-color: rgba(255,255,255,0.2);
    font-weight: 600;
}

/* Hamburger Menu Button - Hidden on Desktop */
.nav-toggle {
    display: none;
    flex-direction: column;
    justify-content: center;
    gap: 4px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 8px;
    min-width: 44px;
    min-height: 44px;
}

.hamburger-line {
    width: 24px;
    height: 3px;
    background-color: var(--white);
    transition: all 0.3s ease;
    display: block;
}

/* Close Button - Always Hidden on Desktop */
.nav-close {
    display: none;
}

/* Overlay - Hidden on Desktop */
.nav-overlay {
    display: none;
}

/* Tablet Styles */
@media (max-width: 1023px) and (min-width: 768px) {
    .nav-list {
        gap: 0.5rem;
    }
    
    .nav-link {
        padding: 0.75rem 1rem;
    }
}

/* Mobile Styles */
@media (max-width: 767px) {
    /* Show hamburger button */
    .nav-toggle {
        display: flex;
        z-index: 998;
        transition: opacity 0.3s ease;
    }
    
    /* Hide hamburger when menu is open */
    body.menu-open .nav-toggle {
        opacity: 0;
        pointer-events: none;
    }
    
    /* Overlay for background dimming */
    .nav-overlay {
        display: block;
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background-color: rgba(0, 0, 0, 0.5);
        opacity: 0;
        visibility: hidden;
        transition: opacity 0.3s ease, visibility 0.3s ease;
        z-index: 999;
    }
    
    .nav-overlay--active {
        opacity: 1;
        visibility: visible;
    }
    
    /* Mobile Menu Container */
    .nav-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 280px;
        max-width: 85%;
        height: 100vh;
        background-color: var(--primary);
        transition: right 0.3s ease;
        z-index: 1001;
        overflow-y: auto;
        box-shadow: -2px 0 10px rgba(0,0,0,0.2);
    }
    
    .nav-menu--active {
        right: 0;
    }
    
    /* Close button for mobile - properly positioned */
    .nav-close {
        display: flex;
        position: fixed;
        top: 20px;
        right: 20px;
        background: rgba(255, 255, 255, 0.1);
        border: 2px solid var(--white);
        border-radius: 50%;
        cursor: pointer;
        padding: 0;
        width: 48px;
        height: 48px;
        align-items: center;
        justify-content: center;
        z-index: 1002;
        transition: background 0.3s ease, transform 0.2s ease;
    }
    
    .nav-close:hover,
    .nav-close:focus {
        background: rgba(255, 255, 255, 0.2);
        transform: scale(1.1);
    }
    
    .close-line {
        position: absolute;
        width: 20px;
        height: 2px;
        background-color: var(--white);
    }
    
    .close-line:first-child {
        transform: rotate(45deg);
    }
    
    .close-line:last-child {
        transform: rotate(-45deg);
    }
    
    /* Mobile Menu List */
    .nav-list {
        flex-direction: column;
        gap: 0;
        padding: 4rem 1rem 2rem;
    }
    
    .nav-item {
        margin: 0.25rem 0;
    }
    
    .nav-link {
        padding: 1rem;
        min-height: 48px;
        display: flex;
        align-items: center;
        font-size: 1.1rem;
        border-radius: 4px;
    }
    
    .nav-link:hover,
    .nav-link:focus {
        background-color: rgba(255,255,255,0.1);
    }
    
    .nav-link.active {
        background-color: rgba(255,255,255,0.2);
        font-weight: 600;
    }
}

/* Ensure no horizontal scroll */
body {
    overflow-x: hidden;
}
</style>
`;

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    // Add styles to head
    document.head.insertAdjacentHTML('beforeend', navStyles);
    // Initialize navigation
    initNav();
});