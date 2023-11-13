
class Header extends HTMLElement {
    constructor() {
        super();
    }

    connectedCallback() {
        this.innerHTML = `
            <div class="logo">
                <img src="image/logo.png" alt="Your Web App Logo" height="100px">
            </div>
            <div class="nav">
                <a href="#"> Мэдээ</a>
                <a href="#">Бидний тухай</a>
            </div>
            <div class="icons">
                <div class="search-icon">
                    <i class="material-icons">search</i>
                </div>
                <div class="heart-icon">
                    <i class="material-icons">favorite</i>
                </div>
                <div class="account-icon">
                    <i class="material-icons">person</i>
                </div>
            </div>
        `;
    }
}

customElements.define('custom-header', Header);
export default Header;
