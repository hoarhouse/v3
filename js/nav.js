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
                body.style.overflow = 'hidden'; // Prevent scrolling when menu is open
            });
        }
        
        // Close menu function
        const closeMenu = () => {
            navMenu.classList.remove('nav-menu--active');
            navOverlay.classList.remove('nav-overlay--active');
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
}

.nav-brand a {
    color: var(--white);
    font-size: 1.5rem;
    font-weight: bold;
    text-decoration: none;
}

.nav-menu {
    list-style: none;
    display: flex;
    gap: 2rem;
    margin: 0;
    padding: 0;
}

.nav-link {
    color: var(--white);
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: background-color 0.3s ease;
}

.nav-link:hover {
    background-color: rgba(255,255,255,0.1);
    text-decoration: none;
}

.nav-link.active {
    background-color: rgba(255,255,255,0.2);
    font-weight: 600;
}

.nav-toggle {
    display: none;
    flex-direction: column;
    gap: 4px;
    background: none;
    border: none;
    cursor: pointer;
    padding: 4px;
}

.nav-toggle span {
    width: 25px;
    height: 3px;
    background-color: var(--white);
    transition: all 0.3s ease;
}

.nav-toggle--active span:nth-child(1) {
    transform: rotate(45deg) translate(5px, 5px);
}

.nav-toggle--active span:nth-child(2) {
    opacity: 0;
}

.nav-toggle--active span:nth-child(3) {
    transform: rotate(-45deg) translate(7px, -6px);
}

@media (max-width: 768px) {
    .nav-toggle {
        display: flex;
    }
    
    .nav-menu {
        position: fixed;
        left: -100%;
        top: 70px;
        flex-direction: column;
        background-color: var(--primary);
        width: 100%;
        text-align: center;
        transition: left 0.3s ease;
        padding: 2rem 0;
        box-shadow: 0 10px 27px rgba(0,0,0,0.05);
    }
    
    .nav-menu--active {
        left: 0;
    }
    
    .nav-item {
        margin: 0.5rem 0;
    }
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