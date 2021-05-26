

function RotateMatrix(matrix){
    let row = matrix.length;
    let col = matrix[0].length;

    let new_matrix = [];
    for(let i=0; i<col;i++){
        let temp = [];
        for (let j=0; j<row;j++)
        {
            temp += matrix[j][i];
        }
        new_matrix += temp;
    }
    return new_matrix
}

matrix = [[3,4,5],[10,6,7],[3,3,3]];
rMatrix = RotateMatrix(matrix);
