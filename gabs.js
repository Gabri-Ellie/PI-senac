const inputSearch = document.querySelector("#Search")
const navMenu = document.querySelector("[data-type='nav-menu']")

inputSearch.addEventListener("input",function(){
    const str = this.value;

    if(str){
        filterData(str)
    } else{
        showAllItems()
    }
})