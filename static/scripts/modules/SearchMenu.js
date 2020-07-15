class SearchMenu {
    constructor() {
      this.menuIcon = document.querySelector(".site-header__search")
      this.menuContent = document.querySelector(".search-bar__overlay")
      this.events()
    }
  
    events() {
      this.menuIcon.addEventListener("click", () => this.toggleTheMenu())
    }
  
    toggleTheMenu() {
      this.menuContent.classList.toggle("search-bar__overlay--is-visible")
      this.menuIcon.classList.toggle("search_bar-icon--close-x")
    }
  }

export default SearchMenu