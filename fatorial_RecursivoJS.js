

function fatorial_Recursivo(n) {

if (n===0) {
    return 1;
} else {
    return n * fatorialRecursivo(n-1);
    }
}

console.log(fatorial_Recursivo(4));