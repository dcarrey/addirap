myInterval = null;
var operation = "";

$(document).ready(function(){
  operation  = document.getElementsByName("operation")[0].value;
  console.log(operation);
  startDecompte(5,startCompteur);
  $("input[name=resultat]").focusout(updateScore);
})

checkAddition = function(op1,op2,resultat){
  return op1+op2 == resultat
}

checkSoustraction = function(op1,op2,resultat){
  return op1-op2 == resultat
}

checkOperation = function(op,op1,op2,resultat){
  if(op == "addition")
    return checkAddition(op1,op2,resultat)
  else if(op == "soustraction")
    return checkSoustraction(op1,op2,resultat)
}

updateScore = function(){
  $(".resop").remove()
  var total = 0;
  $("input[name=resultat]").each(function( index, value ) {
    //console.log($(this).data("op1"),$(this).data("op2"),$(this).val());
    if($(this).val() != ''){
      if(checkOperation(operation,$(this).data("op1"),$(this).data("op2"),parseInt($(this).val()))){
        $(this).after("<i class='resop fa-solid fa-check' style='color:green'></i>");
        total += 1
      }
      else
        $(this).after("<i class='resop fa-solid fa-xmark' style='color:red'></i>");
    }
  });
  $("#total").text(total);
  if($("#total").text() == $("#nbOperations").text()){
    $(".total").addClass("success")
    $(".total").removeClass("danger")
    $(".total").removeClass("warning")
    clearInterval(myInterval);
  }
  else if( (parseInt($("#total").text()) < parseInt($("#nbOperations").text())) &&
           (parseInt($("#total").text()) > (parseInt($("#nbOperations").text())/3))
         ){
    $(".total").addClass("warning")
    $(".total").removeClass("danger")
    $(".total").removeClass("success")
  }
  else{
    $(".total").addClass("danger")
    $(".total").removeClass("success")
    $(".total").removeClass("warning")
  }
}

startDecompte = function(delay,callback){
  var compteur = 1; //parseInt($(".compteur").text())
  myInterval = setInterval(function(){
    compteur -= 1
    $(".compteur").text(compteur)
    if(compteur == 0){
      clearInterval(myInterval);
      callback();
    }
  },1000);
}


startCompteur = function(){
  $("input[name=resultat]").prop('readonly', false);
  $(".container-operations").removeClass('d-none');
  $(".container-decompte").addClass('d-none');
  var compteur = parseInt($("#duree").val()) + 1
  myInterval = setInterval(function(){
    compteur -= 1
    minutes = Math.trunc(compteur / 60)
    secondes = (compteur%60 < 10)?"0"+(compteur % 60):(compteur % 60)
    $(".compteur").text(minutes+":"+secondes)
    if(compteur == 0){
      $("input[name=resultat]").prop('readonly', true);
      updateScore()
      clearInterval(myInterval);
    }
  },1000);
}
