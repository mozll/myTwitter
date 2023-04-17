function show_search_results() {
    document.querySelector("#search_results").classList.remove("hidden")
}
  
  function hide_search_results() {
    document.querySelector("#search_results").classList.add("hidden")
}


let the_timer


// ## SEARCH Function, CLEARS TIMER THEN SEARCHES FROM THE API SEARCH
function search() {
    clearTimeout(the_timer)
    the_timer = setTimeout( async function(){
        const conn = await fetch("/search",{
            method : "POST"

        })
        const data = await conn.json()
        console.log(data)
    console.log("x")

    // Loop and show the names in the div
    let results = ""


    
    data.forEach( ( item )=>{
        console.log(item.name)
        results += `<div>${item.name} </div>`
    } )
    console.log(results);
    document.querySelector("#search_results").insertAdjacentHTML("afterbegin", results)
    }, 500 );
}