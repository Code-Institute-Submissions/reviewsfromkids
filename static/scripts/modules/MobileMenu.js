class MobileMenu {
  constructor() {
    this.menuIcon = document.querySelector(".site-header__menu-icon");
    this.menuContent = document.querySelector(".site-header__overlay");
    this.events();
  }

  events() {
    this.menuIcon.addEventListener("click", () => this.toggleTheMenu());
  }

  toggleTheMenu() {
    this.menuContent.classList.toggle("site-header__overlay--is-visible");
    this.menuIcon.classList.toggle("site-header__menu-icon--close-x");
  }
}

export default MobileMenu;