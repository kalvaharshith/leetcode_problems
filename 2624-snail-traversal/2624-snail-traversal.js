/**
 * @param {number} rowsCount
 * @param {number} colsCount
 * @return {number[][]}
 */
Array.prototype.snail = function(rowsCount, colsCount) {
    const nums = this;

    if (nums.length !== rowsCount * colsCount) {
        return [];
    }

    const result = Array.from(
        { length: rowsCount },
        () => Array(colsCount)
    );

    let index = 0;

    for (let col = 0; col < colsCount; col++) {
        if (col % 2 === 0) {
            for (let row = 0; row < rowsCount; row++) {
                result[row][col] = nums[index++];
            }
        } else {
            for (let row = rowsCount - 1; row >= 0; row--) {
                result[row][col] = nums[index++];
            }
        }
    }

    return result;
};