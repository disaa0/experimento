/*
* esribir una aplicaicon en js para evaluar una expresionaritmetica
* las operaciones que peude incluir la expresion son suma, resta
* multiplicacion y division. cuando la expresion aritmetica involucra
* sumas restas, multiplicacion y division en orden que se deben de realizr
* las operaciones es:
* 1. operaciones agrupadas en parentesis
* 2. multiplicaciones y divisiones
* 3. sumas y restas
* */
function evaluarExpresion(expresion){
    // remover espacios en blanco
    expresion = expresion.replace(/\s/g,'');
    function evaluarParentesis(exp){
        // evaluar el parentesis
        var regex = /\(([ˆ()]+)\)/g;
        while (regex.test(exp)){
            exp = exp.replace(regex, function (match,contenido){
                return evaluarMultiplicacionDivision(contenido); // evaluar interior del parentesis
            });
        }
        return evaluarMultiplicacionDivision(exp);

    }
    function evaluarMultiplicacionDivision(exp){
        //var regex = /(\d+\.?\d*)[\/*](\d+\.?\d*)/g;
        var regex = /(\d+\.?\d*)[\/\*](\d+\.?\d*)/g;
        while (regex.test(exp)){
            exp = exp.replace(regex, function (match, n1, n2 ){
                if(match.includes("*")){
                    return parseFloat(n1) * parseFloat(n2);
                }else{
                    return parseFloat(n2) / parseFloat(n2);
                }
            });
        }
        return exp;
    }
    /*function evaluarSumasRestas(exp){
        //dividir la expresion en sumas y restas
        //var regex = /(\d+(\.\d+)?)([-+])/g;
        //var regex = /([-+]?\d+\._\d*|\-)/g;
        var regex = /[-+]?\d+(\.\d+)?/g;
        var numeros = exp.match(regex);
        // nonononon
        // 121212121
        // n = 1 = numerp
        // o = 2 = operador
        console.log(numeros);
        /*for (let i = 0; i < numeros.length; i+=2) {
            var numero = parseFloat(numeros[i]);
            var operador = numeros[i];
            if (!isNaN(numero)){
                if (operador === "+"){
                    resultado += numero;
                }else if(operador === "-"){
                    resultado -= numero;
                }
            }
        }
        if (numeros){
            var resultado = parseFloat(numeros[0]);
            for (let i = 0; i < numeros.length; i++) {
                var numero = parseFloat(numeros(i));
                if (!isNaN(numero)){
                    resultado +=numero;
                }
            }
            return resultado;
        }else{
            return 0;
        }
        return resultado;

    }*/
    function evaluarSumasRestas(exp){
        var regex = /([-+]?[0-9]*\.?[0-9]+)/g; // Encuentra números enteros, decimales y signos
        var elementos = exp.match(regex);

        if (elementos) {
            var resultado = parseFloat(elementos[0]);

            for (var i = 1; i < elementos.length; i++) {
                var elemento = elementos[i];

                if (!isNaN(elemento)) {
                    resultado += parseFloat(elemento);
                }
            }

            return resultado;
        } else {
            return 0;
        }
    }
    var resultado = evaluarParentesis(expresion);
    resultado = evaluarSumasRestas(resultado);
    console.log(resultado);
    return resultado;
}



var expresion = "2 + 3 * (5 - 1)";
var resultado = evaluarExpresion(expresion);
console.log("el resultado es: %s",resultado);