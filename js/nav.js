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
/* Navigation Base Styles - Apple Clean */
#main-nav {
    background-color: rgba(255, 255, 255, 0.98);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    padding: 1rem 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
}

.nav-brand a {
    color: var(--primary);
    font-size: 1.25rem;
    font-weight: 600;
    text-decoration: none;
    letter-spacing: -0.02em;
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
    color: var(--primary);
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 6px;
    transition: all 0.3s ease;
    display: block;
    font-size: 0.95rem;
    font-weight: 400;
}

.nav-link:hover {
    color: var(--secondary);
    text-decoration: none;
}

.nav-link.active {
    color: var(--secondary);
    font-weight: 500;
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
    width: 20px;
    height: 1.5px;
    background-color: var(--primary);
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
        background-color: var(--background);
        transition: right 0.3s ease;
        z-index: 1001;
        overflow-y: auto;
        box-shadow: -2px 0 20px rgba(0,0,0,0.1);
    }
    
    .nav-menu--active {
        right: 0;
    }
    
    /* Close button for mobile - properly positioned */
    .nav-close {
        display: flex;
        position: absolute;
        top: 20px;
        right: 20px;
        background: var(--light-background);
        border: none;
        border-radius: 50%;
        cursor: pointer;
        padding: 0;
        width: 44px;
        height: 44px;
        align-items: center;
        justify-content: center;
        z-index: 1002;
        transition: all 0.3s ease;
    }
    
    .nav-close:hover,
    .nav-close:focus {
        background: var(--accent);
        transform: scale(1.05);
    }
    
    .close-line {
        position: absolute;
        width: 18px;
        height: 1.5px;
        background-color: var(--primary);
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
        padding: 1rem 1.5rem;
        min-height: 48px;
        display: flex;
        align-items: center;
        font-size: 1rem;
        border-radius: 8px;
        color: var(--primary);
    }
    
    .nav-link:hover,
    .nav-link:focus {
        background-color: var(--light-background);
        color: var(--secondary);
    }
    
    .nav-link.active {
        background-color: var(--light-background);
        color: var(--secondary);
        font-weight: 500;
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