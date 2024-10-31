document.getElementById('DepositeButton').addEventListener('click', function(){
    // Step1: Get the Input data from Deposite input
    const deposite = document.getElementById('DespositeValue');
    const deposite2 = deposite.value;
    const newdeposite = parseFloat(deposite2);
    deposite.value = '';
    if(isNaN(newdeposite)){
        alert('provide a number');
        return;
    }


    const Balanceofdeposite = document.getElementById('Despitebalance');
    const Balanceofdepositevalue = Balanceofdeposite.innerText;
    const newBalanceofdepositevalue = parseFloat(Balanceofdepositevalue);
    const totalDeposite = newBalanceofdepositevalue+newdeposite;

    Balanceofdeposite.innerText = totalDeposite;
 


    const balance = document.getElementById('Balance');
    const nbalance = balance.innerText;
    const nebalance = parseFloat(nbalance);
    const newbalance = nebalance+newdeposite;
    balance.innerText = newbalance;

})
document.getElementById('Withdrawbutton').addEventListener('click',function(){
    // step1 get the input data and convert in float
    const withdrawAmount = document.getElementById('withdrawAmo');
    const makewithdrawAmountstring = withdrawAmount.value;
    const newamountForWithdraw = parseFloat(makewithdrawAmountstring);
    withdrawAmount.value = '';
    if(isNaN(newamountForWithdraw)){
        alert('Provide a number')
        return;
    }

    // step2 get the withdraw amount and set the value
   
    
    

    const balance = document.getElementById('Balance');
    const getInnertext = balance.innerText;
    const makeItfloat = parseFloat(getInnertext);
    if(makeItfloat<=newamountForWithdraw){
        alert('unsufficient fund');
        return;
    }

    const withdraw = document.getElementById('Withdraw');
    const GetvalueofWithdraw = withdraw.innerText;
    const makewithDrawAmountfloat = parseFloat(GetvalueofWithdraw);
        const newAmount = makewithDrawAmountfloat+newamountForWithdraw;
        withdraw.innerText = newAmount;

    const Newbalance = makeItfloat-newamountForWithdraw;
        balance.innerText = Newbalance;
    
})