// when user click on start button
function click_start(){
    //return options to confirm
    let theURL='/start/';
    
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        // Run the anonymous function on the received JSON response
        .then(function(response) {
            
            document.getElementById('option1').innerHTML = response["item1"]
            
            document.getElementById('option2').innerHTML = response["item2"]

            document.getElementById('option3').innerHTML = response["item3"]
            
        });

    
}


function click_operation(){
    let operation_id = document.getElementById('operation').value
    
    let theURL='/operation/'+operation_id;
    fetch(theURL)
        
        
}






// when user clicks on confirm button
function click_confirm(){
    // Get the current value from the input box
    let confirm_id = document.getElementById('confirm').value
    let theURL='/confirm/'+confirm_id;
    // fetch function to send a request to a server
    
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        // Run the anonymous function on the received JSON response
        .then(function(response) {
            
            document.getElementById('calories').innerHTML = response["cal"]
            document.getElementById('protein').innerHTML = response["pro"]

            document.getElementById('carbs').innerHTML = response["car"]
            document.getElementById('fats').innerHTML = response["fat"]

            document.getElementById('cholestrol').innerHTML = response["chol"]
            document.getElementById('fiber').innerHTML = response["fib"]
            

        });
}


function clicked(){
    //return options to confirm
    //let confirm_id = document.getElementById('confirm').value

    let theURL='/total/';
    
    fetch(theURL)
        .then(response=>response.json()) // Convert response to JSON
        // Run the anonymous function on the received JSON response
        .then(function(response) {
            
            document.getElementById('calories').innerHTML = response["cal"]
            document.getElementById('protein').innerHTML = response["pro"]

            document.getElementById('carbs').innerHTML = response["car"]
            document.getElementById('fats').innerHTML = response["fat"]

            document.getElementById('cholestrol').innerHTML = response["chol"]
            document.getElementById('fiber').innerHTML = response["fib"]

        });

    
}

