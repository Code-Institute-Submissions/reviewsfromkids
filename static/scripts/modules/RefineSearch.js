class RefineSearch {
    constructor() {
      this.buttonBoys = document.querySelector(".refine-search__boys")
      this.contentBoys = document.getElementsByClassName("sort-data-gender")
      this.events()
    }
  
    events() {
      this.buttonBoys.addEventListener("click", () => this.toggleBoys())
    }
  
    toggleBoys() {
        
      var i=0;
      while(i < this.contentBoys.length) {
        if(this.contentBoys.innerHTML = "girls"){
          document.querySelector(".sort-visible").classList.add("invisible")
        } else if(this.contentBoys.innerHTML = "boys"){
          console.log("hide boys");
          console.log(i);
        }
        i++;
      }
        
        
    }
  }

export default RefineSearch