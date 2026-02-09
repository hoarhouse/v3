// Centralized Navigation Controller for DCF Hungary Website

// Define menu structure in one place
const menuItems = [
    { text: 'Blog', href: '/v3/blog.html', page: 'blog' },
    { text: 'Library', href: '/v3/library.html', page: 'library' },
    { text: 'Home', href: '/v3/index.html', page: 'index' },
    { text: 'About', href: '/v3/about.html', page: 'about' },
    { text: 'Initiatives', href: '/v3/initiatives.html', page: 'initiatives' },
    { text: 'Budapest Appeal', href: '/v3/budapest-appeal.html', page: 'budapest-appeal' },
    { text: 'Get Involved', href: '/v3/get-involved.html', page: 'get-involved' },
    { text: 'Contact', href: '/v3/contact.html', page: 'contact' },
    { text: 'Privacy Policy', href: '/v3/privacy.html', page: 'privacy' }
];

// Generate navigation HTML
function generateNav() {
    const currentPage = window.location.pathname.split('/').pop().replace('.html', '') || 'index';
    
    const navHTML = `
        <div class="nav-container">
            <div class="nav-brand">
                <a href="/v3/index.html">DCF</a>
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
                    <li class="nav-item nav-item-donate">
                        <a href="/v3/get-involved.html" class="nav-donate-btn">Donate</a>
                    </li>
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
    padding: 0.75rem 0;
    position: sticky;
    top: 0;
    z-index: 1000;
    box-shadow: 0 1px 0 rgba(0, 0, 0, 0.1);
}

.nav-container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 1.5rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    position: relative;
    flex-wrap: nowrap;
}

.nav-brand a {
    color: var(--primary);
    font-size: 1.125rem;
    font-weight: 600;
    text-decoration: none;
    letter-spacing: -0.02em;
    flex-shrink: 0;
}

/* Desktop Navigation */
.nav-menu {
    display: flex;
    align-items: center;
}

.nav-list {
    list-style: none;
    display: flex;
    gap: 0.5rem;
    margin: 0;
    padding: 0;
    align-items: center;
}

.nav-item {
    margin: 0;
}

/* Reset donate item spacing on desktop */
.nav-item-donate {
    margin: 0;
    padding: 0;
    border: none;
}

.nav-link {
    color: var(--primary);
    text-decoration: none;
    padding: 6px 12px;
    border-radius: 6px;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    font-size: 0.875rem;
    font-weight: 500;
    white-space: nowrap;
    line-height: 1;
    vertical-align: middle;
}

.nav-link:hover {
    color: var(--secondary);
    text-decoration: none;
}

.nav-link.active {
    color: var(--secondary);
    font-weight: 500;
}

/* Donate Button in Navigation */
.nav-donate-btn {
    background: #e53e3e;
    color: #ffffff !important;
    padding: 6px 16px;
    border-radius: 6px;
    text-decoration: none;
    font-weight: 600;
    font-size: 0.875rem;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    margin: 0 0 0 0.5rem;
    white-space: nowrap;
    line-height: 1;
    height: auto;
    vertical-align: middle;
}

.nav-donate-btn:hover {
    background: #c53030;
    text-decoration: none;
    opacity: 1;
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

/* Tablet Styles - Tighter spacing for medium screens */
@media (max-width: 1200px) and (min-width: 901px) {
    .nav-list {
        gap: 0.4rem;
    }
    
    .nav-link {
        padding: 5px 10px;
        font-size: 0.825rem;
    }
    
    .nav-donate-btn {
        padding: 5px 14px;
        font-size: 0.825rem;
        margin-left: 0.4rem;
    }
}

/* Mobile Styles - Earlier breakpoint at 900px */
@media (max-width: 900px) {
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
    
    /* Donate button in mobile menu */
    .nav-item-donate {
        margin-top: 1rem;
        padding-top: 1rem;
        border-top: 1px solid var(--border-light);
    }
    
    .nav-donate-btn {
        background: #e53e3e;
        color: #ffffff !important;
        text-align: center;
        margin-left: 0;
        width: calc(100% - 3rem);
        margin: 0 1.5rem;
    }
    
    .nav-donate-btn:hover {
        background: #c53030;
    }
}

/* Ensure no horizontal scroll */
body {
    overflow-x: hidden;
}
</style>
`;

// Footer generation function
function generateFooter() {
    const footerHTML = `
        <div class="footer-content">
            <div class="footer-main">
                <div class="footer-brand">Domus Communis Foundation</div>
                <div class="footer-links">
                    <a href="/v3/blog.html">Blog</a>
                    <a href="/v3/library.html">Library</a>
                    <a href="/v3/index.html">Home</a>
                    <a href="/v3/about.html">About</a>
                    <a href="/v3/initiatives.html">Initiatives</a>
                    <a href="/v3/get-involved.html">Get Involved</a>
                    <a href="/v3/contact.html">Contact</a>
                    <a href="/v3/budapest-appeal.html">Budapest Appeal</a>
                    <a href="/v3/privacy.html">Privacy Policy</a>
                </div>
                <div class="footer-nonprofit">
                    <p>Domus Communis Foundation is a registered 501(c)(3) non-profit organization. Your donations are tax-deductible within the fullest extent allowed by law. EIN: 99-1778616.</p>
                </div>
            </div>
            <div class="footer-bottom">
                <p>© 2025 Domus Communis Foundation. All rights reserved.</p>
                <p>Inspired by Catholic Social Teaching. Serving people of all faiths and values.</p>
            </div>
        </div>
    `;
    
    return footerHTML;
}

// Inject footer into page
function initFooter() {
    const footerElement = document.getElementById('main-footer');
    if (footerElement) {
        footerElement.innerHTML = generateFooter();
    }
}

// Add footer styles
const footerStyles = `
<style>
/* Footer Styles - Dark Theme */
#main-footer {
    background: #1d1d1f;
    color: #ffffff;
    padding: 4rem 0 0;
    margin-top: 0;
    border-top: none;
}

.footer-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.footer-main {
    padding-bottom: 3rem;
}

.footer-brand {
    font-size: 1.25rem;
    font-weight: 600;
    margin-bottom: 2rem;
    letter-spacing: -0.02em;
    color: #ffffff;
}

.footer-links {
    display: flex;
    gap: 2rem;
    flex-wrap: wrap;
    margin-bottom: 2rem;
}

.footer-links a {
    color: #ffffff;
    text-decoration: none;
    font-weight: 400;
    transition: all 0.3s ease;
    opacity: 0.9;
}

.footer-links a:hover {
    opacity: 0.7;
}

.footer-nonprofit {
    margin-top: 2rem;
    color: #86868b;
    font-size: 0.9rem;
    max-width: 800px;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.footer-nonprofit p {
    line-height: 1.6;
    word-wrap: break-word;
    overflow-wrap: break-word;
}

.footer-bottom {
    border-top: 1px solid rgba(255,255,255,0.1);
    padding: 2rem 0 3rem;
    text-align: center;
    color: #86868b;
    font-size: 0.9rem;
    font-weight: 300;
}

.footer-bottom p {
    margin-bottom: 0.5rem;
    color: #86868b;
}

/* Mobile Responsive */
@media (max-width: 767px) {
    #main-footer {
        padding: 3rem 0 0;
    }
    
    .footer-content {
        padding: 0 1rem;
    }
    
    .footer-main {
        padding-bottom: 2rem;
    }
    
    .footer-links {
        gap: 1rem;
        font-size: 0.9rem;
        flex-direction: column;
        align-items: flex-start;
    }
    
    .footer-nonprofit {
        font-size: 0.85rem;
    }
    
    .footer-bottom {
        padding: 1.5rem 0 2rem;
        font-size: 0.85rem;
    }
}
</style>
`;

// Initialize on DOM load
document.addEventListener('DOMContentLoaded', () => {
    // Add styles to head
    document.head.insertAdjacentHTML('beforeend', navStyles);
    document.head.insertAdjacentHTML('beforeend', footerStyles);
    // Initialize navigation and footer
    initNav();
    initFooter();
});