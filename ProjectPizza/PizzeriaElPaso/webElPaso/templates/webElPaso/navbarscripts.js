function resizeText() {
    alert("holis");
    var e = document.getElementById("selectedTextSize");
    var multiplier = e.options[e.selectedIndex].value;

         if (document.body.style.fontSize == "") {
             document.body.style.fontSize = "1.0em";
            }
            document.body.style.fontSize = parseFloat(document.body.style.fontSize) + (multiplier * 0.2) + "em";
 }

function changeTheme(){
            var selected = document.getElementById("selectedContrast");
             var tone = selected.options[selected.selectedIndex].value;
             switch(tone) {
                        case "gray":                   
                            document.body.style.filter = "contrast(50%)";                                                   
                            break;
                        case "inverted":
                            document.body.style.filter = "invert(100%)"; 
                            break;
                        case "normal":                   
                            document.body.style.filter = "contrast(100%)"; 
                            document.body.style.filter = "invert(0%)";   
                            document.body.style.filter = "sepia(0%)";                  
                            break;
                        case "warm":
                            document.body.style.filter = "sepia(100%)";
                            break;                              
                }

            }