
















document.getElementById('Button').addEventListener('click', function(){
    // step1: Get the Emailfield Data 
    const Emailfield = document.getElementById('Emailfield');
    console.log(Emailfield);
    const Emailfieldval = Emailfield.value;
    // Step2: Get The password
    const Passfield = document.getElementById('Passwordfield');
    const Passfieldval = Passfield.value;
    // compare the value for valid user
    if(Emailfieldval==="hasnatkabirsupto@gmail.com" && Passfieldval==="Hasnatkabir165103"){
        window.location.href = "Dashboard.html";
    }
    else{
        alert("Invalid User")
    }
})