class RefineSearch {
    constructor() {
        this.refineStart = document.querySelector("#refine-sort__btn")
        this.refineContent = document.querySelector(".refine-sort__overlay")
        this.events()
      }
    
      events() {
        this.refineStart.addEventListener("click", () => this.toggleRefineMenu())
      }
    
      toggleRefineMenu() {
        this.refineContent.classList.toggle("refine-sort__overlay--is-visible")
        this.refineStart.classList.toggle("site-header__menu-icon--close-x")
        
      }
  }

export default RefineSearch