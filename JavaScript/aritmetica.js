
/* Escribir una aplicación en JavaScript para evaluar una expresion artimética
Puede icluir los operadores +, -, *, /
Debe de seguir la seguinete orden de operaciones
Operaciones agrupadas por paréntesis
Multiplicación y división
Suma y resta 
El usuario debe de ingresar la expresion a evaluar
Ejemplo: 2 + 2 / 2
Resultado: 2
Si la expresion tiene error debe de mostrar un mensaje de error
Ejemplo: 2 + 2 / 0
Resultado: Error

*/



function evaluarExpresion() {
    
    let expression = prompt("Enter the expression to evaluate:");
    
    let result = eval(expression);
    try {
        switch (result) {
            case Infinity:
                alert("You can not divide by 0")
                evaluarExpresion();
            case null:
                break;
            default: 
                alert("The result is: " + resultado);
                evaluarExpresion();
        } 
    } catch (ReferenceError) {
        alert("The expression entered is not valid");
        evaluarExpresion();
    }

    
}

evaluarExpresion();


