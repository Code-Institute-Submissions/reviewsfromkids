class RefineSearch {
    constructor() {
        this.refineStart = document.querySelector("#refine-sort__btn")
        this.refineEnd = document.querySelector(".refine-sort__btn-close-x")
        this.refineContent = document.querySelector(".refine-sort__overlay")
        this.events()
      }
    
      events() {
        this.refineStart.addEventListener("click", () => this.toggleRefineMenu())
        this.refineEnd.addEventListener("click", () => this.toggleRefineMenu())
      }
    
      toggleRefineMenu() {
        this.refineContent.classList.toggle("refine-sort__overlay--is-visible")
        this.refineEnd.classList.toggle("refine-sort__overlay--is-visible")
        
      }
  }

export default RefineSearch