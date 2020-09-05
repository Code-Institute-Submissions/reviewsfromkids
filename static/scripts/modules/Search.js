let searchStart = document.querySelector("#searchBtn");
let searchContent = document.querySelector(".books-search__overlay");

function togglesearchMenu() {

    searchContent.classList.toggle("books-search__overlay--is-visible");

}

searchStart.addEventListener("click", event => {
    
    togglesearchMenu();   
    
});

  