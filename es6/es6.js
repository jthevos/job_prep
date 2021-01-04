// greatest in entire array
function adjacentElementsProduct(inputArray) {

    // brute force approach
    // take array[length], multiply it by array[i = 0];
    // we want to test from the back so we dont need to check array bounds.
    // set max and test against i + 2
    // if greater, set max
    let max = 0;

    for (i = inputArray.length; i > 0; i--) {
        for (j = 0; j < inputArray.length; j++) {
            // ensure not the same index, cannot multiply by self
            if (i == j) {
                break;
            }
            temp_product = inputArray[i] * inputArray[j];
            console.log("arrayi = ", inputArray[i]);
            console.log("arrayj = ", inputArray[j]);
            console.log("product = ", inputArray[i] * inputArray[j]);
            if (temp_product > max) {
                max = temp_product;
            }
        }
    }
    return max;
}

// need MIN_SAFE_INTEGER for the event of
// all negative arrays. Cannot use ABS
// because abs(-48) > abs(-1) but -1 is
// what we want
function adjacentElementsProduct(inputArray) {
    let max = Number.MIN_SAFE_INTEGER;

    for (i = 0; i < inputArray.length - 1; i++) {
        let temp_product = inputArray[i] * inputArray[i+1];
        if (temp_product > max) {
            max = temp_product;
        }
    }
    return max;
}


// n-interesting polygon area
function shapeArea(n) {
    return (n*n)+((n-1)*(n-1))
}

// fill in array with consecutives
function makeArrayConsecutive2(statues) {
    // get array and sort
    // make a NEW array using for i0 to iarraymax
    // diff the lengths

    statues = statues.sort();

    let new_array = [];
    let smallest = statues[0];
    let biggest = statues[statues.length-1];

    for (i = smallest; i <= biggest; i++) {
        new_array.push(i);
        console.log(i);

    }
    return new_array.length - statues.length;
}

// You must define your own sorting function because
// JS defaults to alphabetical because it is a shit language.
function makeArrayConsecutive2(statues) {
    // get array and sort
    // make a NEW array using for i0 to iarraymax
    // diff the lengths

    statues = statues.sort(function(a,b){return a-b}); // define the lambda

    let new_array = [];
    let smallest = statues[0];
    let biggest = statues[statues.length-1];


    for (i = smallest; i < biggest; i++) {
        new_array.push(i);
    }

    new_array.push(biggest);

    return new_array.length - statues.length;
}


function almostIncreasingSequence(sequence) {
    let tmp = [];
    // remember to test for length two because removing either will
    // give the answer
    if (sequence.length == 2) {
        return true;
    }

    for (i = 0; i < sequence.length; i++) {
        tmp = sequence.map((x) => {return x});
        tmp.splice(i, 1);

        for (j = 0; j < tmp.length - 1; j++) {
            if (tmp[j] >= tmp[j+1]) {
                break;
            }
            if (j == tmp.length - 2) {
                return true;
            }
        }
    }
    return false;
}


/*
def almostIncreasingSequence(sequence):
    tmp = []
    for i in range(len(sequence)):

        for elem in sequence:
            tmp.append(elem)
        tmp.remove(tmp[i])

        for j in range(len(tmp)-1):
            if tmp[j] >= tmp[j+1]:
                break;
            if j == len(tmp) -2:
                return True;

    return False


*/
